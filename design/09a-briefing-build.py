#!/usr/bin/env python3
"""Embed the pictures into the briefing deck as data URIs.

The briefing deck (design/09-professor-briefing.html) is one self-contained
file: it opens from disk with no network and prints to PDF with no assets, so
every picture has to travel inside it. What gets embedded is the nine CAD
renders and the four public-domain market photographs; every other figure in
the deck is a diagram drawn inline in the HTML.

Each picture is addressed by a marker in its src attribute:

    src="@@IMG:<name>@@"      first run
    data-img="<name>"         after the first run

so the script is re-runnable: later passes replace the existing payload rather
than appending to it. Renders are downscaled to twice their on-page width and
quantised to 256 colours, which is invisible on flat-shaded CAD output;
photographs are resized and re-encoded as JPEG instead, because quantising a
photograph to 256 colours bands visibly in sky and skin.

    python3 design/09a-briefing-build.py
"""

import base64
import io
import os
import re
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.join(HERE, "09-professor-briefing.html")
CAD = os.path.join(ROOT, "submission", "deck", "figures", "cad")
MARKET = os.path.join(ROOT, "submission", "deck", "figures", "market")
THESIS = os.path.join(ROOT, "submission", "deck", "figures", "thesis")

# name -> (folder, file, layout width in px, how to encode)
# The payload is embedded at twice the layout width so it stays sharp when the
# PDF is rasterised or projected.
IMAGES = {
    # CAD renders
    "01-assembly-iso":           (CAD, "01-assembly-iso.png", 470, "render"),
    "05-shell-kit-section":      (CAD, "05-shell-kit-section.png", 470, "render"),
    "10-section-through-axis":   (CAD, "10-section-through-axis.png", 470, "render"),
    "11-section-machine":        (CAD, "11-section-machine.png", 430, "render"),
    "12-exploded-stack":         (CAD, "12-exploded-stack.png", 330, "render"),
    "14-part-ring-canards":      (CAD, "14-part-ring-canards.png", 470, "render"),
    "18-part-bearing-path":      (CAD, "18-part-bearing-path.png", 470, "render"),
    "19-part-electronics-stack": (CAD, "19-part-electronics-stack.png", 470, "render"),
    "21-part-fuze-train":        (CAD, "21-part-fuze-train.png", 470, "render"),
    # thesis figures, reproduced with attribution — see figures/thesis/README.md
    "thesis-kit-design":         (THESIS, "thesis-kit-design.jpg", 250, "photo"),
    "thesis-test-rig":           (THESIS, "thesis-test-rig.jpg", 260, "photo"),
    "thesis-hardware":           (THESIS, "thesis-hardware.jpg", 230, "photo"),
    "thesis-torque-elev":        (THESIS, "thesis-torque-elev.jpg", 200, "photo"),
    "thesis-ring-tracking":      (THESIS, "thesis-ring-tracking.jpg", 200, "photo"),
    # market photographs, public domain — see figures/market/CREDITS.md
    "m1156-diagram":             (MARKET, "m1156-diagram.jpg", 430, "photo"),
    "wang-correction-part":      (MARKET, "wang-correction-part.jpg", 290, "photo"),
    "excalibur-m982":            (MARKET, "excalibur-m982.jpg", 430, "photo"),
}


def embed(path, layout_width, kind):
    """Downscale to twice the layout width and encode as a data URI."""
    img = Image.open(path).convert("RGB")
    target = int(layout_width * 2)
    if img.width > target:
        img = img.resize((target, round(img.height * target / img.width)), Image.LANCZOS)
    buf = io.BytesIO()
    if kind == "render":
        img.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.NONE).save(buf, "PNG", optimize=True)
        mime = "image/png"
    else:
        img.save(buf, "JPEG", quality=78, optimize=True)
        mime = "image/jpeg"
    payload = buf.getvalue()
    return "data:%s;base64,%s" % (mime, base64.b64encode(payload).decode("ascii")), len(payload)


def normalize(doc):
    """Turn src="@@IMG:x@@" into data-img="x" so later runs find the tag again."""
    return re.sub(r'(<img\b[^>]*?)src="@@IMG:([a-z0-9\-]+)@@"',
                  lambda m: '%s data-img="%s"' % (m.group(1), m.group(2)), doc)


def main():
    if not os.path.exists(DECK):
        raise SystemExit("no deck at %s" % DECK)
    with open(DECK, encoding="utf-8") as fh:
        doc = fh.read()

    doc = normalize(doc)
    total = 0
    renders = photos = 0
    for name, (folder, filename, width, kind) in IMAGES.items():
        path = os.path.join(folder, filename)
        if not os.path.exists(path):
            raise SystemExit("missing picture: %s" % path)
        uri, nbytes = embed(path, width, kind)
        total += nbytes
        if kind == "render":
            renders += 1
        else:
            photos += 1
        tag_re = re.compile(r'<img\b[^>]*?data-img="%s"[^>]*?>' % re.escape(name))

        def repl(m):
            tag = re.sub(r'\s+src="(?:data:image/[a-z]+;base64,[^"]*|@@IMG:[^"]*@@)"', "", m.group(0))
            return tag[:-1].rstrip() + ' src="%s">' % uri

        doc, n = tag_re.subn(repl, doc)
        if n != 1:
            raise SystemExit("expected one tag for %r, found %d" % (name, n))
        print("   %-26s %7.1f kB  embedded for a %d px box" % (name, nbytes / 1024.0, width))

    if re.search(r"@@[A-Z]+:", doc):
        raise SystemExit("markers left unreplaced: %s" % sorted(set(re.findall(r"@@[A-Z]+:[a-z0-9\-]+@@", doc))))
    if re.search(r'src="https?://|href="https?://|url\(https?://', doc):
        raise SystemExit("the deck must not reference anything external")

    with open(DECK, "w", encoding="utf-8") as fh:
        fh.write(doc)

    pages = len(re.findall(r'<section class="slide', doc))
    print("\nbuilt %s" % DECK)
    print("   pages       %d" % pages)
    print("   pictures    %d renders, %d photographs, %.2f MB" % (renders, photos, total / 1e6))
    print("   file        %.2f MB" % (os.path.getsize(DECK) / 1e6))
    return 0


if __name__ == "__main__":
    sys.exit(main())
