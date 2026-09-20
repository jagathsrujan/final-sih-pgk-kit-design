# DRISHTI-PGK — CAD Evidence and Findings

**Purpose of this file:** the register-facing record of what the CAD workspace (`design/cad/`) has **built, proved, and found**. The CAD evidences; it never decides (README rule 2). Everything below is either a *verified interface fact* — which the submission may quote — or a *finding addressed to a criterion*, which is the register's to rule on.

**Status:** created 2026-09-20, extended the same day. CAD **Phases 0–7 built, every gate PASS** — envelope, kit body, ring and machine, bearings and the C32 retention path, canards, front end, internals, and the eight-state assembly. Findings **T1–T10 open**; none has been ruled on by the register, and none changes a decided value until it is.

**What changed in this extension.** Phases 3–7 completed the hardware definition and produced findings **T5–T10**, two of which (T6, T8) need a decision rather than more analysis. **T9 revises T4**: the kit body's mass was cut by 0.59 kg when the spigot stopped being modelled solid. And the assembly now carries a **measured mass rollup** — the whole kit, off solids, for the first time.

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
| 2 | Ring and machine | air gap **0.400 mm** exactly; machine OD **91.90** against the Ø92 ceiling (0.10 mm margin); stack 28 mm in the 25–30 band; 14 poles / 12 slots; ring OD 98.00 |
| 2b | Two independent cross-checks off the geometry | tooth width computes to the sizing's own **8.45 mm**; slotted stator core **0.296 kg** against C40's 210–250 g band |
| 3 | The C32 launch path | thrust contact band **1074.4 mm²**, face stress **207.9 MPa** at 223.4 kN → **×1.44 margin**; axial travel 0.100 mm; every element monolithic steel (C35's prohibition held). *Margin revised down from ×1.77 when the canards became real geometry — see the defect note in the verification log* |
| 4 | The canard set | tips **Ø151.00** against the cap; cant **10.0000° measured off the inertia tensor**; in-bore **2.000 mm/side**; exposed span 26.50 mm; area **2120.0 mm²** and AR **0.33** reproduce C31(d) |
| 5 | Front end | Ø98 against Ø155 → **28.5 mm/side**; **0.0000 mm³** of metal in the aperture's forward bore; **0.0000 mm³** interference with the ring at 4 phases |
| 6 | Internals, under F9's split | **0.0000 mm³** in the Ø30 reservation from every annular part; **0.0000 mm³** against A1; setter coil in A10's shoulder **0.0000 mm³**; both halves of the contactless link **0.0000 mm³**, 4.0 mm working gap |
| 7 | The eight-state grid (4 rotor phases × FLIGHT/LAUNCH) | **all eight 0.0000 mm³**; the C32 seat closes to **0.0000 mm** gap in LAUNCH and holds 0.100 mm in FLIGHT |

**What the submission may quote from this** (used on the deck, slide 4): **124.70 mm intrusion, zero interference with the reference shell, the seat annulus matching the register's own area to 1.3 %, an air gap of exactly 0.400 mm, and a canard cant measured at 10.0000°.** These are interface verifications, not design decisions — safe to state.

---

## 2. The measured mass rollup

Every value off a solid. Structural parts in steel; aluminium shown as the lever.

| group | steel | aluminium structure |
|---|---:|---:|
| body side | 2.231 kg | — |
| ring side | 2.595 kg | — |
| **kit total** | **4.839 kg** | **2.713 kg** |
| machine alone (C40's own check) | | **1.018 kg** — +5 % over the band top |
| rotating assembly (C26's load) | | **1.876 kg** |

Against **P9's ≤ 1.4 kg**: **+246 %** as modelled, **+94 %** with an aluminium structure.

**The machine is fine — C40 was sound, within 5 %.** Everything else is not. Even with aluminium throughout, the kit is **roughly ×2 over P9**, and the remaining levers are material, ring diameter (T8) and the retention hardware (T6).

---

## 3. The findings, and the criterion each is addressed to

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

### T4 — the kit body and the mass budget → **P9, C40** *(revised by T9)*

As Phase 1 first measured it, the kit body alone was **1.407 kg in steel** — 100 % of P9's budget for the whole kit, before anything else. **T9 then cut it to 0.696 kg**, and the finding is now best read as part of the whole rollup above rather than as a single-part crisis:

| material | A1 kit body, as first modelled | **after T9** |
|---|---:|---:|
| steel | 1.407 kg | **0.696 kg** |
| aluminium | 0.484 kg | **0.239 kg** |

The irreducible core the original finding identified has not gone away — Ø44 OD with the Ø30 train bore through it leaves **7 mm of wall over 105 mm**, and F9 and P6 between them fully determine that. What T9 showed is that the *wall could be 1.5 mm rather than solid*.

**Addressed to P9 and C40 as a joint decision, with the rollup above and T5/T6/T9/T10 in hand.** The honest positions are: (a) raise P9 to the kit's real class and state the net platform effect, (b) hold P9 and pay for it in material and lightening, or (c) both. What is not available is silence.

### T5 — the ring carrier alone outweighs the whole kit budget → **C7, C34/C44, P9**

**1.520 kg in steel** (0.497 aluminium). Most of it is unavoidable in steel: the ring must span from the gap/backiron at **Ø79.5** out to the canard bay at **Ø98** — **9.25 mm of wall over 80 mm of length** — before any bearing bore or web is added. The pure outer shell alone, the thinnest it can be, is 73 cm³.

**Addressed to C7 and the C34/C44 trade.** T8 gives the same trade a second reason to exist.

### T6 — C26's setback case is understated ×3, and C32/C35 inherit it → **C26, C32, C35**

C26 is built on a **0.5 kg** ring assumption. The model measures the rotating assembly at **1.876 kg**:

| | C26 / the register | model |
|---|---:|---:|
| ring carrier | 0.5 kg (assumed) | **1.520 kg** |
| axial setback | **73.5 kN** | **276 kN** (rotating assembly) |
| C35's structural case | 367 N/µm | **1117 N/µm** |

C32's retention collar was sized against the **measured** load and closes at **169.4 MPa on 1318.8 mm², ×1.77 margin** — so the architecture survives. But all three criteria are sized on a load roughly three times what they were written against.

**Addressed to C26, C32 and C35.** Correct the ring-mass assumption and re-baseline the three rows on it. This is the finding that changes a load three criteria depend on.

### T7 — C1's canard sizing formula is a typo, proven by C43's own table → **C1**

C1 states `F_steer = 2·F·cos δ`. **C43's own trade table refutes it:**

| cant | C43's table | `2·F·sin δ` | `2·F·cos δ` |
|---:|---:|---:|---:|
| 8° | 14.5 N | 14.51 ✓ | 103.2 ✗ |
| 10° | 18.1 N | 18.10 ✓ | 102.7 ✗ |
| 14° | 25.3 N | 25.22 ✓ | 101.1 ✗ |
| 16° | 29.0 N | 28.73 ✓ | 100.2 ✗ |

Sine fits all four rows to **within 0.3 N**. Cosine predicts ~102 N throughout and is **flat** — so C43's own textual claim that 10° → 16° buys 60 % more guidance force is **impossible** under it, which would give 0.976, i.e. *less* force for more cant and no coupling to C42 at all.

**C8 is unaffected** — 18.1 N is the datum that pins the implied fin normal force at **52.12 N**, and sine reproduces it by construction. But **C42/C43's coupling depends on it**: the architecture's defining cost, "cant buys force and costs dissipation in equal measure", only holds under sine.

**Addressed to C1.** One word: `cos` → `sin`.

### T8 — the junction step, and it connects two criteria nobody had linked → **C44, M10**

The register truncates the shell's ogive at **Ø50.8 at the seat**. The kit's ring is **Ø98** with its aft face *above* the seat, so the kit overhangs the shell's nose by a rearward-facing step **23.6 mm deep and 5516 mm² in frontal area — 29.3 % of the body cross-section**.

**M10 requires >90 % range retention, and this drag source has never been priced against it.** The chain is not obvious:

> the machine's radial build closes at **Ø91.9** against C34's Ø92 ceiling
> → the ring must wrap it plus a wall → **RingOD ≈ 98** → and RingOD sets the step

| ring OD | junction step | exposed canard span |
|---:|---:|---:|
| **98** | 23.6 mm | 26.5 mm |
| 90 | 19.6 mm | 30.5 mm |
| 80 | 14.6 mm | 35.5 mm |
| 70 | 9.6 mm | 40.5 mm |

A smaller ring buys exposed span *as well as* step — but the machine stops fitting below about Ø96, so it is a C34/C40 trade and not a free choice.

**Addressed to C44 and M10.** **C44 (radial vs axial flux) is OPEN**, and its own register note already observes that this annulus — short and wide, ≤95.25 mm above the seat — is exactly the case where a pancake axial-flux machine wins. **Nothing currently links C44 to M10.**

### T9 — the spigot had to be hollowed, −0.586 kg → **P9, P14, P6**

Phase 1 modelled A1's well section as a **solid** annulus. When the internals arrived there was nowhere for them to go: **8404 mm³ of interference with the very part they were supposed to live inside**. A spigot is a shell.

| | solid (Phase 1) | **1.5 mm shell** |
|---|---:|---:|
| A1 volume | 174.2 cm³ | **88.6 cm³** |
| A1 mass, steel | 1.368 kg | **0.696 kg** |

**The largest single mass saving the CAD produced**, and it revises T4. It is also the right answer thermally: P6 wants a *contacting* path through the well bore, and a thin wall is a low-resistance one.

**Addressed to P9 and P14.** `SpigotWall` is PROVISIONAL; it needs confirming against the ramming case.

### T10 — the annulus is 4.4 mm deep, so buffer energy can only be bought in length → **W4, H5**

With the shell hollowed, the usable annulus is bounded by the *shell's inner* surface, not the spigot's outer one — **4.40 mm of radial space** (r 15.5 → 19.9), 489.3 mm², **51.70 cm³** over the full well. Radial depth is the binding constraint, not the 105.65 mm of length.

That matters most for **W4's 150–200 J buffer**, which is volume-limited:

| buffer length | volume | energy at 7 J/cm³ | against W4 |
|---:|---:|---:|---|
| 36 mm | 17.6 cm³ | **123 J** | **misses** |
| **55 mm** | 26.9 cm³ | **188 J** | closes it ✓ |

55 mm closes W4 but consumes the axial spare, leaving **6.65 mm** across the whole stack. **The kit is now genuinely full in the well, and the next item to add will not fit.**

**Addressed to W4 and H5.** Either W4's energy target is set against the space that exists, or the axial spare is accepted as spent.

---

## 4. What the deck now carries (traceability)

| Deck location | Text | Source |
|---|---|---|
| Slide 4, under the figures | *"And the hardware is now drawn — the kit body is modelled against the fuze well from our own numbers: 124.70 mm intrusion, zero interference with the reference shell, the seat annulus that carries the 121 kJ matching the register's own area to 1.3 %, an air gap of exactly 0.400 mm, and a canard cant measured at 10.0000°."* | §1 verified interface facts |
| Slide 4, "What we cannot claim yet" | mass (the measured rollup is ×2 over P9, and C40's own machine figure is +5 %), the train-bore slot-depth cost (≈7 % of slot depth), and the junction step (T8, against M10) | T3, T4/T5/T6/T9/T10, T8 — stated as open reconciliation items in the deck's own honesty column |

**What the deck must not yet claim:** a kit mass, a revised energy figure, a final exposed length, or that the junction step is resolved. All four are pending the register's rulings below.

---

## 5. What the register is asked to do

| # | Finding | Criteria to rule on | Preferred route |
|---|---|---|---|
| 1 | T1 | P6 | Correct the bore figure or re-state the closing-route area; seat annulus stands |
| 2 | T2 | P12, C4/C5, C31 | Rule the exposed length (the PARAMETRIC reading permits ≈106 mm); chord and force follow |
| 3 | T3 | C19, C42, C32/C35; then P6 | Absorb ×0.926 or buy it back; if absorbed, scale P6's requirement with C42 |
| 4 | T4 | P9, C40 | Joint decision on the mass rollup: raise the limit, pay in material, or both |
| 5 | **T5** | C7, C34/C44 | The ring's diameter is the lever for both T5 and T8 |
| 6 | **T6** | C26, C32, C35 | **A decision, not analysis** — correct the ring mass and re-baseline three rows. C32's collar closed at **×1.44** once the canards were corrected |
| 7 | **T7** | C1 | One word: `cos` → `sin` |
| 8 | **T8** | C44, M10 | **A decision, not analysis** — open the C44 trade and link it to M10 |
| 9 | **T9** | P9, P14 | Confirm `SpigotWall` against the ramming case |
| 10 | **T10** | W4, H5 | Set W4's target against the space, or accept the axial spare as spent |

**T6 and T8 are the two that change architecture rather than bookkeeping.** T6 moves a load three criteria are sized on. T8 is a drag source against a requirement the register already claims, and the row that could fix it is OPEN and currently unconnected to it.

---

## 6. Cross-references

| File | Relationship |
|---|---|
| `design/cad/` | The workspace itself — README, `pgk_params.py` (source of truth), macros, models, screenshots, verification log |
| `design/cad/VERIFICATION-LOG.md` | The gate-by-gate record this file summarises; numbers come from there |
| `design/cad/TRACEABILITY.md` | Generated: every dimension against its criterion, and the PROVISIONAL set with what closes each |
| `design/00-design-criteria-register.md` | Where T1–T10 must land |
| `design/ROADMAP-and-prompts.md` | Carried items track the rulings; P4 status |
| `submission/deck/deck.html` | Slide 4 carries the verified facts and the open items |
| `submission/SIH26098-judge-and-competitor-dossier.md` | Move 2 (ship the CAA CAD) — now shipped through Phase 7; Q28's assembly answer has CAD backing |

---

*Rule carried from the CAD workspace: **the CAD evidences; it never decides.** A criterion does not become DEFINED because the model agrees with it, and a finding does not change a value until the register rules.*
