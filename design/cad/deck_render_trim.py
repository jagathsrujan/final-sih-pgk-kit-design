"""
Deck renders — crop, pad, and publish to the deck's figure folder.

Step 2 of the render pipeline. `macros/95_render_deck_images.py` renders the
views from the FreeCAD session at a fixed 2560 x 1440 with generous margins
(the framing has to work for a 150 mm-wide kit as well as a 240 mm-tall one);
this script trims the white space off each frame, re-pads to the deck's 16:9
slide shape with a consistent margin, and copies the result to

    submission/deck/figures/cad/

which is where the submission's images live. Raw frames stay in
`design/cad/out/deck-renders/` — they are the record of what was rendered, and
this script never overwrites them.

Run:  python3 design/cad/deck_render_trim.py
"""

import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "out", "deck-renders")
ROOT = os.path.dirname(os.path.dirname(HERE))        # the project root
DEST = os.path.join(ROOT, "submission", "deck", "figures", "cad")

ASPECT = 16.0 / 9.0
MARGIN = 0.045          # of the longer side, after trimming
WHITE = (255, 255, 255)


def content_box(img):
    """Bounding box of everything that is not background white.

    The threshold is deliberately tight: the reference shell is drawn at 78 %
    transparency and lands near 240, so anything looser would crop the shell
    out of the frames that show it.
    """
    grey = img.convert("L")
    mask = grey.point(lambda p: 255 if p < 252 else 0)
    return mask.getbbox()


def trim_and_pad(path, dest):
    img = Image.open(path).convert("RGB")
    box = content_box(img)
    if box is None:
        raise ValueError("frame is blank: %s" % path)
    img = img.crop(box)

    w, h = img.size
    pad = int(max(w, h) * MARGIN)
    w += 2 * pad
    h += 2 * pad
    if w / float(h) < ASPECT:            # too tall: widen
        w = int(h * ASPECT)
    else:                                # too wide: heighten
        h = int(w / ASPECT)

    frame = Image.new("RGB", (w, h), WHITE)
    frame.paste(img, ((w - img.size[0]) // 2, (h - img.size[1]) // 2))
    frame.save(dest, "PNG", optimize=True)
    return frame.size


def main():
    if not os.path.isdir(DEST):
        os.makedirs(DEST)
    names = sorted(f for f in os.listdir(RAW) if f.endswith(".png"))
    for name in names:
        src = os.path.join(RAW, name)
        out = os.path.join(DEST, name)
        size = trim_and_pad(src, out)
        print("  %-28s -> %sx%s" % (name, size[0], size[1]))
    print("published %d images to %s" % (len(names), DEST))


if __name__ == "__main__":
    main()
