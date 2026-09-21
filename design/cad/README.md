# DRISHTI-PGK — CAD workspace

The P4 hardware definition: the canard actuation assembly and the whole kit, built
script-by-script in FreeCAD so that every dimension traces to a criterion in
`design/00-design-criteria-register.md`, and so the model can be rebuilt from source
whenever a criterion moves.

**This directory is inside `design/`** because the project's standing rule is that only
`design/` may be written to. `notes/` and `submission/` are never touched from here.

---

## What is being built

A drop-in retrofit that replaces the fuze of a 155 mm HE shell. It screws into the
MIL-STD-333B well on a 2″-12 UNS-2A thread and carries a **de-spun ring** that is
roll-controlled by a frameless outrunner PMSM — the same machine that generates the
kit's power. Four **fixed-incidence** canards on that ring steer the round. One moving
part, no actuation mechanism.

The engineering claim the model has to make visible:

> **The bearing holds it, the motor steers it.**
> Two parallel interfaces between the same two bodies: mechanical (bearing — 100 % of
> structural load, no torque path) and electromagnetic (PMSM — 100 % of torque control,
> no load path).

---

## How to rebuild

```bash
# 1. regenerate the evidence documents from the source of truth
python3 design/cad/write_traceability.py

# 2. audit the numbers without FreeCAD
python3 design/cad/pgk_params.py

# 3. build (from the FreeCAD MCP session, or freecadcmd)
freecadcmd design/cad/macros/00_phase0_envelope.py
```

Every macro is re-runnable and idempotent: it closes any existing document of its own
name and rebuilds from `pgk_params.py`. Nothing is hand-clicked, so the model is
deterministic and reviewable in diff.

---

## Conventions — fixed before the first sketch

| Item | Convention |
|---|---|
| **Datum origin** | **Z = 0 at the shell's fuze-well mouth plane** — where the ogive truncates. One datum, one meaning, for every part. |
| **Spin axis** | **+Z**, forward toward the nose (out of the shell). The well is at negative Z. |
| **Azimuth** | +X = 0° (steering canard 1), +Y = 90° (control canard 1). Roll measured about +Z, right-hand rule. |
| **Sign conventions** | Cant (+) = the fin leans so that its normal force has a positive tangential component. |
| **Units** | millimetres, degrees, kilograms, newtons, N·m. No unit-less numbers in a sketch. |
| **Mapping to `04-caa-dual-spin-interface.html`** | `x_html → z_cad`. The HTML used +X as the axis; it is a visualisation, the register is authoritative. |
| **Assembly state count** | **Two axial states** (LAUNCH, FLIGHT) × **four rotor phases** (0/45/90/135°). Eight combinations — see `TRACEABILITY.md`. |

### The axial stack, and where the well's faces are

The well is modelled as a real set of faces rather than an assumed area, because P6's
thermal argument is an argument about *areas*:

```
z = 0        shell mouth plane; the ogive truncates here at Ø50.8
z = 0 .. -19.05     threaded bore Ø50.8  (9 turns at 12 TPI = 19.05 mm)
z = -19.05          SEAT ANNULUS, Ø44 -> Ø50.8, faces +Z  — the kit's shoulder lands here
z = -19.05 .. -124.7   plain well bore Ø44
below -124.7        booster cavity, tapering to Ø30 on the axis (F9)
```

The kit's own shoulder is the matching annulus, which is what makes P6's seat figure a
real face rather than a radius picked to give the right area.

---

## Files

```
pgk_params.py          THE SOURCE OF TRUTH — every dimension + criterion + status
part_index.py          THE VOCABULARY — every part's name, group, material,
                       colour and one-line purpose; what the tree shows
write_traceability.py  regenerates TRACEABILITY.md, PARAMETERS.txt, PARTS.md
TRACEABILITY.md        generated: every dimension against its criterion
PARAMETERS.txt         generated: the audit listing + closure checks
PARTS.md               generated: every part, named, grouped and measured
VERIFICATION-LOG.md    hand-kept: what each gate proved, and when
macros/
  00_phase0_envelope.py      reference shell, well, bore, train-bore, ogive bound
  10_phase1_kit_body.py      (Phase 1)
  ...
  95_render_deck_images.py   presentation renders for the submission deck
out/
  PGK-Envelope.FCStd         the envelope document
  screenshots/               visual evidence, one per gate
  deck-renders/              the raw 2560x1440 frames the deck images come from
deck_render_trim.py          trims those frames and publishes them to
                             submission/deck/figures/cad/
```

`95_render_deck_images.py` is **not a phase**: it builds nothing and decides
nothing, it only draws what the phases already built, in a colour per functional
group, with staged and sectioned views. Its destination folder carries the
colour key and the list of views.

---

## How to read the model

Open `out/PGK-Assembly.FCStd`. The tree is the first thing anyone reads, so it
is arranged the way the architecture is:

```
1 Body side — turns with the shell        17 parts
2 Ring side — de-spun, carries the fins    9 parts
3 Between the two bodies                   1 part
Parameters — pgk_params.py (source of truth)
```

- **Every part is named in words**, not just in codes: the tree shows
  `A1 Kit body`, `B1 Ring carrier`, `B5 Fin, control A`. The code is still the
  object's internal name, so nothing in the scripts moved.
- **Every part is coloured by what it is**, and it is the same colour it has in
  the deck renders — the board stack, the copper, the magnets, the bearing path
  and the fuze train each read as themselves. The steering and control fins are
  two shades of one blue because they are one part made twice, mounted at two
  cants.
- **The groups are the claim.** Body side and ring side are the two bodies in
  relative rotation; what lies between them is the bearings. That split is the
  same one the interference grid and the mass rollup use.

`PARTS.md` is the same information in writing: one row per part with its group,
material, measured mass and what it does, generated from `part_index.py` so it
cannot drift from the model. **`part_index.py` is where a part's entry lives** —
adding a part without adding it there still builds, but the build says so out
loud rather than letting another grey box into the tree.

---

## The rules this workspace follows

Carried from the register, and not negotiable:

1. **No literal numbers in geometry.** Every dimension is read from `pgk_params`. If a
   number is needed and isn't there, it gets added to the SSOT with its criterion and
   status first.
2. **The CAD evidences; it never decides.** A criterion is not `DEFINED` because the
   CAD agrees with it. Every value resting on an OPEN criterion is marked
   **PROVISIONAL** and names that criterion.
3. **Report the conflict, don't hide it.** Where the register's own numbers are in
   tension, the model computes both sides and states the gap rather than quietly
   choosing one. Two such tensions are already recorded below.
4. **No mass is quoted from the envelope solids.** The reference shell is a *contour*
   model; P2/P3/P4/P5 come from the calibrated model in
   `02-reference-155mm-model.md`. Only kit masses computed from the kit's own solids
   in Phases 1–6 are quoted, and they are labelled with the criterion they serve.

---

## Tensions the model has already found

Recorded here because each is a real finding against the register, not a modelling
inconvenience. They are recorded in `design/07-cad-evidence.md`, with the criterion each
is addressed to and the ruling still owed.

**T1 — P6 quotes two well diameters that cannot both hold.** P6 sizes its thermal
closing route on a well-bore contact area of 18.8 × 10⁻³ m², which is a **Ø48** bore;
but it also quotes a seat annulus of 0.5 × 10⁻³ m² over a ring **Ø44–50.8**, which
implies a Ø44 spigot. The model adopts **Ø44** — the self-consistent reading, and the
one that makes the seat a real face — and reproduces P6's seat figure to 1.3 %
(0.506 vs 0.500 × 10⁻³ m²). The cost is **8.3 %** of the bore area P6's ≥58 W/K
argument leans on. Both areas are computed outputs; the register picks.

**T2 — P12's visible length and C8's canard chord are in tension.** P12 caps the kit's
exposed length at the fielded benchmark's 95.25 mm. C31 caps the canard span at Ø151,
and C31(d) shows the span cap must be paid for in **chord** (area cannot buy the force
back). The chord C8 needs is ~80 mm, which leaves 9.25 mm for the nose against the
~20 mm a radome plus the spin-axis aperture needs. **Shortfall: 10.75 mm** — the kit
needs ≈106 mm exposed, and the chord that *would* fit P12 is 69.25 mm. Since P12 is a
PARAMETRIC benchmark rather than a hard requirement, and C31's permanent exposure
removes the folding option that let the fielded kit hide its chord, the likely answer is
that this kit is legitimately slightly longer. That is a register decision, not a CAD one.

**T3 — the train bore costs slot depth, and no criterion owned it.** F9 reserves a clear
≈Ø30 through the whole well *and* machine section. The machine sizing's radial build
assumes the stator core's own bore **is** that reservation, so it is charged nothing for
the structure that holds the machine together. A spine tube of 1.5 mm (`SpineWall`, at
Ø30–33) is needed, and the core then builds outside it: **slot depth falls 19.60 → 18.15 mm
(−7.4 %)**, and because torque scales with slot area, **C19's 5.76 N·m and C42's 2.92 kW /
121 kJ each carry a ×0.926 factor.** `SpineWall` is PROVISIONAL and belongs with C32/C35.

**T4 — the kit body alone consumes P9's entire mass budget.** Measured off the solid:

| material | A1 kit body | against P9's ≤ 1.4 kg for the *whole kit* |
|---|---:|---|
| steel | **1.407 kg** | **100 % of the budget, before anything else** |
| titanium | 0.794 kg | 57 % |
| aluminium | 0.484 kg | 35 % |

C40 already puts the machine alone at 0.81–0.97 kg, and C40's own note conceded the kit
would land at 1.4–1.7 kg. With the ring, canards, bearings, boards, fuze, dump and buffer
added the kit looks like **roughly ×2 over P9**. The spigot is the irreducible core of it:
Ø44 OD with the Ø30 train bore leaves 7 mm of wall over 105 mm, which is 0.675 kg in steel
— 48 % of the budget in one tube that F9 and P6 between them fully determine. The levers
are **material** (the spigot is not strength-critical if C32 routes the launch load through
the seat) and **lightening every web that is not a load path**. P9 and C40 need a joint
decision; the CAD prices it.

---

## Gate discipline

A phase does not advance on a failed gate. Every gate result is written to
`VERIFICATION-LOG.md` with the numbers that produced it, and a screenshot is saved to
`out/screenshots/`.

**Step 0 environment** (recorded 2026-09-19): FreeCAD **1.1.3** (build 20260725), Python
3.11.14. Workbenches present: PartDesign, Sketcher, Part, Spreadsheet, Assembly,
TechDraw, Material, Import, Mesh. Assembly is available, but the build deliberately
**does not depend on it** — parts are placed by scripted `Placement` from the SSOT and
interference is checked with `Part::MultiCommon`, so the model survives any FreeCAD
version and every placement is data rather than a drag.
