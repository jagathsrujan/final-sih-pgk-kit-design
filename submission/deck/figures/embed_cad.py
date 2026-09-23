#!/usr/bin/env python3
"""Inline the CAD renders into deck.html, between their marker pairs.

The deck is a single self-contained file and prints to PDF with no external
assets, so the images cannot be linked - they are embedded as data URIs, the
same way the generated SVGs are. This script is the CAD counterpart of
`make_figures.py` and uses the same marker convention:

    <!-- CAD:<slot>:start -->   ... <figure> ...   <!-- CAD:<slot>:end -->

Slots are defined below: which renders go in, at what width, with what caption.
Captions follow the deck's tone rules - no criterion IDs, no numbers that are
still unruled in design/07-cad-evidence.md.

    python3 embed_cad.py --inline ../deck.html

Renders are taken from ./cad/ (published there by
`python3 design/cad/deck_render_trim.py`) and embedded at twice their layout
width, so they stay sharp when the PDF is rasterised or the deck is projected.
"""

import argparse
import base64
import io
import os
import re

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
CAD = os.path.join(HERE, "cad")

# slot -> (list of (file, caption, alt), layout width in px)
SLOTS = {
    # Slide 3 — the hardware column: what the ring is, what holds it, what
    # carries the load.  One render, at a size where the section reads.
    "s3-hardware": ([(
        "11-section-machine.png",
        "The ring, its machine and its bearings, cut on the axis. Fourteen "
        "magnets on the ring, twelve coils on the body, one 0.40 mm gap "
        "between them.",
        "Half-section through the machine: stator and windings on the body, "
        "magnets and backiron on the ring, bearings either side",
    )], 268),

    # Slide 4 — the fit claim.  The render that used to sit in a fourth column
    # here is deliberately not embedded any more: slide 4 carries three text
    # columns and they cannot hold its copy at a readable size with an image
    # taking a quarter of the row.  The 124.70 mm fit it proves is stated in
    # the sentence above those columns, and the render is on slides 3 and 5.
    # To put it back, restore this entry and the matching marker pair in
    # deck.html (see the note left in its place):
    #
    # "s4-fit": ([(
    #     "05-shell-kit-section.png",
    #     "The kit in the well, cut on the axis. 124.70 mm inside, nothing "
    #     "touching, and the whole 121 kJ leaves through the face it seats on.",
    #     "Half-section of the kit installed in the reference shell's fuze well",
    # )], 200),

    # Slide 5 — the gun-line column: the same shell, the same gun.
    "s5-gunline": ([(
        "04-shell-kit-iso.png",
        "The kit on the shell it was designed against. Nothing forward of the "
        "fuze well is touched, and no gun-line equipment changes.",
        "The guidance kit installed on the nose of a 155 mm shell",
    )], 372),
}


def embed(path, layout_width):
    """Downscale to 2x the layout width and return a data URI."""
    img = Image.open(os.path.join(CAD, path)).convert("RGB")
    target = int(layout_width * 2)
    if img.width > target:
        img = img.resize((target, round(img.height * target / img.width)),
                         Image.LANCZOS)
    # these are flat-colour renders, so a palette costs nothing visible and
    # keeps the embedded payload small
    quant = img.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.NONE)
    buf = io.BytesIO()
    quant.save(buf, "PNG", optimize=True)
    data = base64.b64encode(buf.getvalue()).decode("ascii")
    return "data:image/png;base64," + data, len(buf.getvalue())


def slot_html(slot):
    items, width = SLOTS[slot]
    out = []
    for path, caption, alt in items:
        uri, nbytes = embed(path, width)
        print("   %-22s %-26s %6.1f kB -> %d px wide" % (slot, path, nbytes / 1024.0, width))
        out.append(
            '        <figure class="cad">\n'
            '          <img src="%s"\n'
            '               alt="%s" style="width:%dpx">\n'
            '          <figcaption>%s</figcaption>\n'
            '        </figure>' % (uri, alt, width, caption))
    return "\n".join(out)


def inline(deck_path):
    with open(deck_path, encoding="utf-8") as fh:
        doc = fh.read()
    for slot in SLOTS:
        pat = re.compile(r"(<!-- CAD:%s:start -->)(.*?)(<!-- CAD:%s:end -->)"
                         % (slot, slot), re.S)
        if not pat.search(doc):
            raise SystemExit("marker pair for %s not found in %s" % (slot, deck_path))
        body = slot_html(slot)
        doc = pat.sub(lambda m: m.group(1) + "\n" + body + "\n      " + m.group(3), doc)
    with open(deck_path, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("inlined %d CAD slots into %s (%.1f MB)"
          % (len(SLOTS), deck_path, os.path.getsize(deck_path) / 1e6))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inline", metavar="DECK_HTML", required=True,
                    help="the deck to embed into")
    inline(os.path.abspath(ap.parse_args().inline))
