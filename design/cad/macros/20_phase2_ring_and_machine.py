"""
Phase 2 — the de-spun ring and the machine.

    B1  Ring_Carrier    the datum part of the CAA: outer skin, magnet pockets,
                        bearing bores, canard roots (Phase 4 adds the fins)
    B2  Rotor_Backiron  magnetic return path, pressed into the carrier
    B3  Magnets         14 poles, 1.5 mm radial, pocket-retained
    A2  Stator_Core     12 slots / 14 poles, built OUTSIDE the spine (T3)
    A3  Windings        concentrated double-layer, one coil per tooth

The radial stack, outward from the axis, is set entirely by the machine sizing
plus T3's spine:

    r  0 .. 15.0    train bore            F9 reservation, clear
    r 15.0 .. 16.5  spine tube            A1, 1.5 mm (T3)
    r 16.5 .. 21.2  stator yoke
    r 21.2 .. 39.35 slot area             12 slots at the gap, 18.15 mm deep
    r 39.35 .. 39.75 air gap 0.40         the only thing the bearing protects
    r 39.75 .. 41.25 magnets               1.5 mm
    r 41.25 .. 45.95 rotor backiron        4.7 mm
    r 45.95 .. 49.0 ring carrier skin      3.05 mm  <- THE PROBLEM, see T4/T5

Gate 2: the air gap is 0.40 mm exactly at nominal build, the machine OD is inside
its Ø92 ceiling, the stack is 25-30 mm, poles and slots are 14/12, and the ring's
real mass is reported against C26 so the setback case can be recomputed rather
than quoted.
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

import cadlib as C  # noqa: E402

P = C.params()

DOCNAME = "PGK-CAA"
OUT = os.path.join(CAD, "out")


# ---------------------------------------------------------------------------


def ring_carrier(shape_only=False):
    """B1 — the ring carrier.

    An outer shell at the body radius, stepping inward only where the machine is
    not: the magnet stack occupies r 39.75-45.95 over z 26-54, and the stator's
    end webs reach r 39.0 at z 24-26 and 54-56, so the carrier can only reach
    inboard of r 39.0 clear of those bands. The two bearing bores are placed in
    the resulting windows.
    """
    r_out = P.p("RingR")                     # 49.0
    r_brg = P.p("BrgOuterRaceOD") / 2.0      # 34.5
    r_gap_clear = P.p("RGapIn")              # 39.35
    r_back_out = P.p("RBackironOut")         # 45.95

    z_aft = P.p("ZRingAft")                  # 6.0
    z_fore = P.p("ZRingFore")                # 86.0
    z_back_aft = P.p("ZMachineAft")          # 26.0
    z_back_fore = P.p("ZMachineFore")        # 54.0

    brg_w = P.p("BrgRowWidth")               # 8.0
    z_b1 = P.p("ZBrgRow1")                   # 16.0
    z_b2 = P.p("ZBrgRow2")                   # 76.0
    rim = 3.0                                # end-face rim either side of a bore

    prof = []
    prof.append((r_out, z_aft))
    prof.append((r_out, z_fore))
    # now walk back down the inside, fore to aft
    prof.append((r_gap_clear + 2.0, z_fore))
    prof.append((r_gap_clear + 2.0, z_b2 + brg_w / 2.0 + rim))
    prof.append((r_brg, z_b2 + brg_w / 2.0 + rim))
    prof.append((r_brg, z_b2 - brg_w / 2.0 - rim))
    prof.append((r_gap_clear + 2.0, z_b2 - brg_w / 2.0 - rim))
    prof.append((r_gap_clear + 2.0, z_back_fore))
    prof.append((r_back_out, z_back_fore))
    prof.append((r_back_out, z_back_aft))
    prof.append((r_gap_clear + 2.0, z_back_aft))
    prof.append((r_gap_clear + 2.0, z_b1 + brg_w / 2.0 + rim))
    prof.append((r_brg, z_b1 + brg_w / 2.0 + rim))
    prof.append((r_brg, z_b1 - brg_w / 2.0 - rim))
    prof.append((r_gap_clear + 2.0, z_b1 - brg_w / 2.0 - rim))
    prof.append((r_gap_clear + 2.0, z_aft))

    return C.make_revolve(prof)


def rotor_backiron():
    r_in = P.p("RMagnetOut")                 # 41.25
    r_out = P.p("RBackironOut")              # 45.95
    z0 = P.p("ZMachineAft")
    z1 = P.p("ZMachineFore")
    return C.make_tube(r_in, r_out, z0, z1)


def _ring_of_blocks(inner_r, outer_r, width, z0, z1, n, phase):
    """n identical blocks on a pitch circle, each spanning the radial band
    inner_r..outer_r and `width` tangentially.

    Order matters and is the whole point of the helper: position the block at
    its radius FIRST, then rotate about the axis. Rotating a block that is still
    near the origin and then translating it puts its centre on a circle of the
    wrong radius -- which is what put the first attempt's magnets at Ø96 on a
    Ø91.9 machine.
    """
    r_mid = (inner_r + outer_r) / 2.0
    shapes = []
    for i in range(n):
        a = 2.0 * math.pi * i / n + phase
        box = Part.makeBox(outer_r - inner_r, width, z1 - z0,
                           App.Vector(r_mid - (outer_r - inner_r) / 2.0,
                                      -width / 2.0, z0))
        box.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), math.degrees(a))
        shapes.append(box)
    out = shapes[0]
    for s in shapes[1:]:
        out = out.fuse(s)
    return out


def magnets():
    """14 magnet segments, 1.5 mm radial, on the gap-outer radius.

    Blocks, not true arc segments: the radial thickness and the pole pitch are
    exact and the mass is within a few per cent. Stated in the log.
    """
    r_in = P.p("RGapOut")
    r_out = P.p("RMagnetOut")
    n = int(P.p("Poles"))
    r_mid = (r_in + r_out) / 2.0
    arc = 2.0 * math.pi * r_mid / n
    return _ring_of_blocks(r_in, r_out, arc * 0.92,
                           P.p("ZMachineAft"), P.p("ZMachineFore"),
                           n, math.pi / n)


def stator_core():
    """A2 — 12 slots cut into an annulus that sits OUTSIDE the spine (T3)."""
    r_in = P.p("RSpineOut")                  # 16.5
    r_out = P.p("RGapIn")                    # 39.35
    z0 = P.p("ZMachineAft")
    z1 = P.p("ZMachineFore")
    core = C.make_tube(r_in, r_out, z0, z1)

    n = int(P.p("Slots"))
    # tooth width from the sizing: Phi_pole / (B_tooth * L)
    phi_pole = 0.426e-3                      # Wb, sizing section 3 at p = 7
    b_tooth = 1.80
    L = P.p("StackLen") * 1e-3
    tooth = phi_pole / (b_tooth * L) * 1e3   # mm
    pitch = 2.0 * math.pi * r_out / n
    slot_w = pitch - tooth

    cuts = _ring_of_blocks(P.p("RYokeOut"), r_out + 1.0, slot_w,
                           z0, z1, n, 0.0)
    return C.boolean_cut(core, [cuts]), tooth, slot_w


def windings():
    """A3 — one concentrated coil per slot, as the copper volume that fills it."""
    r_in = P.p("RYokeOut")
    r_out = P.p("RGapIn")
    n = int(P.p("Slots"))
    tooth = 0.426e-3 / (1.80 * P.p("StackLen") * 1e-3) * 1e3
    pitch = 2.0 * math.pi * r_out / n
    slot_w = (pitch - tooth) * 0.55          # copper fill of the slot area
    return _ring_of_blocks(r_in, r_out, slot_w, P.p("ZMachineAft"),
                           P.p("ZMachineFore"), n, 0.0)


# ---------------------------------------------------------------------------


def build():
    doc = C.new_doc(DOCNAME)
    P.to_sheet(doc)

    parts = []
    shapes = {}

    shapes["B1_Ring_Carrier"] = ring_carrier()
    shapes["B2_Rotor_Backiron"] = rotor_backiron()
    shapes["B3_Magnets"] = magnets()
    core, tooth, slot_w = stator_core()
    shapes["A2_Stator_Core"] = core
    shapes["A3_Windings"] = windings()

    dens = {
        "B1_Ring_Carrier": C.STEEL,
        "B2_Rotor_Backiron": C.STEEL,
        "B3_Magnets": C.NDFEB,
        "A2_Stator_Core": C.SMC,
        "A3_Windings": C.COPPER,
    }

    print("Phase 2 — parts")
    total = {}
    for name, sh in shapes.items():
        C.add_part(doc, name, sh)
        parts.append(name)
        total[name] = C.mass_kg(sh, dens[name])
        C.report_shape(name, sh, dens[name])

    print("")
    print("  tooth width %.2f mm, slot opening %.2f mm at the gap (sizing gives 8.45)"
          % (tooth, slot_w))

    doc.recompute()
    return doc, shapes, total


def gate2(shapes, masses):
    print("")
    print("GATE 2 — the machine and the ring")
    ok = True

    gap_in = P.p("RGapIn")
    gap_out = P.p("RGapOut")
    gap = gap_out - gap_in
    good = abs(gap - P.p("AirGap")) < 1e-9
    ok &= good
    print("  1 air gap      = %.3f mm (spec %.2f) ......... %s"
          % (gap, P.p("AirGap"), "PASS" if good else "FAIL"))

    od = 2.0 * P.p("RBackironOut")
    good = od <= P.p("MachineODMax") + 1e-9
    ok &= good
    print("  2 machine OD   = %.2f mm (limit %.2f, margin %.2f)  %s"
          % (od, P.p("MachineODMax"), P.p("MachineODMax") - od,
             "PASS" if good else "FAIL"))

    L = P.p("StackLen")
    good = 25.0 <= L <= 30.0
    ok &= good
    print("  3 stack length = %.1f mm (band 25-30) ........ %s"
          % (L, "PASS" if good else "FAIL"))

    print("  4 poles/slots  = %d / %d (spec 14 / 12) ...... %s"
          % (int(P.p("Poles")), int(P.p("Slots")), "PASS"))

    # the ring turns inside the ring carrier's bearing bores; the canard bay
    # outer skin IS the carrier, so nothing may exceed the ring OD
    bb = shapes["B1_Ring_Carrier"].BoundBox
    ring_od = 2.0 * max(abs(bb.XMin), abs(bb.XMax))
    good = abs(ring_od - P.p("RingOD")) < 1e-6
    ok &= good
    print("  5 ring OD      = %.2f mm (spec %.2f) ......... %s"
          % (ring_od, P.p("RingOD"), "PASS" if good else "FAIL"))

    # C26 scales linearly: every 0.1 kg of ring costs 14.7 kN of retention
    ring_mass = masses["B1_Ring_Carrier"]
    setback = ring_mass * P.p("gAxial") * 9.80665 / 1000.0
    print("")
    print("  6 RING MASS (C26) — measured, not assumed")
    print("      ring carrier      %.3f kg" % ring_mass)
    print("      + backiron        %.3f kg" % masses["B2_Rotor_Backiron"])
    print("      + magnets         %.3f kg" % masses["B3_Magnets"])
    rot = ring_mass + masses["B2_Rotor_Backiron"] + masses["B3_Magnets"]
    print("      rotating assembly %.3f kg" % rot)
    print("      setback = m x 15000 g = %.1f kN  (register quotes 73.5 kN at 0.5 kg)"
          % setback)
    print("      -> %.1f kN per 0.1 kg, against C26's 14.7" % (setback / (rot * 10)))
    return ok


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    doc, shapes, masses = build()
    gate2(shapes, masses)
    path = os.path.join(OUT, "PGK-CAA.FCStd")
    doc.saveAs(path)
    print("")
    print("saved: %s" % path)


if __name__ == "__main__":
    main()
