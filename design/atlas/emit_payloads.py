#!/usr/bin/env python3
"""Emit an architecture-atlas sheet as Excalidraw MCP batch payloads.

    python3 emit_payloads.py sheet1            # all elements, one JSON array
    python3 emit_payloads.py sheet1 --chunk 60 # split into pasteable batches
    python3 emit_payloads.py sheet1 --out p.json

Why this exists: the Excalidraw MCP in this session is headless - elements
persist, but `export_to_image`, `export_scene` and `get_canvas_screenshot` all
need a browser frontend.  So the canvas is a *destination*, not the source of
truth; `atlas_scene.py` is.  This script pushes the same geometry into the MCP
so the sheet can be opened, hand-tuned and presented in Excalidraw, and the
work is never trapped there.

Colour: the scene stores deck CSS custom properties (`var(--f-accent, #0b5cad)`).
Excalidraw has no CSS, so each one is resolved to its fallback here - which is
exactly the colour the standalone PNG renders in, so canvas and deck agree.
"""

import argparse
import json
import os
import re
import sys
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from atlas_scene import SCENES  # noqa: E402

# The fallback may itself contain parentheses - rgba(11,92,173,.13) - so the
# capture must be greedy to the *last* closing paren, not the first. A
# non-greedy or [^)]+ class silently truncates it to "rgba(11,92,173,.13".
VAR = re.compile(r"var\(--[a-z0-9-]+,\s*(.+)\)")
COLOUR = re.compile(r"^(#[0-9a-fA-F]{3,8}|rgba?\(.+\)|transparent|none)$")


def resolve(c):
    """var(--f-x, #hex) -> #hex. Excalidraw has no custom properties."""
    m = VAR.search(c)
    val = m.group(1).strip() if m else c.strip()
    if not COLOUR.match(val):
        raise SystemExit("unresolved or malformed colour %r (from %r) - "
                         "Excalidraw would reject it" % (val, c))
    return val


def _seed(eid):
    """Deterministic seed/nonce so a re-emit produces an identical file."""
    return zlib.crc32(eid.encode("utf-8")) & 0x7FFFFFFF


def to_payload(e, prefix):
    """Scene element -> the element object batch_create_elements expects.

    Connectors are skipped: that reduced schema has no `points` field, so an
    arrow cannot be expressed through it.  Use --scene and import_scene, which
    carries the full element schema and the route vertices with it."""
    if e["type"] == "arrow":
        return None
    p = {"id": "%s-%s" % (prefix, e["id"]), "type": e["type"],
         "x": e["x"], "y": e["y"], "width": e["width"], "height": e["height"]}
    if e["type"] in ("rectangle", "cell"):
        p["type"] = "rectangle"
        p["backgroundColor"] = resolve(e.get("fill", "transparent"))
        p["strokeColor"] = resolve(e["stroke"] if "stroke" in e else e["fill"])
        p["strokeWidth"] = e.get("sw", 1)
        p["roughness"] = 0
        if e.get("dash"):
            p["strokeStyle"] = e["dash"]
    elif e["type"] == "text":
        p["text"] = e["text"]
        p["fontSize"] = e["fontSize"]
        p["fontFamily"] = 2                  # helvetica/sans
        p["strokeColor"] = resolve(e["fill"])
    return p


def to_excalidraw(e, prefix, ts):
    """Scene element -> list of complete .excalidraw scene elements.

    Returns a list because a `cell` with a half fill is one element on the
    sheet but two shapes in Excalidraw (an outline plus a half-width fill).

    The import path needs the full base schema - seed, versionNonce and friends
    - not the reduced shape batch_create_elements accepts."""
    eid = "%s-%s" % (prefix, e["id"])

    # Connectors are handled first: a scene `arrow` carries `points` and has no
    # x/y/width/height of its own, so it cannot share the common dict below.
    if e["type"] == "arrow":
        pts = e["points"]
        ox, oy = pts[0]
        rel = [[round(px - ox, 2), round(py - oy, 2)] for px, py in pts]
        xs = [p[0] for p in rel]
        ys = [p[1] for p in rel]
        return [{
            "id": eid, "type": "arrow", "x": ox, "y": oy, "points": rel,
            "width": max(xs) - min(xs), "height": max(ys) - min(ys),
            "angle": 0, "strokeColor": resolve(e["stroke"]),
            "backgroundColor": "transparent", "fillStyle": "solid",
            "strokeWidth": e.get("sw", 1.4),
            "strokeStyle": e.get("dash") or "solid", "roughness": 0,
            "opacity": 100, "groupIds": [], "frameId": None,
            "roundness": {"type": 2}, "seed": _seed(eid), "version": 1,
            "versionNonce": _seed(eid + "n"), "isDeleted": False,
            "boundElements": None, "updated": ts, "link": None, "locked": False,
            "startBinding": None, "endBinding": None, "startArrowhead": None,
            "endArrowhead": "arrow", "elbowed": False,
        }]

    common = {
        "id": eid, "x": e["x"], "y": e["y"],
        "width": e["width"], "height": e["height"],
        "angle": 0, "strokeColor": resolve(e["stroke"] if "stroke" in e
                                          else e["fill"]),
        "backgroundColor": resolve(e.get("fill", "transparent")),
        "fillStyle": "solid", "strokeWidth": e.get("sw", 1),
        "strokeStyle": e.get("dash") or "solid", "roughness": 0,
        "opacity": 100, "groupIds": [], "frameId": None,
        "roundness": {"type": 3} if e["type"] in ("rectangle", "cell") else None,
        "seed": _seed(eid), "version": 1, "versionNonce": _seed(eid + "n"),
        "isDeleted": False, "boundElements": None, "updated": ts,
        "link": None, "locked": False,
    }

    if e["type"] == "text":
        common.update({
            "type": "text", "text": e["text"], "originalText": e["text"],
            "fontSize": e["fontSize"], "fontFamily": 2,
            "textAlign": "left", "verticalAlign": "top",
            "containerId": None, "lineHeight": 1.25,
        })
        return [common]

    if e["type"] == "cell":
        # outline always; a filled/half cell adds an inner filled rect
        out = [dict(common, type="rectangle", backgroundColor="transparent")]
        if e["filled"]:
            frac = 1.0 if e["filled"] is True else 0.45
            out.append(dict(common, id=eid + "-f", type="rectangle",
                            width=e["width"] * frac, height=e["height"],
                            strokeWidth=0,
                            backgroundColor=resolve(e["fill"]),
                            roundness={"type": 3}))
        return out

    common["type"] = "rectangle"
    return [common]


def write_scene(sheet, prefix, path, ts):
    """Write a complete .excalidraw file, loadable by Excalidraw itself."""
    elements = []
    for e in sheet["elements"]:
        elements.extend(to_excalidraw(e, prefix, ts))
    scene = {
        "type": "excalidraw", "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {"gridSize": None, "viewBackgroundColor": "#ffffff"},
        "files": {},
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(scene, fh, ensure_ascii=False, indent=1)
    w, h = sheet["canvas"]
    n_arr = sum(1 for e in elements if e["type"] == "arrow")
    print("%s: %d shapes (%d connectors), canvas %dx%d -> %s (%.1f kB)"
          % (prefix, len(elements), n_arr, w, h, path,
             os.path.getsize(path) / 1e3))


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sheet")
    ap.add_argument("--chunk", type=int, default=0,
                    help="split into batches of N elements")
    ap.add_argument("--out", metavar="PATH", help="write JSON to a file")
    ap.add_argument("--scene", metavar="PATH",
                    help="write a complete .excalidraw scene file")
    a = ap.parse_args()

    if a.sheet not in SCENES:
        raise SystemExit("unknown sheet %r; have %s" % (a.sheet, list(SCENES)))

    sheet = SCENES[a.sheet]()
    payload = [p for p in (to_payload(e, a.sheet) for e in sheet["elements"])
               if p is not None]

    if a.scene:
        # fixed timestamp so the file is reproducible run to run
        write_scene(sheet, a.sheet, a.scene, 1758420000000)

    if a.chunk:
        payload = [payload[i:i + a.chunk]
                   for i in range(0, len(payload), a.chunk)]

    text = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        n = sum(len(c) for c in payload) if a.chunk else len(payload)
        print("%s: %d elements -> %s (%.1f kB)"
              % (a.sheet, n, a.out, len(text) / 1e3))
    elif not a.scene:
        print(text)


if __name__ == "__main__":
    main()
