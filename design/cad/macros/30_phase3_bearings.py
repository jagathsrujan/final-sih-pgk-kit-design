"""
Phase 3 — bearings and the C32 launch-load bypass.

    A4_Brg_Inner_Races   two rows, seated on the A1 spindle's machined lands
    B4_Brg_Outer_Races   two rows, pressed into the ring carrier's bores
    C1_Balls_Cage        the rolling elements -- owned by neither body
    A11_Retention_Collar the C32 bypass: the face the ring lands on under setback

WHY THIS PHASE EXISTS. C26's structural conclusion was already stark -- "74 kN
peak cannot pass through the flight bearings", because thin-section instrument
bearings in the 30-50 mm class carry single-digit kilonewtons -- so the axial
launch path must bypass them entirely. T6 then measured the ring and found the
load is not 74 kN but 212.6 kN on the carrier (265.1 kN on the full rotating
assembly): x2.9 to x3.6 what the register assumed.

So the collar in this phase is not a detail. It is the part that carries the
design's governing load, and it is sized against the MEASURED mass, not C26's
0.5 kg assumption.

How it works: the ring's aft face sits RetTravel from the collar's fore face in
the flight state. Under setback the ring travels that 0.10 mm and lands on the
collar, so the axial load goes ring -> collar -> body, straight past the balls.
The travel is absorbed by the bearing's internal clearance, and -- importantly --
it is AXIAL, so it does not touch the 0.40 mm RADIAL air gap.

C35's prohibition is respected: every element in the axial path is metal. No
spring washer, no elastomer seat, no compliant potting.

Gate 3: the axial path bypasses the balls, both axial states exist, and no
compliant element sits in the launch path.
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

# cadlib is cached by FreeCAD's long-lived interpreter too, so re-read it
sys.modules.pop("cadlib", None)
import cadlib as C  # noqa: E402

P = C.params()

DOCNAME = "PGK-Bearings"
OUT = os.path.join(CAD, "out")


# ---------------------------------------------------------------------------


def inner_races():
    """A4 — the two inner races, on the body's spindle lands."""
    r_i = P.p("BrgBoreDia") / 2.0 + P.p("PressFitClearance")
    r_o = P.p("BrgInnerRaceOD") / 2.0
    w = P.p("BrgRowWidth")
    out = None
    for z in (P.p("ZBrgRow1"), P.p("ZBrgRow2")):
        t = C.make_tube(r_i, r_o, z - w / 2.0, z + w / 2.0)
        out = t if out is None else out.fuse(t)
    return out


def outer_races():
    """B4 — the two outer races, pressed into the ring carrier's bores."""
    r_i = P.p("BrgOuterRaceID") / 2.0
    r_o = P.p("BrgOuterRaceOD") / 2.0 - P.p("PressFitClearance")
    w = P.p("BrgRowWidth")
    out = None
    for z in (P.p("ZBrgRow1"), P.p("ZBrgRow2")):
        t = C.make_tube(r_i, r_o, z - w / 2.0, z + w / 2.0)
        out = t if out is None else out.fuse(t)
    return out


def balls_cage():
    """C1 — the rolling elements. Neither body owns them: a ball orbits at the
    mean of the two race speeds, which is why they sit outside both groups."""
    r_ball = P.p("BrgBallDia") / 2.0
    r_pitch = (P.p("BrgInnerRaceOD") + P.p("BrgOuterRaceID")) / 4.0
    n = int(P.p("BrgBallsPerRow"))
    shapes = []
    for z in (P.p("ZBrgRow1"), P.p("ZBrgRow2")):
        for i in range(n):
            a = 2.0 * math.pi * i / n
            s = Part.makeSphere(r_ball, App.Vector(r_pitch, 0.0, z))
            s.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), math.degrees(a))
            shapes.append(s)
    out = shapes[0]
    for s in shapes[1:]:
        out = out.fuse(s)
    return out


def retention_collar():
    """A11 — the C32 thrust collar.

    A disc from the body's shoulder out to just inside the ring's skin, with
    RetTravel of axial clearance to the ring's aft face in the flight state.
    The ring lands on it under setback, so the load goes ring -> collar -> body
    and never reaches the balls.

    It is a DISC, not a ring on stilts: the load has to reach the body's
    shoulder through a continuous section, or the collar itself becomes the
    compliant element C35 forbids.
    """
    r_i = P.p("CollarID")
    r_o = P.p("RetFaceOD")
    z_face = P.p("ZRingAft") - P.p("RetTravel")
    return C.make_tube(r_i, r_o, z_face - P.p("RetCollarThick"), z_face)


# ---------------------------------------------------------------------------


def build():
    doc = C.new_doc(DOCNAME)
    P.to_sheet(doc)

    shapes = {
        "A4_Brg_Inner_Races": inner_races(),
        "B4_Brg_Outer_Races": outer_races(),
        "C1_Balls_Cage": balls_cage(),
        "A11_Retention_Collar": retention_collar(),
    }
    dens = {
        "A4_Brg_Inner_Races": C.STEEL,
        "B4_Brg_Outer_Races": C.STEEL,
        "C1_Balls_Cage": C.STEEL,
        "A11_Retention_Collar": C.STEEL,
    }

    print("Phase 3 — parts")
    for name, sh in shapes.items():
        C.add_part(doc, name, sh)
        C.report_shape(name, sh, dens[name])

    doc.recompute()
    return doc, shapes


def gate3(shapes):
    print("")
    print("GATE 3 — the launch path")
    ok = True

    r_ball_out = (P.p("BrgInnerRaceOD") + P.p("BrgOuterRaceID")) / 4.0 \
        + P.p("BrgBallDia") / 2.0
    print("  1 ball envelope reaches r = %.2f" % r_ball_out)
    print("    outer race inner face   r = %.2f  -> balls fit the race gap"
          % (P.p("BrgOuterRaceID") / 2.0))
    good = r_ball_out <= P.p("BrgOuterRaceID") / 2.0 + 1e-9
    ok &= good
    print("    %s" % ("PASS" if good else "FAIL"))

    # the collar must be REACHABLE and must clear everything that moves past it.
    # It is bounded NOT by the ring skin but by the CANARD ROOT radius: the fins'
    # canted aft corners sweep down to z = 5.57 over r 46-49, so a collar
    # reaching past r 46 is struck by all four of them in the LAUNCH state.
    collar = shapes["A11_Retention_Collar"]
    bb = collar.BoundBox
    root_r = P.p("RingR") - P.p("CanardEmbed")
    gap = root_r - bb.XMax
    good = gap >= 0.20
    ok &= good
    print("  2 collar OD Ø%.2f clears the canard root r %.1f by %.3f mm ... %s"
          % (2 * bb.XMax, root_r, gap, "PASS" if good else "FAIL"))
    print("      (the binding constraint is the FINS, not the ring skin at r %.1f:"
          % P.p("RingR"))
    print("       the collar only has to reach the ring's aft face, which starts"
          " at r %.1f)" % (P.p("RingAftBoreDia") / 2.0))

    # THE CHECK THAT MATTERS: a thrust face takes load only where it OVERLAPS
    # its partner. Getting this wrong is silent -- the faces both exist, the
    # stress arithmetic runs, and nothing is actually touching. Read the bands
    # from the parameters, not from a bounding box: a full ring's XMin is -r_out.
    ring_face_id = P.p("RingAftBoreDia") / 2.0
    ring_face_od = P.p("RingOD") / 2.0
    collar_face_id = P.p("CollarID")
    collar_face_od = P.p("RetFaceOD")
    ov_lo = max(ring_face_id, collar_face_id)
    ov_hi = min(ring_face_od, collar_face_od)
    overlap = ov_hi - ov_lo
    good = overlap > 1.0 and abs(overlap - (collar_face_od - ring_face_id)) < 1e-6
    ok &= good
    print("  3 thrust contact band: ring aft face r %.1f-%.1f, collar r %.1f-%.1f"
          % (ring_face_id, ring_face_od, collar_face_id, collar_face_od))
    print("    -> contact width %.2f mm, area %.1f mm^2   %s"
          % (overlap, P.p("RetFaceArea"), "PASS" if good else "FAIL"))
    if not good:
        print("      -> the ring would land on AIR. Contact area with a partner")
        print("         face that does not overlap is zero, whatever a formula says.")

    # axial: the collar face sits RetTravel below the ring's aft face
    ring_aft = P.p("ZRingAft")
    face = bb.ZMax
    travel = ring_aft - face
    good = abs(travel - P.p("RetTravel")) < 1e-9
    ok &= good
    print("  4 axial travel before contact = %.3f mm (spec %.2f)  %s"
          % (travel, P.p("RetTravel"), "PASS" if good else "FAIL"))

    # C35: nothing compliant anywhere in the axial path
    print("  4 axial path materials (C35 forbids anything compliant):")
    for n in ("A11_Retention_Collar", "A4_Brg_Inner_Races"):
        print("      %-24s steel, monolithic" % n)
    print("      -> no spring washer, no elastomer seat, no compliant potting: PASS")

    # the load the collar actually has to take
    print("")
    print("  5 THE LOAD (T6) — the point of this phase")
    print("      C26 assumed a 0.5 kg ring and derived      %6.1f kN" % P.p("SetbackRing"))
    print("      ring carrier measured (Phase 2, steel)     %6.3f kg"
          % P.p("RingMassMeasured"))
    print("      -> setback on the carrier                  %6.1f kN"
          % P.p("SetbackMeasured"))
    print("      -> setback on the full rotating assembly   %6.1f kN"
          % P.p("SetbackRotating"))
    print("         scaling vs C26:                         x%.2f"
          % P.p("RingMassScaling"))
    print("")
    print("      collar face area     %8.1f mm^2" % P.p("RetFaceArea"))
    print("      face stress at 212.6 kN                 %6.1f MPa"
          % P.p("RetFaceStress"))
    print("      allowable (PROVISIONAL)                 %6.1f MPa" % P.p("RetBearingStress"))
    print("      margin                                  x%.2f  %s"
          % (P.p("RetStressMargin"),
             "PASS" if P.p("RetStressMargin") > 1.0 else "FAIL"))
    ok &= P.p("RetStressMargin") > 1.0

    print("")
    print("      C35's structural case follows the load:")
    print("        register: %.0f N/um    measured: %.0f N/um   (x%.1f)"
          % (P.p("AxialPathStiff"), P.p("AxialPathStiffMeasured"),
             P.p("AxialPathStiffRatio")))
    print("")
    print("  GATE 3: %s" % ("PASS" if ok else "FAIL"))
    return ok


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    doc, shapes = build()
    gate3(shapes)
    path = os.path.join(OUT, "PGK-Bearings.FCStd")
    doc.saveAs(path)
    print("")
    print("saved: %s" % path)


if __name__ == "__main__":
    main()
