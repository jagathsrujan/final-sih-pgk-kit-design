#!/usr/bin/env python3
"""Render an architecture-atlas sheet to deck-token SVG.

    python3 render_svg.py sheet1              -> out/sheet1.svg
    python3 render_svg.py --all
    python3 render_svg.py sheet1 --png        -> out/sheet1.png (Chrome, for review)

Output rules, borrowed from `submission/deck/figures/figlib.py` so an inlined
sheet behaves exactly like every other figure in the deck:

  * each colour is emitted as `style="fill:var(--f-x, #fallback)"` - a CSS
    custom property WITH a fallback.  Inlined, it resolves from the deck's own
    token block; standalone, the fallback applies.
  * no <style> element is emitted, so an inlined sheet cannot leak rules into
    the deck.  All presentation is per-element.
  * the root carries `style="font-family:var(--font)"` and only a viewBox, so
    the deck's CSS owns the displayed size.
"""

import argparse
import html
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from atlas_scene import SCENES  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")

CSS_FONT = ("-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,"
            "'Helvetica Neue',Arial,sans-serif")

# Chrome resolves this stack's Arial entry to Liberation Sans on this machine,
# so that is the font the overflow check must measure with.
MEASURE_FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
_font_cache = {}


def text_width(s, size):
    """Width of `s` in sheet units, measured with the font Chrome will use."""
    from PIL import ImageFont
    key = int(round(size))
    if key not in _font_cache:
        try:
            _font_cache[key] = ImageFont.truetype(MEASURE_FONT, key)
        except OSError:
            return len(s) * size * 0.55          # fallback estimate
    try:
        return _font_cache[key].getlength(s)
    except AttributeError:                        # very old Pillow
        return _font_cache[key].getsize(s)[0]


def check_fit(sheet):
    """Report any label wider than the box it sits in. A label that overflows
    its node is a drawing error, so it should fail here and not at the printer."""
    bad = []
    for e in sheet["elements"]:
        if e["type"] != "text":
            continue
        over = text_width(e["text"], e["fontSize"]) - e["width"]
        if over > 0:
            bad.append((e["id"], e["text"], e["fontSize"], round(over, 1)))
    return bad


def check_overlap(sheet):
    """Report pairs of labels whose *rendered* extents collide.

    check_fit() only asks whether a label fits its own box; two labels in
    adjacent boxes can each fit and still run into each other, which is how the
    timeline's tick row would fail.  Measure real widths, not declared ones."""
    items = []
    for e in sheet["elements"]:
        if e["type"] != "text":
            continue
        w = text_width(e["text"], e["fontSize"])
        # vertical extent of the glyphs, generous by a couple of px
        y0, y1 = e["y"], e["y"] + e["fontSize"] * 1.15
        items.append((e["id"], e["x"], e["x"] + w, y0, y1, e["text"]))
    hits = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a, b = items[i], items[j]
            if a[2] <= b[1] or b[2] <= a[1]:
                continue                      # no horizontal overlap
            if a[4] <= b[3] or b[4] <= a[3]:
                continue                      # no vertical overlap
            ov = min(a[2], b[2]) - max(a[1], b[1])
            hits.append((a[0], b[0], round(ov, 1), a[5], b[5]))
    return hits



def svg_rect(e):
    parts = ['<rect x="%g" y="%g" width="%g" height="%g"' %
             (e["x"], e["y"], e["width"], e["height"]), 'rx="1.5"']
    style = "fill:%s;stroke:%s;stroke-width:%g" % (e["fill"], e["stroke"],
                                                   e.get("sw", 1))
    if e.get("dash"):
        style += ";stroke-dasharray:4 3"
    parts.append('style="%s"' % style)
    parts.append("/>")
    return " ".join(parts)


def svg_text(e):
    size = e["fontSize"]
    # sheet y is the top of the text box; SVG y is the baseline
    baseline = e["y"] + size * 0.80
    anchor = e.get("anchor", "start")
    xs = {"start": 0, "middle": 0.5, "end": 1.0}[anchor]
    x = e["x"] + e["width"] * xs
    return ('<text x="%g" y="%g" font-size="%g" text-anchor="%s" '
            'style="fill:%s">%s</text>' %
            (x, baseline, size, anchor, e["fill"], html.escape(e["text"])))


# Arrowheads are defined per colour rather than with fill="context-stroke",
# because context-stroke is SVG 2 and not reliably supported.
MARKERS = (("ah-a", "#0b5cad"), ("ah-f", "#a4551a"), ("ah-g", "#7b8794"))


def defs():
    out = ["<defs>"]
    for mid, colour in MARKERS:
        out.append(
            '<marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" '
            'markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
            '<path d="M 0 1 L 9 5 L 0 9 z" fill="%s"/></marker>' % (mid, colour))
    out.append("</defs>")
    return "\n".join(out)


def _marker_for(stroke):
    if "accent" in stroke:
        return "ah-a"
    if "flag" in stroke:
        return "ah-f"
    return "ah-g"


def svg_arrow(e):
    pts = e["points"]
    d = "M %g %g" % pts[0] + "".join(" L %g %g" % p for p in pts[1:])
    style = "fill:none;stroke:%s;stroke-width:%g;stroke-linejoin:round" % (
        e["stroke"], e.get("sw", 1.4))
    if e.get("dash"):
        style += ";stroke-dasharray:5 3"
    return ('<path d="%s" style="%s" marker-end="url(#%s)"/>'
            % (d, style, _marker_for(e["stroke"])))


def svg_cell(e):
    """Three visually distinct fill states: hollow, half, filled."""
    x, y, s, st = e["x"], e["y"], e["width"], e["state"]
    common = 'style="stroke:%s;stroke-width:1.2"' % e["fill"]
    if st == "off":
        common = 'style="stroke:%s;stroke-width:1;opacity:.55"' % e["fill"]
    out = ['<rect x="%g" y="%g" width="%g" height="%g" rx="2" fill="none" %s/>'
           % (x, y, s, s, common)]
    if e["filled"] is True:
        out.append('<rect x="%g" y="%g" width="%g" height="%g" rx="2" '
                   'style="fill:%s" stroke="none"/>' % (x, y, s, s, e["fill"]))
    elif e["filled"] == "half":
        out.append('<rect x="%g" y="%g" width="%g" height="%g" rx="2" '
                   'style="fill:%s" stroke="none"/>'
                   % (x, y, s * 0.45, s, e["fill"]))
    return "\n".join(out)


def render(sheet_id, png=False, strict=False):
    sheet = SCENES[sheet_id]()
    w, h = sheet["canvas"]

    over = check_fit(sheet)
    if over:
        print("%-8s %d label(s) overflow their box:" % (sheet_id, len(over)))
        for eid, s, size, px in over:
            print("           %-10s %5.1f px over  %d px  %r" % (eid, px, size, s))
    collide = check_overlap(sheet)
    if collide:
        print("%-8s %d label collision(s):" % (sheet_id, len(collide)))
        for a, b, px, sa, sb in collide:
            print("           %-10s x %-10s %5.1f px  %r / %r"
                  % (a, b, px, sa, sb))
    if (over or collide) and strict:
        raise SystemExit("refusing to write %s: fix the layout first" % sheet_id)

    # A flow sheet has a third failure mode the two checks above cannot see: a
    # connector that vanishes behind a box. Only the flow sheet declares boxes.
    try:
        from atlas_scene import check_routes
        crossings = check_routes()
    except (ImportError, AttributeError):
        crossings = []
    if crossings:
        print("%-8s %d connector(s) cross a node box:"
              % (sheet_id, len(crossings)))
        for name, seg in crossings:
            print("           crosses %-8s  segment %s" % (name, seg))
        if strict:
            raise SystemExit("refusing to write %s: a connector is hidden "
                             "behind a box" % sheet_id)

    # Paint order: connectors first, then boxes and cells, then labels.  A box
    # must cover the end of a connector that reaches it, and a label must never
    # be hidden behind a fill.
    paint = {"arrow": 0, "rectangle": 1, "cell": 1, "text": 2}
    els = sorted(sheet["elements"], key=lambda e: paint[e["type"]])

    body = []
    for e in els:
        if e["type"] == "rectangle":
            body.append("  " + svg_rect(e))
        elif e["type"] == "text":
            body.append("  " + svg_text(e))
        elif e["type"] == "cell":
            body.append("  " + svg_cell(e))
        elif e["type"] == "arrow":
            body.append("  " + svg_arrow(e))
        else:
            raise SystemExit("unhandled element type %r" % e["type"])

    doc = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g" '
           'role="img" aria-label="%s" '
           'style="display:block;font-family:var(--font,%s)">\n'
           '<title>%s</title>\n%s\n%s\n</svg>\n' %
           (w, h, html.escape(sheet["title"]), CSS_FONT,
            html.escape(sheet["title"]), defs(), "\n".join(body)))

    os.makedirs(OUT, exist_ok=True)
    dest = os.path.join(OUT, sheet_id + ".svg")
    # fail loudly here rather than shipping a sheet the deck cannot parse:
    # an inlined SVG is XML, so a malformed attribute breaks the whole slide
    import xml.etree.ElementTree as ET
    try:
        ET.fromstring(doc)
    except ET.ParseError as exc:
        raise SystemExit("sheet %s produced malformed XML: %s" % (sheet_id, exc))
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("%-8s %4d elements -> %s (%.1f kB)" %
          (sheet_id, len(sheet["elements"]), dest, len(doc) / 1024.0))

    if png:
        # standalone: the CSS vars have no definition, so the fallbacks apply
        png_path = os.path.join(OUT, sheet_id + ".png")
        scale = 1.6
        subprocess.run([
            "google-chrome", "--headless", "--disable-gpu", "--no-sandbox",
            "--hide-scrollbars",
            "--screenshot=" + png_path,
            "--window-size=%d,%d" % (int(w * scale), int(h * scale)),
            "--force-device-scale-factor=%g" % scale,
            "--default-background-color=FFFFFFFF",
            "file://" + os.path.abspath(dest),
        ], check=True, capture_output=True)
        print("         png -> %s" % png_path)
    return dest


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("sheet", nargs="?", help="sheet id, or --all")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--png", action="store_true",
                    help="also render a PNG with headless Chrome")
    ap.add_argument("--strict", action="store_true",
                    help="fail instead of writing a sheet with overflowing labels")
    a = ap.parse_args()
    ids = list(SCENES) if (a.all or not a.sheet) else [a.sheet]
    for i in ids:
        if i not in SCENES:
            raise SystemExit("unknown sheet %r; have %s" % (i, list(SCENES)))
        render(i, png=a.png, strict=a.strict)
