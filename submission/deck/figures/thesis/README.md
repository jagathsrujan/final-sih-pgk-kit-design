# Reference-thesis figures

Five figures reproduced from the reference platform's M.Sc. thesis, used on the
fielded-system, control and evidence pages of
`design/09-professor-briefing.html`:

| File | Figure | Page | What it shows | Source |
|---|---|---|---|---|
| `thesis-hardware.jpg` | 4 | 5 | The kit's nose with its fixed canards, as built and tested | Günay, *Controller Design and Implementation for a Guidance Kit Used at Spinning Rockets and Projectiles*, M.Sc. thesis, METU, 2022, as built |
| `thesis-kit-design.jpg` | 5 | 5 | The kit's two bodies, the machine between them, and the two torques it balances | ibid., Figure 2.2 |
| `thesis-torque-elev.jpg` | 22 | 31 | Aerodynamic torque on the kit at four firing elevations — the evidence that the apogee collapse moves with elevation | ibid., Figure 5.10 |
| `thesis-ring-tracking.jpg` | 23 | 32 | Ring angle commanded against ring angle measured on the bench rig | ibid., Figure 7.8 |
| `thesis-test-rig.jpg` | 25 | 41 | The bench rig, labelled: torque motor, spin motor, alternator, torque sensor, slip ring and drives | ibid., Figure 2.7 |

## Licence

The thesis is © G. Günay / METU, 2022. These five figures are reproduced with
the author credited, as scholarly quotation inside an internal academic review.
That is stated beneath each figure and in the credits table on page 44.

**If this briefing is ever published or uploaded publicly, these five figures
need the author's permission** — unlike the pictures in
`../market/CREDITS.md`, which are public domain or CC BY. Removing them means
deleting their five `<img data-img="thesis-…">` elements from the deck and
re-running `design/09a-briefing-build.py`.

## Also reviewed and not used

The folder holds 95 extracted figures. The rest were Simulink model captures,
Bode and step-response plots, and simulation-versus-test traces of the same
loop that Figure 23 already shows. Three were strong enough to keep in reserve:
the disturbance observer validated against test (p125), the combined
limit-law result (p118), and the observer filter's step response (p163). None
of them fits a page legibly without cutting prose, so they are noted here
rather than squeezed in.

## Rebuilding

Embedded as data URIs by `design/09a-briefing-build.py`. Keep the filenames if
replacing; add to the script's `IMAGES` table if adding.
