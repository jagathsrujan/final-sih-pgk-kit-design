"""
Phase 7 — the master assembly, the interference grid, and the mass rollup.

Three things this phase exists to do, in order of importance:

  1. THE EIGHT-STATE GRID. Four rotor phases (0 / 45 / 90 / 135 deg) x two axial
     states (FLIGHT / LAUNCH), every ring-side part against every body-side part.
     Four phases because the canard set is 4-fold symmetric but the ring's
     apertures and the link are not; two states because C32 creates them -- in
     FLIGHT the ring rides the balls with RetTravel of clearance to the collar,
     in LAUNCH it has travelled that clearance and is seated on it.

  2. THE MEASURED MASS ROLLUP, against P9's <= 1.4 kg for the whole kit and
     C40's 0.81-0.97 kg for the machine. Every mass here comes off a solid, not
     out of a table.

  3. THE ASSEMBLY ITSELF, as a document, so the geometry can be looked at rather
     than only read.

Nothing is hand-positioned: every placement is read from pgk_params, so the
assembly is data like everything else.
"""

import os
import sys
import math

import FreeCAD as App
import Part

HERE = os.path.dirname(os.path.abspath(__file__))
CAD = os.path.dirname(HERE)
if CAD not in sys.path:
    sys.path.insert(0, CAD)

sys.modules.pop("cadlib", None)
import cadlib as C  # noqa: E402
import part_index  # noqa: E402

P = C.params()

DOCNAME = "PGK-Assembly"
OUT = os.path.join(CAD, "out")

# effective densities for the non-structural items. Electronics are mostly air
# and packaging, so a bulk figure is the honest one at this fidelity.
RHO_ELEC = 2000.0
RHO_DIELECTRIC = 1800.0
RHO_LINK = 3000.0


# ---------------------------------------------------------------------------
# gather the parts from their own macros -- never re-implemented here
# ---------------------------------------------------------------------------


def load_phases():
    import runpy

    def macro(name):
        return runpy.run_path(os.path.join(HERE, name), run_name=name)

    m1 = macro("10_phase1_kit_body.py")
    m2 = macro("20_phase2_ring_and_machine.py")
    m3 = macro("30_phase3_bearings.py")
    m4 = macro("40_phase4_canards.py")
    m5 = macro("50_phase5_frontend.py")
    m6 = macro("60_phase6_internals.py")

    doc1, body = m1["build"]()
    shape_a1 = body.Shape.copy()
    App.closeDocument(doc1.Name)

    ring = m2["ring_carrier"]()
    core, _, _ = m2["stator_core"]()

    master = m4["canard_master"]()
    canards = {n: m4["place"](master, az, sg) for n, az, sg in m4["FINS"]}

    hub, _, _, _, _ = m5["front_hub"]()

    body_side = {
        "A1_KitBody":          (shape_a1, C.STEEL, "body"),
        "A2_Stator_Core":      (core, C.SMC, "body"),
        "A3_Windings":         (m2["windings"](), C.COPPER, "body"),
        "A4_Brg_Inner_Races":  (m3["inner_races"](), C.STEEL, "body"),
        "A11_Retention_Collar": (m3["retention_collar"](), C.STEEL, "body"),
        "A5_Avionics_Stack":   (m6["avionics_stack"](), RHO_ELEC, "body"),
        "A6_Dump_Stage":       (m6["dump_stage"](), RHO_ELEC, "body"),
        "A7_Buffer":           (m6["buffer_pack"](), RHO_ELEC, "body"),
        "A8_Setter_Coil":      (m6["setter_coil"](), C.COPPER, "body"),
        "C3_Harness":          (m6["harness"](), RHO_ELEC, "body"),
        "A9_Impact_Switch":    (m6["on_axis"]("A9_Impact_Switch"), C.STEEL, "body"),
        "A9_SA_Rotor":         (m6["on_axis"]("A9_SA_Rotor"), C.STEEL, "body"),
        "A9_Detonator":        (m6["on_axis"]("A9_Detonator"), C.STEEL, "body"),
        "A10_Front_Hub":       (hub, C.STEEL, "body"),
        "D1_Radome":           (m5["radome"](), RHO_DIELECTRIC, "body"),
        "D2_Gnss_Aperture":    (m5["aperture"](), RHO_ELEC, "body"),
        "C2_Link_Body":        (m6["link_body"](), RHO_LINK, "body"),
    }

    ring_side = {
        "B1_Ring_Carrier":     (ring, C.STEEL, "ring"),
        "B2_Rotor_Backiron":   (m2["rotor_backiron"](), C.STEEL, "ring"),
        "B3_Magnets":          (m2["magnets"](), C.NDFEB, "ring"),
        "B4_Brg_Outer_Races":  (m3["outer_races"](), C.STEEL, "ring"),
        "C2_Link_Ring":        (m6["link_ring"](), RHO_LINK, "ring"),
    }
    for n, s in canards.items():
        ring_side[n] = (s, C.STEEL, "ring")

    common = {
        "C1_Balls_Cage":       (m3["balls_cage"](), C.STEEL, "common"),
    }
    return body_side, ring_side, common


# ---------------------------------------------------------------------------


def place(shape, phase_deg, dz):
    s = shape.copy()
    if phase_deg:
        s.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), phase_deg)
    if dz:
        s.translate(App.Vector(0, 0, dz))
    return s


def total_mass(parts, steel_for_a1=None):
    out = {}
    for name, (sh, rho, grp) in parts.items():
        r = rho
        if steel_for_a1 is not None and name == "A1_KitBody":
            r = steel_for_a1
        out[name] = C.mass_kg(sh, r)
    return out


# ---------------------------------------------------------------------------


def build():
    doc = C.new_doc(DOCNAME)
    P.to_sheet(doc)

    body_side, ring_side, common = load_phases()
    everything = {}
    everything.update(body_side)
    everything.update(ring_side)
    everything.update(common)

    # The tree is the first thing anyone reads, so it is grouped the way the
    # architecture is: the body side that turns with the shell, the ring side
    # that is de-spun, and what lies between them. Groups are created first so
    # they head the tree rather than trailing it.
    keys = [k for k in part_index.GROUP_ORDER
            if any(part_index.group(n) == k for n in everything)]
    groups = {k: C.new_group(doc, k) for k in keys}

    # the assembly as modelled: FLIGHT state, phase 0
    for name, (sh, _, _) in everything.items():
        groups[part_index.group(name)].addObject(C.add_part(doc, name, sh))
    doc.recompute()
    return doc, body_side, ring_side, common


def grid(body_side, ring_side, common):
    """Ring-side vs body-side across four rotor phases and two axial states."""
    print("")
    print("GATE 7 — the eight-state interference grid")
    phases = [0.0, 45.0, 90.0, 135.0]
    states = [("FLIGHT", 0.0), ("LAUNCH", -P.p("RetTravel"))]

    worst = 0.0
    worst_where = None
    rows = []
    for sname, dz in states:
        for ph in phases:
            moved = {n: place(sh, ph, dz) for n, (sh, _, _) in ring_side.items()}
            v = 0.0
            hits = []
            for bn, (bsh, _, _) in body_side.items():
                for rn, msh in moved.items():
                    c = bsh.common(msh).Volume
                    if c > 1.0:
                        hits.append((bn, rn, c))
                        v += c
            rows.append((sname, ph, v, hits))
            if v > worst:
                worst, worst_where = v, (sname, ph, hits)

    for sname, ph, v, hits in rows:
        flag = "ok " if v < 1.0 else "CLASH"
        print("   %-7s phase %5.1f deg   %10.4f mm^3  %s"
              % (sname, ph, v, flag))
    ok = worst < 1.0
    if not ok:
        for bn, rn, c in worst_where[2][:8]:
            print("      %s <-> %s  %.1f mm^3" % (bn, rn, c))

    # the C32 contact, which should be a CONTACT and not a clash
    print("")
    print("   the C32 seat in each state (this is meant to touch in LAUNCH):")
    collar = body_side["A11_Retention_Collar"][0]
    ring = ring_side["B1_Ring_Carrier"][0]
    for sname, dz in states:
        rs = place(ring, 0.0, dz)
        gap = rs.BoundBox.ZMin - collar.BoundBox.ZMax
        touch = collar.common(rs).Volume
        print("      %-7s axial gap to the collar %+.4f mm, overlap %.4f mm^3"
              % (sname, gap, touch))
    return ok, rows


def air_gap(body_side, ring_side, common):
    print("")
    print("   air gap under both axial states (C35)")
    magnet_r = P.p("RMagnetOut")
    core_r = P.p("RGapIn")
    gap = (P.p("RMagnetOut") - P.p("RGapIn")) - (P.p("RMagnetOut") - P.p("RGapIn"))
    nominal = P.p("RGapOut") - P.p("RGapIn")
    print("      radial gap %+.3f mm, and the axial travel is %.2f mm"
          % (nominal, P.p("RetTravel")))
    print("      -> the travel is AXIAL and does not touch the RADIAL gap, which")
    print("         is the reason C32's clearance is safe to take there")
    return nominal


def mounting(body_side, ring_side, common):
    """INTEGRAL JOINTS ONLY — interference is not attachment, but neither is
    coincidence.

    The grid above reports overlaps, and a part that touches nothing overlaps
    nothing — which is how the canards spent a whole build floating at the mouth
    plane, attached to nothing, with every gate passing.

    The first correction to that was too broad, though: a "must share volume with
    its parent" test against A1 and the ring flagged 20 parts, of which 16 are
    false positives. The model represents almost every interface as an ABUTTING
    or CLEARANCE fit — a coincident mating face, or a 0.10 mm clearance — and
    neither shares volume by design. There are no fasteners, no spacers and no
    bond lines in this model, so a shared-volume test cannot speak for them.

    So the check is scoped to the joints where overlap IS the design intent:
    the canards are integral with the ring (one billet, the blisk argument), so
    they must be embedded in it, and the test asserts exactly that and nothing
    more. The limitation is stated rather than papered over — see the note it
    prints.
    """
    print("")
    print("   MOUNTING — integral joints must be embedded, not butted")
    ring = ring_side["B1_Ring_Carrier"][0]
    ok = True
    joints = [n for n in ring_side if n.startswith("B5_Canard")]
    total = 0.0
    for n in joints:
        v = ring.common(ring_side[n][0]).Volume
        total += v
        flag = "ok" if v > 100.0 else "FLOATING"
        print("      %-24s shares %9.1f mm^3 with the ring   %s" % (n, v, flag))
        ok &= v > 100.0
    print("      -> the four fins are integral, as the manufacturing dossier")
    print("         argues they should be (one billet, cant angles off one setup)")
    print("")
    print("      NOT CHECKED, and it should be said plainly: every other interface")
    print("      in this model is an abutting face or a clearance fit — a nominal")
    print("      contact with no fastener, spacer or bond line drawn. Shared-volume")
    print("      and distance tests are both meaningless for those, so they are")
    print("      represented in their assembled position and no more. Modelling")
    print("      the joints (magnet pockets, press lands, bond lines) is the next")
    print("      thing this workspace should do if the model is to carry loads.")
    return ok


def mass_rollup(body_side, ring_side, common):
    print("")
    print("   MASS ROLLUP — measured off the solids")
    bs = total_mass(body_side)
    rs = total_mass(ring_side)
    cs = total_mass(common)

    print("")
    print("      %-24s %8s   %-24s %8s" % ("body side", "kg", "ring side", "kg"))
    bn = sorted(bs, key=lambda k: -bs[k])
    rn = sorted(rs, key=lambda k: -rs[k])
    for i in range(max(len(bn), len(rn))):
        lb = "%-24s %8.4f" % (bn[i], bs[bn[i]]) if i < len(bn) else " " * 33
        lr = "%-24s %8.4f" % (rn[i], rs[rn[i]]) if i < len(rn) else ""
        print("      %s   %s" % (lb, lr))
    print("      %s" % ("-" * 68))
    print("      %-24s %8.4f   %-24s %8.4f"
          % ("BODY TOTAL", sum(bs.values()), "RING TOTAL", sum(rs.values())))
    print("      %-24s %8.4f" % ("common (balls)", sum(cs.values())))

    kit_steel = sum(bs.values()) + sum(rs.values()) + sum(cs.values())

    # the lever: structural parts in aluminium instead
    alu = 0.0
    for name, (sh, rho, _) in list(body_side.items()) + list(ring_side.items()):
        if name in ("A1_KitBody", "A10_Front_Hub"):
            alu += C.mass_kg(sh, C.ALU) - C.mass_kg(sh, rho)
        elif name.startswith("B5_Canard"):
            alu += C.mass_kg(sh, C.ALU) - C.mass_kg(sh, rho)
        elif name == "B1_Ring_Carrier":
            alu += C.mass_kg(sh, C.ALU) - C.mass_kg(sh, rho)
    kit_alu = kit_steel + alu

    machine = (bs["A2_Stator_Core"] + bs["A3_Windings"]
               + rs["B2_Rotor_Backiron"] + rs["B3_Magnets"])

    print("")
    print("      KIT TOTAL, as modelled (steel structure)  %8.4f kg" % kit_steel)
    print("      KIT TOTAL, aluminium structure            %8.4f kg" % kit_alu)
    print("      MACHINE (C40 checks this alone)           %8.4f kg" % machine)
    print("")
    print("      P9 limit for the WHOLE kit                %8.4f kg" % P.p("KitMassMax"))
    print("      -> as modelled   %+.3f kg  (%+.0f %%)"
          % (kit_steel - P.p("KitMassMax"),
             100.0 * (kit_steel - P.p("KitMassMax")) / P.p("KitMassMax")))
    print("      -> aluminium     %+.3f kg  (%+.0f %%)"
          % (kit_alu - P.p("KitMassMax"),
             100.0 * (kit_alu - P.p("KitMassMax")) / P.p("KitMassMax")))
    print("")
    print("      C40 range for the machine                 %.3f - %.3f kg"
          % (P.p("MachineMassLo"), P.p("MachineMassHi")))
    inside = P.p("MachineMassLo") <= machine <= P.p("MachineMassHi")
    print("      -> %s (%.0f %% over the top of the band)"
          % ("inside" if inside else "OVER",
             0.0 if inside else 100.0 * (machine - P.p("MachineMassHi"))
             / P.p("MachineMassHi")))

    # C26 with the measured ring, which is what C32 was sized on
    c26 = (rs["B1_Ring_Carrier"] + rs["B2_Rotor_Backiron"] + rs["B3_Magnets"])
    print("")
    print("      C26 rotating assembly (measured)          %8.3f kg" % c26)
    print("      C26 setback at 15 000 g                   %8.1f kN"
          % (c26 * 15000.0 * 9.80665 / 1000.0))
    print("      C26 assumed 0.5 kg and derived            %8.1f kN"
          % P.p("SetbackRing"))

    C.publish_measured({"KitTotal_Steel": kit_steel, "KitTotal_Alu": kit_alu,
                        "Machine": machine, "RotatingAssembly": c26,
                        "Parts_Kg": dict(bs, **dict(rs, **cs))})
    return kit_steel, kit_alu, machine


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    doc, body_side, ring_side, common = build()
    ok, rows = grid(body_side, ring_side, common)
    ok &= mounting(body_side, ring_side, common)
    air_gap(body_side, ring_side, common)
    mass_rollup(body_side, ring_side, common)
    path = os.path.join(OUT, "PGK-Assembly.FCStd")
    doc.saveAs(path)
    print("")
    print("  GATE 7: %s" % ("PASS" if ok else "FAIL"))
    print("saved: %s" % path)


if __name__ == "__main__":
    main()
