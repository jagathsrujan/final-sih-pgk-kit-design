"""
Deck renders — presentation images of the P4 hardware, for the submission deck.

This is NOT a gate phase. It builds nothing, measures nothing and decides
nothing: every shape it draws is the shape Phase 7 already built and verified.
Its only output is pictures.

Why it exists: the phase screenshots in `out/screenshots/` are gate evidence —
one grey material, framed to prove a check. The submission needs the same
geometry shown as a product: functional groups in distinct colours, staged
views that take the assembly apart one layer at a time so the fit can be read
off the picture, and sectioned views with the housings cut away and the
internals left whole.

Rules carried from the workspace:
  * No literal geometry. Every number below is a PRESENTATION parameter —
    camera direction, explode fraction, margin. Nothing here feeds a dimension.
    Cut planes and explode offsets are derived from the solids' own bounding
    boxes rather than typed in.
  * The source documents are opened read-only and never saved. The render
    document lives in memory and is closed without saving, so a render pass
    cannot touch PGK-Assembly.FCStd.

Requires the FreeCAD GUI — this is an offscreen-render pass, so `freecadcmd`
cannot run it. See `deck_render_trim.py` for the step that crops the raw
frames and copies them into the deck.

Usage (from the FreeCAD MCP session):
    exec(open("design/cad/macros/95_render_deck_images.py").read())
or, to re-render a subset:
    PGK_RENDER_ONLY=15,16 exec(open(...).read())
"""

import math
import os
import sys

import FreeCAD as App
import FreeCADGui as Gui
import Part
from pivy import coin

CAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(CAD, "out", "deck-renders")
if CAD not in sys.path:
    sys.path.insert(0, CAD)

import part_index as PI  # noqa: E402  (names, groups and colours live there)

ASM_PATH = os.path.join(CAD, "out", "PGK-Assembly.FCStd")
ENV_PATH = os.path.join(CAD, "out", "PGK-Envelope.FCStd")

RENDER_DOC = "PGK_Render"
SHELL_NAME = "REF_Shell_155mm"

# 2560 x 1440 = the deck's 16:9 slide at twice its 1280 x 720 layout.
WIDTH, HEIGHT = 2560, 1440

# How much of the reference shell's body is shown past the kit's deepest point.
SHELL_CONTEXT_MM = 40.0

# ---------------------------------------------------------------------------
# what is drawn, and in what colour
# ---------------------------------------------------------------------------
# Colour is not decided here. Every part carries its colour, its readable name
# and its group in `part_index.py`, which is also what the build uses - so the
# model in FreeCAD and the pictures in the deck are the same picture. The group
# names below are the views' own vocabulary: which parts are shown together.

CANARDS = ["B5_Canard_Steer_A", "B5_Canard_Steer_B",
           "B5_Canard_Ctrl_A", "B5_Canard_Ctrl_B"]

GROUPS = {
    "body":         ["A1_KitBody"],
    "front":        ["A10_Front_Hub", "D1_Radome", "D2_Gnss_Aperture"],
    "stator":       ["A2_Stator_Core", "A3_Windings"],
    "brg_body":     ["A4_Brg_Inner_Races", "A11_Retention_Collar"],
    # the ring and its fins are separate groups so a section can cut the
    # housing and leave the fins whole (the +Y fin lies entirely in y > 0 and
    # would otherwise vanish from a y-cut, which reads as a modelling error)
    "ring":         ["B1_Ring_Carrier"],
    "canards":      CANARDS,
    "rotor":        ["B2_Rotor_Backiron", "B3_Magnets"],
    "brg_ring":     ["B4_Brg_Outer_Races"],
    "balls":        ["C1_Balls_Cage"],
    "elec":         ["A5_Avionics_Stack", "A6_Dump_Stage", "A7_Buffer",
                     "A8_Setter_Coil", "C3_Harness",
                     "C2_Link_Body", "C2_Link_Ring"],
    "train":        ["A9_Impact_Switch", "A9_SA_Rotor", "A9_Detonator"],
    "shell":        [SHELL_NAME],
}

KIT_GROUPS = [g for g in GROUPS if g != "shell"]

# explode offsets, as a fraction of the kit's own axial length. Sign is +Z.
# The fins carry the ring's offset: they are the same billet, so an exploded
# view that separated them would be showing an assembly that cannot be built.
EXPLODE = {
    "train": -0.60, "elec": -0.30, "body": 0.0,
    "stator": 0.0, "brg_body": 0.0,
    "balls": 0.30, "brg_ring": 0.36, "rotor": 0.44,
    "ring": 0.55, "canards": 0.55,
    "front": 0.95,
}

# camera direction = the direction the camera LOOKS ALONG (FreeCAD convention),
# so a camera at (+X, -Y, +Z) looks along (-x, +y, -z).
ISO = (-0.62, 0.62, -0.48)           # front-right, slightly above
ISO_BACK = (0.62, 0.62, -0.44)       # back-right, for the well end
PROFILE = (0.0, 1.0, 0.0)            # camera on -Y: the kit's profile
NOSE_ON = (0.0, 0.0, -1.0)           # camera on +Z: looking at the nose
SECTION_ISO = (-0.42, -0.80, -0.43)  # sees the cut face after removing y > 0

# ---------------------------------------------------------------------------
# the view list. "groups" selects what is shown; "cut" cuts the housings named
# in "cut_scope" and leaves everything else whole; "explode" separates the
# groups along the axis.
# ---------------------------------------------------------------------------

VIEWS = [
    # --- the assembly, as it will be fielded ------------------------------
    dict(name="01-assembly-iso", groups=KIT_GROUPS, dir=ISO),
    dict(name="02-assembly-profile", groups=KIT_GROUPS, dir=PROFILE),
    dict(name="03-assembly-nose-on", groups=KIT_GROUPS, dir=NOSE_ON),
    dict(name="04-shell-kit-iso", groups=KIT_GROUPS + ["shell"], dir=ISO),
    dict(name="05-shell-kit-section", groups=KIT_GROUPS + ["shell"],
         dir=SECTION_ISO, cut="half",
         cut_scope=["shell", "body", "ring", "front", "brg_ring", "balls"]),

    # --- staged: parts taken off, so the fit reads off the picture --------
    dict(name="06-nose-removed",
         groups=["body", "stator", "brg_body", "ring", "canards", "rotor",
                 "brg_ring", "balls", "elec", "train"], dir=ISO),
    dict(name="07-ring-removed",
         groups=["body", "front", "stator", "brg_body", "elec", "train"],
         dir=ISO),
    dict(name="08-ring-group-alone",
         groups=["ring", "canards", "rotor", "brg_ring", "balls"], dir=ISO),
    dict(name="09-body-removed",
         groups=["front", "stator", "brg_body", "elec", "train", "ring",
                 "canards", "rotor", "brg_ring", "balls"], dir=ISO_BACK),
    dict(name="10-section-through-axis", groups=KIT_GROUPS,
         dir=SECTION_ISO, cut="half",
         cut_scope=["body", "ring", "front", "brg_ring", "balls", "rotor"]),
    dict(name="11-section-machine",
         groups=["body", "stator", "brg_body", "ring", "canards", "rotor",
                 "brg_ring", "balls"], dir=SECTION_ISO, cut="half",
         cut_scope=["body", "ring", "brg_ring", "rotor"]),
    dict(name="12-exploded-stack", groups=KIT_GROUPS, dir=ISO, explode=True),

    # --- parts ------------------------------------------------------------
    dict(name="13-part-body", groups=["body"], dir=ISO),
    dict(name="13b-part-body-section", groups=["body"], dir=SECTION_ISO,
         cut="half", cut_scope=["body"]),
    dict(name="14-part-ring-canards", groups=["ring", "canards"], dir=ISO),
    dict(name="15-part-canard", groups=["B5_Canard_Steer_A"],
         dir=(0.5, 0.72, -0.48)),
    dict(name="16-part-stator-windings", groups=["stator"], dir=ISO),
    dict(name="17-part-rotor-magnets", groups=["rotor"], dir=ISO),
    dict(name="18-part-bearing-path", groups=["brg_body", "brg_ring", "balls"],
         dir=SECTION_ISO, cut="half", cut_scope=["brg_ring", "brg_body"]),
    dict(name="19-part-electronics-stack", groups=["elec"], dir=ISO),
    dict(name="20-part-front-end", groups=["front"], dir=ISO),
    dict(name="21-part-fuze-train", groups=["train"], dir=ISO),
]


# ---------------------------------------------------------------------------


def pump(n=4):
    """Camera commands are queued; the event loop has to turn before the next
    one is computed, or every readback below is stale."""
    for _ in range(n):
        Gui.updateGui()


def view_basis(direction):
    """Screen basis for a camera looking along `direction`, with the kit's own
    axis (+Z, toward the nose) as close to the screen's up as the direction
    allows. FreeCAD's own view commands roll the model whenever they feel like
    it, which is why this is built rather than asked for."""
    d = App.Vector(*direction)
    d.normalize()
    up_ref = App.Vector(0, 0, 1)
    if abs(d.dot(up_ref)) > 0.94:          # nose-on: no unique up, use +Y
        up_ref = App.Vector(0, 1, 0)
    zc = -d                                 # camera looks along its own -Z
    xc = up_ref.cross(zc)
    xc.normalize()
    yc = zc.cross(xc)
    yc.normalize()
    return d, xc, yc


def frame_camera(view, direction, shapes, margin=1.10):
    """Frame `shapes` — and only those — with a stated margin.

    fitAll() is not used: it frames hidden objects too, so a staged view comes
    out off-centre. Everything here is computed from the visible solids.
    """
    d, xc, yc = view_basis(direction)
    zc = -d
    pts = []
    for s in shapes:
        b = s.BoundBox
        corners = (b.XMin, b.XMax, b.YMin, b.YMax, b.ZMin, b.ZMax)
        if any(c != c or c in (float("inf"), float("-inf")) for c in corners):
            continue        # an empty solid would frame the camera to infinity
        for x in (b.XMin, b.XMax):
            for y in (b.YMin, b.YMax):
                for z in (b.ZMin, b.ZMax):
                    pts.append(App.Vector(x, y, z))
    if not pts:
        raise ValueError("nothing visible to frame in this view")
    lo = App.Vector(min(p.x for p in pts), min(p.y for p in pts),
                    min(p.z for p in pts))
    hi = App.Vector(max(p.x for p in pts), max(p.y for p in pts),
                    max(p.z for p in pts))
    centre = (lo + hi) * 0.5
    span = max(hi.x - lo.x, hi.y - lo.y, hi.z - lo.z)

    across = [p.dot(xc) for p in pts]
    upright = [p.dot(yc) for p in pts]
    wide = max(across) - min(across)
    tall = max(upright) - min(upright)
    height = max(tall, wide * HEIGHT / float(WIDTH)) * margin

    dist = 4.0 * span + 10.0
    cam = view.getCameraNode()
    rot = App.Rotation(App.Matrix(xc.x, yc.x, zc.x, 0.0,
                                  xc.y, yc.y, zc.y, 0.0,
                                  xc.z, yc.z, zc.z, 0.0,
                                  0.0, 0.0, 0.0, 1.0))
    qx, qy, qz, qw = rot.Q
    cam.orientation.setValue(coin.SbRotation(qx, qy, qz, qw))
    cam.position.setValue(coin.SbVec3f(centre.x - d.x * dist,
                                       centre.y - d.y * dist,
                                       centre.z - d.z * dist))
    cam.focalDistance.setValue(dist)
    cam.nearDistance.setValue(dist * 0.5)
    cam.farDistance.setValue(dist * 2.0)
    cam.height.setValue(height)
    return height


def resolve(groups):
    names = []
    for g in groups:
        names.extend(GROUPS.get(g, [g]))
    return sorted(set(names))


def context_box(shape):
    """A box comfortably larger than the shape, for use as a cutter."""
    b = shape.BoundBox
    L = 3.0 * max(b.XLength, b.YLength, b.ZLength) + 10.0
    bbox_min = App.Vector(b.XMin - L, b.YMin - L, b.ZMin - L)
    return b, L, bbox_min


def half(shape, name=""):
    """Cut away y > 0, about the kit's own axis.

    A part lying wholly in y > 0 would come back empty from this cut, and an
    empty shape carries an infinite bounding box that then poisons the camera.
    Body-of-revolution housings are the intended input; anything that cuts away
    to nothing is left whole and named in the log."""
    b, L, bmin = context_box(shape)
    cut = shape.cut(Part.makeBox(2 * L, L, 2 * L, App.Vector(bmin.x, 0.0, bmin.z)))
    if cut.isNull() or cut.Volume <= 0.0:
        print("      note: %s lies wholly outside the section half; kept whole"
              % (name or "part"))
        return shape
    return cut


def open_sources():
    docs = App.listDocuments()
    asm = docs.get("PGK_Assembly") or App.openDocument(ASM_PATH)
    env = docs.get("PGK_Envelope") or App.openDocument(ENV_PATH)
    return asm, env


def build_render_doc(asm, env):
    """One Part::Feature per kit part, plus the nose of the reference shell.
    Nothing is written back to the sources."""
    old = App.listDocuments().get(RENDER_DOC)
    if old is not None:
        App.closeDocument(old.Name)
    doc = App.newDocument(RENDER_DOC)

    for o in asm.Objects:
        try:
            shape = o.Shape
            if shape.isNull():
                continue
        except Exception:
            continue
        doc.addObject("Part::Feature", o.Name).Shape = shape.copy()

    # the shell is a whole 155 mm body; only its nose is wanted, cut off at the
    # kit's deepest point plus a stated margin of body for context.
    shell = env.getObject("Ref_Shell_155mm").Shape.copy()
    kit_zmin = min(o.Shape.BoundBox.ZMin for o in doc.Objects)
    keep_from = kit_zmin - SHELL_CONTEXT_MM
    b, L, bmin = context_box(shell)
    knife = Part.makeBox(2 * L, 2 * L, L, bmin)
    knife.translate(App.Vector(0, 0, keep_from - b.ZMin))
    doc.addObject("Part::Feature", SHELL_NAME).Shape = shell.cut(knife)

    doc.recompute()
    return doc


def style(doc):
    for o in doc.Objects:
        v = o.ViewObject
        if v is None or not hasattr(v, "ShapeColor"):
            continue
        v.ShapeColor = PI.colour(o.Name)
        v.Transparency = PI.transparency(o.Name)
        v.LineColor = (0.06, 0.08, 0.10)
        v.LineWidth = 2.0
        v.DisplayMode = "Flat Lines"
        if o.Name == SHELL_NAME:
            # the shell is context. Drawn with its edges it reads as a mesh of
            # thread rings rather than as a body, so it is shaded only.
            v.DisplayMode = "Shaded"
            v.LineWidth = 1.0
        v.Visibility = False
    pump()


def render(doc, base, state, view):
    """Frame and save one view. Shapes are rebuilt from `base` every time, so
    a section or an exploded view cannot leak into the next one."""
    parts = {o.Name: o for o in doc.Objects}
    show = resolve(view["groups"])
    scope = set(resolve(view.get("cut_scope", [])))
    do_cut = view.get("cut")
    do_explode = view.get("explode")
    zlen = 0.0
    if do_explode:
        zlen = (max(s.BoundBox.ZMax for s in base.values())
                - min(s.BoundBox.ZMin for s in base.values()))

    for name, o in parts.items():
        if name not in show:
            o.ViewObject.Visibility = False
            continue
        want = "base"
        if do_cut and name in scope:
            want = "half"
        elif do_explode:
            want = "explode"
        if state.get(name) != want:
            s = base[name]
            if want == "half":
                s = half(s, name)
            elif want == "explode":
                frac = 0.0
                for g, f in EXPLODE.items():
                    if name in GROUPS.get(g, [g]):
                        frac = f
                        break
                s = s.copy().translated(App.Vector(0, 0, frac * zlen))
            o.Shape = s
            state[name] = want
        o.ViewObject.Visibility = True
    pump()

    v = Gui.ActiveDocument.ActiveView
    frame_camera(v, view["dir"], [parts[n].Shape for n in show if n in parts])
    pump()
    path = os.path.join(OUT, view["name"] + ".png")
    v.saveImage(path, WIDTH, HEIGHT, "White")
    print("   %-26s %2d parts" % (view["name"], len(show)))
    return path


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    only = [t for t in os.environ.get("PGK_RENDER_ONLY", "").split(",") if t]

    asm, env = open_sources()
    doc = build_render_doc(asm, env)
    base = {o.Name: o.Shape.copy() for o in doc.Objects}
    state = {n: None for n in base}
    style(doc)
    Gui.ActiveDocument = Gui.getDocument(RENDER_DOC)
    pump()

    mw = Gui.getMainWindow()
    if mw.isMaximized():
        mw.showNormal()
    v = Gui.ActiveDocument.ActiveView
    for _ in range(6):                      # drive the viewport to 16:9
        vw, vh = v.getSize()
        if abs(vw / float(vh) - float(WIDTH) / HEIGHT) < 0.01 and vw > 1500:
            break
        mw.resize(mw.width() + (1600 - vw), mw.height() + (900 - vh))
        pump()
    print("viewport %s, %d views in the list" % (v.getSize(), len(VIEWS)))

    done = []
    for view in VIEWS:
        if only and not any(view["name"].startswith(t) for t in only):
            continue
        done.append(render(doc, base, state, view))
    print("rendered %d images into %s" % (len(done), OUT))

    # the render document is a scratch copy and is never saved, so it does not
    # get left behind in the session for someone to mistake for the model (the
    # name has to be read out first: closing the document deletes the wrapper)
    scratch = doc.Name
    App.closeDocument(scratch)
    print("closed %s (never saved)" % scratch)
    return done


if __name__ == "__main__":
    main()
