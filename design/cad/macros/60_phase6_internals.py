"""
Phase 6 — the internals, and F9's split of the cross-section.

    A5_Avionics_Stack      the annular board stack (H5)
    A6_Dump_Stage          the 121 kJ dump and its spreader (W7, W12)
    A7_Buffer              the supercapacitor buffer (W4)
    A8_Setter_Coil         the AOP-22 inductive interface (F11)
    A9_Impact_Switch       on the axis (F5)
    A9_SA_Rotor            out-of-line rotor, on the axis (F6)
    A9_Detonator           on the axis at the well bottom (F9)
    C2_Link_Body / _Ring   the contactless ring-body link (H7)
    C3_Harness             the annular harnessing run

F9 IS THE ORGANISING PRINCIPLE OF THIS PHASE, not a detail. The kit replaces the
fuze, so the initiation path has to reach the shell's booster on the centreline
at the well bottom. F9 therefore reserves a clear Ø30 through the full length of
the well AND the machine section, with everything else built as rings about it.

That splits this phase's parts into two groups that must never be confused:

    ANNULAR   boards, dump, buffer, harness, the ring-body link
              -> must NOT enter the Ø30 cylinder, at any z
    ON AXIS   the explosive train: impact switch, S&A rotor, detonator
              -> lives IN the Ø30 cylinder, which is what it is reserved for

Gate 6 is written on that distinction, because an annular part that crosses the
line is a real defect -- it would block the train -- while the train itself
crossing it is the design.

Gate 6 also reports the packaging budget: the annulus is only 6.9 mm of radial
space, which is the binding constraint, not the 105.65 mm of length.
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

DOCNAME = "PGK-Internals"
OUT = os.path.join(CAD, "out")

# THE ANNULAR STACK IS LAID OUT SEQUENTIALLY, from the seat aft, each item's
# station derived from the previous item's length. It is NOT a hand-set table.
#
# It was a hand-set table, and this is what that cost: the buffer is 55 mm long
# and was placed at z = -74, so it ran to z = -19 -- straight through the board
# stack sitting at -36..-20. 3914.7 mm^3 of overlap between two body-side parts,
# and no gate could see it: Gate 6 checks the annulus against the bore and
# against A1, and Gate 7 checks ring-side against body-side. Nothing ever
# compared two body-side parts with each other.
#
# Deriving the stations from the lengths makes the overlap unrepresentable --
# item n+1 starts where item n ends, by construction. Gate 6 now also asserts it.
STACK_ORDER = [
    ("A5_Avionics_Stack", "BoardStackLen"),
    ("A7_Buffer",         "BufferLen"),
    ("A6_Dump_Stage",     "DumpLen"),
    ("C3_Harness",        "HarnessLen"),
]


def stack_layout():
    """{name: (z_aft, z_fore)} for the annular stack, packed from the seat aft."""
    z = P.p("ZThreadRoot")
    out = {}
    for name, key in STACK_ORDER:
        L = P.p(key)
        out[name] = (z - L, z)
        z -= L
    return out


ON_AXIS = [
    ("A9_Impact_Switch",   -106.0,   6.0),
    ("A9_SA_Rotor",        -113.5,   6.0),
    ("A9_Detonator",       -124.7,  10.0),
]


def annulus():
    """The usable annulus: bounded by the TRAIN BORE inside and by the
    SPIGOT SHELL's inner surface outside. Using the spigot's outer radius here
    (as this first did) puts every internal inside the wall that is supposed to
    contain it -- which is what the 8404 mm^3 of interference was."""
    r_in = P.p("RTrainBore") + P.p("AnnularClear")
    r_out = (P.p("WellBoreDia") / 2.0 - P.p("SpigotClearance")
             - P.p("SpigotWall") - P.p("AnnularClear"))
    return r_in, r_out


def avionics_stack():
    r_in, r_out = annulus()
    z = stack_layout()["A5_Avionics_Stack"][0]
    shapes = []
    for i in range(int(P.p("BoardCount"))):
        shapes.append(C.make_tube(r_in, r_out, z, z + P.p("BoardThick")))
        z += P.p("BoardThick") + P.p("BoardGap")
    out = shapes[0]
    for s in shapes[1:]:
        out = out.fuse(s)
    return out


def buffer_pack():
    r_in, r_out = annulus()
    z0, z1 = stack_layout()["A7_Buffer"]
    return C.make_tube(r_in, r_out, z0, z1)


def dump_stage():
    """The dump resistors sit against the spigot wall, because the shell IS the
    sink: W7's finding is that the 121 kJ leaves through the well interface, so
    the shortest thermal path to it is the right place to put them."""
    r_in, r_out = annulus()
    z0, z1 = stack_layout()["A6_Dump_Stage"]
    return C.make_tube(r_in, r_out, z0, z1)


def harness():
    r_in, r_out = annulus()
    z0, z1 = stack_layout()["C3_Harness"]
    return C.make_tube(r_in + 1.5, r_out - 1.5, z0, z1)


def on_axis(name):
    z0, L = dict((n, (za, ln)) for n, za, ln in ON_AXIS)[name]
    dia = {"A9_Impact_Switch": P.p("ImpactSwitchDia"),
           "A9_SA_Rotor": P.p("SARotorDia"),
           "A9_Detonator": P.p("DetonatorDia")}[name]
    return C.make_tube(0.0, dia / 2.0, z0, z0 + L)


def setter_coil():
    """F11's inductive interface, in the body-side nose shoulder.

    NOT in the well: the setter is a gun-line head approaching from the front,
    and a coil 19 mm down inside the well would be a coupling question nothing
    has answered. The shoulder is the natural place and it is body-side, so the
    coil does not have to cross the de-spun interface.
    """
    z = P.p("ZRingFore") + 2.0
    return C.make_tube(20.0, 26.0, z, z + P.p("SetterCoilLen"))


def link_body():
    z = 58.0
    return C.make_tube(P.p("LinkBodyR"), P.p("LinkBodyR") + 6.0, z, z + 10.0)


def link_ring():
    z = 58.0
    return C.make_tube(P.p("LinkRingR"), P.p("LinkRingR") + 5.0, z, z + 10.0)


def spigot_for_check():
    """A1's real geometry, via its own macro, so the check is against the part.

    The shape must be COPIED out before the document closes: a Shape owned by a
    document object dies with it, and the reference here would be dangling.
    """
    import runpy
    ns = runpy.run_path(os.path.join(HERE, "10_phase1_kit_body.py"),
                        run_name="phase1_import")
    doc, body = ns["build"]()
    shape = body.Shape.copy()
    App.closeDocument(doc.Name)
    return shape


# ---------------------------------------------------------------------------


def build():
    doc = C.new_doc(DOCNAME)
    P.to_sheet(doc)

    annular_parts = {
        "A5_Avionics_Stack": avionics_stack(),
        "A7_Buffer": buffer_pack(),
        "A6_Dump_Stage": dump_stage(),
        "C3_Harness": harness(),
    }
    axis_parts = {n: on_axis(n) for n, _, _ in ON_AXIS}
    other = {
        "A8_Setter_Coil": setter_coil(),
        "C2_Link_Body": link_body(),
        "C2_Link_Ring": link_ring(),
    }

    print("Phase 6 — internals")
    for group, label in ((annular_parts, "annular (about the train bore)"),
                         (axis_parts, "on axis (the explosive train)"),
                         (other, "other")):
        print("")
        print("  %s" % label)
        for name, sh in group.items():
            C.add_part(doc, name, sh)
            C.report_shape(name, sh, None)

    r_in, r_out = annulus()
    print("")
    print("  annulus: r %.1f .. %.1f  (%.2f mm of radial space)"
          % (r_in, r_out, r_out - r_in))
    lay = stack_layout()
    print("  annular stack, packed sequentially from the seat aft:")
    for n, _ in STACK_ORDER:
        z0, z1 = lay[n]
        print("      %-22s Z %8.2f .. %8.2f  (%.1f mm)" % (n, z0, z1, z1 - z0))
    low = min(z0 for z0, _ in lay.values())
    print("      stack ends at Z = %.2f, well bottom %.2f, spare %.2f mm"
          % (low, P.p("ZWellBottom"), low - P.p("ZWellBottom")))
    print("  train spans        z %.1f .. %.1f across %d items"
          % (min(za for _, za, _ in ON_AXIS),
             max(za + ln for _, za, ln in ON_AXIS), len(ON_AXIS)))
    print("  they share the z band because F9's split is RADIAL, not axial")

    doc.recompute()
    return doc, annular_parts, axis_parts, other


def gate6(annular_parts, axis_parts, other):
    print("")
    print("GATE 6 — F9's split, and the packaging budget")
    ok = True

    # 1. THE GATE: no annular part may enter the Ø30 reservation, at any z
    train_bore = Part.makeCylinder(P.p("RTrainBore"),
                                   400.0, App.Vector(0, 0, -180.0))
    intruding = []
    total = 0.0
    for name, sh in annular_parts.items():
        v = sh.common(train_bore).Volume
        if v > 1.0:
            intruding.append((name, v))
        total += v
    good = not intruding
    ok &= good
    print("  1 F9 Ø30 reservation vs the annular parts: %.4f mm^3 ...... %s"
          % (total, "PASS" if good else "FAIL"))
    for n, v in intruding:
        print("      %s intrudes %.1f mm^3 into the train bore" % (n, v))
    print("      (boards, dump, buffer, harness: none may cross the line)")

    # 1b. THE CHECK THAT WAS MISSING. Every other gate compares ACROSS the F9
    #     line -- annular against the bore, ring-side against body-side -- and
    #     nothing compared two parts on the SAME side with each other. That is
    #     how a 55 mm buffer came to be laid straight through the board stack.
    names = list(annular_parts)
    clashes = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            v = annular_parts[names[i]].common(annular_parts[names[j]]).Volume
            if v > 1.0:
                clashes.append((names[i], names[j], v))
    good = not clashes
    ok &= good
    print("")
    print("  1b annular items against EACH OTHER: %d overlaps ......... %s"
          % (len(clashes), "PASS" if good else "FAIL"))
    for a, b, v in clashes:
        print("      %s <-> %s  %.1f mm^3  <-- CLASH" % (a, b, v))
    if clashes:
        print("      -> they share a radius band by design, so the only thing")
        print("         separating them is their AXIAL stations. stack_layout()")
        print("         derives those from the lengths; hand-set ones overlapped.")

    # the train is SUPPOSED to be in there -- report what occupies it
    print("")
    print("  2 what legitimately occupies the reservation (F9's own intent):")
    for name, sh in axis_parts.items():
        print("      %-22s Od %.1f, %.1f mm long, inside the Ø30"
              % (name, 2.0 * max(sh.BoundBox.XMax, sh.BoundBox.YMax),
                 sh.BoundBox.ZMax - sh.BoundBox.ZMin))

    # 3. everything inside the intrusion limit
    worst = 0.0
    for grp in (annular_parts, axis_parts, other):
        for name, sh in grp.items():
            b = sh.BoundBox
            if b.ZMin < P.p("ZWellBottom"):
                worst = max(worst, P.p("ZWellBottom") - b.ZMin)
    good = worst < 1.0
    ok &= good
    print("")
    print("  3 parts past the %.1f mm intrusion limit: %.3f mm ...... %s"
          % (P.p("KitIntrusionMax"), worst, "PASS" if good else "FAIL"))

    # 4. interference with the spigot
    print("")
    print("  4 checking against A1's real geometry ...")
    spigot = spigot_for_check()
    v = 0.0
    for grp in (annular_parts, axis_parts, other):
        for name, sh in grp.items():
            if name.startswith("C2_") or name == "A8_Setter_Coil":
                continue          # these sit outside the well by design
            v += sh.common(spigot).Volume
    good = v < 1.0
    ok &= good
    print("      interference with the kit body: %.4f mm^3 ......... %s"
          % (v, "PASS" if good else "FAIL"))

    # the parts that DO live outside the well are checked against the part they
    # live in, not skipped: A8 against the nose, C2 against body and ring
    print("")
    print("  4b the out-of-well parts, against the parts they actually sit in")
    import runpy
    ns5 = runpy.run_path(os.path.join(HERE, "50_phase5_frontend.py"),
                         run_name="phase5_import")
    hub5, _, _, _, _ = ns5["front_hub"]()
    v8 = other["A8_Setter_Coil"].common(hub5).Volume
    good8 = v8 < 1.0
    ok &= good8
    print("      A8 setter coil in A10's shoulder: %.4f mm^3 ......... %s"
          % (v8, "PASS" if good8 else "FAIL"))
    ns2 = runpy.run_path(os.path.join(HERE, "20_phase2_ring_and_machine.py"),
                         run_name="phase2_import")
    ring = ns2["ring_carrier"]()
    vb = other["C2_Link_Body"].common(spigot).Volume
    vr = other["C2_Link_Ring"].common(ring).Volume
    goodc = vb < 1.0 and vr < 1.0
    ok &= goodc
    print("      C2 link, body side %.4f mm^3 / ring side %.4f mm^3 ... %s"
          % (vb, vr, "PASS" if goodc else "FAIL"))
    gap = P.p("LinkRingR") - (P.p("LinkBodyR") + 6.0)
    print("      -> the contactless link's working gap is %.1f mm" % gap)

    # 5. the packaging budget
    print("")
    print("  5 PACKAGING BUDGET — 6.9 mm of radial space is the real constraint")
    print("      annulus area        %8.1f mm^2" % P.p("WellAnnulusArea"))
    print("      annulus depth       %8.2f mm" % P.p("WellAnnulusDepth"))
    print("      available volume    %8.2f cm^3" % P.p("WellAnnulusVolume"))
    print("      annular demand      %8.2f mm  ->  %.2f cm^3"
          % (P.p("InternalsDemand"), P.p("InternalsVolume")))
    print("      margin              %8.2f cm^3  (%+.1f %%)  %s"
          % (P.p("InternalsMargin"), P.p("InternalsMarginPct"),
             "PASS" if P.p("InternalsMargin") > 0 else "FAIL"))
    print("      axial spare         %8.2f mm" % P.p("InternalsAxialSpare"))
    ok &= P.p("InternalsMargin") > 0

    print("")
    print("  GATE 6: %s" % ("PASS" if ok else "FAIL"))
    return ok


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    doc, annular_parts, axis_parts, other = build()
    gate6(annular_parts, axis_parts, other)
    path = os.path.join(OUT, "PGK-Internals.FCStd")
    doc.saveAs(path)
    print("")
    print("saved: %s" % path)


if __name__ == "__main__":
    main()
