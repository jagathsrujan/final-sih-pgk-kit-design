#!/usr/bin/env python3
"""Embed the typefaces and the pictures into the slide deck as data URIs.

The slide deck (design/09b-slides.html) is one self-contained file: three
typefaces and six pictures travel inside it, so it opens from disk with no
network and projects or prints with no assets beside it.

TYPEFACES.  The faces are subset to the characters this deck can print and
cached in design/fonts/ as WOFF2. The cache means a later run does not depend
on the fonts being installed and rebuilds the file byte for byte; delete the
folder, or pass --fonts, to regenerate them from the system fonts. The Latin of
Noto Sans CJK is Source Sans and of Noto Serif CJK is Source Serif, which is
what this deck sets its text in.

PICTURES.  Each picture is addressed by a marker in its src attribute:

    src="@@IMG:<name>@@"      first run
    data-img="<name>"         after the first run

so the script is re-runnable: later passes replace the existing payload rather
than appending to it. Renders are downscaled to twice their box width and
quantised to 256 colours, which is invisible on flat-shaded CAD output;
photographs are resized and re-encoded as JPEG instead.

    python3 design/09b-slides-build.py            # use the cached faces
    python3 design/09b-slides-build.py --fonts    # rebuild the subsets first
"""

import base64
import io
import os
import re
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.join(HERE, "09b-slides.html")
FONTS = os.path.join(HERE, "fonts")
CAD = os.path.join(ROOT, "submission", "deck", "figures", "cad")
MARKET = os.path.join(ROOT, "submission", "deck", "figures", "market")
THESIS = os.path.join(ROOT, "submission", "deck", "figures", "thesis")

# face -> (family, weight, system font, face number in a collection, cache file)
FACES = {
    "sans":    ("Deck Sans", 400, "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 0, "sans-regular.woff2"),
    "sans-b":  ("Deck Sans", 700, "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 0, "sans-bold.woff2"),
    "serif":   ("Deck Serif", 400, "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc", 0, "serif-regular.woff2"),
    "serif-b": ("Deck Serif", 700, "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", 0, "serif-bold.woff2"),
    "mono":    ("Deck Mono", 400, "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", None, "mono-regular.woff2"),
    "mono-b":  ("Deck Mono", 700, "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", None, "mono-bold.woff2"),
}

# name -> (folder, file, box width in px, how to encode)
# The payload is embedded at twice the box width so it stays sharp projected or
# when the PDF is rasterised.
IMAGES = {
    "assembly-iso":     (CAD, "01-assembly-iso.png", 430, "render"),
    "shell-section":    (CAD, "05-shell-kit-section.png", 620, "render"),
    "machine-section":  (CAD, "11-section-machine.png", 520, "render"),
    "ring-canards":     (CAD, "14-part-ring-canards.png", 430, "render"),
    "evidence-rig":     (THESIS, "thesis-test-rig.jpg", 470, "photo"),
    "m1156":            (MARKET, "m1156-diagram.jpg", 520, "photo"),
}


def subset_font(src, number, out):
    """Write a WOFF2 subset holding every character this deck can print."""
    from fontTools import subset
    from fontTools.ttLib import TTFont

    opts = subset.Options()
    opts.layout_features = ["kern", "liga", "tnum"]
    opts.flavor = "woff2"
    opts.recalc_bounds = True
    # opened directly rather than through subset.load_font, which has no way to
    # name a face inside a collection
    font = TTFont(src, fontNumber=number or 0, lazy=False)
    ss = subset.Subsetter(opts)
    ss.populate(unicodes=UNICODES)
    ss.subset(font)
    font.flavor = "woff2"
    font.save(out)


def unicode_set():
    cps = set(range(0x20, 0x7F)) | set(range(0xA0, 0x100))
    cps |= {0xB0, 0xB5, 0xB7, 0xD7, 0xF7, 0x2010, 0x2011, 0x2012, 0x2013,
            0x2014, 0x2015, 0x2018, 0x2019, 0x201C, 0x201D, 0x2020, 0x2022,
            0x2026, 0x2030, 0x2032, 0x2033, 0x2039, 0x203A, 0x2080, 0x2081,
            0x2082, 0x2083, 0x2084, 0x2085, 0x2086, 0x2087, 0x2088, 0x2089,
            0x20AC, 0x2190, 0x2191, 0x2192, 0x2193, 0x2194, 0x2196, 0x2197,
            0x2198, 0x2199, 0x21A6, 0x21D2, 0x2202, 0x2206, 0x2207, 0x220F,
            0x2211, 0x2212, 0x221A, 0x221D, 0x2225, 0x222B, 0x2248, 0x2260,
            0x2261, 0x2264, 0x2265, 0x2560, 0x25A0, 0x25AA, 0x25B2, 0x25BC,
            0x25CF, 0x25E6, 0x2605, 0x2606, 0x2713, 0x2717, 0x0391, 0x0394,
            0x03A9, 0x03B1, 0x03B2, 0x03B3, 0x03B4, 0x03B8, 0x03BB, 0x03BC,
            0x03C0, 0x03C3, 0x03C4, 0x03C6, 0x03C9, 0x2044, 0x2045, 0x00BD}
    return cps


UNICODES = unicode_set()


def ensure_fonts(force):
    os.makedirs(FONTS, exist_ok=True)
    for key, (family, weight, src, number, cache) in FACES.items():
        out = os.path.join(FONTS, cache)
        if force or not os.path.exists(out):
            if not os.path.exists(src):
                raise SystemExit("typeface not installed: %s" % src)
            subset_font(src, number, out)
            print("   %-10s subset from %s" % (key, os.path.basename(src)))
        yield key, family, weight, out


def embed_font(path):
    payload = open(path, "rb").read()
    return "data:font/woff2;base64,%s" % base64.b64encode(payload).decode("ascii"), len(payload)


def trim_white(img, margin=10, threshold=246):
    """Crop the empty paper around a CAD render, keeping a small margin.

    The renders are framed on a wide white field, so without this the model
    occupies a third of the box it is given. Only the renders are trimmed:
    photographs have real backgrounds and must not be cut into.
    """
    grey = img.convert("L")
    mask = grey.point(lambda v: 255 if v < threshold else 0)
    box = mask.getbbox()
    if not box:
        return img, (0, 0, 0, 0)
    left, top, right, bottom = box
    left = max(0, left - margin); top = max(0, top - margin)
    right = min(img.width, right + margin); bottom = min(img.height, bottom + margin)
    return img.crop((left, top, right, bottom)), (img.width - (right - left), img.height - (bottom - top))


def embed_image(path, box_width, kind):
    """Downscale to twice the box width and encode as a data URI."""
    img = Image.open(path).convert("RGB")
    trimmed = ""
    if kind == "render":
        before = img.size
        img, _ = trim_white(img)
        trimmed = "  trimmed %dx%d -> %dx%d" % (before[0], before[1], img.width, img.height)
    target = int(box_width * 2)
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
    return "data:%s;base64,%s" % (mime, base64.b64encode(payload).decode("ascii")), len(payload), trimmed


def main(argv):
    refresh_fonts = "--fonts" in argv
    if not os.path.exists(DECK):
        raise SystemExit("no deck at %s" % DECK)
    with open(DECK, encoding="utf-8") as fh:
        doc = fh.read()

    font_bytes = 0
    for key, family, weight, path in ensure_fonts(refresh_fonts):
        uri, nbytes = embed_font(path)
        font_bytes += nbytes
        rule = re.compile(r"(font-family:'%s';font-style:normal;font-weight:%d;src:url\()([^)]*)(\))"
                          % (re.escape(family), weight))
        doc, n = rule.subn(lambda m: m.group(1) + uri + m.group(3), doc)
        if n != 1:
            raise SystemExit("expected one @font-face for %s %d, found %d" % (family, weight, n))
        print("   %-10s %6.1f kB  %s %d" % (key, nbytes / 1024.0, family, weight))

    doc = re.sub(r'(<img\b[^>]*?)src="@@IMG:([a-z0-9\-]+)@@"',
                 lambda m: '%s data-img="%s"' % (m.group(1), m.group(2)), doc)
    image_bytes = 0
    renders = photos = 0
    for name, (folder, filename, width, kind) in IMAGES.items():
        path = os.path.join(folder, filename)
        if not os.path.exists(path):
            raise SystemExit("missing picture: %s" % path)
        uri, nbytes, trimmed = embed_image(path, width, kind)
        image_bytes += nbytes
        renders += kind == "render"
        photos += kind == "photo"
        tag_re = re.compile(r'<img\b[^>]*?data-img="%s"[^>]*?>' % re.escape(name))

        def repl(m):
            tag = re.sub(r'\s+src="(?:data:image/[a-z]+;base64,[^"]*|@@IMG:[^"]*@@)"', "", m.group(0))
            return tag[:-1].rstrip() + ' src="%s">' % uri

        doc, n = tag_re.subn(repl, doc)
        if n != 1:
            raise SystemExit("expected one image tag for %r, found %d" % (name, n))
        print("   %-10s %6.1f kB  embedded for a %d px box%s" % (name, nbytes / 1024.0, width, trimmed))

    if re.search(r"@@[A-Z]+:", doc):
        raise SystemExit("markers left unreplaced: %s" % sorted(set(re.findall(r"@@[A-Z]+:[a-z0-9\-]+@@", doc))))
    if re.search(r'src="https?://|href="https?://|url\(https?://', doc):
        raise SystemExit("the deck must not reference anything external")

    with open(DECK, "w", encoding="utf-8") as fh:
        fh.write(doc)

    print("\nbuilt %s" % DECK)
    print("   slides      %d" % len(re.findall(r'<section class="slide', doc)))
    print("   typefaces   %d, %.1f kB" % (len(FACES), font_bytes / 1024.0))
    print("   pictures    %d renders, %d photographs, %.1f kB" % (renders, photos, image_bytes / 1024.0))
    print("   file        %.2f MB" % (os.path.getsize(DECK) / 1e6))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
