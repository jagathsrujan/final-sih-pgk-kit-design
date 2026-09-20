"""
DRISHTI-PGK — shared CAD helpers.

Extracted so the geometry helpers exist in one place. The bug that prompted it:
`Part.Wire()` does NOT close a wire for you, so a profile whose last point does
not coincide with its first revolves into an open SHELL. An open shell is not a
solid, booleans silently cut nothing, and `isInside` answers nonsense -- which
is exactly the kind of quiet wrongness this workspace exists to prevent.

Every macro should build geometry through these helpers.
"""

import math
import os
import sys

import FreeCAD as App
import Part

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

EPS = 1e-9


def params():
    """Import the SSOT, always freshly.

    FreeCAD keeps a long-lived interpreter, so a cached pgk_params from an
    earlier macro run would silently shadow an edited source of truth.
    """
    sys.modules.pop("pgk_params", None)
    import pgk_params
    return pgk_params


def make_revolve(profile_rz, axis_start=None, axis_dir=None):
    """Revolve a CLOSED (radius, z) profile 360 deg about +Z and return a solid.

    The profile is closed automatically, consecutive duplicates are dropped
    (a zero-length edge is an OCC error), and the result is forced to a Solid.
    """
    clean = []
    for pt in profile_rz:
        if not clean or (abs(pt[0] - clean[-1][0]) > EPS
                         or abs(pt[1] - clean[-1][1]) > EPS):
            clean.append(pt)
    if len(clean) < 3:
        raise ValueError("profile needs at least 3 distinct points")
    if abs(clean[0][0] - clean[-1][0]) > EPS or abs(clean[0][1] - clean[-1][1]) > EPS:
        clean.append(clean[0])

    a0 = axis_start if axis_start is not None else App.Vector(0, 0, 0)
    ad = axis_dir if axis_dir is not None else App.Vector(0, 0, 1)
    pts = [App.Vector(r, 0.0, z) for (r, z) in clean]
    edges = [Part.makeLine(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    shell = Part.Wire(edges).revolve(a0, ad, 360.0)
    return Part.Solid(shell)


def make_tube(r_in, r_out, z0, z1):
    """Plain annular ring, outer radius r_out, bore r_in, between two stations."""
    return make_revolve([(r_in, z0), (r_out, z0), (r_out, z1), (r_in, z1)])


def make_cylinder(r, z0, z1, x=0.0, y=0.0):
    """Solid cylinder on an axis parallel to +Z, positioned at (x, y)."""
    return Part.makeCylinder(r, z1 - z0, App.Vector(x, y, z0), App.Vector(0, 0, 1))


def boolean_cut(base, tools):
    """Subtract a list of shapes from `base`, one at a time (robust on OCC)."""
    out = base
    for t in tools:
        out = out.cut(t)
    return out


def boolean_common(a, b):
    return a.common(b)


def mass_kg(shape, density):
    """Mass in kg from a shape whose Volume is in mm^3 and a density in kg/m^3."""
    return shape.Volume * 1e-9 * density


def new_doc(name):
    """Fresh document. FreeCAD normalises '-' to '_' in internal names, so match
    on the prefix, or the old document survives and the new one becomes `...1`."""
    for n in list(App.listDocuments()):
        if n.startswith(name.replace("-", "_")):
            App.closeDocument(n)
    return App.newDocument(name)


def add_part(doc, name, shape, color=None):
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = shape
    if color is not None and hasattr(obj, "ViewObject"):
        obj.ViewObject.ShapeColor = color
    return obj


def report_shape(label, shape, density=None):
    bb = shape.BoundBox
    print("  %-22s Z %8.2f .. %8.2f   max Ø %7.2f   vol %8.1f cm^3"
          % (label, bb.ZMin, bb.ZMax, 2.0 * max(abs(bb.XMin), abs(bb.XMax)),
             shape.Volume / 1000.0))
    if density:
        print("  %-22s mass @ %.0f kg/m^3 = %.3f kg"
              % ("", density, mass_kg(shape, density)))
    if not shape.Solids:
        print("  %-22s *** NOT A SOLID — geometry downstream is meaningless ***" % "")


# ---------------------------------------------------------------------------
# measurement feedback
# ---------------------------------------------------------------------------

MEASURED_JSON = os.path.join(HERE, "out", "measured.json")


def publish_measured(values):
    """Write measured masses so the SSOT can size other parts on them.

    This is the loop that makes T6 automatic: Phase 2 measures the ring, the
    file records it, and pgk_params reads it back to size C32's collar against
    the real load instead of C26's 0.5 kg assumption. Values are merged, so a
    phase only has to publish what it owns.
    """
    import json
    os.makedirs(os.path.dirname(MEASURED_JSON), exist_ok=True)
    data = {}
    if os.path.exists(MEASURED_JSON):
        try:
            with open(MEASURED_JSON) as f:
                data = json.load(f)
        except Exception:
            data = {}
    data.update({k: round(float(v), 6) for k, v in values.items()})
    with open(MEASURED_JSON, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")
    return MEASURED_JSON


def wall_at(shape, r, z, theta_deg=0.0):
    """True if the point (r, theta, z) is inside the solid."""
    a = math.radians(theta_deg)
    return shape.isInside(App.Vector(r * math.cos(a), r * math.sin(a), z), 1e-6, True)


def probe_table(shape, points):
    """points: list of (label, r, theta_deg, z, expected). Prints a table and
    returns the number of mismatches."""
    bad = 0
    for (label, r, th, z, exp) in points:
        got = wall_at(shape, r, z, th)
        ok = (got == exp)
        bad += 0 if ok else 1
        print("    %-28s r%7.2f th%6.1f z%8.2f  %-5s expect %-5s %s"
              % (label, r, th, z, "STEEL" if got else "void",
                 "STEEL" if exp else "void", "ok" if ok else "MISMATCH"))
    return bad


# ---------------------------------------------------------------------------
# materials
# ---------------------------------------------------------------------------

STEEL = 7850.0
ALU = 2700.0
TI = 4430.0
NDFEB = 7500.0
SMC = 7600.0        # laminations / soft magnetic composite, sizing section 2
COPPER = 8960.0
