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
