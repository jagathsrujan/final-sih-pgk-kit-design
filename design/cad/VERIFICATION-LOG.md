# CAD verification log

One entry per gate. A phase does not advance on a failed gate. Numbers here come out
of the model, not out of the register — where they disagree, both are shown.

Environment (Step 0, recorded 2026-09-19): FreeCAD **1.1.3** build 20260725, Python
3.11.14. PartDesign, Sketcher, Part, Spreadsheet, Assembly, TechDraw, Material, Import,
Mesh all present. Assembly available but deliberately unused — placements are scripted
from `pgk_params` and interference is checked with booleans, so the model is
version-independent and every position is data.

---

## Phase 0 — envelope and reference platform · **PASS** · 2026-09-19

Document `PGK-Envelope`: `Params`, `Ref_Shell_155mm`, `Env_Bore_155mm`,
`Env_TrainBore_30mm`, `Env_OgiveBound`.
Macro `macros/00_phase0_envelope.py`. Screenshots `out/screenshots/p0-*.png`.

### Gate 0a — reference shell reproduces P8's published table

P8's table is the register's platform anchor, so it is checked *before* anything is
built on it. Independently re-derived from the tangent ogive
(ρ = (R² + L_n²)/2R = 1342.62 mm with L_n = 449.4 mm, R = 77.445 mm):

| station aft of seat (mm) | P8 dia (mm) | model dia (mm) | delta (mm) |
|---:|---:|---:|---:|
| 0 | 50.8 | 50.85 | +0.055 |
| 20 | 61.9 | 61.99 | +0.091 |
| 40 | 72.4 | 72.47 | +0.066 |
| 60 | 82.2 | 82.29 | +0.086 |
| 80 | 91.4 | 91.46 | +0.059 |
| 95 | 97.9 | 97.92 | +0.018 |
| 370 | 154.9 | 154.89 | −0.010 |

**Worst |delta| = 0.091 mm against a ±0.5 mm gate → PASS.** The residual is a uniform
+0.06 to +0.09 mm, i.e. the register's table is rounded, not the curve being wrong.

*Incidental result:* solving the ogive for Ø50.8 puts the fuze seat **79.3 mm from the
theoretical tip**, which is what makes P8's 370 mm station the ogive's own end. The
register's table header ("station **aft** of the fuze seat") and its §5 prose ("the kit's
outer contour **forward** of the fuze seat") disagree; the table is correct as headed.

### Gate 0b — the well's faces reproduce P6's own arithmetic

The well is modelled as real faces (thread, seat annulus, bore) rather than an assumed
area, because P6's thermal argument is an argument about areas.

| quantity | model | P6 quotes | agreement |
|---|---:|---:|---:|
| thread flank, 9 turns × π·d_p·b | 1.1180 × 10⁻³ m² | 1.1200 × 10⁻³ m² | **0.18 %** |
| seat annulus, Ø44 → Ø50.8 | 0.5063 × 10⁻³ m² | 0.5000 × 10⁻³ m² | **1.3 %** |
| well bore, π·d·124.7 | 17.237 × 10⁻³ m² | 18.800 × 10⁻³ m² | 8.3 % low |

The third row is **finding T1**. Solving P6's own seat figure for the seat inner
diameter gives **44.09 mm** — confirming Ø44 as the self-consistent reading, and
confirming that P6's 18.8 × 10⁻³ m² contact area, which implies a Ø48 bore, cannot hold
at the same time. The model adopts Ø44 (it is the reading that makes the seat a real
face) and reports the 8.3 % area it costs against P6's ≥58 W/K route.

### Gate 0c — solid verified by point membership

Because a rendered picture cannot prove a cavity exists, the solid was probed directly
with `Shape.isInside` at thirteen points spanning the mouth, thread bay, seat step, well
bore, booster taper, body wall and outside. All thirteen returned the expected
membership. The two initial "failures" were **both errors in the probe's own
expectations**, not in the model: the well bore is Ø44 (r = 22), so r = 22.5 is wall;
and at z = −130 the booster taper is already at r ≈ 20.9, so r = 16 is cavity.
Screenshot `p0-well-section2.png` shows the thread recess, the seat step, the Ø44 bore
and the taper to the Ø30 booster cavity.

### Gate 0d — the envelopes exist

`Env_Bore_155mm` (the C31/P14 in-bore limit), `Env_TrainBore_30mm` (the F9 keep-out
cylinder, from the well bottom to the front hub), `Env_OgiveBound` (P8's table as a
solid) are present in the document and are the frames every later part is tested against.

### Phase 0 outputs

- `out/PGK-Envelope.FCStd`
- `out/screenshots/p0-shell-iso.png`, `p0-shell-front.png`,
  `p0-shell-halfsection.png`, `p0-well-section.png`, `p0-well-section2.png`

### Phase 0 — carried forward

| # | item | where it goes |
|---|---|---|
| T1 | P6's two well figures conflict; model adopts Ø44, costs 8.3 % of bore area | `design/07-cad-evidence.md`; P6 |
| T2 | P12's 95.25 mm exposed length vs C8's ~80 mm canard chord → 10.75 mm shortfall | `design/07-cad-evidence.md`; P12, C4/C5 |
| — | The reference shell has zero wall between the Ø50.8 thread and the Ø50.8 ogive truncation at the mouth — a real shell needs a thread boss (Ø56–58). Affects the shell's own local wall only, not the kit, which is set by the well. | P6, P8 |
| — | The reference shell is a **contour** model. Its solid volume (11 790 cm³) is not the projectile's mass. P2/P3/P4/P5 come from the calibrated model in `02-reference-155mm-model.md`. | README rule 4 |

---

## Phase 1 — A1 kit body · **PASS** · 2026-09-19

Document `PGK-KitBody`. Macro `macros/10_phase1_kit_body.py`.
Screenshots `p1-body-iso.png`, `p1-body-section.png`.

The part everything else bolts to: the well spigot and its thread, the seat
shoulder, the spine that carries the machine between its two races, and the two
end plates that hold the stator.

### Gate 1 — the interface

| # | check | result |
|---|---|---|
| 1 | intrusion ≤ 124.7 mm | **124.70 → PASS** |
| 2 | spigot clears the well bore | Ø43.80 in Ø44.00 (0.10 mm radial, P6) → PASS |
| 3 | thread crest clears the shell's thread | Ø50.60 vs Ø50.80 → PASS |
| 4 | **no interference with the reference shell** | **0.0000 mm³ → PASS** |
| 5 | seat annulus matches P6 | 0.5063 vs 0.5000 × 10⁻³ m² → 1.3 % |

Gate 1 initially **failed** on check 4 with 114 175 mm³ of overlap — the whole
spigot — because zero-clearance nominal fits boolean-clash against themselves.
That is a modelling artefact, not a design error, and the fix is the one the
design needs anyway: `SpigotClearance` and `ThreadClearance` are now named
parameters. **P6 rules that this gap conducts nothing** (a 0.1 mm air film is
only ≈5 W/K), so the clearance is *not* the thermal path — P6's compliant
contacting element goes in it, and that is Phase 6's job. The two are now
separated in the model, which is what makes P6's argument checkable instead of
rhetorical.

### Gate 1b — the solid verified by point membership

Ten probes across the train bore, spigot wall, thread crest, seat annulus,
spine, stator end web, and both the hole and the land of the lightening pattern:
**0 mismatches.** Volume confirms independently — the model's 179.2 cm³ matches a
hand integration of the same profile (178.8 cm³) to 0.2 %.

### Two bugs caught by the gate, worth recording

1. **A revolved closed wire comes back from OCC as a SHELL, not a solid.** The
   first build produced 50 faces and no solids; booleans cut nothing and
   `isInside` answered nonsense — the lightening holes "did not cut" because
   there was nothing to cut. Fixed in `cadlib.make_revolve`, which now forces
   `Part.Solid`.
2. **`Part.Wire()` does not close a wire.** A profile whose last point does not
   coincide with its first revolves into an *open* shell. My duplicate-dedup had
   been popping the closing point, which is why the train bore read as steel at
   every radius (the part was a solid spindle, 106 cm³ heavy). `cadlib` now
   closes the profile explicitly. Both helpers are shared so the classes of bug
   cannot recur in later phases.

### Findings

**T3 — the train bore costs slot depth, and nothing owned it.** F9 reserves a
clear ≈Ø30 through the full length of the well *and* the machine section. The
machine sizing's radial build assumes the stator core's own bore **is** that
reservation — so it is charged nothing for the structure that has to hold the
machine together. It must be charged something: a spine tube of `SpineWall` sits
on the reservation and the core is built outside it.

| | sizing | with the spine | cost |
|---|---:|---:|---:|
| stator bore (yoke inner) | Ø30.0 | Ø33.0 | — |
| slot depth | 19.60 mm | **18.15 mm** | −1.45 mm, **−7.4 %** |
| machine OD (check) | 91.90 | 91.90 | 0.10 mm margin, unchanged |

Torque scales with slot area, so **C19's 5.76 N·m and C42's 2.92 kW and 121 kJ
each carry a ×0.926 factor** unless the loss is bought back elsewhere. `SpineWall`
is set at 1.5 mm as the thin end of what carries the machine's bending; it is
PROVISIONAL and belongs with C32/C35.

**T4 — the kit body alone consumes P9's entire mass budget.** Measured from the
solid, not estimated:

| material | body mass | vs P9's ≤ 1.4 kg for the *whole kit* |
|---|---:|---|
| steel (7850 kg/m³) | **1.407 kg** | **100 % of the budget, before anything else** |
| titanium (4430) | 0.794 kg | 57 % |
| aluminium (2700) | 0.484 kg | 35 % |

Against that, C40 already puts the machine at 0.81–0.97 kg on its own — and C40's
own note already conceded the kit would land at 1.4–1.7 kg. Add the ring,
canards, bearings, boards, fuze, dump and buffer and the kit is a **factor of
about two** over P9.

The spigot is the irreducible part of it: Ø44 OD with the Ø30 train bore through
it leaves 7 mm of wall over 105 mm, and that is 0.675 kg in steel by itself —
48 % of the budget in one tube that F9 and P6 between them fully determine. The
levers are therefore **material** (the spigot is not a strength-critical member if
C32 puts the launch load through the seat), and **lightening every web that is not
a load path** — which this phase has started, with 8 holes per spider. P9 and C40
need a joint decision; the CAD now prices it.

### Phase 1 outputs

- `out/PGK-KitBody.FCStd`
- `out/screenshots/p1-body-iso.png`, `p1-body-section.png`

---

## Phase 2 — the de-spun ring and the machine · **PASS (design) / FAIL (mass)** · 2026-09-19

Document `PGK-CAA`. Macro `macros/20_phase2_ring_and_machine.py`.
Screenshot `p2-machine-section.png`.

`B1_Ring_Carrier`, `B2_Rotor_Backiron`, `B3_Magnets`, `A2_Stator_Core`, `A3_Windings`.

### Gate 2 — the machine closes exactly

| # | check | result |
|---|---|---|
| 1 | air gap | **0.400 mm exactly** → PASS |
| 2 | machine OD | **91.90** against the Ø92 ceiling — **0.10 mm margin** → PASS |
| 3 | stack length | 28.0 mm inside the 25–30 band → PASS |
| 4 | poles / slots | 14 / 12 → PASS |
| 5 | ring OD | 98.00 as specified → PASS |

Two independent cross-checks fell out of the geometry, both exact:

- **Tooth width computes to 8.45 mm** from Φ_pole/(B_tooth·L) — the same figure the
  machine sizing states, arrived at from the model's own radii.
- **Slotted stator core = 39.0 cm³**, and the mass at 7600 kg/m³ is 0.296 kg against
  C40's 210–250 g band — the first time C40's stator-iron figure has been checked
  against real geometry.

### Machine mass rollup — the model vs C40

| item | model | C40 states | |
|---|---:|---:|---|
| stator iron | 0.296 kg | 0.210–0.250 kg | +18 % over the top of the band |
| copper | 0.365 kg | 0.280–0.340 kg | +7 % over |
| rotor backiron | **0.283 kg** | 0.250–0.300 kg | ✓ inside |
| magnets | **0.074 kg** | 0.072–0.086 kg | ✓ inside |
| **machine total** | **1.018 kg** | 0.812–0.976 kg | **+4 % over the top of the band** |

The machine is 1.018 kg against C40's declared **0.81–0.97 kg**. It is over, but only
by 4 % — C40's sizing was sound. Note the T3 spine (1.5 mm of steel at Ø30–33, running
the machine's length) is **not** counted here; it is part of A1.

### Three placement/geometry bugs, all caught by gate numbers

1. **Rotate-then-translate.** Building a block near the axis, rotating it, and only
   then translating it puts its centre on a circle of the *wrong radius* — the box
   has to be placed at its radius first. This put the magnets at **Ø96.2 on a Ø91.9
   machine**, i.e. buried in the ring carrier. Fixed in `_ring_of_blocks`, which both
   the magnets, the windings and the stator slots now go through.
2. **The same bug in the stator slot cuts**, which is why the core first weighed
   0.671 kg — the slots were being cut in the wrong place and removing a third of
   the iron they should have.
3. Both were found because the *numbers* disagreed with an independent figure (C40's
   band, and the ring OD), not because anything looked wrong.

### Findings

**T5 — the ring carrier alone is heavier than the whole kit budget.** Measured off the
solid:

| | steel | titanium | aluminium |
|---|---:|---:|---:|
| **B1 ring carrier** | **1.445 kg** | 0.816 kg | 0.497 kg |
| + backiron | 0.283 | 0.283 | 0.283 |
| + magnets | 0.074 | 0.074 | 0.074 |
| **rotating assembly** | **1.802 kg** | 1.173 kg | 0.854 kg |

The carrier is 184.1 cm³, and most of it is unavoidable: the ring must span from the
gap/backiron (Ø79.5) out to the canard bay skin (Ø98), which is **9.25 mm of wall over
80 mm of length** before any bearing bore or web is added. The pure outer shell —
Ø91.9 bore to Ø98 skin, the thinnest it can be — is 73 cm³ on its own.

**T6 — C26's setback case is understated by ×2.9 to ×3.6, and C35 follows it.** C26 is
built on a *0.5 kg* ring assumption ("0.5 kg × 15 000 g ≈ 73.5 kN"). The measured
rotating assembly is **1.802 kg in steel**, which gives **212.6 kN** on the carrier alone
and **265 kN** on the rotating assembly:

| | C26 / the register | model |
|---|---:|---:|
| ring mass | 0.5 kg (assumed) | **1.445 kg** (carrier, steel) |
| axial setback | **73.5 kN** | **212.6 kN** |
| with backiron + magnets | — | **265.1 kN** |
| C35 structural stiffness case | 367 N/µm | **1325 N/µm** |

Of the two levers, **material moves it more than geometry**: aluminium puts the rotating
assembly at 0.854 kg, i.e. 126 kN — still ×1.7 on the register's figure. C26's "every
0.1 kg costs 14.7 kN of retention" now reads as 14.7 kN per 0.1 kg *at the assumption*
and **≈11.8 kN per 0.1 kg at the measured value** — but the measured mass is 3.6× the
assumption, so the absolute load triples.

**This is the finding that matters most.** C26 is the governing structural case for the
whole CAD, C32's retention design exists to route it, and C35's air-gap stiffness case is
derived from it. All three now have a load that is roughly three times what they were
sized on. T4 and T5 together say the same thing from two directions: **the kit's mass
budget is short by roughly a factor of two, and it is structural material — not the
machine, not the electronics — that is spending it.**

### Phase 2 outputs

- `out/PGK-CAA.FCStd`
- `out/screenshots/p2-machine-section.png`

---

## Phase 3 — bearings and the C32 launch-load bypass · **PASS** · 2026-09-19

Document `PGK-Bearings`. Macro `macros/30_phase3_bearings.py`.
Screenshot `p3-retention-section.png`.
`A4_Brg_Inner_Races`, `B4_Brg_Outer_Races`, `C1_Balls_Cage`, `A11_Retention_Collar`.

### Gate 3 — the launch path

| # | check | result |
|---|---|---|
| 1 | balls fit the race gap | envelope r 30.75 vs race face r 31.00 → PASS |
| 2 | collar clears the ring skin | Ø97.60 inside Ø98.00, 0.200 mm → PASS |
| 3 | **thrust contact band overlaps** | 22.30 mm of radius, **1318.8 mm²** → PASS |
| 4 | axial travel before contact | 0.100 mm exactly → PASS |
| 5 | no compliant element in the axial path | collar and races monolithic steel → PASS |

Sized against the load T6 measured, not C26's assumption:

| | C26 assumed | Phase 2/3 measured |
|---|---:|---:|
| ring mass | 0.5 kg | **1.520 kg** |
| axial setback (carrier) | 73.5 kN | **223.4 kN** |
| axial setback (rotating assembly) | — | **275.8 kN** |
| scaling | — | **×3.04** |
| C35 structural stiffness case | 367 N/µm | **1117 N/µm** |

The collar's face is **1318.8 mm²** and sees **169.4 MPa** at 223.4 kN against a
PROVISIONAL 300 MPa allowable → **×1.77 margin**. For comparison, the first
arrangement that was tried put the same load on 935.6 mm² (233 MPa, ×1.29) —
widening the ring's aft recess from Ø53 … Ø69 to reach inboard of the bearing bore
cost 0.036 kg and bought a third of the margin back. That is the T4/T5 trade being
spent where it actually pays.

### Two bugs, and the second one would have shipped

1. **Units.** `SetbackMeasured * 1000 / AirGapDeflMax` gives **N/mm**, which the
   code then printed as N/µm — reporting C35's case as 1 040 322 N/µm, a factor of
   1000 wrong and absurd enough to notice. Fixed at source, with the conversion
   written into the expression rather than into a comment.
2. **A thrust face that does not overlap its partner takes no load, whatever the
   area formula says.** The collar's face was placed at r 39.35–45.85 while the
   ring's aft face sat at r 45.95–49.00 — a 0.10 mm radial gap, so the ring would
   have landed on **air**. Every number in the stress arithmetic still ran and
   still looked healthy; only an explicit *overlap* check catches this. Gate 3 now
   has one, and it is the check that matters most in this phase.

### Measurement feedback

Phase 2 now writes `out/measured.json`, and `pgk_params` reads it back. So C26's
ring mass, the setback derived from it, the collar sized on that setback and C35's
stiffness case all follow the *model* rather than a number typed into the source.
If the file is absent the last recorded figure is used and labelled a fallback.

### Session note — FreeCAD restarted mid-phase

The FreeCAD process was restarted between Phase 2 and Phase 3, taking the
in-memory documents with it. **All four phases were rebuilt from their macros with
identical results** (Phase 0 reproduced its 0.091 mm worst deviation and its
11 789.6 cm³ exactly). This is the scripted approach earning its keep: a
hand-modelled CAD session would have lost the work.

Two development-loop bugs surfaced by the same restart, both now fixed: FreeCAD's
long-lived interpreter caches `pgk_params` **and** `cadlib`, so an edited source of
truth was being silently shadowed by the previous import. Every macro now re-reads
both deliberately.

### Phase 3 outputs

- `out/PGK-Bearings.FCStd`
- `out/screenshots/p3-retention-section.png`

---

## Phase 4 — the four fixed-incidence canards · **PASS** · 2026-09-20

Document `PGK-Canards`. Macro `macros/40_phase4_canards.py`.
Screenshots `p4-canards-front.png`, `p4-canards-iso.png`.

`B5_Canard_Master` plus the four placed instances at 0 / 90 / 180 / 270°.

### Gate 4 — the canard set

| # | check | result |
|---|---|---|
| 1 | tip envelope | **Ø151.00** against the Ø151 cap → PASS |
| 2 | **cant measured off the solid** | **10.0000°** from the inertia tensor → PASS |
| 3 | in-bore clearance | **2.000 mm/side** at four rotor phases → PASS |
| 4 | exposed span | 26.50 mm, matching C31's own arithmetic → PASS |

Two of the register's numbers reproduce exactly off the geometry without being
used to build it: the **planform area computes to 2120.0 mm²** and the **aspect
ratio to 0.33** — which is what C31(d)'s "21.2 cm² per canard, AR 0.33" means,
arrived at independently.

The set is 4-fold symmetric, so a rotor phase rotation maps it onto itself and
the in-bore envelope cannot change with phase. That is stated rather than
assumed — the phase grid still earns its keep in Phases 5–7, where the front
end and internals are *not* symmetric.

### T7 — C1's canard sizing formula is a typo, and the register's own table proves it

C1 states `F_steer = 2·F·cos δ_s`. **C43's own trade table says otherwise:**

| cant | C43's table | `2·F·sin δ` | `2·F·cos δ` |
|---:|---:|---:|---:|
| 8° | 14.5 N | 14.51 ✓ | 103.2 ✗ |
| 10° | 18.1 N | 18.10 ✓ | 102.7 ✗ |
| 14° | 25.3 N | 25.22 ✓ | 101.1 ✗ |
| 16° | 29.0 N | 28.73 ✓ | 100.2 ✗ |

The sine form fits all four rows to **within 0.3 N**; the cosine form predicts
~102 N throughout and is flat over the range. C43's textual claim — *"going from
10° to 16° buys 60 % more guidance force"* — is `sin 16° / sin 10° = 1.587`, and
is **impossible** under a cosine, which would give 0.976, i.e. *less* force for
more cant and no coupling to C42 at all.

The model uses the sine form. Two consequences worth stating:

- **C8's requirement is unaffected.** F_steer ≥ 18.1 N is the datum that *pins*
  the implied fin normal force at **F = 52.12 N**, and the sine form reproduces
  the datum by construction. Nothing C8 claims moves.
- **C42/C43's coupling depends on it.** The architecture's defining cost —
  "cant buys force and costs dissipation in equal measure" — only holds under
  sine. Under the register's stated cosine, the 2.92 kW / 121 kJ would not scale
  with cant, and C43 would be describing a different machine.

This is a one-word fix in the register, and it is the kind of error that would
have been invisible without putting numbers through it.

### Canard mass — another T4/T5-class item

| | steel | titanium |
|---|---:|---:|
| one canard | 0.1331 kg | 0.0751 kg |
| **four** | **0.5325 kg** | **0.3005 kg** |

Four canards in steel are **38 % of P9's entire kit budget**, and they hang on the
ring, so they also add to C26's setback (every 0.1 kg is ~11.9 kN at the measured
scale). This is the third independent place the mass budget is being spent — body
(1.37 kg), rotating assembly (1.88 kg), canards (0.53 kg) — and it is the same
finding each time.

### Modelling notes, stated rather than hidden

- The fin is a **flat plate** with sharp edges. C6 (section / aerofoil) is OPEN, so
  no section is claimed; a real fin would carry an aerofoil and shaped edges.
- The planform is **rectangular**, because that is the only shape that yields the
  register's own area of 2120 mm² at a constant 80 mm chord over 26.5 mm of span.
  A swept or tapered planform would change the area, and area is not a free
  parameter here.
- The root is lofted from the 12 mm root thickness to the 4 mm tip. The register's
  `CanardRootThick` is PROVISIONAL; the manufacturing intent is that the root
  blends integrally into the ring carrier (the blisk argument), which is a Phase 7
  assembly question.

### Phase 4 outputs

- `out/PGK-Canards.FCStd`
- `out/screenshots/p4-canards-front.png`, `p4-canards-iso.png`

---

## Phase 5 — the front end, and the nose-ownership decision · **PASS** · 2026-09-20

Document `PGK-FrontEnd`. Macro `macros/50_phase5_frontend.py`.
Screenshot `p5-nose-section.png`.
`A10_Front_Hub`, `D1_Radome`, `D2_Gnss_Aperture`, `D3_Radar_Keepout`.

### The decision the plan flagged, now taken and defended

The CAA interface visualisation draws the nose as part of the roll-controlled
group with the fuze cavity inside it. **F9 and H5 cannot both hold with that
reading**, so the model takes the other one:

> the RF front end, the radome and the spin-axis aperture ride a **body-side
> axial hub** forward through the ring's bore; the ring ends at its fore face and
> keeps no nose of its own.

F2 says the radar is *"body-mounted in the nose tip ahead of the canard ring"*
and N3 makes the aperture rotationally symmetric on the spin axis *so that spin
cannot modulate it* — both statements about the body side. So the whole nose
turns with the shell, and the ring is exactly the canard bay. This is the
reading that satisfies F2 + N3 + F9 together.

### Gate 5

| # | check | result |
|---|---|---|
| 1 | in-bore | front end Ø98.0 against Ø155 → **28.5 mm/side** → PASS |
| 2 | forward bore clear of metal | **0.0000 mm³** in the Ø48 bore → PASS |
| 3 | interference with the ring, 4 phases | **0.0000 mm³** → PASS |

### A design error this gate caught, worth keeping

The aperture was **first drawn as a circumferential band looking radially
outward** at Ø48. That is wrong: N3's aperture has to see the *sky*, and the
round's nose points up throughout the ascent, so a band looking at the horizon
would be the wrong geometry — and the check that caught it was reading
450.8 mm³ of metal "in front of" the aperture, which turned out to be the hub's
own forward rim at a *larger* radius that blocks nothing.

The corrected geometry is what the physics wanted anyway: a **ring of elements
around the spin axis inside the cavity, looking forward through the radome.**
That has N3's symmetry *exactly* — the array maps onto itself under any rotation
— and it puts both antennas (radar on the axis, GNSS ring around it) inside one
dielectric window, which is the only version that fits a nose with no volume to
spare (risk 27). The check was then rewritten to test the **forward bore** rather
than a plane, because that is the geometry that actually matters.

### T8 — the junction step, and it connects two criteria nobody had linked

The register truncates the shell's ogive at the standard fuze diameter, **Ø50.8,
at the seat**. The kit's ring is **Ø98** and its aft face sits *above* the seat.
So the kit overhangs the shell's nose:

| | value |
|---|---:|
| rearward-facing step depth | **23.6 mm** |
| step frontal area | **5516 mm²** |
| as a fraction of the body cross-section | **29.3 %** |

**M10 requires >90 % range retention, and this is a drag source that has never
been priced against it.** The chain that produces it is not obvious:

> the machine's radial build closes at **Ø91.9** against C34's Ø92 ceiling
> → the ring must wrap it plus a wall → **RingOD ≈ 98**
> → and RingOD is what sets the step.

**The lever is C44 (radial vs axial flux), which is OPEN** — a pancake axial-flux
machine is the one change that shrinks the machine, the ring and the step
together, and the register's own note on C44 already observes that this annulus
("short and wide, ≤95.25 mm above the seat, Ø92 mm") is exactly the case where it
wins. **Nothing currently links C44 to M10.**

The trade, priced by the model:

| ring OD | junction step | exposed canard span |
|---:|---:|---:|
| **98** | 23.6 mm | 26.5 mm |
| 90 | 19.6 mm | 30.5 mm |
| 80 | 14.6 mm | 35.5 mm |
| 70 | 9.6 mm | 40.5 mm |

A smaller ring buys exposed span *as well as* step, which is a second reason to
want one — but the machine stops fitting below about Ø96, so this is a C34/C40
trade and not a free choice.

### Mass

`A10_Front_Hub` is **0.486 kg** in steel on its own — a fourth T4/T5-class item,
and the nose is a place aluminium is entirely defensible (it is not a magnetic
or wear-critical member).

### Phase 5 outputs

- `out/PGK-FrontEnd.FCStd`
- `out/screenshots/p5-nose-section.png`

---

## Phase 6 — internals and F9's split · **PASS** · 2026-09-20

Document `PGK-Internals`. Macro `macros/60_phase6_internals.py`.
Screenshot `p6-internals-section.png`.

### F9 is the organising principle, not a detail

The kit replaces the fuze, so the initiation path has to reach the shell's booster
on the centreline at the well bottom. F9 therefore reserves a clear Ø30 through the
well **and** the machine section, with everything else built as rings about it.
That splits this phase's parts into two groups that must never be confused:

| | parts | rule |
|---|---|---|
| **annular** | boards, buffer, dump, harness | must NOT enter the Ø30, at any z |
| **on axis** | impact switch, S&A rotor, detonator | lives IN the Ø30 — that is what it is for |

Gate 6 is written on that distinction, because an annular part crossing the line is
a real defect while the train crossing it is the design.

### Gate 6

| # | check | result |
|---|---|---|
| 1 | **F9 Ø30 reservation vs the annular parts** | **0.0000 mm³** → PASS |
| 2 | the train's legitimate occupation | impact switch Ø20, rotor Ø28, detonator Ø16 — all inside Ø30 |
| 3 | past the intrusion limit | 0.000 mm → PASS |
| 4 | interference with A1's real geometry | **0.0000 mm³** → PASS |
| 4b | A8 in A10's shoulder / C2 both sides | **0.0000 mm³** / **0.0000 mm³**, link gap 4.0 mm → PASS |
| 5 | packaging budget | 51.70 cm³ available, 48.44 demanded → **+6.3 %**, 6.65 mm spare |

The annular parts run the **same z band** as the train — the split is radial, not
axial. Packing them end-to-end instead would have thrown away most of the length,
and it is what "the fuze stack built as rings about it" means.

### T9 — the spigot had to be hollowed, and it is the biggest mass win yet

**Phase 1 modelled A1's well section as a solid annulus.** When the internals
arrived there was nowhere for them to go: 8404 mm³ of interference with the very
part they were supposed to live inside. A spigot is a **shell**, and modelling it
as one changes the whole mass picture:

| | solid spigot (Phase 1) | **shell, 1.5 mm wall** |
|---|---:|---:|
| A1 volume | 174.2 cm³ | **88.6 cm³** |
| A1 mass, steel | 1.368 kg | **0.696 kg** |
| A1 mass, aluminium | 0.470 kg | **0.239 kg** |

**That is 0.586 kg off the kit in steel — the single largest mass saving the CAD
has produced, and it revises T4.** The kit body is no longer the whole of P9's
budget on its own. It is also the *right* answer thermally: P6 wants a contacting
path through the well bore, and a thin wall is a low-resistance one.

### T10 — the annulus is 4.4 mm deep, so buffer energy can only be bought in LENGTH

With the shell hollowed, the usable annulus is bounded by the *shell's inner
surface*, not the spigot's outer one — which is smaller than it first looked:

| | value |
|---|---:|
| radial space for every internal | **4.40 mm** (r 15.5 → 19.9) |
| annulus area | 489.3 mm² |
| available volume over the full well | 51.70 cm³ |

That is the binding constraint, not the 105.65 mm of length. It matters most for
**W4's 150–200 J buffer**, which is a volume-limited item: W4's figure cannot be
met radially, only axially.

| buffer length | volume | energy at 7 J/cm³ | against W4 |
|---:|---:|---:|---|
| 36 mm | 17.6 cm³ | **123 J** | **short** |
| **55 mm** | 26.9 cm³ | **188 J** | inside 150–200 J ✓ |

55 mm closes W4 but consumes the axial spare, leaving **6.65 mm** across the whole
stack. The kit is now genuinely full in the well, and the next item to be added
will not fit.

### Two integration bugs worth keeping

1. **The internals were sized to the wrong radius.** `annulus()` was written before
   `SpigotWall` existed, so it returned the spigot's *outer* radius — putting every
   internal inside the wall meant to contain it. 8404 mm³ of interference. A
   derived bound must be re-derived when the geometry it bounds changes.
2. **A check compared against a shape that does not exist.** Phase 5's coil pocket
   was cut in `build()`, so Phase 6's check — which calls `front_hub()` directly —
   compared the coil against the *uncut* hub and reported 5202 mm³ of interference
   on a part that was actually fine. The pocket now lives inside `front_hub()`.
   A part function must return the part, not a pre-modification version of it.

### Phase 6 outputs

- `out/PGK-Internals.FCStd`
- `out/screenshots/p6-internals-section.png`
