"""Figure 3 - canard force and guidance authority against time.

The force envelope is drawn as a band about zero because the available control
force is oscillatory in the body-fixed plane as the de-spun ring sweeps
relative to the body.  The guided phase is shaded; the provisionally inhibited
band is cut out of it.

Numbers and their criterion IDs
  G3   guided phase opens at max(arming distance, nav convergence) - a
       t ~ 15 s placeholder, provisional on F8 and N2/N3 - and closes at
       impact t ~ 86 s; the inhibited band is provisionally t ~ 35-55 s
  M7   terminal window ~45 s from apogee t ~ 41 s to impact t ~ 86 s
  C8   minimum net guidance force over the guided window >= 18.1 N at the 45 s
       design window; 14.1 N on G3's 51 s two-segment phase; >= 18.1 N sits
       above the floor of the reference's own +-15-25 N band
  C31  the permanently exposed canards are span-capped at D151 mm, so the gate
       may not open below q ~ 23 kPa
  [ref] force profile: +-85 N launch transient, +-15-25 N mid-band, ~0 at
       apogee, ~20 N on descent - a reference profile, PROVISIONAL on the
       aerodynamic coefficient set (risk 8)
"""

import os
import figlib as F

W, H = 566, 240
out = []
A = out.append

X0, X1 = 46.0, 546.0
TOP, BASE = 34.0, 152.0
FMAX = 95.0

def px(t): return X0 + t * (X1 - X0) / 90.0
def py(f): return (TOP + BASE) / 2.0 - f * (BASE - TOP) / (2.0 * FMAX)

UP = [(0, 85), (5, 85), (8, 25), (25, 25), (33, 18), (41.16, 0.5),
      (48, 8), (58, 17), (68, 20), (90, 20)]

A(F.txt(46, 22, "Canard force and guidance authority against time",
        size=11.5, weight="600"))

# guided phase, then the inhibited band cut out of it
A(F.rect(px(15), TOP, px(86) - px(15), BASE - TOP, fill="f-tint"))
A(F.rect(px(35), TOP, px(55) - px(35), BASE - TOP, fill="f-paper",
         stroke="f-flag", sw=1, dash="3 3"))

for f in (-50, 0, 50):
    A(F.line(X0, py(f), X1, py(f), stroke="f-rule", sw=1.2 if f == 0 else 1))
    A(F.txt(X0 - 6, py(f) + 3, "%+d" % f if f else "0", size=9,
            fill="f-ink3", anchor="end"))
A(F.txt(X0 - 6, TOP - 6, "N", size=9, fill="f-ink3", anchor="end"))
for t in (0, 15, 30, 45, 60, 75, 90):
    A(F.line(px(t), BASE, px(t), BASE + 4, stroke="f-rule"))
    A(F.txt(px(t), BASE + 15, "%d" % t, size=9, fill="f-ink3", anchor="middle"))
A(F.txt(X1, BASE + 29, "time of flight (s)", size=9, fill="f-ink3", anchor="end"))

# available-force envelope, both signs
band = [(px(t), py(f)) for t, f in UP]
band += [(px(t), py(-f)) for t, f in reversed(UP)]
A(F.poly(band, fill="f-tint2"))
for sign in (1, -1):
    A(F.path("M " + " L ".join("%g,%g" % (px(t), py(sign * f)) for t, f in UP),
             stroke="f-accent", sw=1.4))

# requirement lines, labelled as a legend because the envelope surrounds them
for y in (18.1, 14.1):
    A(F.line(X0, py(y), X1, py(y), stroke="f-ink", sw=1.2, dash="4 3"))
    A(F.line(X0, py(-y), X1, py(-y), stroke="f-ink", sw=1.2, dash="4 3"))
A(F.txt(X1 - 2, TOP + 11,
        "dashed: 18.1 N required (14.1 N on the gated phase)",
        size=8.5, fill="f-ink2", anchor="end"))

for t, lab, anc, y in ((41.16, "apogee t \u2248 41 s", "end", BASE - 7),
                       (86, "impact t \u2248 86 s", "end", BASE - 7)):
    A(F.line(px(t), TOP, px(t), BASE, stroke="f-ink3", sw=1, dash="2 3"))
    A(F.txt(px(t) + (-5 if anc == "end" else 5), y, lab, size=9,
            fill="f-ink3", anchor=anc))

A(F.txt(px(15) + 5, BASE - 7, "guided", size=9, fill="f-accent", weight="600"))
_mid = (px(35) + px(55)) / 2
A(F.line(_mid, TOP + 26, _mid, py(17) - 2, stroke="f-flag", sw=0.9, dash="2 2"))
A(F.txt(_mid, TOP + 23, "inhibited band", size=8.5, fill="f-flag",
        anchor="middle"))

A(F.txt(46, 196,
        "Envelope taken from the reference flight profile.  It moves when our own "
        "aerodynamic data arrives.", size=8.5, fill="f-ink3"))
A(F.txt(46, 210,
        "The requirement is on the worst point inside the window, not on the average.",
        size=8.5, fill="f-ink3"))

F.write_svg(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "fig3-canard-authority.svg"),
            F.open_svg(W, 216, "Canard force and guidance authority against time",
                       "Available control force envelope with the guided window "
                       "shaded and the inhibited band marked.", "".join(out)) + F.close_svg())
print("fig3-canard-authority.svg")
