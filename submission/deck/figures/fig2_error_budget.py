"""Figure 2 - the error-budget waterfall at the register's current G4 numbers.

The terms are combined in RSS, so the waterfall accumulates in RSS space
(sqrt of the running sum of squares) rather than by addition - reading it as a
sum is the standard misreading of this chart.

Numbers and their criterion IDs
  G4   1 sigma allocations: navigation 5 m; guidance and control 17 m
       (IPP propagation and model 13 m, ring angle 9 m, actuation and loop
       lag 6 m); meteorological residual 5 m; ballistic and aero model 8 m;
       fuze and detonation 3 m.   RSS = sqrt(25+289+25+64+9) = 20.3 m
       CEP = 1.1774 x 20.3 = 23.9 m against the 30 m claim (approx 20 % margin)
  M5   the claim is stated as CEP with the fraction of rounds within 30 m
  N1   the 5 m navigation line is a top-down allocation closed from below at
       3.7 m: GNSS 3.0 + IMU/filter 2.0 + time and lever-arm 1.0
  R5   the campaign publishes the worst corner's 95 % upper bound and a
       per-condition breach fraction; the model-error terms are sampled with a
       stated correlation
"""

import math
import os
import figlib as F

W, H = 566, 240
out = []
A = out.append

X0, X1 = 44.0, 546.0
TOP, BASE = 40.0, 166.0
YMAX = 30.0
COLW = (X1 - X0) / 7.0
BW = 46.0

def py(v): return BASE - v * (BASE - TOP) / YMAX
def cx(i): return X0 + COLW * (i + 0.5)

steps = [("NAV", 5.00), ("G&C", 17.00), ("MET", 5.00), ("AERO", 8.00), ("FUZE", 3.00)]
acc, running = [], 0.0
for name, v in steps:
    lo = running
    running = math.sqrt(running ** 2 + v ** 2)
    acc.append((name, v, lo, running))
rss, cep = running, 1.1774 * running

A(F.txt(44, 22, "Error budget \u2014 1\u03c3 terms combined in RSS",
        size=11.5, weight="600"))
A(F.txt(546, 22, "against the 30 m claim", size=9, fill="f-ink3", anchor="end"))

for v in (0, 10, 20, 30):
    A(F.line(X0, py(v), X1, py(v), stroke="f-rule", sw=1.2 if v == 0 else 1))
    A(F.txt(X0 - 6, py(v) + 3, "%d" % v, size=9, fill="f-ink3", anchor="end"))
A(F.txt(X0 - 6, TOP - 8, "m", size=9, fill="f-ink3", anchor="end"))
A(F.line(X0, py(30), X1, py(30), stroke="f-accent", sw=1.4, dash="5 4"))
A(F.txt(300, py(30) - 5, "30 m claim", size=9, fill="f-accent", weight="600"))

for i, (name, v, lo, hi) in enumerate(acc):
    x = cx(i) - BW / 2
    A(F.rect(x, py(hi), BW, py(lo) - py(hi),
             fill="f-accent" if name == "G&C" else "f-tint2"))
    A(F.txt(cx(i), py(hi) - 6, "%g" % v, size=9.5, anchor="middle",
            weight="600", fill="f-accent" if name == "G&C" else "f-ink2"))
    A(F.txt(cx(i), BASE + 15, name, size=9, fill="f-ink2", anchor="middle"))

A(F.line(X0 + 5 * COLW, TOP - 6, X0 + 5 * COLW, BASE + 22,
         stroke="f-rule", sw=1, dash="3 3"))
for i, v, tone in ((5, rss, "f-ink2"), (6, cep, "f-accent")):
    x = cx(i) - BW / 2
    A(F.rect(x, py(v), BW, BASE - py(v), fill=tone))
    A(F.txt(cx(i), py(v) - 6, "%.1f" % v, size=9.5, anchor="middle",
            weight="600", fill=tone))
    A(F.txt(cx(i), BASE + 15, ("RSS" if i == 5 else "CEP"), size=9,
            fill="f-ink2", anchor="middle"))

A(F.txt(44, 196,
        "\u221a(5\u00b2 + 17\u00b2 + 5\u00b2 + 8\u00b2 + 3\u00b2) = 20.3 m, "
        "and CEP = 1.1774 \u00d7 20.3 = 23.9 m.", size=8.5, fill="f-ink3"))
A(F.txt(44, 210,
        "The terms add as root-sum-square, not straight.  Guidance and prediction "
        "dominate; the rest are small.", size=8.5, fill="f-ink3"))

F.write_svg(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "fig2-error-budget.svg"),
            F.open_svg(W, 216, "Error-budget waterfall",
                       "One-sigma error terms accumulated in RSS to a CEP of "
                       "23.9 m against the 30 m claim.", "".join(out)) + F.close_svg())
print("fig2-error-budget.svg")
