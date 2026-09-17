# DRISHTI-PGK — Design Criteria Register

**Problem statement:** SIH26098 — *Development of a Low-Cost Precision Guidance and Smart Electronic Fuze System for a 155 mm Artillery Shell*
**Organisation:** Ministry of Defence (MoD) / Yantra India Limited, Ambajhari, Nagpur
**Purpose of this file:** the single working record of every criterion the design must satisfy or decide. It is the evidence base for the submission — every number that appears in the submission should trace back to a row here.

---

## How to use this file

**Every criterion carries one of three types:**

| Type | Meaning | What you do |
|---|---|---|
| **Given** | Imposed by the customer, the platform, or a defence standard | Extract it. Do not invent it. |
| **Derived** | Falls out of physics once the givens are fixed | Compute it. Show the arithmetic and the assumptions. |
| **Chosen** | A design decision of ours | Decide it, and justify it against the givens with a trade. |

**Status values — keep them honest:**

| Status | Meaning |
|---|---|
| `OPEN` | Not yet defined |
| `OPEN-BLOCKED` | Cannot be fixed until external data arrives (e.g. YIL shell drawing). A placeholder value is in use. |
| `PROPOSED` | A value is proposed but not yet confirmed by the team |
| `DEFINED` | Confirmed by the team |
| `DERIVED` | Computed from other defined criteria |
| `VERIFIED` | Confirmed by analysis, simulation or test |

**Governing criteria are marked ⚑.** These are where the margins are thinnest and where the design will be won or lost. Get these right before anything else.

**Values marked *provisional* are derived on top of a placeholder, an unconfirmed anchor, or a [ref] value.** A provisional value names the input it depends on and never counts as closed, however solid the arithmetic looks.

**Values marked **[ref]** are carried from the reference literature for the 155 mm class (`notes/00-PGK-thesis-working-notes.md`) and must be confirmed against YIL's actual shell.**

---

## The dependency chain

Criteria cannot be defined out of order. This is the sequence:

```
M  Mission (target, range, charge)
     └─ baseline unguided dispersion
         └─ required correction capability
             └─ G  guidance & control requirements
                 └─ C  canard sizing → Taero → alternator sizing → friction budget
                     └─ N  navigation & sensing requirements
                         └─ W  power, thermal
                             └─ S/P/E/F  structure, stability, environment, fuze
                                 └─ K/R  cost, verification
```

S  (Stability) and P (Platform) run in parallel with the chain — they constrain it, and they are gated on the YIL shell data.

---

## Progress at a glance

| Domain | Criteria | Defined | Blocked | Notes |
|---|---|---|---|---|
| M — Mission & effectiveness | 9 | 3 | 3 | M1, M2, M5 DEFINED; M3, M4, M6 OPEN-BLOCKED — **M6 now on a cited external anchor (M549A1 CEP 267 m → circular 1σ 227 m), not a bare assumption**; M7 DERIVED provisionally at the chosen 80% capture fraction (407 m, 19.5 m/s) |
| P — Platform compatibility | 14 | 0 | 8 | Gated on YIL shell data |
| S — Stability | 7 | 0 | 0 | Gated on YIL shell data |
| G — Guidance & control | 15 | 0 | 0 | |
| C — Canard actuation assembly | 33 | 0 | 0 | |
| F — Fuze | 15 | 0 | 1 | F11 blocked on the in-service setter interface |
| N — Navigation & sensing | 15 | 0 | 0 | |
| W — Power & thermal | 11 | 0 | 0 | |
| E — Environment & qualification | 11 | 0 | 0 | |
| K — SWaP-C & cost | 6 | 0 | 0 | |
| R — Reliability, safety, verification | 10 | 0 | 0 | |
| **Total** | **146** | **3** | **12** | |

*Update this table as criteria are closed.*

---

## Submission-critical track

These are the criteria whose answers actually change what we can claim in the SIH26098 idea submission — the ones that make the Technical Approach and Feasibility slides specific rather than generic. Everything else matters to the design but only in the later design phase, and is deliberately excluded here.

**This shortlist is the priority order for the remaining interview.** Within each domain, work these criteria before the rest of the domain; the domains themselves still run unblocked-first (G → C → F → N → W → R).

| # | ID | Criterion | Why it matters for the submission |
|---:|---|---|---|
| 1 | M3 | Range band and charge compatibility | "Works across charges 3M–6M without touching the ammunition" is the strongest feasibility sentence available; without it the whole retrofit premise collapses. |
| 2 | M4 | Range at which CEP ≤ 30 m is claimed | A 30 m CEP with no range attached is the first thing a reviewer discounts; naming the max-range / 6M condition makes the headline number testable. |
| 3 | M5 | CEP definition and treatment of target-location error | States the claim in a form we control and publishes the dependency instead of hiding it — pre-empts the standing "your CEP excludes what?" challenge. |
| 4 | M6 | Baseline dispersion anchor (CEP 267 m → σ 227 m) | Quantifies the problem we exist to solve and turns "artillery is inaccurate" into a cited number that every performance slide can lean on. |
| 5 | M7 | Required correction authority (407 m and 19.5 m/s at 80% capture) | The feasibility crux: it shows the required authority is achievable by the chosen architecture, states the margin, and is the head of the entire CAA sizing chain. |
| 6 | M8 | Effectiveness metric (rounds per target / Pk) | Translates CEP into the operator-level payoff — rounds and time per mission — which is what the impact story is actually scored on. |
| 7 | G1 | Guidance law type | The PS asks for a "guidance and control algorithm" and the reference work deliberately has none, so this is our clearest novel contribution. |
| 8 | G3 | Guidance window | Shows authority is a window, not a constant — the most technically credible slide in the deck, and the honest basis for the apogee risk. |
| 9 | G4 | Miss-distance allocation to the guidance loop | The error budget is what makes "CEP ≤ 30 m" an engineering claim rather than an aspiration, and this is its largest term. |
| 10 | G6 | Absolute (earth-referenced) ring-angle accuracy | Direct, unattenuated error into the direction the guidance force points; naming the requirement shows the novel sensing problem has been recognised. |
| 11 | G15 | Limit-scheduling law | The reference work lost control between 30 s and 50 s with fixed limits; inheriting the state-dependent fix is a concrete, hardware-validated differentiator. |
| 12 | C1 | Canard count and arrangement | The architecture figure — steering pair plus control pair, no moving control surfaces — makes "canard actuation assembly" concrete in one slide. |
| 13 | C8 | Net guidance force required | Closes M7 against the hardware: the force the canards must actually generate, steady and transient. |
| 14 | C9 | Torque authority — symmetric criterion | The sizing equation tying canard size to alternator capability, and the equation a technical reviewer will test us on. |
| 15 | C12 | Taero minimum near apogee | The thinnest margin in the design and the reason friction and bearing selection are first-order; stating it pre-empts the deepest technical objection. |
| 16 | C13 | Friction budget | Sets what the bearings must achieve — the controllability criterion collapses entirely if this is not held. |
| 17 | C26 | Ring setback load | The launch-survival number the CAD is checked against: evidence that 15 000 g has been turned into a structural case rather than merely quoted. |
| 18 | C31 | In-bore stowage and safety | The safety question every judge asks of a canard kit — nothing protrudes, nothing fouls the bore or rammer — and it must be answered before a flyable concept can be claimed. |
| 19 | F1 | Fuze modes and setting ranges | The PS names proximity, time and impact; the mode set and its setting ranges are the scope statement for the fuze half of the project. |
| 20 | F2 | Proximity sensor technology | Proves the multi-mode fuze is a design and not a wish — a stated technology with a stated operating principle. |
| 21 | F6 | Safe-and-arm type | Safety is where a defence reviewer looks first; an out-of-line rotor against MIL-STD-1316 is a claim that can be made on a slide. |
| 22 | F12 | Setter data package contents | Carries target coordinates and met data, which is what lets the guidance law compute its own solution in flight — the difference between pre-fire programming and a mode word. |
| 23 | F15 | EMI coexistence | An architecture-specific risk created by putting proximity sensor, alternator and magnetometer in one nose volume; showing we found it before a reviewer did is worth more than a clean answer. |
| 24 | N1 | Navigation accuracy at impact | The error budget's second-largest term, and the one that decides whether the 30 m claim is credible. |
| 25 | N3 | GNSS antenna strategy under spin | The hardest sensing problem in the design — a body-fixed antenna at ~260 Hz — and addressing it openly is a credibility marker. |
| 26 | N6 | IMU on the de-spun ring | Converts the trickiest constraint into an architectural advantage by removing spin from the measurement; a genuine novelty claim. |
| 27 | W4 | Generation capability versus demand | "No in-flight battery — the alternator is both actuator and generator" is our strongest SWaP-C sentence, and it needs a budget behind it. |
| 28 | W7 | Control energy dissipation path | Unaddressed in the reference work and a coin-flip question at technical review; having an answer distinguishes us from a straight copy. |
| 29 | K4 | Unit cost target at a stated production volume | "Low-cost" is the only lane open against an $863 M fielded competitor; a cost target attached to a volume turns that adjective into a claim. |
| 30 | R5 | Monte Carlo definition | The mechanism that produces the CEP claim, and the evidence that the claim will be defensible rather than asserted. |
| 31 | R7 | Bench rig capability specification | Directly answers "prototype or proof-of-concept (preferred)" with a rig whose methodology is already validated and which we can actually build. |
| 32 | S1 | Gyroscopic stability factor with the kit installed | **Blocked on YIL.** The criterion that can veto the whole architecture — canards ahead of the CG reduce stability — so it must be named as a tracked risk with a plan even while the number is unavailable. |
| 33 | P9 | Kit mass limit | **Blocked on YIL.** Every drop-in retrofit claim depends on the mass / CG / inertia budget staying inside the shell's stability margin; the limit itself is a submission fact even though its number is not yet available. |

**Excluded from this track** — criteria that only matter in the later design phase: the sub-system selections that follow once the governing numbers are fixed (C2, C3, C5–C7, C10, C14–C25, C27, C28, C30, C32, C33), the qualification detail behind the standards we simply cite (E2–E11), the component-level sensing and power choices (N2, N4, N5, N7–N11, N13–N15, W2, W3, W5, W6, W8–W11), and the drawing-dependent platform rows (P1–P8, P12–P14).

---

## M — Mission & effectiveness

| ID | Criterion | Type | Value | Basis / source | Status |
|---|---|---|---|---|---|
| M1 | Target set (point / area, personnel, materiel, hardened) | Given | Mixed general-purpose: point / light materiel primary, personnel and soft targets secondary (proximity) | PS silent on target set — user requirement, confirmed 2026-09-17 | DEFINED |
| M2 | Target hardness and required terminal effect | Given | Full effect envelope retained: proximity airburst, time airburst, impact with selectable superquick / short delay / graze — all modes configurable before flight; the fuze shall not reduce the terminal-effect envelope of the fuze it replaces | PS (three-mode fuze) + user requirement 2026-09-17. Envelope option B selected on the user's instruction ("decide on one which satisfies it") — the selection is the assistant's recommendation, not the user's instruction | DEFINED |
| M3 | Range band (min / max) and charge(s) (3M–6M; MV 546–943 m/s **[ref]**) | Given | Full functional envelope across charges 3M–6M — safe, stable and functional at every charge; CEP ≤ 30 m claimed only over a bounded range band (set at M4); outside that band accuracy degrades but never below unguided. Charge-/velocity- and range-band numbers remain **[ref]** placeholders until YIL firing tables arrive | PS + user requirement 2026-09-17 (option C); charge table from the thesis **[ref]** — to be replaced by YIL firing tables | OPEN-BLOCKED |
| M4 | Reference range at which "CEP ≤ 30 m" is claimed | Chosen | Maximum-range, full-charge (6M) engagement. Numeric range to be quoted from YIL firing tables. Mid-band accuracy reported as supporting data from the same Monte Carlo campaign, not as a formal second claim | PS states 30 m without a range; user choice 2026-09-17 (option A) | OPEN-BLOCKED — numeric range pending YIL firing tables |
| M5 | CEP definition: 50% probability radius; is target-location error inside or outside the budget? | Chosen | CEP = 2-D circular 50% probability radius (CEP = 1.1774σ for a circular normal distribution). **Formal claim: weapon CEP against the loaded aimpoint, target-location error excluded and stated as excluded.** End-to-end CEP against the true target published as a sensitivity with the assumed target-location error named | PS states 30 m; user choice 2026-09-17 (option C) | DEFINED |
| M6 | ⚑ Baseline unguided dispersion at M3/M4 | Given | **Cited anchor now in use: CEP = 267 m at maximum range for a conventional unguided M549A1 155 mm projectile → equivalent circular 1σ = CEP / 1.1774 = 227 m.** The 267 m applies at the M549A1's maximum range (30.1 km from the M198 howitzer) — the same order as the M4 condition, but it is **not** YIL's round and **not** YIL's range. **The range/deflection split is not yet known:** the source publishes only the circular CEP, so the ratio of range-direction to deflection dispersion must still come from YIL. The CEP form does remove the 1σ-versus-peak-to-peak ambiguity | Public record for the M549A1: **CEP 267 m at maximum range** (Army sources reported 2013; M549A1 max range 30.1 km from M198). σ = 267 / 1.1774 = 226.8 m. YIL firing tables (request 3) confirm or replace — **sizes everything downstream** | OPEN-BLOCKED — value in use is a cited anchor, not an assumption |
| M7 | ⚑ Required correction capability (impact correction in m; equivalent Δv and burn time) | Derived | **Provisional — rests on the M6 anchor and on [ref] platform values.** Restated as a **capture-fraction** problem, not a percentile lookup. For a Rayleigh radial distribution with σ = 227 m, the authority needed to capture a fraction P of rounds is A = σ·√(−2·ln(1−P)): P = 50% → 267 m (the CEP-defining population — buys nothing better than unguided); P = 70% → 352 m; **P = 80% → 407 m — chosen**; P = 85% → 442 m; P = 90% → 487 m, beyond the authority available. With a = F/m = 20 N / 43 kg = 0.465 m/s²: **A = 407 m → full-force burn T = √(2A/a) = 41.8 s, equivalent Δv = aT = 19.5 m/s.** Authority available from a 20 N force across the ≈45 s terminal window (apogee t ≈ 41 s → impact t ≈ 86 s) is 471 m / 20.9 m/s → **margin ≈ 1.16:1**. **Split:** a single 2-D force vector serves both axes, so the components combine as A = √(A_range² + A_def²); the split is unknown pending M6. **Range correction costs more authority than deflection and the two are not interchangeable** — a range correction is trajectory-mediated, must be spent while the force is fighting the velocity vector, and changes time of flight; a deflection correction is a near-pure terminal displacement integral that can be spent late | Derivation: A = σ·√(−2·ln(1−P)) with σ = 227 m from M6; a = F/m with F = 20 N **[ref]** and m = 43 kg **[ref]**; T = √(2A/a), Δv = aT; terminal window ≈ 45 s from apogee t ≈ 41 s to impact t ≈ 86 s **[ref]**. From M6 − M5 | DERIVED — provisional (M6 anchor + [ref] values) |
| M8 | Effectiveness metric (rounds per target, Pk) | Derived | | From M5, M6 | OPEN |
| M9 | Gun platform(s) and calibre length (39 / 45 / 52 cal) | Given | | YIL / user | OPEN |

---

## P — Platform compatibility  *(all gated on YIL shell drawing)*

| ID | Criterion | Type | Value | Basis / source | Status |
|---|---|---|---|---|---|
| P1 | Shell model(s) and drawing/datasheet reference | Given | | YIL | OPEN-BLOCKED |
| P2 | Shell mass | Given | 43 kg **[ref]** | YIL datasheet | OPEN-BLOCKED |
| P3 | Shell CG location | Given | | YIL datasheet | OPEN-BLOCKED |
| P4 | Shell axial inertia Ixx | Given | 0.144 kg·m² **[ref]** | YIL datasheet | OPEN-BLOCKED |
| P5 | Shell transverse inertia Iyy = Izz | Given | 1.216 kg·m² **[ref]** | YIL datasheet | OPEN-BLOCKED |
| P6 | Fuze well thread form, depth, sealing, torque spec | Given | | YIL drawing | OPEN-BLOCKED |
| P7 | Available axial envelope forward of fuze well | Given | | YIL drawing | OPEN-BLOCKED |
| P8 | Ogive contour — maximum kit diameter at each station | Given | | YIL drawing | OPEN-BLOCKED |
| P9 | ⚑ Kit mass limit | Given / Chosen | | Set by stability (S1) and YIL acceptance | OPEN |
| P10 | ⚑ Kit CG shift limit | Given / Chosen | | Set by stability (S1) | OPEN |
| P11 | ⚑ ΔIxx limit | Given / Chosen | | Set by stability (S1) | OPEN |
| P12 | Kit overall envelope (length × diameter) | Derived | | From P7, P8 | OPEN |
| P13 | Driving band / rifling interface (unchanged by design) | Given | | YIL | OPEN |
| P14 | Ramming and in-bore envelope constraints | Given | | Drives stowage (C31) | OPEN |

---

## S — Stability

| ID | Criterion | Type | Value | Basis / source | Status |
|---|---|---|---|---|---|
| S1 | ⚑ Gyroscopic stability factor Sg, minimum across the temperature / charge / altitude envelope, **with kit and canards installed** | Derived | ≥ 1.3–1.5 (typical) | 6-DOF analysis; canards ahead of CG are destabilising | OPEN |
| S2 | ⚑ Destabilising moment contributed by the canards | Derived | | From C4, C5, C7 | OPEN |
| S3 | Dynamic stability margin | Derived | | | OPEN |
| S4 | Maximum permissible angle of attack / yaw | Derived | | | OPEN |
| S5 | Trim angle and epicyclic behaviour limits | Derived | | | OPEN |
| S6 | Spin rate at launch / apogee / impact; spin decay model | Given / Derived | 1600 → 1050 rad/s **[ref]** | YIL + 6-DOF | OPEN |
| S7 | Yaw of repose | Derived | | | OPEN |

---

## G — Guidance & control

| ID | Criterion | Type | Value | Basis / source | Status |
|---|---|---|---|---|---|
| G1 | Guidance law type (impact-point prediction / trajectory shaping) | Chosen | | Trade against C8, G3 | OPEN |
| G2 | Guidance law output (ring-angle command) | Chosen | | | OPEN |
| G3 | ⚑ Guidance window — the phase of flight where dynamic pressure gives usable authority | Derived | authority ≈ 0 at apogee **[ref]** | From C11/C12, canard force vs time | OPEN |
| G4 | Miss-distance allocation to the guidance loop (1σ, m) | Chosen / Derived | | From error budget, R5 | OPEN |
| G5 | ⚑ Ring angle accuracy, relative to body | Derived | | Direct error into guidance-force direction | OPEN |
| G6 | ⚑ Ring angle accuracy, absolute (earth-referenced) | Derived | | Direct error into guidance-force direction | OPEN |
| G7 | Ring angular rate limit | Derived | ±31.4 rad/s **[ref]** | Set by alternator back-EMF | OPEN |
| G8 | Control bandwidth — outer position loop | Derived | ≈ 6 Hz **[ref]** | Inner ≥5× outer | OPEN |
| G9 | Control bandwidth — inner velocity loop | Derived | ≈ 34 Hz **[ref]** | Set by electrical dynamics | OPEN |
| G10 | Settling time target | Chosen | | | OPEN |
| G11 | Overshoot limit | Chosen | | | OPEN |
| G12 | Anti-windup method (clamping / back-calculation) | Chosen | Clamping **[ref]** | Saturation is unavoidable | OPEN |
| G13 | Control loop rate | Chosen | 1 kHz **[ref]** | | OPEN |
| G14 | Disturbance observer filter bandwidth | Derived | | Reject noise, still track Taero and Tf | OPEN |
| G15 | ⚑ Limit-scheduling law (state-dependent current and velocity limits) | Chosen / Derived | | Prevents authority loss near apogee | OPEN |

---

## C — Canard actuation assembly

| ID | Criterion | Type | Value | Basis / source | Status |
|---|---|---|---|---|---|
| C1 | Canard count and arrangement (steering pair + control pair) | Chosen | 4 (0°/180°, 90°/−90°) **[ref]** | Architecture | OPEN |
| C2 | Cant angle — steering pair | Chosen | | Sets F_steer | OPEN |
| C3 | Cant angle — control pair | Chosen | | Sets Taero | OPEN |
| C4 | ⚑ Canard planform and reference area | Derived | | From C8 and G3 | OPEN |
| C5 | Canard span, root and tip chord | Derived | | Must stow (C31) | OPEN |
| C6 | Canard section / aerofoil | Chosen | | Mach 0.5–2.5 operation | OPEN |
| C7 | Ring radius / canard moment arm (r, R) | Chosen | | Sets torque per unit force | OPEN |
| C8 | ⚑ Net guidance force required | Derived | ±15–25 N steady, ±85 N transient **[ref]** | From M7, G3 | OPEN |
| C9 | ⚑ Torque authority — symmetric criterion: Taero ≤ (Talt_max + Tf) / 2 | Derived | 2.93 N·m **[ref]** | Sizing equation | OPEN |
| C10 | ⚑ Torque authority — minimum controllability: Taero > Tf | Derived | | Sizing equation | OPEN |
| C11 | Taero maximum over the envelope | Derived | ≈ 2.2 N·m **[ref]** | 6-DOF + aero | OPEN |
| C12 | ⚑ Taero minimum (near apogee) | Derived | ≈ 0.17 N·m **[ref]** | The thinnest margin in the design | OPEN |
| C13 | ⚑ Friction budget Tf (maximum allowable, all speeds and temperatures) | Derived | 0.1 N·m class **[ref]** | From C10, C12 | OPEN |
| C14 | Alternator torque constant Kt | Chosen | 0.716 N·m/A **[ref]** | | OPEN |
| C15 | Alternator voltage constant Kv | Chosen | 0.749 V/(rad/s) **[ref]** | | OPEN |
| C16 | Alternator pole pairs | Chosen | 7 **[ref]** | | OPEN |
| C17 | Alternator phase resistance and inductance | Chosen | 6.2 Ω / 8.8 mH ph-ph **[ref]** | | OPEN |
| C18 | Maximum alternator current (and its variation with relative speed) | Derived | ≈ 10 A → 5 A near apogee **[ref]** | Thermal + electrical limit | OPEN |
| C19 | Maximum alternator torque Talt_max | Derived | 5.76 N·m **[ref]** | C14 × C18 | OPEN |
| C20 | Alternator continuous power rating | Chosen | ≈ 1.2 kW **[ref]** | Must cover W1 | OPEN |
| C21 | Ring inertia Jgk | Derived | 1.197e-3 kg·m² **[ref]** | CAD mass properties | OPEN |
| C22 | Bearing type and selection | Chosen | | From C13, C24, C26 | OPEN |
| C23 | Bearing preload | Chosen | | Sets friction (C13) and stiffness | OPEN |
| C24 | Bearing life (revolutions / operating duration) | Derived | | ≈90 s flight + storage | OPEN |
| C25 | Bearing friction torque versus relative speed | Derived | | Must satisfy C13 | OPEN |
| C26 | ⚑ Ring setback load (governing structural case for the CAD) | Derived | ≈74 kN for a 0.5 kg ring **[derived]** | E1 × ring mass | OPEN |
| C27 | Canard steady aerodynamic load | Derived | | From C8 | OPEN |
| C28 | Canard launch transient load | Derived | ≈85 N **[ref]** | Structural design case | OPEN |
| C29 | Deployment release mechanism and energy source (setback / spin / spring) | Chosen | | Must be in-bore safe | OPEN |
| C30 | Deployment lock design and retention force | Chosen | | Must resist C27 with margin | OPEN |
| C31 | ⚑ In-bore stowage and safety — flush, locked, cannot foul bore or rammer | Chosen | | Safety-critical | OPEN |
| C32 | Ring axial retention / restraint design | Chosen | | Must survive C26 | OPEN |
| C33 | Damping torque Tad on the ring | Derived | ≈1.8 → 2.1 N·m **[ref]** | Ring aerodynamics | OPEN |

---

## F — Fuze

| ID | Criterion | Type | Value | Basis / source | Status |
|---|---|---|---|---|---|
| F1 | Modes and setting ranges (proximity / time / impact) | Given | | PS | OPEN |
| F2 | Proximity sensor technology and operating frequency | Chosen | | Must not interfere with alternator — see F15 | OPEN |
| F3 | Burst height range and accuracy | Chosen | | | OPEN |
| F4 | Time mode accuracy and resolution | Chosen | | Crystal reference | OPEN |
| F5 | Impact delay options (superquick / delay / graze) | Chosen | | | OPEN |
| F6 | Safe-and-arm type (out-of-line rotor) | Chosen | | MIL-STD-1316 | OPEN |
| F7 | Arming interlock thresholds (setback and spin) | Derived | | Must not arm in bore | OPEN |
| F8 | Arming distance after muzzle exit | Chosen | | | OPEN |
| F9 | Explosive train, detonator type, output | Chosen | | YIL / standard components | OPEN |
| F10 | ⚑ Dud rate target | Chosen | | Safety and effectiveness | OPEN |
| F11 | Setter interface (inductive) and protocol | Given / Chosen | | Existing gun-line equipment | OPEN-BLOCKED |
| F12 | Setter data package contents (mode, time of flight, target coordinates, met, muzzle velocity) | Chosen | | Guidance needs target data — see G1 | OPEN |
| F13 | Safety standards compliance set | Given | MIL-STD-1316, STANAG 4369, AOP-39 | Cite rather than invent | OPEN |
| F14 | Storage life / shelf life | Given / Chosen | | | OPEN |
| F15 | ⚑ EMI coexistence: proximity sensor vs alternator switching vs magnetometer | Derived | | All in one nose volume | OPEN |

---

## N — Navigation & sensing

| ID | Criterion | Type | Value | Basis / source | Status |
|---|---|---|---|---|---|
| N1 | ⚑ Navigation accuracy at impact (1σ, m) | Derived | 5 m budget **[derived]** | From G4, error budget | OPEN |
| N2 | GNSS constellations and update rate | Chosen | | | OPEN |
| N3 | ⚑ GNSS antenna strategy under spin (spin-tolerant pattern / array / ring-mounted) | Chosen | | Body spins at 260 Hz **[ref]** | OPEN |
| N4 | GNSS outage tolerance | Chosen | | Graceful degradation | OPEN |
| N5 | Anti-jam requirement | Chosen | | Possible future upgrade | OPEN |
| N6 | IMU mounting location (de-spun ring) | Chosen | | Removes spin from the measurement | OPEN |
| N7 | IMU rate range required | Derived | Low-rate once spin removed | From N6 | OPEN |
| N8 | IMU bias stability / angular random walk | Derived | | From N1 and outage duration | OPEN |
| N9 | Spin rate measurement range | Given | 1600 → 1050 rad/s **[ref]** | Flight envelope | OPEN |
| N10 | Spin rate sensor type | Chosen | | Magnetic / optical pickoff | OPEN |
| N11 | Barometric altitude accuracy | Derived | | Contributes to aero model density | OPEN |
| N12 | Magnetometer accuracy, calibration and disturbance rejection | Derived | | Absolute ring angle (G6) | OPEN |
| N13 | Sensor shock rating | Given | 15 000 g axial / 5 000 g radial **[ref]** | E1, E2 | OPEN |
| N14 | Navigation filter type (EKF / UKF) and state vector | Chosen | | | OPEN |
| N15 | Time synchronisation across sensors | Derived | | | OPEN |

---

## W — Power & thermal

| ID | Criterion | Type | Value | Basis / source | Status |
|---|---|---|---|---|---|
| W1 | Energy budget by phase (safe state, boost, midcourse, terminal) | Derived | | Drives W5, W6 | OPEN |
| W2 | Peak electrical power | Derived | | | OPEN |
| W3 | Average electrical power | Derived | | | OPEN |
| W4 | Generation capability versus demand | Derived | | From C20 vs W1 | OPEN |
| W5 | Reserve battery chemistry, activation method, capacity | Chosen | | No power before launch = safety enabler | OPEN |
| W6 | Reserve battery shelf life | Given | | | OPEN |
| W7 | ⚑ Energy dissipation path for control power (no load bank in flight) | Chosen | | Unaddressed in reference work | OPEN |
| W8 | Bus voltages and regulated rails | Chosen | | | OPEN |
| W9 | Nose aerodynamic heating profile | Derived | | Mach 2+ flight | OPEN |
| W10 | Component temperature limits versus thermal path | Derived | | From W9 | OPEN |
| W11 | Potting compound and thermal conductivity | Chosen | | | OPEN |

---

## E — Environment & qualification

| ID | Criterion | Type | Value | Basis / source | Status |
|---|---|---|---|---|---|
| E1 | ⚑ Axial acceleration: g-level, **pulse shape and duration** | Given | 15 000 g **[ref]** | YIL / gun data | OPEN |
| E2 | Radial acceleration | Given | 5 000 g **[ref]** | YIL / gun data | OPEN |
| E3 | Vibration: random and sinusoidal levels | Given | | MIL-STD-810 | OPEN |
| E4 | Shock: setback, set-forward, handling, drop | Given | | MIL-STD-810 | OPEN |
| E5 | Storage temperature range | Given | | MIL-STD-810 | OPEN |
| E6 | Operating temperature range | Given | | MIL-STD-810 | OPEN |
| E7 | Humidity, salt fog, sand and dust | Given | | MIL-STD-810 | OPEN |
| E8 | EMC standard | Given | MIL-STD-461 | | OPEN |
| E9 | Aerodynamic heating | Derived | | From W9 | OPEN |
| E10 | Qualification standards list | Given | MIL-STD-810, MIL-STD-461, MIL-STD-1316 | | OPEN |
| E11 | Insensitive munitions assessment | Given | AOP-39 / STANAG 4439 | | OPEN |

---

## K — SWaP-C & cost

| ID | Criterion | Type | Value | Basis / source | Status |
|---|---|---|---|---|---|
| K1 | Kit mass target | Chosen | | From P9 | OPEN |
| K2 | Kit envelope target | Chosen | | From P12 | OPEN |
| K3 | Power target | Chosen | | From W2, W3 | OPEN |
| K4 | Unit cost target and the production volume it assumes | Chosen | | At a **stated** volume | OPEN |
| K5 | Ranked cost drivers | Derived | Bearings, magnets/windings, electronics | From C22, C14, R-architecture | OPEN |
| K6 | Manufacturing process assumptions | Chosen | | YIL capabilities | OPEN |

---

## R — Reliability, safety, verification

| ID | Criterion | Type | Value | Basis / source | Status |
|---|---|---|---|---|---|
| R1 | Reliability target (per round) | Chosen | | | OPEN |
| R2 | Dud rate | Chosen | | From F10 | OPEN |
| R3 | Built-in-test coverage | Chosen | | | OPEN |
| R4 | Graceful degradation defined per failure mode | Chosen | | No mode may be worse than unguided | OPEN |
| R5 | Monte Carlo: number of runs, input distributions, confidence level | Chosen | | Produces the CEP claim | OPEN |
| R6 | CEP demonstration method (rounds, conditions, range) | Chosen | | For the trials plan | OPEN |
| R7 | Bench rig capability specification | Chosen | | Torque motor, speed motor, load, angle sensing | OPEN |
| R8 | Hardware-in-the-loop definition | Chosen | | Ring angle must feed back into flight | OPEN |
| R9 | TRL target for the submission | Chosen | | PS prefers a prototype | OPEN |
| R10 | Post-flight logging and evidence | Chosen | | Data for trials and for the submission | OPEN |

---

## Decision log

Record every Chosen criterion here with its rationale. This is the traceability that makes the submission read as engineering rather than assertion.

| Date | Criteria ID | Decision | Rationale | Trade-offs accepted |
|---|---|---|---|---|
| 2026-09-17 | M1 | Mixed general-purpose target set: point / light materiel primary, proximity-capable soft/area secondary (option D) | PS mandates a three-mode fuze, which only earns its place if soft and defilade targets are in scope; mirrors the M1156 role set; keeps CEP ≤ 30 m as the binding requirement | All three fuze modes stay live, so the setter data package (F12) and aimpoint definition (M5) carry more load; treatment of target-location error deferred to M5 |
| 2026-09-17 | M2 | All three fuze modes — proximity, time, impact — configurable before flight; full terminal-effect envelope retained, impact selectable superquick / short delay / graze (option B) | User instruction: the kit must offer all three fuze modes configurable pre-flight. Option B is the only choice that satisfies it without reducing the round's terminal effect, which the mixed general-purpose target set (M1) requires | Delay bounds, burst-height range and graze-angle limits deferred to F3/F5; compatibility of the explosive-train output with the shell booster becomes a hard F9 item |
| 2026-09-17 | M3 | Option C: full functional envelope across charges 3M–6M, with the CEP claim bounded to a range band set at M4; outside it accuracy degrades but never below unguided | The retrofit premise requires the charge system to be untouched, so full-envelope functionality is not optional; a CEP claim that cannot be verified across the whole band is a liability in trials; the binding loading case is low-q near apogee, so excluding charges buys almost nothing. Accepted by the user | Charge/velocity and range-band values remain **[ref]** placeholders; M3 stays OPEN-BLOCKED until YIL firing tables arrive |
| 2026-09-17 | M4 | Claim CEP ≤ 30 m at the maximum-range, full-charge (6M) condition; mid-band results reported as supporting data only | The kit earns its keep where unguided dispersion is largest, which is max range; the guided window is also longest there; bounding the claim at M3 keeps anything outside the band from being overstated. Accepted by the user | The numeric range is pending YIL firing tables (M4 stays OPEN-BLOCKED); a single formal trial condition, with no second formal claim |
| 2026-09-17 | M5 | CEP defined as the 2-D circular 50% radius; formal claim measured against the loaded aimpoint with target-location error excluded; end-to-end CEP against the true target published as a sensitivity with a named target-location error | Keeps the headline claim inside our control while never hiding the dependency — the bait-and-switch a defence reviewer probes for. Accepted by the user | One extra term in the Monte Carlo (R5) and an explicitly stated target-location assumption; the trials plan (R6) must instrument against a surveyed aimpoint |
| 2026-09-17 | M6 | Re-baselined from a bare "500 m class" assumption to a cited external anchor: unguided M549A1 155 mm CEP = 267 m at maximum range → equivalent circular 1σ = 227 m. Criterion deliberately kept OPEN-BLOCKED pending YIL's firing tables | M6 is the root of the sizing chain, so a guessed value propagates its error into every downstream requirement — not defensible for a number the submission will be judged against. An externally published, citable figure gives a real bound to size against now, and the CEP form settles the 1σ-versus-peak-to-peak ambiguity the YIL request was written around | The anchor is a foreign round at a foreign range (30.1 km from the M198); if YIL's dispersion differs materially the whole chain moves. The range/deflection split is still unknown and YIL request 3 stays live. Logged as risk 12 |
| 2026-09-17 | M7 | Re-derived as a capture-fraction problem rather than a percentile lookup: required authority A = σ·√(−2·ln(1−P)) with σ = 227 m, design capture fraction **P = 80%** → **A = 407 m**, equivalent Δv = 19.5 m/s over a 41.8 s full-force burn. Requirement split into range-direction and deflection components and stated as not interchangeable | A percentile lookup answers "how big is the 50% radius" — the wrong question. What the kit must buy is the fraction of the unguided population the loop can capture. Below 80% the uncorrected tail, not the guided cluster, sets the achievable CEP, so the 30 m claim stops describing our guidance. 80% is the largest capture fraction that stays inside the authority available: P = 85% (442 m) leaves only a 1.07:1 margin and P = 90% (487 m) exceeds what a 20 N force can deliver across the terminal window | Margin is 1.16:1 and assumes continuous full-force authority across the whole 45 s window that G3 says is not uniformly available. Range correction costs more authority than deflection, so the isotropic Rayleigh assumption may be optimistic. Logged as risks 10 and 11 |

---

## Requests outstanding from YIL

Track what is blocking `OPEN-BLOCKED` criteria. These gate the largest number of criteria and should be requested early.

| # | Request | Blocks | Requested on | Received |
|---|---|---|---|---|
| 1 | Shell drawing / datasheet (mass, CG, inertia, ogive contour) | P1–P5, P8, P12, S1–S7 | | |
| 2 | Fuze well thread specification | P6, P7, F9 | | |
| 3 | Baseline unguided dispersion at range — **state the range, and give the range-direction and deflection components separately.** (Interim anchor in use: M549A1 CEP 267 m at max range → circular 1σ 227 m. YIL's own round, its range, and the range/deflection split are all still needed) | M6, M7, M8 | | |
| 4 | Acceptable mass / CG / inertia change | P9, P10, P11 | | |
| 5 | Gun and charge compatibility list | M3, M9, E1, E2 | | |
| 6 | Inductive fuze setter — is one in service, and its interface | F11, F12 | | |

---

## Open risk register

Design risks carried forward; each should be closed by a criterion or by analysis.

| # | Risk | Related criteria | Status |
|---|---|---|---|
| 1 | Friction versus Taero margin near apogee is the thinnest in the design | C10, C12, C13, C22–C25 | Open |
| 2 | Ring-angle error is a direct, unattenuated error in guidance-force direction | G5, G6, N12 | Open |
| 3 | Canards ahead of the CG reduce gyroscopic stability | S1, S2, P9–P11 | Open |
| 4 | Ring bearing survival of the setback load | C26, C32, P12 | Open |
| 5 | GNSS signal under high spin rate | N3, N4 | Open |
| 6 | Proximity fuze EMI against the alternator in one nose volume | F15, E8 | Open |
| 7 | Control energy has no dissipation path in flight | W7 | Open |
| 8 | Aerodynamic coefficient set is unavailable and must be sourced or computed | All C and G criteria | Open |
| 9 | End-to-end CEP depends on target-location error, a term the kit does not own; if the sensitivity is published without a realistic assumption, the 30 m claim is judged against it | M5, G4, R5, R6 | Open |
| 10 | Correction authority is of the same order as the unguided dispersion it must remove. At the chosen 80% capture fraction, M7 asks for 407 m and 19.5 m/s against ≈471 m and 20.9 m/s from a 20 N force over the full ≈45 s terminal window — margin ≈1.16:1, and it assumes continuous full-force authority across a window in which G3 says authority collapses at apogee and is only ±15–25 N over much of the flight | M6, M7, C8, C11, G3 | Open |
| 11 | The range and deflection components of the baseline dispersion are not yet split, and range correction costs more authority than deflection — the two are not interchangeable. If YIL's firing tables show a range-dominated footprint, the 407 m budget is consumed faster than the isotropic Rayleigh assumption implies | M6, M7, C8, G1, G4 | Open |
| 12 | The M6 anchor is a foreign round at a foreign maximum range (M549A1, 30.1 km from M198), not YIL's shell. Sizing the chain from it is defensible and citable, but the whole downstream chain must be re-run the moment YIL's firing tables land | M6, M7, M8 | Open |

---

## Related files

| File | Purpose |
|---|---|
| `notes/02-PGK-SIH-design-brief.md` | Problem statement mapping, coverage analysis, architecture decisions |
| `notes/00-PGK-thesis-working-notes.md` | Reference design for the 155 mm class — all `[ref]` values come from here |
| `notes/figures/` | Extracted reference figures |
| `submission/` | Submission drafts — **reference only**, not to be edited during design work |
