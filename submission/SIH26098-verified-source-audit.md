# SIH26098 — Verified Source Audit

Written 2026-09-19 **after** reading the sources rather than citing them. Every entry below was fetched and read, except where marked otherwise. Where a source contradicts something we have written, the contradiction is stated first.

**Purpose.** The judge dossier (`SIH26098-judge-and-competitor-dossier.md`) reasons from the public record. This file is the check on that record: it says which of our claims the sources *support*, which they *undermine*, and which they *improve*. Anything written into the final deck must survive this list.

**Status key:** ✅ confirmed as written · ⚠️ needs rewording · ❌ wrong, must be changed · ➕ new information we should use

---

## 1. The four findings that change what we can claim

### ❌ 1.1 The M1156 is not a lesser architecture — it is *our* architecture, fielded since 2015

Read the primary source. From the Orbital ATK program update to the 2015 NDIA Armament Systems Forum (approved for public release), the M1156 PGK's key innovations are listed as:

> **"De-Spun Canard Assembly"** — "Simple Mechanical Design · Fixed Canards · **No Mechanical Actuators** · **One moving part** · No Slip Rings" · "**No Battery**" · "**Full two dimensional guidance to impact**" · "Self generating power (no battery)"

Plus, from the U.S. Army's own program page and Wikipedia: it replaces the standard fuze, is a "GPS guidance kit with fuzing functions", weighs **3 lb / 1.4 kg** (1 lb / 0.45 kg more than a standard fuze), and holds an **alternator that generates power in flight so no battery is needed**.

**This is the same list our submission presents as its novelty.** Our form content says: *"no servo actuators, gearboxes or control-surface linkages, and no in-flight battery is required. This directly attacks the Size, Weight, Power and Cost constraint… and removes the least reliable components of a conventional guided shell."* Every clause of that sentence describes the fielded M1156.

**What this means.** The de-spun ring, the fixed canards, the absence of actuators, the single moving part, the alternator and the absence of a battery are **the published specification of the system the problem statement asks India to indigenise.** They are the correct answer to the PS. They are not a novelty claim, and presenting them as one is the fastest way to lose a defence panel.

**The fix is already partly applied** (see `SIH26098-form-content.md` §15, rewritten today). It needs one more turn: the "adopted" list must name the fielded kit explicitly, because the judge will already be thinking it. Naming it converts a trap into evidence of homework.

### ❌ 1.2 The fielded kit has a dud-on-miss failsafe we do not have

Wikipedia's summary of the fielded behaviour: *"if the shell does not impact within 150 m of the intended target, it will land but not explode; the PGK 'decides' five seconds after launch whether it expects to impact close enough to detonate."* This exists for close-support safety — it is the reason a battery can call precision fires near its own position.

Our submission currently says the opposite, twice:

- *"loss of guidance, loss of GNSS or loss of the setter write all degrade accuracy but leave a live, functioning fuze"*
- *"There is no failure mode in which the kit makes accuracy worse than the unguided baseline."*

Both statements are about **accuracy**. The fielded system's failsafe is about **where a 43 kg high-explosive round lands when the guidance has failed.** A fuze-safety judge will not conflate those, and our deck currently has no answer at all.

**This is the highest-value gap in the submission**, because it is (a) real, (b) safety-critical, (c) known to the panel, and (d) cheap to fix with a stated design decision either way. The honest options are to adopt a predicted-miss threshold, or to state why we do not — and either is defensible. Silence is not.

### ❌ 1.3 "No in-flight battery" is a fielded property, not a differentiator

Confirmed twice: Orbital ATK's "Self generating power (no battery)" and Wikipedia's "does not need a battery since the alternator inside generates power in flight."

Our submission leans on this repeatedly as the SWaP-C argument. It remains a true and well-earned property of *our* design; it is simply not a differentiator against the benchmark. Keep the sentence, retire the implication.

### ➕ 1.4 The fielded kit does not use inertial sensors — and that is a question we must answer

Also from the Orbital ATK slide: **"GPS with Roll Angle Determination — No Inertial Sensors."** The fielded PGK determines its canard roll angle from GPS, not from an IMU.

Our N6 headline is "the IMU rides the de-spun ring." Against a panel that knows the fielded design, this is not a pure strength — it is a **cost and complexity addition relative to the benchmark**, and it cuts against our own low-cost claim.

**The answer is good, but it must be stated as a trade rather than a triumph:** the fielded design is GPS-only for roll determination, which is why the US is now fielding **PGK E5 with anti-jam**, with production started in September 2026 and first deliveries expected in early 2028. Our PS requires operation under the stated environmental and operational constraints, and a kit entering service later than that must not be built around the assumption that GNSS is always available. We buy that with an IMU whose cost and mass are declared — and we are the only entry in this field to have priced it.

### ➕ 1.5 The official guidelines give extra weight to business potential

The SIH 2026 guidelines state, verbatim: *"Idea should be unique and novel. **If it has a business potential more weightage will be given.**"* Also confirmed: *"Working prototype is preferable for Hardware Edition, but not mandatory."*

**Consequence for slide 5.** The impact slide should read as a **business case** — volume, unit economics, production line, indigenous content, and who pays — not as a capability statement. Our ₹6.5 lakh target is currently presented as a benchmark subtraction. Recast it as the business proposition it is, with the ranked cost drivers visible.

---

## 2. Source-by-source findings

### 2.1 Orbital ATK, *Precision Guidance Kit (PGK) Program Update*, NDIA 2015 — read in full

| What it gives | Why we should use it |
|---|---|
| "Conventional ammunition with legacy fuzing: **>200 m CEP** at max range"; "with PGK: **30 m objective CEP**" | Independent corroboration of our M6 problem-statement number |
| Accuracy by range for M549A1: **94 / 125 / 150 / 267 m CEP** conventional vs **30 m** with PGK at every range | Four-point evidence for slide 1 that dispersion scales with range — better than our single 267 m figure |
| **Value proposition: 301 projectiles → 77 (74 % reduction); 959 → 208 charges; 18.2 → 4.5 tons (75 %)** | ⚠️ Our M8 impact claim ("4 rounds vs ≈264, 90 %") needs to sit beside this authoritative pair. Ours is a different scenario (point target, 90 % defeat probability, 30 m effective radius) and may be right, but 74–75 % is the fielded, public, checkable number. Cite both, explain the difference, or adopt the fielded band |
| "Maintains **>90 % of range capability** of conventional all up round" | ➕ A design constraint we should also satisfy and state — it is exactly the kind of system-level requirement a YIL judge thinks in |
| "Reliable — **one moving part**" | Their reliability argument. Ours is the same; credit it |
| "Built-In Tactical Telemetry … development tests, stockpile surveillance, lot acceptance tests" | Our flight-event logging is aligned practice; say so |
| Qualified on **M109A6 and M777A2**, M549A1 and M795; demonstrated on M795, M549, M107, DM111, XM1128 | Platform-compatibility framing for our §13 |
| Demonstrated on **DM111 from a PzH 2000 at 27 km**, 10 shots, "hole in roof" | The fielded capability bar, and a citable proof that the class works from rifled and smoothbore howitzers |

### 2.2 M1156 — Wikipedia and U.S. Army PM CAS page — read in full

- ⚠️ **Mass 1.4 kg**, net **+0.45 kg** over a standard fuze. Our kit at 1.4–1.7 kg and +0.7–1.0 kg net is **1.55–2.2× the fielded net penalty**. State both comparisons honestly: total mass is 1.0–1.21× the fielded kit, net penalty is 1.55–2.2×. Do not quote only the flattering one.
- ✅ **Intrusion ≤124.7 mm, visible ≤95.25 mm, overall 220.2 mm** — matches what we have written, and now sourced to a specification table rather than to a secondary summary.
- ✅ **Fuze modes: "Point Detonation; Height of Burst"** (PM CAS) and "Point detonating or proximity airburst" (Wikipedia). Our wider-mode claim holds **against the US kit**.
- ✅ **Unit cost US$13,541 (FY2013)**, with the program's own stated objective below US$10,000. FMS reference points: Australia 4,002 kits / $54 M; Netherlands 3,500 / $70 M; Finland 5,500 / $70 M. Our "US$12.7–20 k" band is right.
- ➕ Over **100,000 units produced** by September 2022 — the volume context for our 5,000/year cost target. A panel will notice that we are proposing two orders of magnitude less volume, so our volume assumption must be justified rather than assumed.
- ➕ Trials data worth citing: **97 % reliability in the first production lot acceptance test (41 of 42)**, and a **median accuracy below 10 m** — materially better than the 30 m objective. **We must never claim accuracy superiority over the fielded kit.** Our claim is compliance plus cost plus mode set.
- ✅ The DOT&E report threshold/objective pair (50 m/30 m CEP) is confirmed by the report's own abstract: *"threshold accuracy of 50 meters CEP and objective accuracy of 30 meters CEP."*

### 2.3 Elbit Systems, *Silver Bullet II* brochure — read in full

This is the most complete fielded competitor and it moves two of our claims:

- ❌ **"Wider mode set than the fielded competitor"** is only true against the US kit. Silver Bullet II offers **a "multi function detonation unit, supporting Point Detonation (PD), Point Detonation Delay (PDD) and Air Burst (AB) modes."** Our three modes are close to parity in count. **The genuine differentiators are (i) a true programmable *time* mode and (ii) in-flight re-synchronisation of that time.** State it that way.
- ➕ **"Adaptive canard system that enables active guidance throughout its trajectory"** — so the fielded Israeli kit uses *adaptive* canards rather than our fixed-canard/de-spun-ring approach. That is a real architectural contrast, and the first one that favours our description: fixed canards and a de-spun ring buy simplicity and remove actuators, at the cost of the kilowatt energy path we have sized.
- ➕ **CEP 20 m**, "GNSS-guided ammunition **can continue guidance under partial GPS degradation**", "reduces ammunition expenditure by **up to 90 percent**", environmental conditions **per MIL-STD 810F and MIL-STD 331C**, compatible with autoloader guns, "no need for adjustment of fire".
- ➕ **A dedicated firing computer / data setter that computes charge, azimuth and elevation and uploads mission data to the kit** — i.e. our F12 "the setter carries the mission data" is fielded practice, not an invention. Good: it validates the approach. Present it as compatibility, not novelty.
- ✅ Our 20 m-class accuracy framing: with Silver Bullet II at 20 m and the M1156 demonstrating sub-10 m median, **23.9 m is compliant but not a headline.** Lead on cost, modes and indigenous content.

**Standards to adopt into our environmental section** (from Elbit and from our own §9): **MIL-STD-331C** for fuze environmental and performance testing, **MIL-STD-810F** for environmental, **MIL-STD-1316** for fuze safety design (already cited), and STANAG 4369 / AOP-39. Our current text says "the applicable defence standards for artillery fuzes" — name them.

### 2.4 IAI TopGun — ⚠️ marketing page not retrievable (bot protection)

Only the search-indexed description is available: *"guidance integrated fuse… performs 2D correction… achieving 20 m CEP at any range"*, without altering firing routines. Treat as **indicative, not verified**, and do not put a number from it on the slide unless the deck says "manufacturer-stated".

### 2.5 Northrop Grumman PGK E5 / Long Range PGK — search-verified

- **PGK E5**: "next-generation precision guidance kit… adding **advanced anti-jam technology** to deliver reliable, first-round precision… even in **GPS-contested environments**, without changing form or training requirements." Production started at Plymouth, Minnesota (announced September 2026), **first deliveries expected early 2028**.
- **M1156E2/A1**: compatible with XM1113 rocket-assisted and XM1128, **10 m accuracy at 30 km and 40 km** from a 39-calibre barrel.
- **Long Range PGK**: for **70 km** from 58-calibre barrels, and specified to *"operate in a near-peer GPS threat environment."*

**Consequence:** by the time any kit we design could enter service, **GNSS-denied operation is table stakes, not a feature.** Our X17 framing (anti-jam GNSS with INS coasting as the primary GPS-denied answer) is correct and should be stated as *alignment with the direction of the fielded programme* — and it strengthens the §1.4 answer about why we carry an IMU that the fielded M1156 does not.

### 2.6 SIH 2026 guidelines and rules — verified via the official PDF's indexed text and a university SPOC notice

- ✅ Evaluation criteria verbatim (nine terms) — as used in the dossier.
- ➕ **Business potential carries additional weight.** New. Changes slide 5's job.
- ✅ 500-idea cap per problem statement; 30 September 2026 nomination and idea deadline.
- ✅ Six-slide cap, use the template, points over paragraphs, all template topics used, **no PPT or Word — PDF only**.
- ➕ "**Apart from this PPT, abstract of your idea will be asked separately while submitting PPT**" — our `form-content.md` abstract is that artifact. It is read as a standalone document; trim it accordingly.
- ✅ **Working prototype preferable but not mandatory** for the hardware edition.
- ⚠️ The 20 September deadline that one tracker shows for this PS is **not** corroborated by the guidelines, which say 30 September. Still verify on the portal, but the official date is 30 September.

### 2.7 Prior art — abstracts verified, full texts paywalled

- **Zhang, Yao & Zheng (2019), Chinese Journal of Aeronautics** — "Impact point prediction guidance based on iterative process for dual-spin projectile with fixed canards." ✅ **Confirms the IPP law is published prior art for this airframe.** Our guidance-law novelty claim must stay retired.
- **AIAA 2024-1105, "Design and Aerodynamic Characterization of Canard Guided Fuze for Dual-Spin Projectile"** — *"four fixed canards at a deflection angle of 4°… two rolling and two lifting canards with a **minimum design torque requirement of 0.8 N·m for a 155 mm artillery projectile** in the supersonic regime."* ➕ This is the closest published relative of our own CAA. **Two consequences:** it independently validates the two-pair rolling/lifting split we use; and its 0.8 N·m figure is a published design torque for a 155 mm dual-spin fuze that a judge may hold against our 0.17–2.12 N·m aerodynamic torque envelope. Have the distinction ready: theirs is an actuator design requirement, ours is the measured *aerodynamic* torque the ring must hold — different quantities, and our alternator's available torque is sized from ours.
- **Defence Technology (2025), "Investigation of flight stability for fixed canard dual-spin projectile"** — CFD/RBD coupling, and it "reproduces the characteristic **resonance instability** of such projectiles." ➕ A named instability mode in our architecture's own literature. Our stability section discusses gyroscopic stability (Sg) but does not name resonance instability. **A domain judge may ask about it; we should name it and say how the design avoids it.**

### 2.8 NATO AOP-22, *Design Criteria and Test Methods for Inductive Setting of Large Calibre Projectile Fuzes*, Edition B Version 1, May 2018 — read in full

**The single most valuable document found in this pass, and it reverses a claim.** AOP-22 is the standard supporting STANAG 4369 / AOP-4369, and it does four things for us.

**It gives F11 the standard it never had.** The setter interface was PARAMETRIC on *"the standard gun-line interface"* with no standard named. AOP-22 fixes the numbers: carrier **100 ± 0.01 kHz**; forward-message bit rate **1 000 ± 10 bit/s**; mark/space rise and fall **≤ 50 µs**; fuze message window **275 ± 5 ms**; power-up period 1–1 000 ms; and a carrier inducing **36.2–48.2 V peak-to-peak** into a standard fuze receive coil.

**❌ It defeats our in-flight time re-synchronisation claim — and this is the important one.** Annex E.16 registers the **XM8 — *"FUZE, COURSE-CORRECTION, ELECTRONIC TIME FUZE"*** — and states:

> *"In course correction mode, the time is also corrected in flight to improve accuracy."*

The audit's §3 had this claim as **"✅ Ours, and no fielded equivalent found"** and §4 told the deck to *promote* it. **That verdict is reversed.** A NATO-registered, fielded course-correction fuze already corrects its time in flight. The claim joins the M1156 list — *adopted and credited, never claimed*. What survives as ours is narrower: the correction is driven by **our own continuous nav solution** rather than a ballistic/firing-table correction, in the bounded one-way gated form F1 specifies. This is the second time in two passes that reading the primary document has removed a novelty claim the literature review left standing.

**❌ Our setter read-back is the standard's own mechanism, not a design feature.** §3.3: *"Error detection is provided by having the setter transmit a message to the fuze, for the fuze to repeat the message back to the setter, and for the setter to compare the two transmissions."* F12's verified read-back is compliance. Keep the sentence; retire the implication. Our **target sanity check against the firing solution** does remain ours.

**➕ It exposes a capacity problem nobody had counted.** The window is **275 ± 5 ms at 1 000 ± 10 bit/s ≈ 275 bits**, and the two registered course-correction fuzes (XM7, XM8) each use **two** windows — so **≈550 bits** is the standard's own budget for a whole CCF mission package. F12 claims target coordinates, met, charge/muzzle-velocity state, time reference, **GNSS ephemeris and keys**, mode and parameters, round ID, *and* a read-back. **Ephemeris alone is of that order.** This is now register **risk 44**, owned by H11, and it is a short derivation rather than a design change — but it must be done before a setter engineer asks.

**➕ Two further uses:** §3.6(c) permits the fuze to **calibrate its time base against the setter's precision time base** (an external anchor for H6/N15, which currently closes on itself); and §3.6 defines a **command mode in which all-zero data bits program the fuze to a safe condition**, plus lists *"specific data bit patterns may be unacceptable for system safety reasons"* among the fuze's own rejection criteria — which is the standard's own hook for **F16**, the predicted-miss failsafe.

### 2.9 How the resonance instability is actually fixed — and that we already did it

Two papers, and together they turn an unnamed failure mode into a **validated design choice**.

- **Defence Technology 2025**, *Investigation of flight stability for fixed canard dual-spin projectile*: a high-fidelity CFD/RBD coupled virtual-flight platform whose reliability is demonstrated by **"reproducing the characteristic resonance instability of such projectiles"**.
- **Acta Armamentarii 2026** (Guo, Peng, Liu et al., DOI 10.12382/bgxb.2026.0534), *Resonance Mechanism and Aerodynamic Optimization of a Canard-Type Two-Dimensional Trajectory Correction Projectile in the Uncontrolled Flight Phase*: complex-angle-of-attack theory shows the mechanism — **"canard disturbance resonates with projectile natural frequency and causes ballistic fluctuation"** — and the proposed fix is **reduced canard span with increased deflection angle**, which *"raises pitching moment derivative and projectile natural frequency to avoid resonance."*

**That fix is this design's C31 (Ø151 mm span cap) and C43 (*cant angle, not area, is the lever*), arrived at independently for different reasons.** So the disposition asks for evidence, not a redesign. **➕ Also useful:** the 2026 paper's own reference list is the best single map of the Chinese-language literature on exactly this architecture, and it yields the exact citation for the field's standalone review — **Norris, Hameed, Economou et al., *A review of dual-spin projectile stability*, Defence Technology 16(1) 2020, pp. 1–9** — plus work on the lever-arm error for a dual-spin correction fuze's inertial navigation (Wang et al., Acta Armamentarii 46(6) 2025), which speaks directly to N1's **"time/lever-arm 1.0 m"** term, currently the register's least-supported error line. Both are in the register as S8's and N1's basis.

### 2.10 In-bore electronics survivability — E1/E2/E4 had a bare `[ref]` and no closure route

- **Defence Technology 2026**, *Establishment of the damage tolerance criterion of projectile-borne electronics under in-bore launch* — the criterion form the E domain lacks. ➕ **E1's real content is the pulse *shape*, not the peak:** the gun-hard MEMS IMU literature specifies a **long-duration component (>5 ms) with a superimposed high-frequency component** at a 10 000–20 000 g peak, so "15 000 g" alone is not a test condition.
- **NSWCIH, *High Shock Modeling of Fuze Components*, 64th NDIA Fuze Conference 2021** — read in full, and it supplies the **method**: material characterisation at high strain rate (Split Hopkinson Bar and 4-point bend) → explicit finite-element modelling → very-high-g test using a **potted accelerometer** to capture the imposed loading, on a national facility with **guns to 21″ at >2 000 ft/s**. ✅ It also independently confirms that **potting is the established protection** (H5's assumption) and that **MEMS safe-and-arm with a setback lock and a command lock is established practice** (F6's direction, not our invention).

### 2.11 The bearing friction literature — and a new failure mode

`Tf* = 0.1567 N·m` is the design's **feasibility gate** and it rested on one reference datum at 83.8 rad/s, scaled 19.4× to flight speed (risk 24). The miniature-bearing literature decomposes friction torque into rolling, sliding, pivoting, cage–ball and cage–race terms and fits **Houpert's model** — the published route to defending that scaling.

**➕ And a practitioner source opened a failure mode nobody had named.** From the mechanisms it sets out: `Q ∝ M_friction × ω`, so **the "flat" 0.10 N·m budget is already ≈160 W** (the register's number, now with a mechanism); and the high-speed failure path is a **closed loop — friction → heat → clearance loss → preload rise → friction rise**. **C23 deliberately buys air-gap stiffness with preload at up to ≈1 900 rad/s**, and our air gap is 0.40 mm with 0.20 mm of deflection allowance, so the clearance the loop consumes is exactly the clearance C35 protects. Also worth carrying: contact seals are a large avoidable friction share (so open or shielded), grease *quantity* is first-order in a miniature bearing, and cold-start torque rises — which is the cold corner of R5's campaign. Register **risk 45**, owned by C23.

### 2.12 The thermal interface — P6's estimate now has a measurement behind it

**Chalmers / RUAG Space, *Thermal Contact Conductance in Bolted Joints* (2012)** — vacuum experiments on aluminium bolted joints. Measured: total joint conductance **≈0.52 / 0.79 / 0.89 W/K** at 0.8 / 1.1 / 1.4 N·m bolt torque, rising to **19.6 / 20.8 / 21.2 W/K with a thermal interface material — a 24×–38× lever.**

Three findings bear directly on us: ✅ the bare-joint **order of magnitude matches** our first-order 3–16 W/K estimate; ✅ **heat flow concentrates within a short radius of each fastener and large areas of the joint carry essentially no flux**, which is why our "a clearance fit does not count" negative result is right; and ➕ **a thin interstitial layer is the closing lever, not more clamping force**. The source also finds the available analytical models disagree strongly and recommends application-specific measurement — which is exactly **R7 item (7)**. **This is P6's evidence base**, and it strengthens rather than changes the ≥ 58 W/K requirement.

### 2.13 The course-correction-fuze comparison literature

**Gagnon & Lauzon (AIAA 2008-6997)** compare drag brake, spin brake and the **roll-decoupled four-canard configuration** head to head with guidance tuned for each; **the ASCE 2016 efficiency analysis** quantifies how much correction a canard CCF actually buys against M7's 407 m and C8's 18.1 N. ➕ Both give C1's "why four fixed canards" a comparative basis rather than an assertion.

### 2.14 RocketPy's own documentation — risk 38's boundary, confirmed by the tool itself

The technical documentation (v1.13.0, MIT) covers equations of motion v0/v1, **elliptical fins** and **individual fins**, roll equations and sensitivity — and states the section is incomplete. **The aerodynamics are fin-oriented: there is no canard model, no de-spun ring degree of freedom and no in-bore phase.** So the register's "harness only, never the model" rule holds, the version and licence are now pinned, and our coefficients must enter through its coefficient-injection path while the ring DOF is ours to add. ➕ This upgrades risk 38's boundary from inference to a documented limit.

### 2.15 A published bench precedent — for R7 and for risk 37

**IEEE 2024, *Robust Velocity Control of a Fixed Canard Decoupled Dual-Spin Projectile***: *"A motor-generator test bench and a dynamical model are developed to emulate the dual-spin system accurately, enabling thorough experimentation and analysis,"* with sliding-mode control strategies. ➕ **That is R7's architecture, published**, and four-quadrant dual-spin actuation is what the bench was built to study — which is exactly **risk 37's ring-hold-duty trade**. Also relevant: **Ramteke & Kothari (JGCD 48(3) 2025)**, an **accessibility analysis** of dual-spin projectiles — the formal reachability form of M7's authority question. (Abstract-only; rated provisionally.)

---

## 3. The corrected claim set

| Claim | Verdict | Action |
|---|---|---|
| De-spun ring, fixed canards, no actuators, one moving part, no battery, 2-D guidance | ❌ Not novel — fielded M1156 | Move to "adopted and credited" |
| The IPP guidance law | ❌ Not novel — Zhang 2019 | Already reframed to the authority gate |
| Fixed-canard two-pair geometry | ❌ Not novel — patent + AIAA 2024 | Keep as description only |
| Machine sized as a loaded generator at flight-representative spin → 2.92 kW / 121 kJ | ✅ Ours, verifiable, uncontested | Lead with it |
| Declared thermal interface; bare thread 3–16 W/K vs ≥58 W/K | ✅ Ours, uncontested | Lead with it |
| Ring-mounted IMU | ⚠️ Ours, but a *cost addition* vs the fielded GPS-roll design | State as a trade, justified by the GNSS-denied requirement |
| Three-mode fuze (proximity, time, impact) | ⚠️ Wider than the US kit; parity with the Israeli kit | Reframe to the *time mode*, and see the row below |
| **In-flight time re-synchronisation** | **❌ REVERSED 2026-09-19 — not novel. AOP-22 Annex E.16 registers the XM8 course-correction fuze: *"In course correction mode, the time is also corrected in flight to improve accuracy."*** | **Move to "adopted and credited".** What survives as ours: the correction is driven by our own continuous nav solution, in the bounded one-way gated form F1 specifies |
| Setter carries mission data | ⚠️ Fielded practice (Silver Bullet II) | Present as compatibility |
| No adjustment fire / reduced rounds | ⚠️ Fielded claim: 74–75 % reduction (PGK), up to 90 % (Elbit) | Align our figure to the fielded band and cite it |
| CEP 23.9 m | ✅ Compliant; below fielded demonstrated performance | Never claim accuracy superiority |
| Mass +0.7–1.0 kg | ⚠️ 1.55–2.2× the fielded net penalty | State both ratios |
| Dud-on-miss behaviour | ❌ Absent from our design | **Design decision required before the deck is written** — now register criterion **F16** with three priced forms |
| HERO / EMR / ESD | ❌ Absent | Add — now register criterion **E12**; standards named at P4 |
| Resonance instability | ❌ Not named | Add — now register criterion **S8**; the design already carries the literature's own fix |
| Standards named | ⚠️ Vague | Name MIL-STD-1316, **MIL-STD-331C**, MIL-STD-810F, MIL-STD-461, **AOP-22**, STANAG 4369 / AOP-39, STANAG 4439, STANAG 9216 |
| **Setter mission-package capacity** | ❌ Never counted | **AOP-22 gives ≈275 bits per window and two windows for a CCF.** F12's package (coordinates, met, charge state, time, ephemeris **and keys**, mode, round ID, read-back) must be budgeted. Register **risk 44**, owned by H11 |
| **Ring-hold duty torque vs the published peak** | ⚠️ Internally inconsistent | The hold duty is 2.36 N·m but C42 publishes 2.92 kW *at launch*, which implies 1.80 N·m. Reconcile the reference speed at P2. Register **risk 46** |
| **Thermal-preload runaway** | ❌ Not named | C23 buys stiffness with preload at ≈1 900 rad/s, where friction → heat → clearance → preload is a known runaway path. Register **risk 45**, owned by C23 |
| **Range retention** | ❌ Unbounded | Now register criterion **M10** at the fielded class figure, >90 % |

---

## 4. What the deck must say that it currently does not

1. **The dud-on-miss decision.** One line, either way — the highest-value gap and now criterion F16.
2. **The fielded kit by name** in the "adopted from established work" list, so the panel sees we know what we are indigenising.
3. **The two-honest-mass-ratios** sentence — total 1.0–1.21× and net 1.55–2.2×.
4. **The range-retention figure** (>90 % of conventional range, as the fielded kit claims) — now M10.
5. **The mode-set nuance** — a true *time* mode and a nav-driven in-flight correction, not "more modes", and **never the re-synchronisation as an invention** (AOP-22 Annex E.16).
6. **Resonance instability**, named and dispositioned — and note that the design's span cap plus cant lever *is* the literature's own recommended fix (S8).
7. **The named standards**: MIL-STD-1316, MIL-STD-331C, MIL-STD-810F, MIL-STD-461, **AOP-22**, STANAG 4369 / AOP-39, STANAG 4439, STANAG 9216.
8. **The business case framing** on slide 5, because business potential carries extra weight.
9. **The fielded impact anchor** — 301→77 rounds, 74 % — alongside our derived figure.
10. **The GNSS-denied alignment argument** — PGK E5, M-code, LR-PGK for the near-peer GPS threat; our IMU-on-ring is a deliberate departure, priced and declared.
11. **The fielded four-point dispersion evidence** on slide 1 (94 / 125 / 150 / 267 m CEP conventional vs 30 m with PGK) instead of the single 267 m figure — it shows dispersion scaling with range, which is the argument.
12. **The fielded rationale for the fuze's withheld detonation**, if F16 is answered by adopting a threshold: it exists so a battery can call precision fires near its own position, and that is a *better* argument for the mechanism than safety language alone.
13. **The setter read-back described as compliance, not invention** (AOP-22 §3.3) — and the target sanity check kept as ours.
14. **The reference speed attached to every power figure.** Slide 4's 2.92 kW must name the condition it is evaluated at, because the register's own duty table implies a higher figure at launch spin (risk 46).
15. **The 400 V bus nowhere on the slides.** H8/H12 set ≈150–200 V, 180 V nominal; any artefact still showing 400 V is quoting a superseded sizing pass.

---

## 5. Sources read, with what each is trusted for

| Source | Read | Trusted for |
|---|---|---|
| [Orbital ATK, PGK Program Update, NDIA 2015](https://ndia.dtic.mil/wp-content/uploads/2015/armament/wed17409_Hunter.pdf) | full PDF | Architecture of the fielded kit, value proposition, range retention, qualification status |
| [M1156 PGK — Wikipedia](https://en.wikipedia.org/wiki/M1156_precision_guidance_kit) | full | Mass, dimensions, modes, cost, failsafe, trials, variants, exports |
| [U.S. Army PM CAS — M1156 PGK](https://www.cpeae.army.mil/Project-Offices/PM-CAS/Organizations/Precision-Fires-Mortars/Products/PGK/) | full | Fuze modes, projectiles, platform qualification |
| [DOT&E FY2015 PGK report](https://www.dote.osd.mil/Portals/97/pub/reports/FY2015/army/2015pgk.pdf) | abstract only (direct fetch 404s; abstract indexed) | Threshold 50 m / objective 30 m CEP |
| [Elbit Silver Bullet II brochure](https://www.elbitsystems.com/sites/default/files/2026-06/silver_bullet_ii_2026_7_web.pdf) | full PDF | Mode set, CEP 20 m, adaptive canards, GNSS-degraded guidance, standards, impact reduction |
| [Northrop Grumman — PGK E5](https://www.northropgrumman.com/what-we-do/advanced-weapons/guided-projectiles-and-precision-weapons/precision-guidance-kit) and [production announcement coverage](https://www.armyrecognition.com/news/army-news/2026/m1156e5-pgk-e5-precision-guidance-kit-production-start) | search-verified | Anti-jam fielding timeline |
| [IAI TopGun](https://www.iai.co.il/product/topgun/) | ⚠️ not retrievable | Manufacturer-stated 20 m CEP only, unverified |
| [SIH 2026 Guidelines](https://sih.gov.in/letters/2026/SIH%202026%20Guidelines.pdf) via [DTU SPOC notice](https://dtu.ac.in/Web/upload/events/aug/file0807.pdf) | PDF + indexed text | Rubric, business-potential weighting, six-slide rule, PDF-only, prototype optional |
| [Zhang et al. 2019](https://www.sciencedirect.com/science/article/pii/S1000936119302419) | abstract | IPP prior art |
| [AIAA 2024-1105](https://arc.aiaa.org/doi/10.2514/6.2024-1105) | abstract | Fixed-canard dual-spin fuze, 0.8 N·m design torque |
| [Defence Technology 2025](https://www.sciencedirect.com/science/article/pii/S2214914725001722) | abstract | Resonance instability in fixed-canard dual-spin projectiles |
| [SRK — competitor sim repo](https://github.com/srkself26-cmd/sih26098-guidance-sim) | full | Competitor archetype C1 |
| [Indian Army fuze RFI](https://idrw.org/indian-army-issues-rfi-for-indigenous-manufacturing-of-155mm-electronic-fuzes-under-make-in-india/) | full | The three fuze categories our modes map onto |

**Added 2026-09-19 (second pass).** `full` = read end to end; `partial` = substantial read (abstract, references and structure); `abstract` = abstract only. Ratings are provisional at `abstract`.

| Source | Read | Trusted for |
|---|---|---|
| [NATO AOP-22, Ed B Ver 1, May 2018](https://www.jedi-sec.us/downloads/MISC_PDF/AOP-22%20EDB%20V1%20E.pdf) — *Design Criteria and Test Methods for Inductive Setting of Large Calibre Projectile Fuzes* | **full** | **The setter interface's governing standard** (carrier, bit rate, window, power levels) · **the XM8's in-flight time correction — which reverses our claim** · the read-back as standard practice · the ≈275-bit window that exposes F12's capacity gap · the time-base calibration route for H6/N15 · the safe-condition command mode behind F16 |
| [Chalmers / RUAG Space — *Thermal Contact Conductance in Bolted Joints*, 2012](https://publications.lib.chalmers.se/records/fulltext/159027.pdf) | **full** | **P6's evidence base**: measured joint conductance 0.52–0.89 W/K bare, 19.6–21.2 W/K with an interface material (24–38×) · flux concentration near fasteners · "a clearance fit does not count" · the recommendation to measure rather than model |
| NSWCIH — *High Shock Modeling of Fuze Components*, 64th NDIA Fuze Conference 2021 ([pdf](https://ndia.dtic.mil/wp-content/uploads/2021/fuze/Cao1.pdf)) | **full** | **E1/E2/E4's closure method** (Split Hopkinson Bar + 4-point bend → explicit FEM → very-high-g test with a potted accelerometer) · national gun capability · **potting as established protection** · MEMS S&A with setback lock as established practice |
| Miniature bearing speed, friction, torque and heat generation — manufacturer technical guide | **full** | The friction decomposition and `Q ∝ M_f ω` · **the thermal-preload runaway loop (risk 45)** · contact seals, grease quantity and cold-start torque as first-order variables. *Vendor guide — not citable as authority, but it changes the design* |
| [NATO AOP-22 Annex E registered-fuze registry](https://www.jedi-sec.us/downloads/MISC_PDF/AOP-22%20EDB%20V1%20E.pdf) (same document, separate use) | **full** | The list of fuzes a setter must already talk to, including **two course-correction fuzes (XM7, XM8), each using two message windows** |
| [Acta Armamentarii 2026](https://www.co-journal.com/en/article/doi/10.12382/bgxb.2026.0534/) — *Resonance Mechanism and Aerodynamic Optimization of a Canard-Type 2-D Trajectory Correction Projectile* | **partial** | The resonance mechanism, **and the span-reduction/deflection-increase fix that our C31+C43 already implements** · the citation trail to the field's review literature |
| [RocketPy technical documentation v1.13.0](https://docs.rocketpy.org/en/latest/technical/index.html) (MIT) | **partial** | Risk 38's boundary **confirmed by the tool's own documentation** — fin-oriented aerodynamics, no canard model, no ring DOF, no in-bore phase · version and licence pin |
| [MDPI *Lubricants* 13(1):12, 2025](https://www.mdpi.com/2075-4442/13/1/12) — friction torque in miniature ball bearings | abstract | The friction-torque decomposition behind C13/C25 (Houpert's model, sliding/pivoting/cage terms) |
| [MDPI *Lubricants* 14(4):145, 2026](https://www.mdpi.com/2075-4442/14/4/145) — influence of the cage on friction torque | abstract | Houpert's model fitted to cage variants — the scaling route from 83.8 to 1 900 rad/s |
| [IEEE 2024 — *Robust Velocity Control of a Fixed Canard Decoupled Dual-Spin Projectile*](https://ieeexplore.ieee.org/document/10663247) | abstract | **A published motor-generator bench for this exact configuration** — R7's precedent, and four-quadrant actuation for risk 37 |
| [*Defence Technology* 2026 — damage tolerance criterion for projectile-borne electronics under in-bore launch](https://www.sciencedirect.com/science/article/pii/S2095034926000012) | abstract | E1/E2's criterion form |
| [*Defence Technology* 2026 — high-g impact survivability of thermal batteries](https://www.sciencedirect.com/science/article/pii/S2214914726001029) | abstract | Risk 35's question, answered for an adjacent storage technology (gas-gun + validated 3-D FEM) |
| *Survivability of MEMS packages at high-g loads* (Springer) | abstract | MEMS IMU survivability to 20 000 g; 60 000 g by gas gun |
| *Survivability of embedded microelectronics in precision guided projectiles*, IJIE 2021 | abstract | Multiphysics shock loading through launch and muzzle exit |
| Gagnon & Lauzon, *Course Correction Fuze Concept Analysis*, AIAA 2008-6997 | abstract | Drag brake vs spin brake vs **roll-decoupled four canard** — the comparative basis for C1 |
| *Efficiency analysis of canards-based CCF for a 155 mm spin-stabilized projectile*, ASCE 2016 | indexed | Correction capability of a canard CCF — M7/C8's published counterpart |
| Norris, Hameed, Economou et al., *A review of dual-spin projectile stability*, *Defence Technology* 16(1) 2020, pp. 1–9 | indexed | **The field's standalone stability review** — what to hand a judge who asks "is it stable?" |
| Wang, Shen, Wang et al., *INS external gimbal arm error … for the fuze of double spin ballistic correction projectile*, Acta Armamentarii 46(6) 2025 | indexed | **N1's lever-arm term** on this airframe |
| Luo, Zhang, Deng et al., *Integrated optimization of de-spin actuator design and operating parameters*, AST 2025 | indexed | The C-domain's own optimisation problem, published |
| Ramteke & Kothari, *Accessibility analysis and robust control design of dual-spin projectiles*, JGCD 48(3) 2025, pp. 575–590 | indexed | The formal reachability form of M7's authority question |
| Shi, Zhang & Liu, *Spin rate and correction ability of 2-D trajectory correction fuze for 155 mm fixed-canard dual-spin projectiles*, Acta Armamentarii 40(8) 2019 | indexed | Correction capability against forebody spin, for our exact calibre |
| Zhao, Shi, Wang et al., *Dynamic stability … of the whole trajectory of fixed canard dual-spin projectiles*, CJTAM 54(5) 2022 | indexed | Full-trajectory stability — S1's missing whole-flight counterpart |
| Zhu, *Flight stability of a dual-spin projectile with canards*, J. Aerospace Engineering 2014 | abstract | A stability criterion that accounts for nose-applied side forces |

**Explicitly not cited** (recorded so no later session re-imports them): IAI TopGun (not retrievable), Kratos and GAJT-AE3 anti-jam pages (marketing), analyst field-size and competitor-count estimates (no method disclosed), Scribd re-hosts of NDIA decks where the primary exists, and the project's own predecessor workspace — which is **in-house analysis, not a public source**, and whose values are labelled cross-checks rather than citations.

**Companion:** `design/05-source-register.md` is the same evidence base with a two-axis rating (**Cite 1–5** / **Adopt 1–5**), a read-depth tag per row, **the claim ledger** that attaches an owner to every number on every slide, and **the gap list** of the seven claims no source at Cite ≥ 3 supports. This file says what the sources *say*; that file says what each is *worth*.
