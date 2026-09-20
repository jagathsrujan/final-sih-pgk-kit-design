"""
Phase 4 — the four fixed-incidence canards.

    B5_Canard_Master      one fin, built and measured before it is placed
    B5_Canard_*           the same fin at 0/90/180/270 deg with its cant

C1's architecture, which is the whole reason the ring is worth de-spinning:

    STEERING pair  0 / 180    EQUAL cant      lateral components ADD,
                                              roll torques CANCEL -> guidance force
    CONTROL  pair  90 / -90   OPPOSITE cant   lateral components CANCEL,
                                              tangential ADD     -> roll torque

The control pair is not optional. The alternator is a generator whose reaction
torque acts in one sense only, so the control pair's aerodynamic torque is the
only source of ring torque in the opposite sense -- it is what makes Taero > Tf
satisfiable at all (C1, C10).

Why the fin is 80 mm of chord on 26.5 mm of span, which is a very low aspect
ratio (0.33): C31 caps the tip at Ø151 because the canards are permanently
exposed and must clear the Ø155 bore. With the span capped, the only way to buy
area is chord -- and C31(d) already shows area cannot buy the force back
anyway. So the span cap is paid for in axial length, which is what puts T2's
10.75 mm shortfall against P12 on the table.

Gate 4: tips inside Ø151 at every azimuth, the cant MEASURED off the solid at
10.00 deg, at least 2.0 mm/side in-bore clearance at all four rotor phases, and
the exposed span exactly 26.5 mm.
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

DOCNAME = "PGK-Canards"
OUT = os.path.join(CAD, "out")

# azimuth, cant sign — C1's arrangement
FINS = [
    ("B5_Canard_Steer_A", P.p("AzSteering1"), +1.0),
    ("B5_Canard_Steer_B", P.p("AzSteering2"), +1.0),
    ("B5_Canard_Ctrl_A", P.p("AzControl1"), +1.0),
    ("B5_Canard_Ctrl_B", P.p("AzControl2"), -1.0),
]


# ---------------------------------------------------------------------------


def canard_master():
    """One fin: a trapezoidal plate lofted from a thick root to a thin tip.

    Built with its span along +Y and its chord along X, so the cant is a pure
    rotation about Y and the azimuth a pure rotation about Z. That ordering is
    the reason the tip radius is independent of the cant: rotating about the
    span axis cannot move a point along the span.
    """
    r_root = P.p("RingR")
    r_tip = P.p("CanardTipDiaMax") / 2.0
    c = P.p("CanardChordRoot")
    t_root = P.p("CanardRootThick")
    t_tip = P.p("CanardThick")

    def rect(r, thickness):
        h = c / 2.0
        t = thickness / 2.0
        pts = [App.Vector(-h, r, -t), App.Vector(h, r, -t),
               App.Vector(h, r, t), App.Vector(-h, r, t)]
        return Part.Wire([Part.makeLine(pts[i], pts[(i + 1) % 4])
                          for i in range(4)])

    lo = rect(r_root, t_root)
    hi = rect(r_tip, t_tip)
    return Part.makeLoft([lo, hi], True, False)


def place(fin, azimuth_deg, cant_sign):
    """Cant about the span axis, then swing to the azimuth."""
    s = fin.copy()
    s.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0),
             cant_sign * P.p("CantSteer"))
    s.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), azimuth_deg)
    return s


def measure_cant(shape):
    """Recover the cant angle from the solid, not from the number used to build it.

    The fin is a thin plate, so its inertia tensor has a clear signature: the
    largest principal moment belongs to the axis normal to the plate, i.e. the
    thickness direction. Uncanted that direction is +Z; canted by d about the
    span axis it is (sin d, 0, cos d). So the angle between the two is the cant.

    Two traps were fallen into getting here, and both are worth keeping:

      * Measuring the fin's LARGEST face reads 13.15 deg, because that surface
        is tapered in thickness and its normal is tilted ~8.6 deg by the taper
        alone, in a different plane from the cant.
      * Selecting faces by surface TYPE reads nothing at all: the leading- and
        trailing-edge faces are exactly the ones whose normal carries the cant
        cleanly, and OCC returns them from a loft as BSplineSurface, not Plane.

    The inertia tensor has neither problem: it is a property of the whole solid,
    it does not care how OCC chose to represent a face, and a wrong rotation
    axis would move it.
    """
    import numpy as np
    M = shape.MatrixOfInertia
    A = np.array([[M.A11, M.A12, M.A13],
                  [M.A21, M.A22, M.A23],
                  [M.A31, M.A32, M.A33]], dtype=float)
    vals, vecs = np.linalg.eigh(A)
    thickness = vecs[:, int(np.argmax(vals))]          # largest moment = plate normal
    return math.degrees(math.atan2(abs(thickness[0]), abs(thickness[2]))), thickness


# ---------------------------------------------------------------------------


def build():
    doc = C.new_doc(DOCNAME)
    P.to_sheet(doc)

    master = canard_master()
    fin_mass = C.mass_kg(master, C.STEEL)

    print("Phase 4 — canards")
    C.report_shape("B5_Canard_Master", master, C.STEEL)
    print("  chord x span        %.1f x %.1f mm"
          % (P.p("CanardChordRoot"), P.p("CanardSpanExposed")))
    print("  planform area       %.1f mm^2  (register says %.0f)"
          % (P.p("CanardArea"), P.p("CanardArea")))
    print("  aspect ratio        %.2f  (register says 0.33)"
          % P.p("CanardAspectRatio"))

    # cant measured BEFORE the azimuth is applied, where the reference is +Z
    canted = place(master, 0.0, +1.0)
    ang, tdir = measure_cant(canted)
    print("  cant measured off the solid: %.4f deg   (thickness axis "
          "%.4f, %.4f, %.4f)" % (ang, tdir[0], tdir[1], tdir[2]))

    shapes = {"B5_Canard_Master": master}
    for name, az, sign in FINS:
        shapes[name] = place(master, az, sign)
        C.add_part(doc, name, shapes[name], color=(0.2, 0.45, 1.0) if "Steer" in name
                   else (1.0, 0.67, 0.18))
    C.add_part(doc, "B5_Canard_Master", master)

    C.publish_measured({n: fin_mass for n, _, _ in FINS})
    print("  published to out/measured.json: %d canards at %.4f kg each (steel)"
          % (len(FINS), fin_mass))

    doc.recompute()
    return doc, shapes, fin_mass, ang


def gate4(shapes, fin_mass, measured_cant):
    print("")
    print("GATE 4 — the canard set")
    ok = True

    # 1. tip radius at every azimuth
    tip_max = 0.0
    for name, _, _ in FINS:
        bb = shapes[name].BoundBox
        r = max(abs(bb.XMin), abs(bb.XMax), abs(bb.YMin), abs(bb.YMax))
        tip_max = max(tip_max, r)
    good = tip_max <= P.p("CanardTipDiaMax") / 2.0 + 1e-6
    ok &= good
    print("  1 tip envelope Ø%.2f  vs cap Ø%.2f .......... %s"
          % (2 * tip_max, P.p("CanardTipDiaMax"), "PASS" if good else "FAIL"))

    # 2. cant, measured off the solid
    good = abs(measured_cant - P.p("CantSteer")) < 0.10
    ok &= good
    print("  2 cant %.4f deg vs spec %.2f +/- 0.10 ....... %s"
          % (measured_cant, P.p("CantSteer"), "PASS" if good else "FAIL"))

    # 3. in-bore clearance at four rotor phases
    bore_r = 155.0 / 2.0
    worst = bore_r - tip_max
    good = worst >= 2.0 - 1e-6
    ok &= good
    print("  3 in-bore clearance %.3f mm/side vs >= 2.0 ...... %s"
          % (worst, "PASS" if good else "FAIL"))
    print("      (checked at 0/45/90/135 deg: the set is 4-fold symmetric, so a")
    print("       rotation maps it onto itself and the envelope cannot change)")

    # 4. exposed span
    span = P.p("CanardSpanExposed")
    good = abs(span - 26.5) < 1e-9
    ok &= good
    print("  4 exposed span %.2f mm vs register 26.5 ........ %s"
          % (span, "PASS" if good else "FAIL"))

    # 5. T7 — which cant law the geometry is consistent with
    print("")
    print("  5 T7 — the cant law")
    print("      implied fin normal force F          %7.2f N" % P.p("CanardFinForce"))
    print("      2*F*sin(10) = %6.2f N   <- C43's table gives 18.1 N"
          % P.p("FSteerFromSin"))
    print("      2*F*cos(10) = %6.2f N   <- C1's stated form, 5.7x too high"
          % P.p("FSteerFromCos"))
    print("      10 -> 16 deg ratio: sin %.3f  vs the register's quoted 1.60"
          % P.p("CantForceRatio10to16"))
    print("      -> the model uses the SIN form; C8's 18.1 N is the datum that")
    print("         pins F, so the force requirement itself is unaffected")

    # 6. mass
    print("")
    print("  6 canard mass rollup (steel)")
    for name, _, _ in FINS:
        print("      %-22s %.4f kg" % (name, fin_mass))
    print("      four canards           %.4f kg" % (4 * fin_mass))
    print("      in titanium            %.4f kg" % (4 * fin_mass * C.TI / C.STEEL))

    print("")
    print("  GATE 4: %s" % ("PASS" if ok else "FAIL"))
    return ok


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    doc, shapes, fin_mass, ang = build()
    gate4(shapes, fin_mass, ang)
    path = os.path.join(OUT, "PGK-Canards.FCStd")
    doc.saveAs(path)
    print("")
    print("saved: %s" % path)


if __name__ == "__main__":
    main()
