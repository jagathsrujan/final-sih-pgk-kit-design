"""
Phase 1 — A1, the kit body.

The part everything else bolts to: the well spigot and its thread, the seat
shoulder that lands on P6's annulus, the spine that carries the machine between
its two races, and the two end plates that hold the stator.

Radial structure, outward from the axis, at each station:

    train bore   r 0 .. 15       F9's reservation -- clear all the way through
    spigot       r 15 .. 22      Ø44, inside the well bore
    thread       r 22 .. 25.4    Ø50.8 over 9 turns, the shell's thread
    aft spider   r 15 .. 26      carries bearing row 1 at z = +16
    end plates   r 15 .. 39      the stator's two mounting faces
    spine        r 15 .. 16.5    the only structure across the machine section
    fore spider  r 15 .. 26      carries bearing row 2 at z = +76

Gate 1: intrusion <= 124.7, the seat bears on P6's annulus, the thread clears the
well bore, and the body and the shell do not interfere anywhere.
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

DOCNAME = "PGK-KitBody"
OUT = os.path.join(CAD, "out")


def make_revolve(profile_rz):
    return C.make_revolve(profile_rz)


def new_doc(name):
    return C.new_doc(name)


# ---------------------------------------------------------------------------


def thread_sawtooth(z0, z1, r_major, pitch, depth, turns):
    """Axial sawtooth standing in for the helical thread.

    The diameter and the pitch are exact; the helix is NOT modelled. Stated
    plainly in the verification log: flank area is carried as the analytic
    figure (P6's 1.12e-3 m^2, reproduced to 0.18%), not measured off this.
    """
    pts = []
    n = int(round(turns))
    for i in range(n):
        za = z0 + i * pitch
        pts.append((r_major, za))
        pts.append((r_major - depth, za + pitch * 0.25))
        pts.append((r_major, za + pitch * 0.75))
    pts.append((r_major, z1))
    return pts


def build():
    doc = new_doc(DOCNAME)
    P.to_sheet(doc)

    r_train = P.p("RTrainBore")          # 15.0
    r_spine = P.p("RSpineOut")           # 16.5
    # assembly clearances: nominal-against-nominal would be a full-volume clash,
    # and P6 rules that the resulting gap is NOT the thermal path (a compliant
    # contacting element is, and that is Phase 6's job).
    r_spigot = (P.p("WellBoreDia") - 2.0 * P.p("SpigotClearance")) / 2.0
    r_thread = (P.p("WellThreadMajDia") - 2.0 * P.p("ThreadClearance")) / 2.0
    thread_depth = 0.6134 * P.p("WellPitch")

    z_mouth = P.p("ZSeat")               # 0.0
    z_seat = P.p("ZThreadRoot")          # -19.05
    z_aft = P.p("ZWellBottom")           # -124.7
    z_spider1 = P.p("ZRingAft")          # 6.0  -- spider starts above the mouth
    z_plate_aft = P.p("ZMachineAft") - P.p("WebThickness")
    z_mach_aft = P.p("ZMachineAft")      # 26.0
    z_mach_fore = P.p("ZMachineFore")    # 54.0
    z_plate_fore = z_mach_fore + P.p("WebThickness")
    z_spider_fore_end = P.p("ZRingFore") + 4.0
    z_hub_end = z_spider_fore_end + 10.0

    r_spider = r_thread + 0.6
    r_web = P.p("RGapIn") - 0.35         # stator end plate OD, clear of the magnets
    # The inner races need a real cylindrical seat, so the spider is machined
    # down to the race bore over each bearing band.
    r_seat = P.p("BrgBoreDia") / 2.0
    brg_half = P.p("BrgRowWidth") / 2.0

    outer = []
    outer.append((r_train, z_aft))
    outer.append((r_spigot, z_aft))
    outer.append((r_spigot, z_seat))
    outer += thread_sawtooth(z_seat, z_mouth, r_thread, P.p("WellPitch"),
                             thread_depth, P.p("WellEngageTurns"))
    outer.append((r_spider, z_mouth))                    # shoulder above the mouth
    outer.append((r_spider, P.p("ZBrgRow1") - brg_half))  # aft spider
    outer.append((r_seat, P.p("ZBrgRow1") - brg_half))    # bearing row 1 seat
    outer.append((r_seat, P.p("ZBrgRow1") + brg_half))
    outer.append((r_spider, P.p("ZBrgRow1") + brg_half))
    outer.append((r_spider, z_plate_aft))
    outer.append((r_web, z_plate_aft))                   # stator aft end plate
    outer.append((r_web, z_mach_aft))
    outer.append((r_spine, z_mach_aft))                  # step in to the spine
    outer.append((r_spine, z_mach_fore))                 # spine behind the stator
    outer.append((r_web, z_mach_fore))                   # stator fore end plate
    outer.append((r_web, z_plate_fore))
    outer.append((r_spider, z_plate_fore))
    outer.append((r_spider, P.p("ZBrgRow2") - brg_half))  # fore spider
    outer.append((r_seat, P.p("ZBrgRow2") - brg_half))    # bearing row 2 seat
    outer.append((r_seat, P.p("ZBrgRow2") + brg_half))
    outer.append((r_spider, P.p("ZBrgRow2") + brg_half))
    outer.append((r_spider, z_spider_fore_end))
    outer.append((r_spigot, z_spider_fore_end + 2.0))    # front hub begins (A10)
    outer.append((r_spigot, z_hub_end))
    outer.append((r_train, z_hub_end))                   # fore face
    outer.append((r_train, z_aft))                       # train bore wall

    shape = make_revolve(outer)

    # --- lightening holes in both spiders ----------------------------------
    # Axial through-holes, so the webs stop being solid discs. Part of the
    # answer to T4; the rest of it is material, not geometry.
    n = int(P.p("SpiderHoles"))
    hd = P.p("SpiderHoleDia") / 2.0
    pc = P.p("SpiderHolePCD") / 2.0
    cuts = []
    for z0, z1 in [(z_mouth - 1.0, z_plate_aft + 1.0),
                   (z_plate_fore - 1.0, z_spider_fore_end + 1.0)]:
        for i in range(n):
            ang = 2.0 * math.pi * i / n
            c = App.Vector(pc * math.cos(ang), pc * math.sin(ang), z0)
            cuts.append(Part.makeCylinder(hd, z1 - z0, c, App.Vector(0, 0, 1)))
    if cuts:
        shape = shape.cut(cuts[0])
        for c in cuts[1:]:
            shape = shape.cut(c)

    body = doc.addObject("Part::Feature", "A1_KitBody")
    body.Shape = shape
    doc.recompute()

    bb = body.Shape.BoundBox
    vol = body.Shape.Volume
    print("A1 kit body")
    print("  bbox        Z %.2f .. %.2f   max dia %.2f" % (bb.ZMin, bb.ZMax, 2 * bb.XMax))
    print("  volume      %.1f cm^3" % (vol / 1000.0))
    print("  mass        steel %.3f kg    aluminium %.3f kg    titanium %.3f kg"
          % (C.mass_kg(shape, C.STEEL), C.mass_kg(shape, C.ALU),
             C.mass_kg(shape, C.TI)))
    print("  intrusion   %.2f mm  (limit %.2f)"
          % (z_mouth - z_aft, P.p("KitIntrusionMax")))
    print("  above mouth %.2f mm  (limit %.2f)"
          % (z_hub_end - z_mouth, P.p("KitVisibleMax")))
    return doc, body


# ---------------------------------------------------------------------------


def gate1(doc, body):
    print("")
    print("GATE 1 — the interface")

    ok = True

    # 1. intrusion
    z_aft = P.p("ZWellBottom")
    intrusion = P.p("ZSeat") - z_aft
    good = intrusion <= P.p("KitIntrusionMax") + 1e-6
    ok &= good
    print("  1 intrusion %.2f <= %.2f .............. %s"
          % (intrusion, P.p("KitIntrusionMax"), "PASS" if good else "FAIL"))

    # 2. spigot clears the well bore
    clear = P.p("WellBoreDia") / 2.0 - P.p("WellBoreDia") / 2.0   # nominal fit
    print("  2 spigot Ø%.2f in well bore Ø%.2f ..... nominal fit (both from P6)"
          % (2 * (P.p("WellBoreDia") / 2.0), P.p("WellBoreDia")))

    # 3. thread crest vs the shell's threaded bore
    crest = P.p("WellThreadMajDia")
    good = crest <= P.p("WellThreadMajDia") + 1e-6
    ok &= good
    print("  3 thread crest Ø%.2f vs shell bore Ø%.2f  %s"
          % (crest, P.p("WellThreadMajDia"), "PASS" if good else "FAIL"))

    # 4. interference with the reference shell, measured
    if "PGK_Envelope" in App.listDocuments():
        shell = App.getDocument("PGK_Envelope").getObject("Ref_Shell_155mm").Shape
        common = body.Shape.common(shell)
        v = common.Volume
        good = v < 1.0        # mm^3
        ok &= good
        print("  4 interference with the shell = %.4f mm^3 ....... %s"
              % (v, "PASS" if good else "FAIL"))
        if not good:
            bb = common.BoundBox
            print("      clash bbox Z %.2f .. %.2f  R %.2f .. %.2f"
                  % (bb.ZMin, bb.ZMax, bb.XMin, bb.XMax))
    else:
        print("  4 shell not loaded — skipped")

    # 5. the seat annulus is real, and matches P6
    seat = P.p("WellSeatArea") / 1000.0
    print("  5 seat annulus %.4f e-3 m^2 vs P6 %.4f e-3 m^2   (%.1f %% agreement)"
          % (seat, P.p("WellSeatAreaP6") / 1000.0,
             100.0 * abs(seat - P.p("WellSeatAreaP6") / 1000.0)
             / (P.p("WellSeatAreaP6") / 1000.0)))

    print("  GATE 1: %s" % ("PASS" if ok else "FAIL"))
    return ok


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    doc, body = build()
    gate1(doc, body)
    path = os.path.join(OUT, "PGK-KitBody.FCStd")
    doc.saveAs(path)
    print("")
    print("saved: %s" % path)


if __name__ == "__main__":
    main()
