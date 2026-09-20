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
