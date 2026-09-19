# DRISHTI-PGK — CAD Evidence and Findings

**Purpose of this file:** the register-facing record of what the CAD workspace (`design/cad/`) has **built, proved, and found**. The CAD evidences; it never decides (README rule 2). Everything below is either a *verified interface fact* — which the submission may quote — or a *finding addressed to a criterion*, which is the register's to rule on.

**Status:** created 2026-09-20. CAD **Phases 0–2 built, gates PASS** (envelope, A1 kit body, ring and machine). Findings **T1–T4 open** — none has been ruled on by the register, and none changes a decided value until it is.

**The authority order, restated:** the register is authoritative; the CAD is evidence. Where a CAD-computed number disagrees with the register, both are carried here and the register picks. This is the rule that made T1 visible instead of silently resolved.

---

## 1. What the gates have proved

| Gate | Check | Result |
|---|---|---|
| 0a | Reference shell reproduces P8's published contour table | worst \|Δ\| **0.091 mm** against a ±0.5 mm gate — PASS (the residual is the register's rounding) |
| 0b | The well's faces reproduce P6's own arithmetic | thread flank **0.18 %**; seat annulus **1.3 %**; well bore **8.3 % low** → **finding T1** |
| 0c | Solid verified by point membership (13 probes) | all 13 as expected; the two initial "failures" were errors in the probe |
| 1 | The kit body's interface to the shell | intrusion **124.70 mm** (≤ 124.7); spigot clearance 0.10 mm radial; thread crest clears; **shell interference 0.0000 mm³**; seat annulus 1.3 % vs P6 |
| 1b | Solid verified by point membership (10 probes) + volume cross-check | **0 mismatches**; 179.2 cm³ against a hand integration's 178.8 cm³ (**0.2 %**) |
| 2 | Ring and machine (document `PGK-CAA`) | built against the machine sizing; see the verification log for the gate record |

**What the submission may quote from this** (used on the deck, slide 4): **124.70 mm intrusion, zero interference with the reference shell, and the seat annulus matching the register's own area to 1.3 %.** These are interface verifications, not design decisions — safe to state.

---

## 2. The findings, and the criterion each is addressed to

### T1 — P6 quotes two well diameters that cannot both hold → **P6**

P6 sizes its thermal closing route on a well-bore contact area of **18.8 × 10⁻³ m²**, which is a **Ø48** bore; but it also quotes a seat annulus of 0.5 × 10⁻³ m² over a ring **Ø44–50.8**, which implies a **Ø44** spigot. Solving P6's own seat figure for its inner diameter gives **44.09 mm** — confirming Ø44 as the self-consistent reading, and confirming Ø48 cannot hold at the same time.

**The CAD adopts Ø44** — the reading that makes the seat a real face — and reports the cost: **8.3 % of the bore area** that P6's ≥ 58 W/K route leans on.

**Addressed to P6.** Either the bore figure is corrected, or the closing route's area budget is re-stated. The seat annulus is unaffected (it is the figure that reproduces).

### T2 — P12's exposed length and C8's canard chord are in tension → **P12, C4/C5, C31**

P12 caps the kit's exposed length at the fielded benchmark's **95.25 mm**. C31 caps canard span at Ø151 mm and shows the span cap must be paid for in **chord**. The chord C8 needs is ≈ **80 mm**, leaving 9.25 mm for the nose against the ≈20 mm a radome plus the spin-axis aperture needs. **Shortfall: 10.75 mm** — the kit needs ≈ **106 mm exposed**, and the chord that *would* fit P12 is 69.25 mm.

**The register's own reading is available and probably right:** P12 is a PARAMETRIC benchmark (the fielded kit's figure), not a hard requirement, and C31's permanent exposure removes the folding option that let the fielded kit hide its chord. So the likely ruling is *this kit is legitimately slightly longer* — but it is a **register decision**, and it interacts with C31 (span) and C8 (force).

**Addressed to P12 and C4/C5/C31.** Decide the exposed length; the canard chord follows, and C8's force follows the chord.

### T3 — the train bore costs slot depth, and no criterion owned it → **C19, C42, C32/C35**

F9 reserves a clear ≈Ø30 through the whole well *and* machine section. The machine sizing's radial build assumed the stator core's own bore **is** that reservation — charging the machine nothing for the structure that holds it together. A **spine tube** (`SpineWall` = 1.5 mm, PROVISIONAL) sits on the reservation and the core builds outside it:

| | sizing | with the spine | cost |
|---|---:|---:|---:|
| stator bore (yoke inner) | Ø30.0 | Ø33.0 | — |
| slot depth | 19.60 mm | **18.15 mm** | **−7.4 %** |
| machine OD (check) | 91.90 | 91.90 | unchanged, 0.10 mm margin |

Torque scales with slot area, so **C19's 5.76 N·m and C42's 2.92 kW / 121 kJ each carry a ×0.926 factor** unless the loss is bought back elsewhere (more length, deeper yoke, higher current density).

**Addressed to C19, C42 and C32/C35.** Two possible rulings: absorb the factor into the numbers, or buy it back — and if it is absorbed, **the thermal interface's ≥ 58 W/K requirement scales with C42**, so P6's requirement moves with it. This is a P2-class reconciliation item.

### T4 — the kit body alone consumes P9's entire mass budget → **P9, C40**

Measured off the solid, not estimated:

| material | A1 kit body | against P9's ≤ 1.4 kg for the *whole kit* |
|---|---:|---|
| steel (7850 kg/m³) | **1.407 kg** | **100 % of the budget, before anything else** |
| titanium (4430) | 0.794 kg | 57 % |
| aluminium (2700) | 0.484 kg | 35 % |

C40 already puts the machine at 0.81–0.97 kg and conceded the kit would land at 1.4–1.7 kg. With ring, canards, bearings, boards, fuze, dump and buffer added, the kit is a **factor of about two** over P9. The spigot is the irreducible core: Ø44 OD with a Ø30 train bore leaves 7 mm of wall over 105 mm — **0.675 kg in steel alone, 48 % of the budget in one tube that F9 and P6 between them fully determine.**

**The levers, in the CAD's own order:** **material** (the spigot is not strength-critical if C32 routes the launch load through the seat) and **lightening every web that is not a load path**. Phase 1 has started the second, with 8 holes per spider.

**Addressed to P9 and C40 as a joint decision.** The honest positions are: (a) raise P9 to the kit's real class and state the net platform effect, (b) hold P9 and pay for it in material and lightening — titanium lands the body at 0.79 kg, which closes the body but not the machine — or (c) both. What is not available is silence: the deck's mass claim and C40's own note already point at this.

---

## 3. What the deck now carries (traceability)

| Deck location | Text | Source |
|---|---|---|
| Slide 4, under the figures | *"And the hardware is now drawn: the kit body is modelled against the fuze well from our own numbers — 124.70 mm intrusion, zero interference with the reference shell, and the seat annulus that carries the 121 kJ matches the register's own area to 1.3 %."* | §1 verified interface facts |
| Slide 4, "What we cannot claim yet" | mass (body alone at the 1.4 kg limit in steel; material + lightening as the levers) and the train-bore slot-depth cost (≈7 % of slot depth) | T3, T4 — stated in the deck as open reconciliation items, in the deck's own honesty column |

**What the deck must not yet claim:** a kit mass, a revised energy figure, or a final exposed length. All three are pending the register's rulings above.

---

## 4. What the register is asked to do

| # | Finding | Criteria to rule on | Preferred route |
|---|---|---|---|
| 1 | T1 | P6 | Correct the bore figure or re-state the closing-route area; seat annulus stands |
| 2 | T2 | P12, C4/C5, C31 | Rule the exposed length (the PARAMETRIC reading permits ≈106 mm); chord and force follow |
| 3 | T3 | C19, C42, C32/C35; then P6 | Absorb ×0.926 or buy it back; if absorbed, scale P6's requirement with C42 |
| 4 | T4 | P9, C40 | Joint decision: raise the limit, pay in material/lightening, or both |

**These are the only open items this file creates.** Everything else the CAD has produced is verification, not tension.

---

## 5. Cross-references

| File | Relationship |
|---|---|
| `design/cad/` | The workspace itself — README, `pgk_params.py` (source of truth), macros, models, screenshots, verification log |
| `design/cad/VERIFICATION-LOG.md` | The gate-by-gate record this file summarises; numbers come from there |
| `design/cad/TRACEABILITY.md` | Generated: every dimension against its criterion |
| `design/00-design-criteria-register.md` | Where T1–T4 must land: P6, P12, C4/C5/C31, C19, C42, C32/C35, P9, C40 |
| `design/ROADMAP-and-prompts.md` | Carried items track the rulings; P4 status |
| `submission/deck/deck.html` | Slide 4 carries the verified facts and the two open items |
| `submission/SIH26098-judge-and-competitor-dossier.md` | Move 2 (ship the CAA CAD) — now partially shipped; Q28's assembly answer now has CAD backing |

---

*Rule carried from the CAD workspace: **the CAD evidences; it never decides.** A criterion does not become DEFINED because the model agrees with it, and a finding does not change a value until the register rules.*
