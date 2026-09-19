"""Figure 1 - the problem: unguided dispersion against the 30 m claim.

Left panel : cited unguided CEP against engagement range, with the 30 m
             requirement line and the dispersion the kit has to remove.
Right panel: rounds per target for a 90 % defeat probability, guided against
             unguided (M8), on a log axis.

Numbers and their criterion IDs
  M6   unguided CEP 267 m at 30.1 km  -> circular 1 sigma = 267/1.1774 = 227 m
       bracketed by M549 259 m (max range) and M795 139 m (22.5 km)
  M4   the formal claim is at the maximum-range, full-charge condition
  M8   4 guided rounds vs ~264 unguided for 90 % defeat, r_eff = 30 m
       sensitivity: r_eff 20 m -> 8 vs 592; 50 m -> 2 vs 95
"""

import os
import figlib as F

W, H = 1160, 290
out = []
A = out.append

# ---------------------------------------------------------------- geometry
AX0, AX1 = 76.0, 690.0          # left panel plot box
TOP, BASE = 44.0, 224.0
KM0, KM1 = 20.0, 31.0
M_MAX = 300.0

def px(km):  return AX0 + (km - KM0) * (AX1 - AX0) / (KM1 - KM0)
def py(m):   return BASE - m * (BASE - TOP) / M_MAX

BX0, BX1 = 790.0, 1120.0        # right panel log axis, 1 .. 1000 rounds
def pyb(v):  return BASE - (v and __import__("math").log10(v) / 3.0)  * (BASE - TOP)

# ---------------------------------------------------------------- panel A
A(F.txt(76, 22, "Unguided dispersion grows with range",
        size=11.5, weight="600"))
A(F.txt(70, 40, "CEP (m)", size=9, fill="f-ink3", anchor="end"))
A(F.txt(383, 254, "engagement range (km)", size=9, fill="f-ink3", anchor="middle"))

for m in (0, 100, 200, 300):
    y = py(m)
    A(F.line(AX0, y, AX1, y, stroke="f-rule", sw=1 if m else 1.2))
    A(F.txt(70, y + 3, "%d" % m, size=9, fill="f-ink3", anchor="end"))
for km in (20, 22, 24, 26, 28, 30):
    x = px(km)
    A(F.line(x, BASE, x, BASE + 4, stroke="f-rule"))
    A(F.txt(x, BASE + 15, "%g" % km, size=9, fill="f-ink3", anchor="middle"))
A(F.line(AX0, TOP, AX0, BASE, stroke="f-rule", sw=1.2))

p_m795  = (px(22.5), py(139))
p_m549  = (px(30.1), py(259))
p_m549a = (px(30.1), py(267))

# the dispersion the kit has to remove
A(F.poly([p_m795, p_m549a, (p_m549a[0], py(30)), (p_m795[0], py(30))], fill="f-tint"))
A(F.line(p_m795[0], p_m795[1], p_m549a[0], p_m549a[1],
         stroke="f-accent", sw=1.6, dash="5 4"))
A(F.line(AX0, py(30), AX1, py(30), stroke="f-accent", sw=1.6))
A(F.txt(686, py(30) - 6, "requirement: CEP \u2264 30 m at full charge",
        size=9, fill="f-accent", anchor="end", weight="600"))

for (x, y), lab, anc, dy in ((p_m795, "M795 \u00b7 139 m @ 22.5 km", "middle", 15),
                             (p_m549, "M549 \u00b7 259 m @ 30.1 km", "end", -13),
                             (p_m549a, "M549A1 \u00b7 267 m \u2192 \u03c3 227 m", "end", 11)):
    A(F.circle(x, y, 3.6, fill="f-accent"))
    A(F.txt(x + (0 if anc == "middle" else -9), y + dy, lab,
            size=9, fill="f-ink2", anchor=anc))
A(F.txt(436, 132, "dispersion the kit has to remove",
        size=9, fill="f-ink3", anchor="middle", italic=True))

# ---------------------------------------------------------------- panel B
A(F.txt(790, 22, "Rounds to reach a 90 % probability of defeat",
        size=11.5, weight="600"))
A(F.txt(1120, 40, "rounds (log)", size=9, fill="f-ink3", anchor="end"))

for v in (1, 10, 100, 1000):
    y = pyb(v)
    A(F.line(BX0, y, BX1, y, stroke="f-rule", sw=1 if v > 1 else 1.2))
    A(F.txt(BX0 - 8, y + 3, "%d" % v, size=9, fill="f-ink3", anchor="end"))

for cx, v, lab, tone in ((880, 4, "guided", "f-accent"),
                         (1030, 264, "unguided", "f-ink3")):
    y = pyb(v)
    A(F.rect(cx - 30, y, 60, BASE - y, fill=tone))
    A(F.txt(cx, y - 7, ("%d" % v) if v < 100 else "\u2248%d" % v,
            size=10.5, anchor="middle", weight="600", fill=tone))
    A(F.txt(cx, BASE + 16, lab, size=9.5, anchor="middle", fill="f-ink2"))
A(F.line(BX0, BASE, BX1, BASE, stroke="f-rule", sw=1.2))
A(F.txt(955, 108, "\u2248 66\u00d7", size=15, anchor="middle",
        weight="600", fill="f-accent"))

# ---------------------------------------------------------------- captions
A(F.txt(76, 268,
        "Left: published unguided CEP for this class of shell \u2014 our own numbers replace "
        "these once we have the drawing.   Right: rounds for a 90 % chance against a point target.",
        size=8.5, fill="f-ink3"))

F.write_svg(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "fig1-dispersion.svg"),
            F.open_svg(W, 276,
                       "The problem: unguided dispersion against the 30 m requirement",
                       "Unguided CEP against range, and rounds per target guided "
                       "against unguided.", "".join(out)) + F.close_svg())
print("fig1-dispersion.svg")
