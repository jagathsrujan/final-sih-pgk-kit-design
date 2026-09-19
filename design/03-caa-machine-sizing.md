# CAA machine sizing — frameless outrunner PMSM

**Purpose:** size the frameless outrunner PMSM that forms the de-spun canard ring's alternator — simultaneously the ring actuator and the kit's generator. Records the calculation, the assumptions, and the recommended specification.

**Status:** sizing result, 2026-09-18 — **confirmed by the team 2026-09-18** (C14–C16, C34, C36, C41 `DEFINED`; C18–C20, C35, C40, C42, C43 `DERIVED`). Every value marked **[derived]** comes from the model in §2–§5; **[ref]** values are carried from the thesis.

> **Superseded in part, 2026-09-19 — read this before quoting a bus voltage from this file.** The **400 V** recommendation in §4 was taken before the H block existed. **H8 (2026-09-19) keeps the winding and sets the bus at ≈150–200 V, with H12 fixing 180 V nominal** — below the flight-minimum EMF, so the four-quadrant stage never crosses the buck↔boost boundary. The machine sizing itself stands unchanged, and so do the currents (they are torque-set by `Kt`, not bus-set): **15.9 A rms peak, 6.5 A rms holding.** The **1 400 V row and the 400 V row in §4's table are therefore a historical trade record, not the recommendation** — keep them as the record of how the choice was made, and do not quote either as the design value. The voltage-dependent figures elsewhere in the file (the 800 V filter capacitor and 1 400 V rectifier on the `[ref]` machine, the "~1.5 F at 400 V" storage argument) are correspondingly historical. Two further reconciliations carried from the same pass: the **power readouts in `04-caa-dual-spin-interface.html` reference the duty torque to launch spin (1 623 rad/s)**, giving ≈3.8 kW hold against **C42's published 2.92 kW peak** — the same physics at a different point in the spin decay, to be reconciled at P2 under risk 37; and **C42's 2.92 kW is the figure that governs W7/W12 and P6**, not anything in this file.

**Companion:** feeds C14–C21 (alternator constants) and the new machine criteria C34–C42 in `00-design-criteria-register.md`.

---

## 1. What the machine must do

| Duty | Requirement | Source |
|---|---|---|
| Hold the ring against `Taero` | continuous torque ≈ **2.36 N·m** (Taero_max 2.2 + Tf 0.157) | C11, C13 |
| Slew the ring | peak torque **5.76 N·m**, transient | C19 |
| Satisfy the symmetric authority criterion | `Talt_max ≥ 2(Taero − Tf)` = 4.09 N·m minimum | C9 |
| Spin | relative speed **1108–1912 rad/s** (body spin) | S6 |
| Survive | 15 000 g axial / 5 000 g radial; ring setback 73.5 kN | C26, E1 |
| Fit | ring OD ≈ 98 mm (canard root station); machine OD ≤ **92 mm**; canard tips capped Ø151 mm | P12, C31 |

**Envelope conclusion.** The machine must live in the annulus inside the ring. There is no larger diameter available: aft of the ogive the kit necks into the Ø50.8 mm fuze well, so a machine further aft would lose the moment arm that makes the torque. **92 mm OD is the hard ceiling.**

---

## 2. Model

Torque for a 3-phase sinusoidal surface-PM machine, derived from power balance:

```
T = 3·p·ψ_PM·I_rms / √2        ψ_PM = N_ph·k_w·Φ_pole
N_ph = A_cu,ph·J / I_rms       A_cu,ph = cu_fill·A_slot / 3
→  T = p·k_w·Φ_pole·cu_fill·A_slot·J / √2
```

**The turns count cancels.** At a fixed slot area, torque depends only on pole count, flux per pole, slot area and current density — so the voltage/current split (Kv) is a free choice that does not change copper loss. That result matters for §6.

Radial build, outside in:

```
rotor backiron t_rb = Φ_pole / (2·B_y·L)
magnet         t_m  = 1.5 mm
air gap        g    = 0.40 mm
stator yoke    t_y  = Φ_pole / (2·B_y·L)
slot depth     t_s  = fills the remaining annulus
tooth width         = Φ_pole / (B_tooth·L)
```

**Assumptions:** `B_g` = 0.80 T (fundamental gap flux density); `B_y` = 1.50 T; `B_tooth` = 1.80 T; `k_w` = 0.933 (concentrated, double-layer); slot fraction 0.50 of the stator annulus; copper fill 0.42 of slot area; NdFeB at 7 500 kg/m³; laminations at 7 600 kg/m³.

---

## 3. Radial build and torque versus pole count

`L` = 30 mm, `J` = 8 A/mm²:

| `p` | Poles | Slots | τ_p mm | Φ_pole mWb | yoke mm | stator OD mm | gap mm | T @ J8 N·m |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 10 | 12 | 23.8 | 0.572 | 6.36 | 75.9 | 75.9 | 2.75 |
| **7** | **14** | **12** | **17.8** | **0.426** | **4.74** | **79.1** | **79.1** | **2.38** |
| 9 | 18 | 9 | 14.2 | 0.340 | 3.77 | 81.1 | 81.1 | 2.05 |
| 12 | 24 | 9 | 10.8 | 0.260 | 2.89 | 82.8 | 82.8 | 1.69 |

Higher pole count thins the yoke (more slot room) but raises electrical frequency and iron loss — see §5. **p = 7 is the balance point**: it matches the reference machine's 7 pole pairs, gives a 4.74 mm yoke with a 19.6 mm slot, and keeps the electrical frequency at 2.1 kHz.

---

## 4. Recommended specification

| Parameter | Value | Basis |
|---|---|---|
| Topology | Radial-flux, frameless **outrunner**, 3-phase | rotor = ring; stator = body |
| Winding | Concentrated, double-layer, fractional slot | short end turns, low mutual inductance, fault-tolerant |
| Slot / pole combination | **12 slots / 14 poles** | `k_w` = 0.933; high cogging period |
| Pole pairs `p` | **7** | matches [ref]; yoke/loss balance |
| Air-gap diameter (mid-gap) | **≈79 mm** | set by the 92 mm OD minus the radial build |
| Active stack length `L` | **25–30 mm, nominal 28 mm** | output axis for P2 |
| Air gap `g` | **0.40 mm** | → allowable relative deflection **0.20 mm** |
| Rotor backiron / stator yoke | 4.7 mm each @ 1.5 T | [derived] |
| Slot depth | ≈19.6 mm | fills the annulus |
| Stator bore | Ø30 mm | structure, not flux |
| Fundamental gap flux density | 0.80 T | NdFeB, 1.5 mm radial |
| Tooth flux density | 1.80 T | sets tooth width |
| Magnet | NdFeB, 1.5 mm radial, **high-coercivity grade (SH/UH)** | W9 nose temperature |
| **Peak current density** | **≈7.5 A/mm²** at 5.76 N·m | transient slew |
| **Continuous current density** | **≈3 A/mm²** at 2.36 N·m | holding duty |
| Copper loss, continuous | **≈6 W** | [derived] |
| Copper loss, peak | ≈40 W, transient | [derived] |
| Electrical frequency at 1912 rad/s | **2 130 Hz** | needs 0.1–0.2 mm laminations or SMC |
| **Machine mass** | **≈0.81 kg at L = 25 mm; ≈0.97 kg at L = 30 mm** | [derived] |
| — copper | ≈280–340 g | |
| — stator iron | ≈210–250 g | |
| — rotor backiron | ≈250–300 g | |
| — magnets | ≈72–86 g | |

**The machine is electromagnetically feasible.** Peak current density of 7.5 A/mm² is well inside transient limits, and the continuous holding duty sits at only 3 A/mm². There is no thermal obstacle in the machine itself.

---

## 5. Iron loss — the one number that is not yet trustworthy

Electrical frequency is **2 130 Hz** at p = 7 and 1912 rad/s, and 3.0–4.3 kHz at p = 10–14. Iron loss at these frequencies is not a background term — it scales roughly with `f^1.5`.

The crude estimator in the model returned 50–60 W at p = 5–7, which is the same order as the copper loss and would dominate the machine's thermal budget. **That figure is not calibrated and must not be quoted.** What is established is the *requirement*: **standard 0.35 mm laminations will not do at 2.1 kHz — this needs 0.1–0.2 mm laminations, or a soft-magnetic-composite stator.** That is now a design constraint and a cost item, and it pushes the pole count down rather than up.

---

## 6. The Kv / bus-voltage choice

The reference machine's `Kv` = 0.749 V/(rad/s) produces a back-EMF of **1 432 V at 1912 rad/s** — which is why the reference rig used an 800 V filter capacitor and a 1 400 V rectifier. It is a ~1.4 kV machine.

Because copper loss is independent of the turns count at a fixed slot area (§2), the bus voltage is a **free design choice**.

**Convention used here:** `Kt` is N·m per ampere **rms line current**; `Kv` is volts **rms line-to-line** per rad/s; and therefore `Kt = √3 · Kv`. *(The reference quotes Kt = 0.716 and Kv = 0.749, which satisfy the `Kt ≈ Kv` SI identity instead — a different convention. This should be reconciled before either is quoted alongside our numbers.)*

| Bus | `Kv` V/(rad/s) LL | `Kt` N·m/A rms | I at 5.76 N·m | I at 2.36 N·m | Back-EMF at 1912 rad/s |
|---:|---:|---:|---:|---:|---:|
| 200 V | 0.105 | 0.182 | 31.7 A | 13.0 A | 200 V |
| **400 V** | **0.209** | **0.362** | **15.9 A** | **6.5 A** | **400 V** |
| 800 V | 0.418 | 0.724 | 8.0 A | 3.3 A | 800 V |
| 1 400 V | 0.732 | 1.268 | 4.5 A | 1.9 A | 1 400 V |

**Recommendation: 400 V, `Kv` = 0.209 V/(rad/s) line-to-line.** At 10–15 km altitude the air is thin, and partial discharge at 1.4 kV in a small potted assembly is a real risk for no efficiency gain — copper loss is identical at every row in the table. 15.9 A peak is unremarkable for modern silicon.

---

## 7. The finding that matters most — the machine is a kilowatt-class generator

**The machine does not idle.** To hold the ring at a commanded angle it must continuously supply `T_alt ≈ Taero` against the **full body spin**. The mechanical power it absorbs is therefore:

```
P = Taero × ω_body
```

| t s | `Taero` N·m | ω_body rad/s | P kW |
|---:|---:|---:|---:|
| 0.0 | 1.800 | 1623 | **2.92** |
| 10.0 | 1.300 | 1550 | 2.02 |
| 20.0 | 0.800 | 1470 | 1.18 |
| 41.2 | 0.171 | 1400 | 0.24 |
| 60.0 | 1.100 | 1300 | 1.43 |
| 86.5 | 2.119 | 1050 | 2.22 |

**Peak 2.92 kW. Integrated over the flight: ≈121 kJ.** [derived]

Three consequences:

1. **The reference alternator is rated 1.2 kW continuous. The flight requirement exceeds it by ×2.4.** The reference machine would be overloaded through most of the trajectory at full scale.
2. **The bench rig could not have shown this.** It ran body spin 21.6× slower, so the same `Taero` produced 21.6× less power — ~150 W, comfortably inside the 400 W load bank. **The rig's speed scaling masked a kilowatt-class problem, exactly as the scaled spin masked the apogee control failure.** This is the second instance of the same rig-fidelity trap in this project.
3. **W7 is not a "dissipation path" detail — it is a kilowatt-scale thermal design problem**, in a nose already carrying aerodynamic heating (W9, W10). 121 kJ cannot be stored: at a 400 V bus it would need ~1.5 F, which will not fit the envelope and will not survive 15 000 g.

**And it couples to cant angle.** Raising the cant angle is risk 25's primary mitigation for canard force. But `Taero` scales with cant, so the dumped power scales with it too:

| Cant | `F_steer` N | `Taero` N·m | P at 1623 rad/s |
|---:|---:|---:|---:|
| 8° | 14.5 | 1.44 | 2.34 kW |
| 10° (datum) | 18.1 | 1.80 | 2.92 kW |
| 14° | 25.3 | 2.52 | 4.09 kW |
| 16° | 29.0 | 2.88 | 4.67 kW |

Going from 10° to 16° buys 60% more guidance force and costs **60% more power to dissipate**. The register currently treats cant angle as free — it is not.

---

## 8. Mechanical checks

| Check | Result | Status |
|---|---|---|
| **Air gap vs launch deflection** | gap 0.40 mm → **relative deflection must stay under 0.20 mm** at 15 000 g, or rotor and stator contact. This becomes the governing stiffness specification for the bearing pair and the stator mount. | new requirement |
| **Magnet retention** | a 5 g magnet at 15 000 g sees **≈736 N of shear**. Adhesive alone will not hold it — mechanical retention (sleeve or pockets) required. | new requirement |
| **Cogging** | 12/14 with a high cogging period; still needs a bounded cogging-torque spec, because it appears as a position-locked disturbance against G5/G6 and competes with the apogee torque of 0.17 N·m | new requirement |
| **Ring setback** | 73.5 kN at 0.5 kg ring mass; scales linearly — 0.3 kg → 44 kN | C26 |
| **Machine mass vs kit budget** | ≈0.89 kg vs the **M1156 benchmark's 1.4 kg for the entire kit**. Net penalty over the replaced ~0.98 kg fuze moves from **+0.42 kg to roughly +0.7–0.9 kg**, and the CG shift from 2.6 mm to roughly 6–8 mm forward. | see note |

**Note on the mass consequence.** The kit would still land in the 1.4–1.7 kg class, so this is an overweight of roughly 10–20%, not a budget failure. The CG shift of 6–8 mm is ~0.8% of the projectile length, inside the platform's own 0.55–0.62 L envelope spread. The direction of the stability effect should be checked at S1 rather than assumed: mass forward reduces the CP–CG separation, which reduces `C_Mα` and *raises* `Sg` — the opposite of the usual intuition, and one more reason the heavy ring may be stability-positive.

---

## 9. Open items this sizing creates

1. Iron loss at 2.1 kHz — needs a proper loss calculation with the actual lamination grade, before the thermal budget in §4 can be trusted.
2. Where 121 kJ goes. A controlled resistive dump is the only option that fits; its mass, its surface area and its location are unresolved, and it competes with the nose-packing risk (risk 27).
3. Whether 400 V is right given potting, altitude and rectifier choice.
4. Bearing stiffness to hold 0.20 mm relative deflection at 73.5 kN — this may be the hardest mechanical requirement in the kit.
5. Make-versus-buy: check whether a standard frameless kit in the right diameter exists before committing to a bespoke lamination stack.
6. Radial-flux versus axial-flux for this annulus — not yet traded.
