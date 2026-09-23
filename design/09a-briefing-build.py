#!/usr/bin/env python3
"""Embed the CAD renders into the briefing deck as data URIs.

The briefing deck (design/09-professor-briefing.html) is one self-contained
file: it opens from disk with no network and prints to PDF with no assets, so
every photograph has to travel inside it. The nine renders are the only
non-text payload; every other figure in the deck is a diagram drawn inline in
the HTML.

Each render is addressed by a marker in its src attribute:

    src="@@IMG:<name>@@"      first run
    data-img="<name>"         after the first run

so the script is re-runnable: later passes replace the existing payload rather
than appending to it. Images are downscaled to twice their on-page width and
quantised to 256 colours, which is invisible on flat-shaded CAD renders and
keeps the deck inside a megabyte.

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

# name -> (file, layout width in px).  The payload is embedded at twice the
# layout width so it stays sharp when the PDF is rasterised or projected.
IMAGES = {
    "01-assembly-iso":           ("01-assembly-iso.png", 470),
    "05-shell-kit-section":      ("05-shell-kit-section.png", 470),
    "10-section-through-axis":   ("10-section-through-axis.png", 470),
    "11-section-machine":        ("11-section-machine.png", 430),
    "12-exploded-stack":         ("12-exploded-stack.png", 330),
    "14-part-ring-canards":      ("14-part-ring-canards.png", 470),
    "18-part-bearing-path":      ("18-part-bearing-path.png", 470),
    "19-part-electronics-stack": ("19-part-electronics-stack.png", 470),
    "21-part-fuze-train":        ("21-part-fuze-train.png", 470),
}


def data_uri(path, layout_width):
    """Downscale to twice the layout width, flatten, quantise, base64."""
    img = Image.open(path).convert("RGB")
    target = int(layout_width * 2)
    if img.width > target:
        img = img.resize((target, round(img.height * target / img.width)), Image.LANCZOS)
    quant = img.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.NONE)
    buf = io.BytesIO()
    quant.save(buf, "PNG", optimize=True)
    payload = buf.getvalue()
    return "data:image/png;base64," + base64.b64encode(payload).decode("ascii"), len(payload)


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
    for name, (filename, width) in IMAGES.items():
        path = os.path.join(CAD, filename)
        if not os.path.exists(path):
            raise SystemExit("missing render: %s" % path)
        uri, nbytes = data_uri(path, width)
        total += nbytes
        tag_re = re.compile(r'<img\b[^>]*?data-img="%s"[^>]*?>' % re.escape(name))

        def repl(m):
            tag = re.sub(r'\s+src="(?:data:image/png;base64,[^"]*|@@IMG:[^"]*@@)"', "", m.group(0))
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
    print("   renders     %d, %.2f MB" % (len(IMAGES), total / 1e6))
    print("   file        %.2f MB" % (os.path.getsize(DECK) / 1e6))
    return 0


if __name__ == "__main__":
    sys.exit(main())
