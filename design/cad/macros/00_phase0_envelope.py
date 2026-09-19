"""
Phase 0 — envelope and reference platform.

Creates the document that every later phase is measured against:

    PGK-Envelope
      Params                 the SSOT spreadsheet (pgk_params.to_sheet)
      Ref_Shell_155mm        tangent-ogive nose, body, boattail, fuze-well cavity
      Ref_Booster_Cavity     the cavity below the well
      Env_Bore_155mm         the in-bore limit (C31 / P14)
      Env_TrainBore_30mm     the F9 keep-out cylinder
      Env_OgiveBound         P8's table as a solid of revolution (the bound the
                             register's §5 note argues about -- see pgk_params
                             STATIONS header)

Gate 0: the reference shell must reproduce P8's own table at all six published
stations within +/-0.5 mm, or nothing downstream is trustworthy.

Run from the FreeCAD MCP bootstrap, or directly:
    freecadcmd 00_phase0_envelope.py
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

# FreeCAD keeps a long-lived interpreter, so a cached pgk_params from an earlier
# macro run would silently shadow an edited SSOT. Always re-read it.
sys.modules.pop("pgk_params", None)
import pgk_params as P  # noqa: E402

DOCNAME = "PGK-Envelope"
OUT = os.path.join(CAD, "out")

# P8's published table: (station aft of the seat, shell diameter)
P8_TABLE = [
    (0.0, 50.8),
    (20.0, 61.9),
    (40.0, 72.4),
    (60.0, 82.2),
    (80.0, 91.4),
    (95.0, 97.9),
    (370.0, 154.9),
]


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def ogive_radius(ztip_from_tip):
    """Tangent-ogive radius at distance `ztip_from_tip` from the theoretical tip."""
    rho = P.p("OgiveRho")
    Ln = P.p("OgiveLen")
    R = P.p("ShellBodyDia") / 2.0
    s = Ln - ztip_from_tip
    if s > rho:
        s = rho
    return math.sqrt(max(rho * rho - s * s, 0.0)) + R - rho


def make_revolve(profile_rz, solid=True):
    """Revolve a closed (radius, z) profile about +Z and return the Shape."""
    pts = [App.Vector(r, 0.0, z) for (r, z) in profile_rz]
    edges = [Part.makeLine(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    wire = Part.Wire(edges)
    shape = wire.revolve(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 360.0)
    if solid:
        try:
            shape = Part.Solid(shape)
        except Exception:
            pass
    return shape


def revolve(profile_rz, name, doc, solid=True, color=None):
    """Revolve a profile and add it to `doc` under `name`."""
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = make_revolve(profile_rz, solid)
    if color is not None and hasattr(obj, "ViewObject"):
        obj.ViewObject.ShapeColor = color
    return obj


def new_doc(name):
    """Fresh document. FreeCAD normalises '-' to '_' in internal names, so match
    on the prefix rather than on an exact label or the old doc survives and the
    new one is created as `...1`."""
    for n in list(App.listDocuments()):
        if n.startswith(name.replace("-", "_")):
            App.closeDocument(n)
    return App.newDocument(name)


# ---------------------------------------------------------------------------
# build
# ---------------------------------------------------------------------------


def build():
    doc = new_doc(DOCNAME)

    # --- the SSOT ---------------------------------------------------------
    P.to_sheet(doc)

    # --- reference shell outer contour ------------------------------------
    # ogive: from the seat (z = 0) aft to the end of the ogive
    z_seat = P.p("ZSeat")
    z_ogive_end = z_seat - (P.p("OgiveLen") - P.p("SeatFromTip"))
    r_body = P.p("ShellBodyDia") / 2.0
    r_trunc = P.p("OgiveTruncDia") / 2.0

    # 120 segments over 370 mm of ogive is a chord deviation of under 1 micron
    # on a 1342 mm radius -- far below P8's own 0.1 mm resolution -- and keeps
    # the boolean cut of the well off the slow path.
    N = 120
    ogive_pts = []
    for i in range(N + 1):
        z = z_seat + (z_ogive_end - z_seat) * (i / N)
        x = P.p("SeatFromTip") - z          # distance from the theoretical tip
        ogive_pts.append((ogive_radius(x), z))
    # ensure the first point sits exactly on the truncation diameter
    ogive_pts[0] = (r_trunc, z_seat)

    z_base = P.p("SeatFromTip") - P.p("ShellTotalLen")
    boattail_len = 60.0
    z_boattail = z_ogive_end - (abs(z_ogive_end - z_base) - boattail_len)
    r_base = 140.9 / 2.0                     # S6 ERFB/BB base diameter

    outer = list(ogive_pts)
    outer.append((r_body, z_boattail))       # cylinder aft
    outer.append((r_base, z_base))           # boattail
    outer.append((0.0, z_base))              # base face to axis
    outer.append((0.0, z_seat))              # axis forward to the seat
    outer.append((r_trunc, z_seat))          # seat face out to the bore mouth

    shell = revolve(outer, "Ref_Shell_155mm", doc)

    # --- fuze-well cavity ---------------------------------------------------
    # z = 0 is the shell's MOUTH plane (where the ogive truncates). The shell's
    # thread is cut BELOW it, then the bore steps down to the seat annulus the
    # kit's shoulder bears on, then the plain well runs to the intrusion limit.
    # That ordering is what makes P6's seat annulus a real face rather than an
    # assumed area.
    r_thread = P.p("WellThreadMajDia") / 2.0
    r_well = P.p("WellBoreDia") / 2.0
    z_thread_root = P.p("ZThreadRoot")           # -19.05, = the seat plane
    z_well_bot = P.p("ZWellBottom")
    z_boost_bot = z_well_bot - 55.0
    r_boost = 15.0                               # booster cavity, on the axis (F9)

    well_prof = [
        (0.0, z_boost_bot),
        (r_boost, z_boost_bot),
        (r_boost, z_boost_bot + 20.0),
        (r_well, z_well_bot),
        (r_well, z_thread_root),                 # up to the seat plane
        (r_thread, z_thread_root),               # seat annulus, faces +Z
        (r_thread, z_seat + 0.001),              # threaded bore, up to the mouth
        (0.0, z_seat + 0.001),
    ]
    shell.Shape = shell.Shape.cut(make_revolve(well_prof))

    # --- envelopes ---------------------------------------------------------
    bore_r = 155.0 / 2.0
    z_bore_fore, z_bore_aft = 140.0, -780.0
    bore_prof = [
        (0.0, z_bore_aft), (bore_r, z_bore_aft),
        (bore_r, z_bore_fore), (0.0, z_bore_fore),
    ]
    bore = revolve(bore_prof, "Env_Bore_155mm", doc)

    train_r = P.p("StatorBoreDia") / 2.0
    z_tr_aft = z_well_bot
    z_tr_fore = P.p("ZFrontHubFore")
    train_prof = [
        (0.0, z_tr_aft), (train_r, z_tr_aft),
        (train_r, z_tr_fore), (0.0, z_tr_fore),
    ]
    train = revolve(train_prof, "Env_TrainBore_30mm", doc)

    # --- P8's table as a solid, for the containment argument ---------------
    # Mirrored forward from the seat: the reading pgk_params discusses.
    bound = [(0.0, z_seat), (r_trunc, z_seat)]
    for (st, dia) in P8_TABLE[1:]:
        bound.append((dia / 2.0, z_seat + st))
    bound.append((0.0, z_seat + P8_TABLE[-1][0]))
    revolve(bound, "Env_OgiveBound", doc, color=(0.9, 0.4, 0.2))

    doc.recompute()
    return doc


# ---------------------------------------------------------------------------
# Gate 0 — verify the shell against P8's table
# ---------------------------------------------------------------------------


def gate0(doc):
    shell = doc.getObject("Ref_Shell_155mm")
    print("")
    print("GATE 0 — reference shell vs P8's published table")
    print("  %-12s %-12s %-12s %-10s" % ("station mm", "P8 dia mm", "model dia mm", "delta mm"))
    worst = 0.0
    for (st, dia) in P8_TABLE:
        z = P.p("ZSeat") - st                # P8's stations are AFT of the seat
        x = P.p("SeatFromTip") - z
        model_r = ogive_radius(x) if st < P.p("OgiveLen") - P.p("SeatFromTip") else P.p("ShellBodyDia") / 2.0
        model_dia = 2.0 * model_r
        delta = model_dia - dia
        worst = max(worst, abs(delta))
        print("  %-12.1f %-12.1f %-12.2f %+-10.3f" % (st, dia, model_dia, delta))
    print("  worst |delta| = %.3f mm   ->  %s"
          % (worst, "PASS" if worst <= 0.5 else "FAIL"))

    # independent check on the solid itself, at the seat and at the ogive end
    bb = shell.Shape.BoundBox
    print("  shell bbox: Z %.2f .. %.2f   Rmax %.2f" % (bb.ZMin, bb.ZMax, bb.XMax))
    print("  shell volume = %.1f cm^3" % (shell.Shape.Volume / 1000.0))

    # P6 flank-area cross-check, from the kit's own future thread geometry
    print("  thread: pitch %.4f mm, pitch dia %.4f mm, flank area %.4f e-3 m^2"
          % (P.p("WellPitch"), P.p("WellPitchDia"), P.p("WellFlankArea") / 1000.0))
    print("          P6's own figure       1.1200 e-3 m^2  ->  %.2f %% agreement"
          % (100.0 * abs(P.p("WellFlankArea") - P.p("WellFlankAreaP6")) / P.p("WellFlankAreaP6")))

    # The well's two thermal areas, now real faces in the solid rather than
    # assumed numbers. P6's own figures are quoted alongside.
    print("")
    print("  P6 THERMAL AREAS (model vs register)")
    print("    seat annulus   : %.4f e-3 m^2   vs P6 %.4f e-3 m^2"
          % (P.p("WellSeatArea") / 1000.0, P.p("WellSeatAreaP6") / 1000.0))
    print("    well bore      : %.4f e-3 m^2   vs P6 %.4f e-3 m^2   (%.1f %% low)"
          % (P.p("WellBoreArea") / 1000.0, P.p("WellBoreAreaP6") / 1000.0,
             100.0 * (P.p("WellBoreAreaP6") - P.p("WellBoreArea")) / P.p("WellBoreAreaP6")))
    print("    seat ID that P6's own 0.5e-3 m^2 figure implies: %.2f mm "
          "(model uses WellBoreDia = %.2f)"
          % (P.p("WellSeatIDImpliedByP6"), P.p("WellBoreDia")))
    print("    -> the two P6 figures cannot both hold; the model adopts the "
          "self-consistent 44 mm and reports the area it costs")

    print("")
    print("  NOTE: this shell is a CONTOUR model, not a mass model. Its solid volume")
    print("        is not the projectile's mass -- P2/P3/P4/P5 come from the")
    print("        calibrated model in 02-reference-155mm-model.md and are carried")
    print("        in Params. Do not quote a mass from this solid.")
    return worst


# ---------------------------------------------------------------------------


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    doc = build()
    gate0(doc)
    path = os.path.join(OUT, "PGK-Envelope.FCStd")
    doc.saveAs(path)
    print("")
    print("saved: %s" % path)
    print("objects: %s" % ", ".join(o.Name for o in doc.Objects))


if __name__ == "__main__":
    main()
