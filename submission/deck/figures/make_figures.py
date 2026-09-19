#!/usr/bin/env python3
"""Regenerate the data figures, and optionally re-inline them into deck.html.

  python3 make_figures.py                 # writes the three .svg files
  python3 make_figures.py --inline ../deck.html
                                          # also replaces the marked regions
                                          # in deck.html with the new SVG

deck.html inlines each generated figure between a pair of markers, so the deck
stays a single self-contained file (and prints to PDF with no external assets)
while the figures stay regenerable:

    <!-- FIG:fig1-dispersion:start -->   ... inline <svg> ...   <!-- FIG:...:end -->

Figures 4 (kit architecture) and 5 (control block diagram) are hand-authored
schematics and live only inside deck.html - they carry no computed data.
"""

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

FIGURES = [
    ("fig1-dispersion", "fig1_dispersion"),
    ("fig2-error-budget", "fig2_error_budget"),
    ("fig3-canard-authority", "fig3_canard_authority"),
]


def build():
    for _, mod in FIGURES:
        __import__(mod)


def inline(deck_path, indent="        "):
    with open(deck_path, encoding="utf-8") as fh:
        doc = fh.read()
    for name, _ in FIGURES:
        svg_path = os.path.join(HERE, name + ".svg")
        with open(svg_path, encoding="utf-8") as fh:
            svg = fh.read().rstrip("\n")
        svg = "\n".join(indent + ln if ln.strip() else ln
                        for ln in svg.splitlines())
        pat = re.compile(
            r"(<!-- FIG:%s:start -->)(.*?)(<!-- FIG:%s:end -->)" % (name, name),
            re.S)
        if not pat.search(doc):
            raise SystemExit("marker pair for %s not found in %s" % (name, deck_path))
        doc = pat.sub(lambda m: m.group(1) + "\n" + svg + "\n" + indent[:-4] + m.group(3),
                      doc)
    with open(deck_path, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("inlined %d figures into %s" % (len(FIGURES), deck_path))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inline", metavar="DECK_HTML",
                    help="re-inline the generated SVG into this deck.html")
    args = ap.parse_args()
    build()
    if args.inline:
        inline(os.path.abspath(args.inline))
