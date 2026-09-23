#!/usr/bin/env python3
"""Extract the figures of Wang et al. 2015 into this directory.

Source: "Guidance and Control Design for a Class of Spin-Stabilized Projectiles
with a Two-Dimensional Trajectory Correction Fuze", Int. J. Aerospace
Engineering 2015, Article ID 908304. The PDF sits in the repo root.

Why a script: the PDF's text layer OCRs the equations badly (see
notes/03-wang2015-gnc-application.md section 6), so every number taken from this
paper is read off a rendered page, not off the text layer. The crop boxes below
are therefore the record of which region was read, at what resolution.

Run from the repo root:  python3 notes/figures/wang2015/extract.py
Requires: poppler-utils (pdftoppm), Pillow.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

REPO = Path(__file__).resolve().parents[3]
PDF = REPO / "Guidance_and_Control_Design_for_a_Class_of_Spin-St.pdf"
OUT = Path(__file__).resolve().parent
DPI = 300
QUALITY = 88

# (page, x0, y0, x1, y1) as fractions of the page box; (page, name)
CROPS = [
    (7, 0.050, 0.045, 0.480, 0.115, "p7-fig3-projectile-with-fixed-canards"),
    (7, 0.495, 0.040, 0.980, 0.565, "p7-fig4-5-phase-angle-and-phase-shift"),
    (8, 0.045, 0.040, 0.525, 0.425, "p8-fig6-phase-shift-mach-polynomial-fit"),
    (10, 0.055, 0.040, 0.975, 0.575, "p10-fig9-10-predictive-results-and-fading-memory-filter"),
    (11, 0.055, 0.040, 0.975, 0.560, "p11-fig11-12-filter-at-45deg-and-gnc-process"),
    (12, 0.495, 0.040, 0.975, 0.560, "p12-fig13-14-predictive-derivation-and-correction-authority"),
    (13, 0.045, 0.040, 0.485, 0.400, "p13-fig15-16-range-vs-altitude-and-cross-range"),
    (13, 0.495, 0.040, 0.975, 0.565, "p13-fig17-19-predictive-results-sideslip-and-command-angle"),
    (14, 0.045, 0.055, 0.485, 0.465, "p14-table2-and-fig20-disturbances-and-monte-carlo"),
]


def main() -> int:
    if not PDF.exists():
        print(f"source PDF not found: {PDF}", file=sys.stderr)
        return 1
    pages = sorted({c[0] for c in CROPS})
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["pdftoppm", "-r", str(DPI), "-png", "-f", str(pages[0]),
             "-l", str(pages[-1]), str(PDF), f"{tmp}/page"],
            check=True,
        )
        rendered = {}
        for page in pages:
            matches = list(Path(tmp).glob(f"page-*{page:02d}.png"))
            if not matches:
                print(f"page {page} did not render", file=sys.stderr)
                return 1
            rendered[page] = Image.open(matches[0])

        for page, x0, y0, x1, y1, name in CROPS:
            img = rendered[page]
            w, h = img.size
            box = (round(x0 * w), round(y0 * h), round(x1 * w), round(y1 * h))
            target = OUT / f"{name}.jpg"
            img.crop(box).convert("RGB").save(target, quality=QUALITY)
            print(f"{target.relative_to(REPO)}  {box[2] - box[0]}x{box[3] - box[1]}")

    for page in pages:
        rendered[page].close()
    return 0


if __name__ == "__main__":
    if shutil.which("pdftoppm") is None:
        print("pdftoppm not on PATH (install poppler-utils)", file=sys.stderr)
        raise SystemExit(1)
    raise SystemExit(main())
