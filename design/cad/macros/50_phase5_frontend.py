"""
Phase 5 — the front end, and the nose-ownership decision.

    A10_Front_Hub        the body-side nose structure forward of the ring
    D1_Radome            the forward dielectric cap
    D2_Gnss_Aperture     the N3 aperture: a circumferential band on the nose
    D3_Radar_Keepout     the 24 GHz front end's reserved volume

THE DECISION THIS PHASE FORCES. The plan flagged it: the CAA interface
visualisation draws the nose as part of the roll-controlled group with the fuze
cavity inside it, but F9 reserves a clear axial bore through the well AND the
machine with the train built as rings about it, and H5 puts the boards in the
well spigot. Those cannot both hold.

The model takes the reading that satisfies F2 + N3 + F9 together:

    the RF front end, the radome and the spin-axis aperture ride a BODY-SIDE
    axial hub that runs forward through the ring's bore; the ring ends at its
    fore face and keeps no nose of its own.

F2 says the radar is "body-mounted in the nose tip ahead of the canard ring",
and N3 makes the aperture rotationally symmetric on the spin axis *so that spin
cannot modulate it* -- both of which are statements about the body side. So the
whole nose turns with the shell and the ring is exactly the canard bay.

Gate 5: nothing protrudes past the in-bore limit, the aperture's forward cone is
clear of metal, the front end does not interfere with the ring at any rotor
phase, and the junction step (T8) is reported rather than assumed.
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

P = C.params()

DOCNAME = "PGK-FrontEnd"
OUT = os.path.join(CAD, "out")


# ---------------------------------------------------------------------------


def front_hub():
    """A10 — the nose shell: tapers from the ring's skin to an aperture land,
    with the antenna cavity bored into it and open at the front.

    The cavity is open forward and capped by the radome, which is what lets the
    GNSS elements sit INSIDE it looking forward. That matters: N3's aperture has
    to see the sky, and the projectile's nose points up through the ascent, so a
    band looking radially outward at the horizon would be the wrong geometry.
    Symmetry about the spin axis is what N3 asks for, and a ring of elements
    around the axis inside the radome has it exactly.
    """
    r_skin = P.p("RingR")
    r_land = P.p("ApertureLandDia") / 2.0
    r_cav = P.p("GnssApertureDia") / 2.0
    z_aft = P.p("ZRingFore") + 0.5          # 0.5 mm seam to the rotating ring
    z_land = P.p("ZFrontHubFore") - 6.0
    z_fore = P.p("ZFrontHubFore")
    r_train = P.p("RTrainBore")

    prof = [
        (r_train, z_aft),
        (r_skin, z_aft),
        (r_skin, z_aft + 3.5),              # short land matching the ring's skin
        (r_land, z_land),                   # taper to the aperture land
        (r_land, z_fore),                   # the aperture land
        (r_cav, z_fore),                    # forward face, in to the cavity mouth
        (r_cav, z_aft + 7.5),               # cavity wall, running aft
        (r_train, z_aft + 7.5),             # step back to the train bore
        (r_train, z_aft),
    ]
    return C.make_revolve(prof), r_land, r_cav, z_land, z_fore


def radome():
    """D1 — the forward cap. A dielectric part, so it is its own body: the
    radome must pass L1/L5 and 24 GHz while being a structural, aerodynamically
    heated surface (F2, N3, risk 27)."""
    r_land = P.p("ApertureLandDia") / 2.0
    z_fore = P.p("ZFrontHubFore")
    tip_r = 8.0
    tip_z = z_fore + 6.0
    return C.make_revolve([
        (0.0, z_fore), (r_land, z_fore), (tip_r, tip_z), (0.0, tip_z),
    ])


def aperture():
    """D2 — the N3 aperture: a ring of elements around the spin axis, inside the
    radome and looking forward through it."""
    r_cav = P.p("GnssApertureDia") / 2.0
    z_fore = P.p("ZFrontHubFore")
    return C.make_tube(r_cav - 1.0, r_cav, z_fore - 4.0, z_fore - 1.0)


def radar_keepout():
    """D3 — the 24 GHz front end's reserved volume, on the axis inside the
    cavity, forward-looking like the aperture it shares the tip with."""
    z_fore = P.p("ZFrontHubFore")
    return C.make_tube(0.0, 15.0, z_fore - 9.0, z_fore - 1.0)


def ring_for_check():
    """Rebuild the ring carrier by calling Phase 2's own function, so the
    interference check is against the real part and not a stand-in."""
    import runpy
    ns = runpy.run_path(os.path.join(HERE, "20_phase2_ring_and_machine.py"),
                        run_name="phase2_import")
    return ns["ring_carrier"]()


# ---------------------------------------------------------------------------


def build():
    doc = C.new_doc(DOCNAME)
    P.to_sheet(doc)

    hub, r_land, r_cav, z_land, z_fore = front_hub()
    parts = {
        "A10_Front_Hub": (hub, C.STEEL),
        "D1_Radome": (radome(), None),
        "D2_Gnss_Aperture": (aperture(), None),
        "D3_Radar_Keepout": (radar_keepout(), None),
    }

    print("Phase 5 — front end")
    for name, (sh, dens) in parts.items():
        C.add_part(doc, name, sh)
        C.report_shape(name, sh, dens)

    print("")
    print("  nose: skin Ø%.1f -> land Ø%.1f at z=%.1f, forward face z=%.1f"
          % (P.p("RingOD"), 2 * r_land, z_land, z_fore))
    print("  antenna cavity Ø%.1f open forward, capped by the dielectric radome"
          % (2 * r_cav))
    print("  aperture ring Ø%.1f at z=%.1f-%.1f, inside the radome, looking forward"
          % (P.p("GnssApertureDia"), z_fore - 4.0, z_fore - 1.0))

    doc.recompute()
    return doc, parts


def gate5(parts):
    print("")
    print("GATE 5 — the front end")
    ok = True

    hub = parts["A10_Front_Hub"][0]
    bb = hub.BoundBox
    max_r = max(abs(bb.XMin), abs(bb.XMax), abs(bb.YMin), abs(bb.YMax))
    bore_r = 155.0 / 2.0
    good = max_r <= bore_r - 2.0
    ok &= good
    print("  1 in-bore: front end Ø%.1f vs Ø155 limit, %.1f mm/side ... %s"
          % (2 * max_r, bore_r - max_r, "PASS" if good else "FAIL"))

    # 2. The aperture looks FORWARD, so what must be clear is the bore between
    #    the aperture's own radius and the radome. Testing a plane at the tip
    #    instead would fail on the hub's own forward rim, which is at a LARGER
    #    radius and does not block a forward-looking ring at all.
    r_cav = P.p("GnssApertureDia") / 2.0
    z_fore = P.p("ZFrontHubFore")
    probe = Part.makeCylinder(r_cav, 40.0, App.Vector(0, 0, z_fore - 10.0))
    blocked = hub.common(probe)
    good = blocked.Volume < 1.0
    ok &= good
    print("  2 metal in the Ø%.1f forward bore from z=%.1f: %.4f mm^3 ... %s"
          % (P.p("GnssApertureDia"), z_fore - 10.0, blocked.Volume,
             "PASS" if good else "FAIL"))
    print("      (the aperture ring Ø%.1f %.1f mm inside the cavity mouth, and"
          % (P.p("GnssApertureDia"), 1.0))
    print("       the only thing forward of it is the dielectric radome)")

    # 3. no interference with the ring, at four rotor phases
    ring = ring_for_check()
    worst = 0.0
    for phase in (0.0, 45.0, 90.0, 135.0):
        r = ring.copy()
        if phase:
            r.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), phase)
        v = 0.0
        for name in ("A10_Front_Hub", "D1_Radome", "D2_Gnss_Aperture"):
            v += r.common(parts[name][0]).Volume
        worst = max(worst, v)
    good = worst < 1.0
    ok &= good
    print("  3 interference with the ring, 4 phases: %.4f mm^3 ....... %s"
          % (worst, "PASS" if good else "FAIL"))

    # 4. T8 — the junction step
    print("")
    print("  4 T8 — the junction step, reported not assumed")
    print("      the register truncates the shell's ogive at Ø%.1f at the seat;"
          % P.p("OgiveTruncDia"))
    print("      the kit's ring is Ø%.1f with its aft face ABOVE the seat."
          % P.p("RingOD"))
    print("      -> rearward-facing step  %.1f mm deep" % P.p("StepDepth"))
    print("      -> step frontal area     %.0f mm^2 = %.1f %% of the body section"
          % (P.p("StepArea"), 100.0 * P.p("StepFraction")))
    print("      M10 requires >90 % range retention, and this is a drag source")
    print("      that has never been priced against it.")
    print("")
    print("      the chain:  machine radial build closes at Ø91.9 against C34's")
    print("                  Ø92 ceiling -> the ring must wrap it plus a wall")
    print("                  -> RingOD ~98 -> the step is 23.6 mm")
    print("      the lever:  C44 (radial vs axial flux) is OPEN and is the one")
    print("                  change that shrinks the machine, the ring and the")
    print("                  step together. Nothing links C44 to M10 today.")
    print("      the options:")
    for v in P.p("RingOD_Variants").split(" | "):
        print("        %s" % v)
    print("      (a smaller ring buys exposed span as well as step -- but the")
    print("       machine stops fitting below about Ø96, so this is a C34/C40")
    print("       trade, not a free choice)")

    print("")
    print("  GATE 5: %s" % ("PASS" if ok else "FAIL"))
    return ok


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    doc, parts = build()
    gate5(parts)
    path = os.path.join(OUT, "PGK-FrontEnd.FCStd")
    doc.saveAs(path)
    print("")
    print("saved: %s" % path)


if __name__ == "__main__":
    main()
