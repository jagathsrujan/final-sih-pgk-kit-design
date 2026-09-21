# DRISHTI-PGK — Architecture Atlas: number ledger and how it is built

**Purpose of this file:** the traceability record for the architecture sheets in
`design/atlas/`. Every number that appears on a sheet is listed here against the
criterion that owns it and that criterion's status, so a sheet can be audited
line by line the way the deck can be audited slide by slide.

**Authority order, restated:** the register is authoritative
(`design/00-design-criteria-register.md`); the atlas is a *view* of it. Where a
sheet and the register disagree, the register wins and the sheet is wrong. Like
the CAD, **the atlas evidences; it never decides** — no value in the register
changes because a sheet shows it.

**Status of the sheets:** Sheets 1–5 built 2026-09-21, all gates pass (no label
overflows its box, no label collides with another, every sheet parses as XML).
Sheet 1 is inlined into `submission/deck/deck.html` and prints to PDF.

---

## 1. What the six sheets are for

| Sheet | Canvas | Purpose | Audience |
|---|---|---|---|
| **flow — connections and activation** | 1560 × 710 | Nodes wired left to right by the real interfaces, with a 16-row × 7-phase activation table. **This is the deck figure** (slide 3). | Submission, judges |
| **1 — System architecture over the flight** | 1560 × 660 | The same system as swimlanes on a time axis. **Superseded on slide 3 by `flow`**, kept as a review sheet. | Design review |
| **2 — Mechanical architecture** | 1560 × 488 | The three bodies, every solid with its measured mass. | Design, rig, finale |
| **3 — Power, energy and heat** | 1560 × 488 | The 121 kJ path from generation to the shell. | Design, thermal review |
| **4 — Guidance, control, error budget** | 1560 × 488 | The law, the loop, the limits, and the budget to the CEP claim. | Design, control review |
| **5 — Timeline and action → reaction** | 1560 × 404 | What happens when, and what the design does in response. | Design, safety review |

**Why `flow` replaced `sheet1` on the slide (2026-09-21).** A swimlane grid shows
what exists but not **what is wired to what** — every band sat at a different x,
so no two blocks were ever visibly connected. The template's Technical Approach
slide asks for *"Methodology and process for implementation (Flow
Charts/Images)"*, and a flow chart is what it wants. `sheet1` is not deleted: it
is still rendered and still in the review set.

**The two audiences are not the same and the sheets differ accordingly.** Sheets
1–5 are working documents: they carry criterion IDs on every row and draw the
unruled items as unruled. `flow` obeys the deck's tone rules — **no criterion
IDs, and no number that is still unruled** — because it is printed for a reader
who has not read the register.

---

## 2. Why sheet 1 is 1560 × 660, and why 12 px is the floor there

The deck's slide is 1280 × 720 CSS px = 13.333 in × 7.5 in, so **1 CSS px
= 0.75 pt** in print. The body of slide 3 leaves **561 px** of height after its
head and foot, and the body is **1172 px** wide.

At 1172 px the 1560-wide sheet scales by **0.751**, so:

| sheet text | printed size |
|---|---|
| 12 px (detail lines) | **6.8 pt** |
| 14 px (node titles) | **7.9 pt** |
| 20 px (sheet title) | **11.3 pt** |

The deck's pre-existing figures already print at about **6.3 pt** (the slide-3
block diagram was `viewBox 1160×286` shown at 268 px → 0.94 scale, 9 px text).
**Nothing on sheet 1 is smaller than the deck already asks a reader to read**,
and the 20 px title is larger.

Two deliberate divergences from the Excalidraw diagram guide, both recorded
rather than silent:

- **12 px, not the guide's 14 px minimum.** The guide sizes for a diagram read
  at 1:1 on screen. Sheet 1 is a scaled print artifact, not a screen diagram.
  Sheets 2–5 use a 13/14 px pair and are read at 100 % on screen.
- **The project's own palette, not Excalidraw's defaults.** The sheets carry
  **zero new design tokens**: every colour is one of the eleven `--f-*`
  properties the deck already defines, referenced as `var(--f-x, fallback)` the
  same way `submission/deck/figures/figlib.py` does it. So the deck restyles the
  atlas with everything else, and the sheet matches the CAD renders.

The guide's other rules are followed: solid (`roughness: 0`) strokes because a
hand-drawn wobble is wrong for a defence submission, background zone rectangles
for the swimlanes, consistent same-role sizing, and no manual arrow coordinates.
One rule is deliberately broken: **band 1 places elements by timestamp, not on
the 20 px grid**, because x carries meaning on a time axis.

---

## 3. Sheet 1 — every number against its criterion

### Band FLIGHT — the timeline

| Shown | Value | Criterion | Status |
|---|---|---|---|
| muzzle velocity | 546–943 m/s | M3 | PARAMETRIC |
| body spin at launch | 1 108–1 913 rad/s (176–304 Hz) | S6 | PARAMETRIC (confirmed by the 1:20 cal rifling check) |
| ring rate | ±31.42 rad/s | G7 | DERIVED (basis corrected 2026-09-18) |
| authority | Δv 19.0 m/s | M7 | DERIVED — provisional (M6 anchor + reference mass) |
| guided phase opens | 15 s | G3 | DERIVED — **provisional**, placeholder pending F8 and N2/N3 |
| inhibited band | 35–55 s | G3 | DERIVED — provisional on the aero set (risk 8) |
| apogee | 41.16 s | — | **reference work**, not ours |
| impact | 86.5 s | — | **reference work**, not ours |

### Band SENSE — on board

| Shown | Value | Criterion | Status |
|---|---|---|---|
| IMU on the de-spun ring | ±2 000 °/s, ≥100 Hz | N6, N7 | DEFINED / DERIVED |
| GNSS aperture on the spin axis | symmetric, no spin modulation | N3 | DEFINED |
| magnetometer band | ≤50 Hz | N5, F15 | DERIVED |
| ring angle pickoff | ≤0.8° body-relative | G5 | DERIVED |
| ring angle absolute | ≤1.0° earth-referenced | G6 | DERIVED |
| relative speed | body-side (N9/N10) | H7 | DEFINED |
| coil current | in-flight calibration input | F15 | DERIVED |
| 24 GHz Doppler | burst height 2–15 m | F2, F1 | DEFINED |

### Band NAV — state

| Shown | Value | Criterion | Status |
|---|---|---|---|
| one hardware time base | GNSS as epoch label only | H6 | DEFINED |
| stamp at conversion | ≤100 µs, mission set | N15 | DERIVED |
| nav filter terms | GNSS 3.0 + IMU 2.0 (+ time/lever-arm 1.0) | N1 | DERIVED |
| RSS at impact | 3.7 m against a 5 m allocation | N1 | DERIVED — provisional on N3, N8 |
| in-flight magnetometer calibration | rejects 1 234–2 131 Hz | F15 | DERIVED |

### Band GUIDE — the law

| Shown | Value | Criterion | Status |
|---|---|---|---|
| propagate to impact, each cycle | — | G1 | DEFINED |
| target from the setter | uploaded pre-flight | F12 | DEFINED |
| **command is θ_gk only** | magnitude is not commandable | G2 | DEFINED |
| authority gate | 15 s open, 35 s shut | G3 | DERIVED — **drawn dashed**, see §4 |
| dwell-fraction phasor | d = a_cmd / a_auth(t) | G2 | DEFINED |
| parks at ±90° | cycle mean is the command | G2 | DEFINED |
| rate | ≈6 Hz, ≈300 propagations per flight | G2, G10 | DEFINED / DERIVED |

### Band CONTROL — the loop

| Shown | Value | Criterion | Status |
|---|---|---|---|
| outer position loop | 6.2 Hz | G8 | DERIVED |
| inner velocity loop | 33.6 Hz, 0.29 + 7.82/s | G9 | DERIVED |
| settling | 0.103 s | G10 | DEFINED |
| DOB filter | Q = 1/(0.5s + 1) | G14 | DERIVED |
| limit is a minimum | 2·Î_dist and I_avail(ω_rel) | G15 | DEFINED |
| velocity limit | 26 rad/s per A | G15 | DEFINED |
| clamping anti-windup | live limit every 1 ms | G12, G13 | DEFINED |
| guard band | δ ≈ 18° | G11 | DEFINED — δ provisional pending R7 |

### Band RING — and machine

| Shown | Value | Criterion | Status |
|---|---|---|---|
| 12 slots / 14 poles | — | C36 | DEFINED |
| machine OD / air gap | Ø91.9 mm · 0.400 mm | C34, C35 | DEFINED / DERIVED (CAD gate 2 verified) |
| Talt peak | 5.76 N·m at 0.362 N·m/A · 15.9 A | C19, C14, C18 | DERIVED |
| Taero | 0.171 → 2.12 N·m | C12, C11 | **reference work** — see §4 |
| friction | Tf ≤ 0.10 N·m, flat; gate 0.1567 N·m | C13, C12 | DERIVED — provisional (C25 must confirm by test) |
| fins and cant | 4 fixed fins, 10° cant | C1, C31 | DEFINED |
| guidance force | F_steer ≥ 18.1 N | C8 | DERIVED — provisional (M7 + G3) |
| setback | 276 kN, seats past the bearings | C26, C32, T6 | DERIVED — **re-baselined by CAD finding T6, unruled** |

### Band POWER — and heat

| Shown | Value | Criterion | Status |
|---|---|---|---|
| peak generation | 2.92 kW | C42 | DERIVED (magnitude provisional on the aero set) |
| energy per flight | 121 kJ, not storable | C42 | DERIVED |
| demand | ≈12 W peak / ≈10 W average | W1–W4 | DERIVED |
| demand against generation | ≈20:1 at the apogee floor | W4 | DERIVED |
| bus | 180 V nominal, below flight-min EMF 231 V | C41, H8, H12 | DEFINED |
| dump and buffer | 150–200 J, derate then trip | W4, H9 | DEFINED |
| thermal interface | ≥58 W/K peak | P6, W7, W12 | PARAMETRIC — the bare thread does **not** deliver it |
| shell body rise | 5.8 K asymptote | W12 | DERIVED |

### Band FUZE — and safety

| Shown | Value | Criterion | Status |
|---|---|---|---|
| three modes | proximity · time · impact | F1 | DEFINED |
| out-of-line rotor | setback + spin + electrical command | F6 | DEFINED |
| no in-bore function | by construction, not by timer | F6 | DEFINED |
| in-flight time re-sync | bounded, one-way, arming-gated | F1 | DEFINED — **credited to the XM8, see §4** |
| predicted-miss veto | >150 m → latch, dud | F16 | DEFINED 2026-09-20 |
| BIT tiers | hold / derate / fuze-autonomous | H13, R3, R4 | DEFINED |
| fuze keeps its own MCU | one bounded one-way crossing | H10 | DEFINED |

---

## 3b. The flow sheet — what its activation states mean

The right-hand half of `flow` is a 16-row × 7-phase table. **The cell states are
a claim, so they are defined here rather than left to the legend alone.**

| Cell | Means | Not the same as |
|---|---|---|
| **filled accent** | acting — in the loop and commanding | |
| **half accent** | powered and monitoring, but not commanding (holding) | not "off" — the block is running |
| **hollow grey** | off — unpowered or not yet valid | not "failed" |
| **hollow copper** | inhibited by design — the block is able and the command is withheld | not "broken" |
| **filled copper** | armed — able to function | |

**The phases** are `IN-BORE · LAUNCH (0 s) · PRE-NAV (0–15 s) · GUID-A (15–35 s)
· INHIB (35–55 s) · GUID-B (55–86.5 s) · IMPACT (86.5 s)`.

Four rows carry an argument rather than a fact, and each is stated on the sheet:

- **The whole left column is `off`.** In-bore the kit is unpowered — the machine
  only generates once there is relative spin, and the fuze is out of line by
  construction (F6). This is the "no in-bore function" claim drawn as a column.
- **`IPP guidance law` and `Authority gate` are `inhibited` in INHIB and `off`
  in PRE-NAV, and those are different states.** In PRE-NAV the nav solution has
  not converged, so there is nothing to command from. In INHIB the solution is
  good and the command exists — the gate withholds it because there is not
  enough dynamic pressure left to steer with (G3). Collapsing the two would hide
  the design's central claim.
- **`Phasor → θ_gk` is `holding` in INHIB, not `off`.** G2 says the force is on
  from launch to impact and the magnitude is not commandable, so the law cannot
  switch the force off — it can only null the *net* impulse by time-sharing the
  aim direction. A blank cell there would contradict G2.
- **`Fuze S/A and fireset` is `safe` for six phases and `armed` only at
  IMPACT.** The rotor is released by setback and spin early (F6), but the
  electrical arm command is the third, independent condition and is given last;
  F16 can withhold it and the failure direction is a dud.

**The graph's 17 nodes carry the same values as sheet 1's bands**, section by
section: `Sensing` = the four sensor rows; `NAV filter` = N1/H6; `IPP law` =
G1; `Authority gate` = G3; `Phasor → θ_gk` = G2; `Cascade` = G8–G13; `Machine`,
`Ring`, `fins` = C14–C19, C13, C1/C31/C8; `DOB + limits` = G14/G15; the power
chain = C42/W4/W7/P6; the fuze chain = F1/F6/F16/H10. The one node drawn dashed
is **`Authority gate`**, for the reason in §4.1.

---



### 4.1 Drawn dashed — carried from the reference work, not ours

Three elements on sheet 1 and three rows on sheet 5 are drawn with a dashed
stroke because the value does not come from our own work. They are marked so a
reader cannot mistake them for our results:

1. **Taero 0.171 → 2.12 N·m** (band RING). The torque profile is the thesis
   flight replay. The register's C11/C12 carry it as the transferable quantity,
   with the ratio Taero_max/Taero_min = 12.4 as the shape parameter that
   survives re-baselining.
2. **The authority gate, 15 s / 35 s** (band GUIDE). The *mechanism* is ours
   (G3, DEFINED — a computed gate, not a schedule); the *edges* are derived from
   the reference force profile and are provisional until the aero set exists.
3. **Apogee 41.16 s and impact 86.5 s** (band FLIGHT). Reference flight
   timings — a 43 kg airframe at 63° from the thesis simulation, not our
   design point (45.0 kg, M4's maximum-range condition). M7's 45 s terminal
   window is built on these, so **the whole authority chain inherits them.**

**This is the atlas's most important honesty feature.** The reference flight and
our design point are not the same round, and a diagram that blends them silently
would be the easiest way for this project to mislead a reviewer.

### 4.2 Drawn open — not yet ruled or not yet demonstrated

| Sheet | Item | Why it is open |
|---|---|---|
| 1 | the inhibited band (dashed) | edges pending the aero set (risk 8) |
| 2 | all five mass rows | rollup is ×2 over P9; findings T4/T5/T9/T10 unruled |
| 3 | E = V_bus at launch | no current-control headroom at peak load (W8/C17) |
| 4 | cogging against 0.171 N·m | C37's budget is not set |
| 5 | GNSS lost | N4 owes a bounded outage tolerance |
| 5 | all five "declared open" rows | friction at flight speed, the thermal joint, coexistence at speed, the ring–body link, the buffer under launch — **all five are bench items on the R7 rig, and the rig is gated on shortlisting (P7)** |

---

## 5. What these sheets must not be used to claim

Carried from `design/05-source-register.md` §3.4 and the CAD's own rule:

- **Not a novelty claim.** The de-spun ring, the fixed canards and the absence
  of an actuator are the **fielded kit's own published specification**. Sheet 1's
  subtitle is deliberately descriptive for this reason; it says what the
  architecture *is*, never that it is new.
- **Not our in-flight time correction.** AOP-22 Annex E.16 registers the XM8
  course-correction fuze already correcting its time in flight. What is ours is
  narrower: the re-synchronisation is driven by *our own continuous nav
  solution*.
- **Not a simulated result.** No number on any sheet comes from a run of our own
  model. P3 is blocked on the aerodynamic coefficient set (risk 8). Every flight
  number is either the reference work's or an allocation.
- **Not a kit mass.** Sheet 2's masses are what the model weighs off the solids,
  never what the kit will weigh.
- **Not a resolved thermal design.** P6 shows the bare 2″-12 UNS thread does not
  deliver ≥58 W/K; the closing route (well bore + a conductance-specified joint)
  is specified but not demonstrated.

---

## 6. How the sheets are built and regenerated

The Excalidraw MCP in this session runs **headless**: elements persist, but
`export_to_image`, `export_scene` and `get_canvas_screenshot` all require a
browser frontend, so the MCP cannot produce an SVG. The atlas therefore has a
**single source of truth in Python** and two generated consumers — the same
arrangement as `design/cad/`, where `pgk_params.py` is the authority and the
macros build from it.

```
design/atlas/
  atlas_scene.py    source of truth: every sheet, as data. No number typed twice.
  render_svg.py     -> out/sheetN.svg  (token-mapped) and out/sheetN.png (review)
  out/sheet1.svg    inlined into the deck
  embed_atlas.py    -> submission/deck/deck.html, between ATLAS:<slot> markers
  emit_payloads.py  -> the same elements as Excalidraw MCP batch payloads
```

```bash
cd design/atlas
python3 atlas_scene.py                 # report element counts, write scenes.json
python3 render_svg.py --all --png --strict   # render; fail on any layout defect
python3 embed_atlas.py --inline ../../submission/deck/deck.html
python3 emit_payloads.py sheet1        # MCP payloads, to populate the canvas
```

**Three checks gate every render, and all three fail loudly** (`--strict`):

- **`check_fit`** — is any label wider than the box it sits in? Text is measured
  with **Liberation Sans**, which is what Chrome resolves this font stack's Arial
  entry to on this machine, so the check measures the glyphs that will actually
  print rather than an estimate.
- **`check_overlap`** — do two labels' *rendered* extents collide? `check_fit`
  cannot catch this: two labels in adjacent boxes can each fit inside their own
  box and still run into each other, which is exactly how a timeline's tick row
  fails.
- **`check_routes`** — does any connector pass through a node box? Only the flow
  sheet has this failure mode, and it is the one a reader cannot see past: a
  line that disappears behind a box leaves no way to tell whether it goes under,
  over or nowhere. Every vertex pair is tested against every box with a 2 px
  guard.

`check_fit` and `check_overlap` were verified to fire on synthetic defects (72.0 px
collision, 148.7 px overflow) before being trusted. The renderer also parses its
own output as XML before writing it, because an inlined SVG is XML and one bad
attribute breaks the whole slide — which is how the first build failed.

**Why not Excalidraw's own export:** it emits a `<style>` element and its own
font stack, which breaks the deck's standing rule that an inlined figure leaks no
rules, and it would clash typographically. `render_svg.py` emits per-element
`var(--f-*, fallback)` styles instead — the `figlib.py` convention exactly.
`embed_atlas.py` asserts the no-`<style>` rule so a future change cannot quietly
break the deck.

---

## 7. What is in the deck, and what is not

**In the deck:** the **`flow`** sheet only, on **slide 3 (Technical Approach)** —
the slide whose template asks for *"Methodology and process for implementation
(Flow Charts/Images)"*. The deck remains **6 slides and one self-contained
file**, as the format requires.

**Not in the deck:** sheets 1–5. The format caps the deck at six slides
including the title, and the deck was already at six, so there is no seventh
page for them. They are the working atlas — repo, rig, finale and the judge
dossier.

**Why the sheet is 1560 × 710 and not taller.** Slide 3's body is 561 px after
its head and foot, and the figure needs room for its caption. At the deck's
1172 px body width this sheet is 533 px tall, leaving 28 px. An earlier build at
1560 × 745 came to 560 px and left nothing for the caption, so the vertical
budget was retuned — the sheet's height is set by the slide, not by taste.

**The connectors are the point, so they are drawn explicitly.** Excalidraw
auto-routes arrows between bound shapes; this renderer has no layout engine, so
every vertex is spelled out in `flow_edges()`. That is a feature: the route *is*
the drawing. Connectors run in the gaps — 16 px corridors between rows, and a
16 px vertical corridor between the 372-wide node columns — so nothing crosses a
box, and `check_routes` proves it.

**What the atlas displaced, and how to get it back.** Slide 3 previously carried a
hand-authored block diagram, three bullet columns and a CAD half-section, and the
slide was already full: 268 px of diagram plus a ≈288 px row, against a 561 px
body. The atlas needs the whole body, so the old content is **hidden, not
deleted** — it sits inside `<div class="atlas-superseded">`, and removing one CSS
rule brings all of it back:

```bash
# to restore slide 3 as it was:
#   delete or comment out  .atlas-superseded{ display:none; }  in deck.html
git diff 94ddb1c -- submission/deck/deck.html     # or read the committed copy
```

The CAD half-section (the machine, cut on the axis) came off slide 3 with it. It
is a genuine loss from the deck; slides 4 and 5 still carry CAD renders of the
kit in the well and on the shell.

---

## 8. Verifying the PDF

The PDF is produced by Chrome's print path against the deck's
`@page size:13.333in 7.5in` rule — there was no render tooling in the repository
before this, so it is now recorded here:

```bash
google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf=/tmp/deck.pdf "file://$PWD/submission/deck/deck.html"
pdfinfo /tmp/deck.pdf | grep -E "Pages|Page size"   # expect 6 pages, 960x540 pts
pdftoppm -png -r 110 -f 3 -l 3 /tmp/deck.pdf /tmp/slide   # look at slide 3
```

**Verified 2026-09-21:** 6 pages, 960 × 540 pt (= 13.333 in × 7.5 in), sheet 1
legible on slide 3 at 110 dpi, slides 4 onward unaffected.

---

## 9. Cross-references

| File | Relationship |
|---|---|
| `design/00-design-criteria-register.md` | Authoritative. Every number above traces to a row here |
| `design/07-cad-evidence.md` | The masses in sheet 2, and findings T1–T10 that sheets 2 and 3 draw as open |
| `design/04-caa-dual-spin-interface.html` | The interactive 3D companion to sheet 2's two interfaces |
| `design/05-source-register.md` §3.4 | The claim corrections §5 of this file carries |
| `submission/deck/deck.html` | Where sheet 1 is inlined (slide 3) |
| `submission/deck/figures/figlib.py` | The colour and no-`<style>` convention the renderer follows |
| `submission/deck/figures/embed_cad.py` | The marker-pair convention `embed_atlas.py` follows |
| `notes/00-PGK-thesis-working-notes.md` | The source of every value drawn dashed |

---

*Rule carried from the CAD workspace: **the atlas evidences; it never decides.**
A criterion does not become DEFINED because a sheet shows it, and a number does
not move until the register rules.*
