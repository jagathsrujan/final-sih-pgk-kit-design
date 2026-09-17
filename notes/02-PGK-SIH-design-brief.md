# Design Brief — SIH Problem **SIH26098**

**Problem title (organiser's wording):** *Design and Development of a Precision Guidance Kit with Canard Actuation and Multi-Mode Electronic Fuze for a 155 mm Artillery Shell*

**Organisation / problem statement source:** Yantra India Limited (YIL) — SIH 2026, problem ID **SIH26098**, title *"Development of a Low-Cost Precision Guidance and Smart Artillery Shell"*.

**Why this note exists:** `00-PGK-thesis-working-notes.md` distils the METU thesis (Günay, 2022) — our closest validated engineering reference. This note is the **phase-2 bridge**: it takes that thesis and reasons it against the actual competition problem statement, so the design phase starts from a traced requirement register rather than a blank page.

**Status of this note:** problem-statement decomposition, coverage mapping, sizing anchors and design-decision register. Quantitative checks I computed myself are marked **[derived]**. Items to verify before quoting externally are marked **[verify]**.

---

## 1. What the problem statement is actually asking for

Read carefully, SIH26098 is not open-ended research. It is a request to build an **indigenous, low-cost equivalent of the US M1156 Precision Guidance Kit**. Compare the two specification sheets:

| | SIH26098 (YIL) | M1156 PGK (US baseline) |
|---|---|---|
| Platform | Standard 155 mm artillery shell | M795 / M549A1 155 mm HE |
| Guidance | Canard actuation assembly + GNC | GPS guidance with canards |
| Fuze | Multi-mode electronic fuze: proximity / time / impact | Combined fuze + guidance module, multi-option fuze |
| Accuracy target | **CEP ≤ 30 m** | Threshold **50 m CEP**, objective **30 m CEP** |
| Constraint | Compatible with existing shell casing, low SWaP-C | Replaces the fuze, fits existing stockpile, no new round |
| Programming | Pre-fire fuze configuration interface | Fuze setter on the gun line |

That mapping is the single most important framing fact in this project: **the target number, the fizusing architecture, and the retrofit philosophy are all borrowed from a fielded, documented system.** The competition's "low-cost" adjective is the differentiator — the US Army's Sept-2026 award to Northrop Grumman is an **$863 M** IDIQ production contract for this product class, so the demand and the performance bar are both real and the only competitive lane open to us is cost, indigenous manufacturability, and SWaP-C.

### Requirements register

Traceable IDs — use these in the final architecture document so every claim maps to a requirement.

| ID | Requirement (from PS) | Type | Notes |
|---|---|---|---|
| **R1** | Canard actuation assembly (CAA) for in-flight trajectory correction | Functional | Must both *deploy* (one-shot, post-muzzle) and *actuate* (continuous) — two different mechanisms, see §5.4 |
| **R2** | GNC system improving terminal accuracy | Functional | Implies nav solution + guidance law + control loop |
| **R3** | Multi-mode electronic fuze: proximity, time, impact | Functional | Complete gap in our reference material |
| **R4** | Embedded electronics + software for real-time flight control | Functional | Flight-worthy, not bench hardware |
| **R5** | Power management for high-g launch and flight | Functional | Alternator covers flight; pre-launch needs a reserve source |
| **R6** | Communication/programming interface for pre-fire fuze configuration | Functional | Should carry more than a mode word — see §5.5 |
| **R7** | **CEP ≤ 30 m** | Performance | The headline number; needs a full error budget, §7 |
| **R8** | Compatibility with existing 155 mm shell design | Constraint | Fuze-well threads, ogive contour, mass/CG/Ixx budget |
| **R9** | Survive launch acceleration, vibration, spin, environment | Constraint | 15 000 g axial / 5 000 g radial + thermal + storage |
| **R10** | Low Size, Weight, Power and Cost (SWaP-C) | Constraint | The competitive lever |
| **R11** | High reliability and safety | Constraint | Safe-and-arm, no in-bore function, no dud |
| **R12** | Modular design for future upgrades | Constraint | Drives the interface definitions |

### Deliverables the PS asks us to submit

| PS deliverable | Where it comes from |
|---|---|
| System architecture document | This note + §3–§6 become its skeleton |
| CAD model of the canard actuation assembly | New work; thesis has only a concept section view |
| Electronics block diagram | New work; thesis used lab hardware |
| Guidance and control algorithm | Control loop inherits from thesis; **guidance law is new** |
| Simulation demonstrating trajectory correction | Thesis 7-DOF model is the starting point |
| Prototype / proof-of-concept (preferred) | Thesis rig methodology de-risks this |
| Performance estimation showing CEP ≤ 30 m | Error budget, §7 |

---

## 2. Coverage matrix — problem statement vs. what we already hold

`00-PGK-thesis-working-notes.md` is a validated **actuation-and-control layer for exactly this airframe** (155 mm, 43 kg, spin-stabilised). It is valuable precisely because it de-risks the hardest mechanical/control question — and it stops exactly where our design work has to begin.

| Req | Coverage | What the thesis gives us | What is missing |
|---|---|---|---|
| R1 | **Partial — high value** | De-spun ring carrying 4 fixed-incidence canards on two isolation bearings; **no moving control surfaces**; the alternator *is* the actuator. Steering pair (0°/180°, equal cant) → codirectional force, 2×F, no net torque. Control pair (90°/−90°, opposite cant) → zero net force, net roll torque. Ring roll angle `θgk` aims the force vector = 2-D steering on a single axis. | Stow/deploy mechanism; CAD; bearing survival at 15 000 g; ring-angle sensing in flight |
| R2 | **Partial** | 7-DOF de-spun flight model in the Body-Fixed-Plane frame; full flight envelope; bench-validated cascade controller (PI velocity `0.29 + 7.82/s`, P position `29.7` → 33.6 Hz / 6.2 Hz at 1 kHz) | **No guidance law at all; no navigation filter; no GNSS/IMU selection; no in-flight `θgk` sensing** — the author flags this himself as his largest open question |
| R3 | **Complete gap** | — | Fuze type, S&A, proximity sensing, timing, impact switch, and a physical layout conflict (§5.3) |
| R4 | **Gap** | 1 kHz control loop demonstrated on a cRIO-9063 + FPGA on a bench | Flight-worthy embedded target, thermal/vibration qualification, EMC |
| R5 | **Partial — a strength** | Alternator is simultaneously actuator and generator → free in-flight power, no flight battery. Stated advantage over canard-actuator designs. | Power and thermal budgets; pre-launch/reserve power; **where control energy is dissipated in flight** (on the rig a load bank absorbed it) |
| R6 | **Gap** | — | Interface definition, data package, gun-line setter compatibility |
| R7 | **Gap** | Control-side error contributions only | Nav / guidance / meteo / detonation error budget |
| R8 | **Partial** | 155 mm mass and inertia properties; guidance-kit aero term formulation | Threads, contour, mass/CG/Ixx budget, gyroscopic stability check |
| R9 | **Stated but not solved** | Load levels named: **15 000 g axial, 5 000 g radial** | Only the bench rig survives those by not experiencing them; no bearing/electronics launch survival analysis |
| R10 | **Partial** | Architecture inherently removes actuators *and* the in-flight battery — a genuinely strong cost story | Bearing cost, magnet/coil cost, manufacturing plan |
| R11 | **Gap** | — | S&A design, in-bore safety, dud rate |
| R12 | **Partial** | Clean separation already exists between ring, alternator and body | Formal interface control |

**Honest summary: the thesis covers roughly 40 % of this problem — the portion someone else already de-risked. The remaining 60 % (fuze integration, navigation under spin, the guidance law, stow/deploy, launch survival, CEP budget) is where our design has to innovate.**

---

## 3. The five problems that decide this design

Ordered by risk, not by PS bullet order.

### 3.1 Sensing and navigating on a body spinning at 15 000–20 000 rpm

This is the crux, and the thesis does not solve it. Flight spin is **1623 rad/s at launch decaying to ~1050 rad/s** (10 000–20 000 rpm across charges 3M–6M). No flight-representative off-the-shelf MEMS gyroscope measures that rate; the author used a laboratory encoder on his rig and explicitly lists in-flight `θgk` feedback as his largest unaddressed problem.

The architectural answer is to **use the de-spun ring as the sensing platform**:

- The ring is already roll-decoupled from the body by the isolation bearings and turns at only **±30 rad/s** (velocity limit 31.42 rad/s), not 1600 rad/s. It still sees the projectile's pitch/yaw coning motion, so a ring-mounted IMU sees a *conventional* low-rate attitude signal with the spin removed — precisely what a navigation filter wants.
- The ring's own rotation must be measured **relative to the body** (hall / inductive / optical) and **absolutely** (magnetometer, or a hybrid), because the guidance force direction is set by the ring's earth-referenced angle, not its body-relative angle.
- GNSS is a separate problem: a body-fixed antenna rotating at ~260 Hz chops the carrier and modulates the pattern. **A spin-tolerant antenna arrangement is a first-class design item, not an afterthought.**

Prior art named in the thesis for this exact problem: Zhang et al. used a gyro; Yin et al. used geomagnetic + Hall. Both are worth chasing.

### 3.2 Guidance authority is a *window*, not a constant

Canard force scales with dynamic pressure (ρV²/2). From the thesis flight simulation (Fig. 5.8, reproduced in `figures/p103-...`):

| Flight phase | Available control force |
|---|---|
| Launch transient (t ≈ 0–5 s) | up to **±85 N** |
| Mid-flight band (t ≈ 10–80 s) | **±15–25 N** |
| Apogee (t ≈ 45 s) | **≈ 0** |
| Descent (t ≈ 85–90 s) | **±20 N** |

So the guidance law **cannot steer at apogee** by construction, and the correction authority is concentrated early (highest q, but a correction there perturbs the whole trajectory and range) and late (descent, where it only has to trim the impact). This asymmetry is the entire substance of the guidance-law design and it is exactly the piece the thesis left as future work — our clearest novelty space.

### 3.3 Ring torque margin near apogee is thin

Control of the ring is a torque-balance problem: `Taero` (unavoidable, aerodynamic) versus `Talt` (controllable, alternator) + `Tf` (friction).

- `Taero` collapses to **0.1706 N·m at t = 41.16 s** against a measured friction of **0.1 N·m** → only a **1.7× margin**.
- Sizing criteria from the thesis, to be reused as *equations*: symmetric authority requires `Taero ≤ (Talt_max + Tf)/2 = 2.93 N·m`; minimum controllability requires `Taero > Tf`.
- Consequence: **bearing specification, preload and contamination control matter more than control tuning.** The design must also adopt the thesis's proven fix — disturbance observer plus *state-dependent* dynamic current and velocity limits (`I_lim = 2 × Î_disturbance`, `VL = 26 rad/s per A`), because the alternator's available current itself falls with relative speed (≈10 A at launch → ≈5 A near apogee).

### 3.4 Stability, mass and CG budget

Canards mounted **forward of the CG are destabilising** — they generate a normal force at a station ahead of the centre of mass, which reduces the static margin of a shell that is already only marginally gyroscopically stable. The kit's mass, CG shift and axial inertia change must be shown to keep the gyroscopic stability factor safe across the charge and temperature envelope.

Also, the launch load case on the ring is severe and must be designed, not assumed: an ~0.5 kg ring assembly at 15 000 g sees **≈74 kN** of setback load **[derived]** that the bearing and axial retention must carry without brinelling or seizing.

### 3.5 Power and thermal

The alternator's free in-flight power is a major advantage for a 90 s flight — keep it. But three things are unaddressed: a **safe pre-launch state** needs a reserve/thermal battery (also the safety enabler: no power until launch); the **control energy has nowhere to go** in flight once the load bank is gone (dump resistor, or charge the battery); and the electronics sit inside a nose that also has to survive gun-launch thermal and setback.

---

## 4. Design anchors — the number set to size against

All values from the thesis (155 mm case). This is the data sheet the CAD, electronics and simulation all close against.

| Quantity | Value |
|---|---|
| Body diameter / mass | 155 mm / 43 kg |
| Inertia | Ixx 0.144, Iyy = Izz 1.216 kg·m² |
| **Launch loads** | **15 000 g axial, 5 000 g radial** |
| Spin at launch | 1600 rad/s (≈15 300 rpm); 10 000–20 000 rpm across charges 3M–6M |
| Spin at t = 86 s | ≈1050 rad/s |
| Muzzle velocity | 546 m/s (3M) → 943 m/s (6M); simulation at 800 m/s |
| Firing elevation (sim) | 63° (0.925 rad case studied in detail) |
| Time of flight / apogee | ≈90–95 s / t ≈ 41 s |
| `Taero` (aero torque on kit) | 0 → 2.2 N·m; **min 0.1706 N·m at t = 41.16 s**; 2.119 N·m at t = 86.5 s |
| `Tf` (bearing friction) | **0.1 N·m** at 800 rpm relative |
| `Talt_max` | 5.76 N·m (Kt 0.72 × 8 A) |
| Authority criteria | `Taero ≤ (Talt_max + Tf)/2 = 2.93 N·m`; `Taero > Tf` |
| Control force (BFP) | ±85 N launch transient → ±15–25 N → ≈0 at apogee |
| Alternator | Kt 0.716 N·m/A, Kv 0.749 V/(rad/s), 7 pole pairs, R 6.2 Ω / L 8.8 mH ph-ph, 1.2 kW continuous |
| Ring inertia `Jgk` | 1.197e-3 kg·m² [derived] |
| Ring velocity limit | ±31.42 rad/s (300 rpm) |
| Control bandwidth | velocity 33.6 Hz, position 6.2 Hz, loop rate 1 kHz |

---

## 5. Architecture decisions to take

Each is a real fork. My leaning is stated, not fixed.

**D1 — Canard control concept.** (a) De-spun ring + fixed canards + alternator-as-actuator *(thesis)*; (b) de-spun front section + servo-actuated canards; (c) reciprocating canard pair.
→ **Lean (a).** No control actuators, no gearboxes, no in-flight battery, one moving part. It is the strongest answer to R10 and the only one already validated on hardware. Note the PS wording "canard actuation assembly" is satisfied by (a): "actuation" here means ring-angle control.

**D2 — Ring angle sensing.** Relative (hall/inductive/optical) + absolute (magnetometer) hybrid.
→ **Lean hybrid magnetic**, because it survives the environment and has no exposed optics.

**D3 — Navigation architecture.** Body-fixed IMU (saturates under spin) vs. **ring-mounted IMU** (spin removed) vs. hybrid with a dedicated spin-rate channel.
→ **Lean ring-mounted IMU + body spin-rate measurement + spin-tolerant GNSS antenna.** This is a genuine architectural advantage of the de-spun ring and worth stating explicitly in the submission.

**D4 — Fuze location and sensing.** Everything in the kit's nose, forward of the canard ring; proximity technology to be selected (RF Doppler / IR / laser) with crystal-controlled timer and impact switch.
→ **Lean RF Doppler proximity**, standard for artillery, robust to weather and obscurants.

**D5 — Power architecture.** Alternator for in-flight; reserve/thermal battery for pre-launch, S&A and boot; explicit energy sink for control power.

**D6 — Canard stow/deploy.** Canards stowed flush for ramming and in-bore travel, released and locked after muzzle exit (centrifugal and/or spring, with a positive lock).
→ Must be provably safe **in-bore** (R11).

**D7 — Fire-control interface.** Inductive setter occupies the standard gun-line role. The data package should carry **fuze mode, time of flight, target coordinates and met/muzzle-velocity data** — not just a mode word — since an impact-point-prediction guidance law needs the target location to compute its own solution in flight.
→ The existing gun-line fuze setter is the compatibility hook for R8; piggybacking on it is a strong argument in the submission.

---

## 6. Reuse as-is, take with caution, do not inherit

**Adopt unchanged (validated on hardware):**
- De-spun fixed-canard ring + alternator-as-actuator, with the steering/control canard split.
- Cascade control: PI inner (velocity) + P outer (position), inner ≥5× faster, clamping anti-windup, shortest-way rotation logic.
- Disturbance observer + dynamic saturation limits — the thesis's real result; the *combined* (current + velocity) variant is the one to implement.
- Control-authority criteria used as **sizing equations**, not just analysis.
- The **rotating dynamometer test-rig methodology** (torque motor emulates `Taero`, speed motor emulates body spin, programmable load absorbs control power) as our validation approach.

**Take with caution:**
- **Aero data.** The thesis used a 5-point Mach table (0.9/0.95/1.1/1.5/2.0) with no α/β dependence — it produced non-physical jumps in `Taero`. We need a proper Mach × α × β coefficient set. The guidance-kit coefficients (`C_Nδ`, `C_rc`, `C_rdgk`) and body coefficients **are not printed in the thesis**; they come from refs [1] and [23].
- **Rig fidelity.** The rig scaled body spin down, which *created* an overshoot failure mode that would not appear on a real projectile, and *hid* authority losses that did appear on hardware. Our rig must be designed knowing this.
- **Friction budget.** With only 1.7× margin at apogee, bearing selection is a first-order design decision.

**Do not inherit:**
- The sparse Mach aero table and the α/β-free assumption (fatal for a guidance law).
- Fixed saturation limits — make every limit state-dependent by construction.
- The slip-ring rating mismatch (5 A rated, 8 A drawn in the flight-replay test) — a real integration constraint if we copy the architecture.
- The absence of HIL: the thesis never closed the loop between ring position and flight parameters. Our simulation must.

---

## 7. Quantitative sanity checks [derived]

**Control authority versus the 30 m CEP requirement.**

- Guidance force ≈20 N on 43 kg → lateral acceleration ≈ **0.465 m/s²**.
- Applied continuously for 40 s: Δv ≈ **18.6 m/s**; impact displacement from a burn ending at the moment of impact ≈ **372 m** (using Δx = a·τ·T − ½a·τ²).
- Terminal accuracy requirement: with 10 s remaining, a residual lateral velocity error of **3 m/s** already costs 30 m of impact error, and with 30 s remaining, ~1 m/s does.

> **Conclusion: the authority budget closes comfortably.** Roughly 370 m of correction capability against the ~500 m class of dispersion we are trimming, and the terminal velocity must be nulled to the order of 1–3 m/s — which is an ordinary control problem. **30 m CEP will be limited by navigation quality and impact-point-prediction accuracy, not by canard control authority.** This is encouraging and it tells us where to spend effort.

**Ring launch load.** 0.5 kg ring assembly × 15 000 g ≈ **74 kN** axial setback through the isolation bearings and their retention **[derived]** — the governing load case for the CAA bearing design, and a number the CAD must be checked against.

**Circular error relationship.** CEP = 1.1774σ (2-D circular). For **CEP ≤ 30 m**, the 1σ radial budget is **σ ≤ 25.5 m**.

---

## 8. CEP error budget skeleton (deliverable for R7)

1σ radial allocations, combined in RSS to obtain σ, then CEP = 1.1774σ. Values are **target allocations to be substantiated by simulation**, not measured results.

| Source | 1σ allocation (m) | Basis |
|---|---|---|
| Navigation (GNSS/INS) at impact | 5 | GNSS ~1–3 m + INS/filter residual |
| Guidance & control (IPP error, ring angle, actuator) | 15 | Dominant term; must be simulated |
| Meteo / muzzle-velocity prediction residual | 10 | Reducible by muzzle-velocity radar |
| Remaining ballistic / aero uncertainty | 8 | Model and coefficient error |
| Fuze & detonation dispersion | 3 | Small at 155 mm HE |
| **RSS** | **20.4** | **[derived]** |
| **Implied CEP** | **≈24 m** | **≤ 30 m with ≈20 % margin** |

The budget shows the design closes *only if* the guidance/control term is held near 15 m — which is precisely why the impact-point-prediction guidance law, not the airframe, is the make-or-break item.

---

## 9. Validation methodology

Three layers, in order of cost:

1. **6-DOF/7-DOF trajectory simulation.** Extend the thesis model: add proper Mach × α × β aero, earth curvature, and — critically — a **guidance loop in the loop**. Monte-Carlo across muzzle velocity, meteo, target location and launch perturbation to produce the CEP number directly. *This is the primary deliverable artefact and needs no hardware.*
2. **Hardware-in-the-loop.** Feed ring angle back into flight parameters so the actuator is exercised against a live trajectory (the thesis's missing piece).
3. **Bench rig demonstration (recommended for "prototype preferred").** A reduced version of the thesis rig — ring, bearings, alternator, motor-driven relative spin, programmable load, magnetometer for absolute angle — demonstrating commanded ring-angle tracking and the DOB/dynamic-limit behaviour. **This is the highest-value, lowest-cost physical demo and directly answers the PS's "prototype or proof-of-concept (preferred)".**

---

## 10. Open questions to close in the design phase

1. **Which shell exactly?** YIL's specific 155 mm HE round (mass, CG, fuze well thread, ogive contour). Everything scales from this and R8 depends on it.
2. **Aero dataset.** Where do `C_Mα, C_lp, C_mq, C_Nδ, C_rc, C_rdgk` come from — CFD, published data, or refs [1]/[23]? This gates the whole simulation.
3. **Ring radius and canard sizing** — `R`, planform, cant angles, and the resulting `F_steer` and `Taero` at the envelope extremes.
4. **Alternator sizing** — size for worst-case `Taero` under the symmetric criterion, or accept asymmetric authority with scheduling?
5. **Guidance law** — impact-point prediction versus trajectory shaping, using the ~6 Hz ring-angle command channel.
6. **Gyroscopic stability** with the kit installed across the charge/temperature envelope.
7. **Proximity sensor technology** and its interaction with the canard ring and the alternator's magnetic field — an EMI question specific to this architecture.
8. **Energy sink** for control power in flight.
9. **Cost target** — set an indigenous per-unit target against the imported equivalent **[verify current M1156 unit pricing before quoting]**.

---

## 11. Figure index (thesis figures, held in `figures/`)

All referenced figures are already extracted into `notes/figures/`; the ones that matter most for this brief:

| File | Why it matters here |
|---|---|
| `p37-fig2.3-gk-section-view.jpg` | **Layout conflict**: nose is forward of the canard ring — the fuze must live in that tip (§3.3, D4) |
| `p38-fig2.4-steering-and-control-canards.jpg` | Steering vs. control canard split; `r` and `R` geometry (note: `R ≈ 2r`, the thesis wording appears to contain a typo) |
| `p39-fig2.5-torques-on-canard-structure.jpg` | The `Taero` / `Tf` / `Talt` balance that sets the bearing spec |
| `p103-fig5.7-5.8-velocities-and-control-forces.jpg` | **The guidance-authority window**: ±85 N launch transient → ±15–25 N → ≈0 at apogee (§3.2) |
| `p105-fig5.10-5.11-aero-torque-and-damping-vs-flight.jpg` | `Taero` across 4 elevations; the 0 → 2.2 N·m working range — and the non-physical jumps from the sparse Mach table |
| `p109-fig6.1-6.2-flight-scenario-aero-torque-and-body-spin.jpg` | The apogee torque collapse (0.1706 N·m @ 41.16 s) and spin decay |
| `p124-fig7.4-7.6-alternator-saturation-and-observer.jpg` | **Available alternator current falls with relative speed** — the reason limits must be state-dependent |
| `p70-fig4.1-cascade-control-structure.jpg` | The cascade loop we inherit |
| `p41-fig2.6-2.7-test-setup-schematic-and-photo.jpg` | Rig methodology for our bench demo |
| `p30-fig1.3-1.4-fixed-canard-orientation-and-example.jpg` | Prior art (US Patent 6,981,672) — note it calls the torque pair *rotation canards* |

---

## 12. Sources

- [Precision Guidance Kit (PGK) — DOT&E FY2015](https://www.dote.osd.mil/Portals/97/pub/reports/FY2015/army/2015pgk.pdf) — threshold 50 m CEP / objective 30 m CEP; combined fuze and GPS guidance module
- [M1156 precision guidance kit — Wikipedia](https://en.wikipedia.org/wiki/M1156_precision_guidance_kit)
- [Northrop Grumman Wins $863M US Army Deal for M1156 Precision Guidance Kits](https://thedefensepost.com/2026/09/04/northrop-grumman-army-m1156-pgk/)
- [SIH26098 — Development of a Low-Cost Precision Guidance and Smart Artillery Shell](https://sih-fit.vercel.app/problem/SIH26098)
- `10463953.pdf` — Günay, G., *Controller Design and Implementation for a Guidance Kit Used at Spinning Rockets and Projectiles*, M.Sc. thesis, METU, April 2022 (distilled in `00-PGK-thesis-working-notes.md`)

---

*Companion documents: `00-PGK-thesis-working-notes.md` (thesis distillation, all numbers sourced and page-referenced), `01-thesis-full-text-extracted.txt` (full text layer), `figures/` (18 extracted figures).*
