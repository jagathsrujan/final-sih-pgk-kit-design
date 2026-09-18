# SIH26098 — Idea Submission: draft built from the design register

**What this file is.** A tailored draft assembled from `design/00-design-criteria-register.md`, written to be cut down and re-voiced. It is not the wording to submit — it is the argument, with every number carrying the criterion ID it came from. The existing `SIH26098-template-slides.md` and `SIH26098-form-content.md` give the *structure*; this file gives the *content*.

**Refreshed 2026-09-18** against everything closed since the CAA machine sizing: the machine identity and mass (C34/C36/C40/C41), the kilowatt energy path and its thermal interface (C42, W7/W12, P6's thermal check), the air-gap/preload split (C35, C23), the power budget and the supercapacitor buffer (W1–W4), the ring-mounted IMU (N6/N7/N8), the cost target (K4), the Monte Carlo campaign (R5), the bench-rig specification and its post-selection build gate (R7), and the growth-module decision (X1, X3–X6, X17).

**How to use the criterion IDs.** Every bracketed tag — `[G4]`, `[C12]` — points at a row in the register, where the value's basis, status and sensitivities are recorded. A reviewer who challenges any number can be taken straight to its derivation.

**Status of the numbers.** Four kinds appear, and they must stay distinguishable in the final text:

| Marking | Meaning |
|---|---|
| **Claimed** | A requirement or a design decision we own |
| **Derived** | Computed from the givens; the arithmetic is in the register |
| **PARAMETRIC** | Sized over a declared envelope because the customer's platform data is not yet released — **must be shown as such, never as the customer's data** |
| **[ref]** | Carried from published work on the 155 mm class and still provisional |

---

## Basis and disclosure — read this before writing a single slide

**No technical data from Yantra India Limited has been used.** YIL releases the shell drawing and firing tables after shortlisting, and that is the process. Every platform figure in this submission is therefore drawn from the **public 155 mm HE class** — the M795 and M549A1, their published dimensions and dispersion, the MIL-STD-333B fuze interface, and the fielded M1156 PGK as the kit benchmark. The design is specified **parametrically**: kit mass, CG shift and inertia change are stated as *limits the design satisfies across a declared envelope*, which is how a supplier defines a retrofit kit. Post-selection, every value re-baselines against YIL's actual shell.

**Two platform interactions are declared rather than hidden**, and they are the same move in both cases: the kit states what it depends on instead of engineering around it.

- **Target-location error** is excluded from the headline CEP claim and published as a sensitivity `[M5]` — the design does not get to assume the crew's coordinates are right.
- **The fuze-well thermal interface** — the path the control energy takes into the shell — is a declared interface requirement `[W7, P6]`, because its conductance belongs to the platform's thread geometry, not to the kit. The kit's job is to *specify* it and to design its own side of the joint; measuring it is a rig item `[R7]`.

**Say this on the deck.** It is a strength, not a caveat: a kit specified as limits over an envelope, with its platform dependencies named, is a *product*, and it is the only honest form a bid can take before the drawing is released.

---

## FIELD 1 — Technology bucket

**Defence and Security** — with a manufacturing and low-cost-electronics character.

## FIELD 2 — Idea title (max 100 characters)

**DRISHTI-PGK — A Low-Cost De-Spun Canard Guidance Kit with an Integrated Multi-Mode Fuze**

## FIELD 3 — Abstract

Conventional 155 mm artillery is unguided: a conventional round at maximum range lands with a circular error probable of **267 m** `[M6]` — on a public citation, bracketed by independent values of 259 m and 139 m for the two rounds of the class. Neutralising a point target therefore demands volume fire, and volume fire costs time, logistics and collateral.

DRISHTI-PGK is a retrofit kit that screws into the existing **MIL-STD-333B** fuze well `[P6]` and replaces only the fuze and the ogive forward of it `[P13]`. Four **fixed-incidence canards** sit on a ring that is de-spun from the spinning shell by two bearings `[C1]` — there are no moving control surfaces at all. A 0°/180° steering pair produces a net guidance force; a 90°/−90° control pair produces the roll torque that aims it `[C1]`. The **alternator is simultaneously the actuator and the generator** — a frameless outrunner, 12 slots / 14 poles, ≈79 mm gap diameter, 0.40 mm air gap, 400 V bus, **≈0.9 kg** `[C34, C36, C41, C40]` — so the kit carries **no in-flight battery** `[C20, W4]`. The **multi-mode fuze** shares the same nose volume: proximity, time and impact, set inductively on the gun line, with the time setting re-synchronised in flight so a guided round's airburst follows its actual trajectory `[M2, F1, F11]`.

Guidance is **continuous impact-point prediction** `[G1]`, which the reference work for this airframe does not contain — our clearest novel contribution. Navigation rides on the de-spun ring, which removes 15 000–20 000 rpm of spin from the measurement and turns the hardest sensing problem in a spin-stabilised guided shell into a conventional one `[N6, S6]`.

The claim is **CEP ≤ 30 m at maximum-range, full-charge engagement** `[M4, M5]`. Our derived design point is **CEP 23.9 m** — a **1σ budget of 20.3 m**, a 20 % margin under the claim `[G4]`.

**And the design has already found its own hardest problem, which is not the guidance.** Holding the ring costs **2.92 kW peak and ≈121 kJ per flight** `[C42]` — the price of the de-spun architecture, invisible in the reference bench rig because its body spin was scaled 21.6× down. The energy cannot be stored and barely reaches the airstream, so it **leaves through the shell**: a resistive dump stage conduction-coupled to the fuze-well threads, where 121 kJ raises 45 kg of steel by 5.8 K, subject to a **declared thermal interface ≥ 58 W/K at the peak** `[W7, W12]`. Stating that openly — with the measured first-order estimate of what a 2″-12 UNS thread actually conducts, and the design move that closes the gap `[P6]` — is worth more than leaving it out.

Cost target: **≤ ₹6.5 lakh (≈ US$7,800) per unit at 5,000 kits per year**, published as the fielded price minus 40 % `[K4]`.

---

## FIELD 4 — Idea description

### 1. The problem, stated as a number

A conventional unguided 155 mm round at maximum range has a **circular error probable of 267 m** `[M6]`. Two independent public citations bracket this at **259 m** and **139 m** for the two rounds of the class, illustrating how strongly dispersion depends on range — which is why the claim is tied to a stated engagement condition rather than quoted bare `[M6]`.

The problem is not that artillery is inaccurate; it is that inaccuracy scales with range by the squared-cubed law of trajectory sensitivity, so the longest shots are the least useful and the most dangerous to use close to friendly forces.

**The requirement, and what we claim against it.**

| Element | Statement | ID |
|---|---|---|
| Claim | **CEP ≤ 30 m** | [M4] |
| Condition | Maximum-range, full-charge (6M), ≈30 km class, 39-calibre tube | [M4] |
| Definition | 2-D circular 50 % probability radius; measured against the **loaded aimpoint**, with target-location error **excluded and stated as excluded**; the end-to-end figure against the true target published as a sensitivity | [M5] |
| Charge envelope | Full functionality across **3M–6M, 546–943 m/s**; the accuracy claim is bounded to the band above, outside which accuracy degrades but never below unguided | [M3] |
| Derived design point | **CEP 23.9 m** — a 20 % margin | [G4] |

### 2. What the kit is

**It replaces the fuze, not the shell.** The kit occupies the standard fuze well and the ogive forward of it, and nothing else `[P13]`. Published interface anchors: the **MIL-STD-333B** standardised fuze thread and cavity `[P6]`; a **2″-12 UNS-2A** thread as used by in-service 155 mm fuzes `[P6]`; and the fielded **M1156 PGK**, qualified on both rounds of the class, at **≤124.7 mm intrusion and ≤95.25 mm above the seat** `[P7, P12]`.

**The canard architecture.** Four fixed-incidence canards in two pairs on a de-spun ring `[C1]`:

- **Steering pair, 0°/180°, equal cant** — lateral force components add, roll torques cancel. This is the guidance force `[C1]`.
- **Control pair, 90°/−90°, opposite cant** — lateral components cancel, tangential components add. This is a pure roll torque, and it is the only source of ring torque **against** the body spin, because the alternator is a generator whose reaction torque acts in one sense only `[C1]`.

Rotating the ring aims the guidance force anywhere in the plane. **Two-dimensional steering from a single actuation axis, with no moving surfaces** `[C1]`.

**Canards are permanently exposed** — fixed in flight configuration from manufacture, with no deployment mechanism at all `[C31]`. Nothing can deploy, so nothing can deploy wrongly: in-bore safety is a static clearance question rather than a mechanism-safety argument `[C31]`. This also matches the fielded PGK's four fixed external canards.

**The machine, stated concretely** `[C34, C36, C41]`. A **radial-flux, 3-phase, frameless outrunner**: magnets on the ring, coils on the body. 12 slots / 14 poles; ≈79 mm mid-gap diameter; a 0.40 mm air gap; stack length 25–30 mm; **≈0.81–0.97 kg** — the dominant mass item in the kit `[C40]`. **400 V bus**, `Kt` 0.362 N·m/A rms and `Kv` 0.209 V/(rad/s) line-to-line under the stated convention `[C41, C14, C15]`. Rated **≈3.0 kW**, against the reference machine's 1.2 kW `[C20]`. Electromagnetically feasible: peak current density ≈7.5 A/mm² transient, ≈3 A/mm² holding `[C18]`.

**The machine is a loaded generator, not an idler.** Holding the ring against the aerodynamic torque at full body spin means absorbing `P = Taero × ω_body` — **2.92 kW at launch, ≈121 kJ integrated over the flight** `[C42]`. This is the architecture's defining cost, and it is the price of the guidance authority: the 18.1 N force requirement sets cant ≥ 10°, and cant sets the torque and the dissipation together `[C8, C43]`.

**The power architecture** `[W4, W5, W7, W12]`. A single dump-regulated 400 V bus. The avionics demand ≈**12 W peak / ≈10 W average** (≈0.9 kJ per flight) against ≥240 W generated even at the apogee floor — **≈20:1 at the worst point**, so the design question was never supply, it is routing. The surplus (~115 kJ) goes to an actively controlled resistive **dump stage** (≈0.15–0.30 kg, body-side inside the machine's own axial envelope) thermally bonded to the stator mount and conduction-coupled to the fuze-well threads `[W12]`. A **supercapacitor buffer** (≈150–200 J, ≈50–150 g) carries three duties: the fireset reservoir (≥1 J, isolated, charged only under the arming interlock), ≥2 s of avionics hold-up, and the actuator's motoring bursts `[W4]`. A small **reserve battery** covers the pre-launch safe state only `[W5]`. So the SWaP-C sentence survives intact — **no in-flight battery** — and it is now a *checked* sentence: the energy comes from the alternator, and the buffer carries the fireset, the hold-up and the bursts.

**Multi-mode fuze.** Proximity, time and impact, all configurable before flight, with the full terminal-effect envelope of the fuze it replaces retained — superquick, short delay and graze selectable on impact `[M2]`. The **setting envelope** is fixed, not aspirational `[F1]`: proximity burst height **2–15 m** about a 7 m default, time **0.1–199.9 s** at 0.1 s resolution, impact short delay ≈0.05 s — a **wider mode set than the fielded competitor**, whose fuze offers point-detonate and proximity only. Configured over the class-standard **inductive gun-line setter** `[F11]`. Sensing is **RF Doppler at 24 GHz class** through a nose radome — no optical window anywhere on the kit, so there is no line of sight to foul, obscure or heat `[F2]`.

**The time setting is re-synchronised in flight** from the navigation solution, so the airburst follows a guided round's *actual* time of flight rather than a firing-table prediction — a guided round's flight time is changed by the guidance itself, so a pre-set time would inherit the whole prediction error `[F1]`. The fuze stays **autonomous and safety-critical**: it arms and functions on its own, the correction interface is one-way and bounded, and with no correction it falls back to its pre-set time `[F1]`.

**Safety is mechanical before it is electronic.** The explosive train is interrupted by an **out-of-line rotor** to **MIL-STD-1316**, released only by two independent environment stimuli — **setback and spin** — with the electronics' arm command as a third, independent condition `[F6]`. The rotor cannot complete its travel while setback is sustained, so **no in-bore function is possible by construction rather than by timer**; a misfire leaves the fuze safe with no abort logic to get wrong; and dead electronics give a **dud, never a premature burst** `[F6]`.

**Mass, stated honestly** `[C40, P9, risk 33]`. The machine's ≈0.9 kg is the dominant item, and it moves the net retrofit penalty from the published-benchmark +0.42 kg (0.9 % of the projectile) toward **≈ +0.7–1.0 kg (≈1.6–2.2 %)**, with the CG shift moving from 2.6 mm to **≈6–8 mm forward** (≈0.8 % of projectile length). That is an overweight of roughly 10–20 % on the fielded kit, **not a budget failure**: the shift sits inside the platform's own 0.55–0.62 L CG envelope spread, and mass forward *reduces* the CP–CG separation, which should if anything raise the stability margin — a direction to be confirmed at S1 rather than assumed `[risk 33]`. The axial-flux trade (C44) and make-versus-buy (C45) are the open mass levers.

### 3. Guidance, navigation and control

**Impact-point-prediction guidance law** `[G1]`. Each cycle, propagate the navigation state to impact, compare the predicted impact point with the loaded target coordinates, and command a ring angle that drives the predicted miss to zero. It spends authority in proportion to the miss it can actually remove rather than holding an uploaded path — which matters because the authority margin is **1.11:1**, not comfortable `[M7]`. The reference work for this airframe contains **no guidance law at all**; this is new work.

**The mission data travels on the existing gun-line setter** `[F12]`. IPP needs the target *in the round* — the law propagates to impact and drives the predicted miss to zero, so a mode word is not enough. The inductive setter carries the fuze mode and its parameters `[F1]`, **target coordinates**, met data, charge and muzzle-velocity state, a time reference, and **GNSS ephemeris and keys** — the last of which is also what allows a fast fix under spin `[N3]`. The setter **reads back what it wrote** and the crew gets a go/no-go before the round is loaded, and the uploaded target is **sanity-checked against the firing solution** `[F12]`. The target-location term itself stays **outside** the CEP claim and is published as a sensitivity `[M5]`.

**The ring angle is the only command channel** `[G2]`. Force magnitude cannot be commanded — steering comes from cant angle, so the force is set by cant and dynamic pressure and the ring merely aims it. Two consequences are built in: the propagation model **includes the always-on steering force**, or the error budget's largest term is wrong; and the aerodynamic model stays out of the control loop.

**The authority window is state-dependent, not a fixed schedule** `[G3]`. Dynamic pressure collapses near apogee, so an onboard estimate of available force gates the command and the inhibited band is computed in flight. The reference work lost control between t = 30 s and 50 s using fixed limits; inheriting the state-dependent fix is a concrete, hardware-validated differentiator.

**The de-spun ring is the inertial platform** `[N6, S6]`. With spin removed, the ring sees the projectile's coning motion rather than a **1107–1912 rad/s** rotation — the single hardest sensing problem in this class of projectile, converted into a conventional low-rate navigation problem. The decision is the ring mount **plus the body-side spin channel** the design needs anyway (the limit laws read measured relative speed, and the EMI notch locks to the measured rotation), so it costs no new hardware `[N6]`. The derived specs come with it: ±2,000 °/s and ≥100 Hz bandwidth for the rate channel `[N7]`, and ARW ≤ 1 °/√h with bias instability ≤ 5 °/h for the unit — a tactical/industrial MEMS, generous against the filter's need `[N8]`. That claim now has a number behind it: the navigation line closes bottom-up at **RSS 3.7 m against the 5 m allocation**, and the **2 m** IMU term inside it is only available on the ring `[N1]`.

**The GNSS antenna does not fight the spin — it ignores it** `[N3]`. A rotationally symmetric aperture sits on the spin axis with its elements **combined rather than switched**, so the pattern is invariant under rotation and there is **no modulation at 176.3–304.4 Hz to track out** — only the slow coning motion, which a normal loop absorbs. That keeps a standard receiver in place where the obvious alternative — carrying the aperture on the de-spun ring — is refuted by our own architecture: **the ring angle is the guidance command channel** `[G2]`. The consequence to state honestly is that **fast acquisition is now a requirement rather than a goal** — the fix must complete in the opening seconds, because the guided window opens on nav convergence `[G3]` and is spent against a 1.11:1 authority margin `[M7]`. The setter's pre-loaded ephemeris and keys are what buy that `[F12]`.

**Ring-angle accuracy is the guidance-force direction** `[G6, G5]`: **≤ 1.0° (1σ) absolute, earth-referenced** from a magnetometer fused into the navigation solution, and **≤ 0.8° (1σ) body-relative** from the ring pickoff. Combined in RSS, 1.28° → **9.1 m** of residual miss — which is exactly the ring-angle line in the error budget `[G4]`. The crux is **disturbance rejection, not resolution**: the alternator's stray field scales with current and therefore with flight phase, so calibration must be in-flight. **F15 answers it** — the rotating field appears at **1 234–2 131 Hz** (7 pole pairs × the relative rotation, which the kit measures anyway) and is removed by a **coherent notch locked to that measured frequency**, while the current-proportional part is **compensated against measured coil current** in the calibration model. Both use signals the design already carries for the limit laws, so coexistence costs **no new hardware**. The honest negative is worth stating too: for the magnetometer, shielding cannot help at all, because the interference and the earth's field share the same band *and* the same space `[F15]`.

**Control.** A cascade of **PI inner velocity at 33.6 Hz and P outer position at 6.2 Hz**, both hardware-validated, running at **1 kHz** with the control loop in FPGA fabric and the guidance law on the processor `[G9, G8, G13]`. A **disturbance observer** estimates the unmeasurable aerodynamic and friction torques `[G14]`. **Every limit is state-dependent by construction** — `I_lim = min(2·Î_disturbance, I_avail(ω_rel))` — so authority loss is a designed constraint rather than a failure mode `[G15]`. Guidance updates at **≈6 Hz**, which is a *ceiling* set by the outer loop's 0.103 s settling time, not an arbitrary rate `[G10, G2]`.

**Where the control energy goes** `[C42, W7, W12]`. This is the part of the design the reference work could not have seen, and it is where the architecture earns its keep honestly. The dump stage converts the 121 kJ to heat; the heat is conduction-coupled through the fuze-well threads into the shell, whose 45 kg absorbs it as a 5.8 K rise in the long-time limit `[W7]`. The requirement is therefore an **interface**, not a radiator, and it is declared: **≥ 58 W/K at the 2.92 kW peak, ≥ 20–27 W/K on the flight average** `[W7, P6]`. Two honest refinements belong on the slide. First, the **bare thread does not deliver it** — a first-order estimate of the 2″-12 UNS flank and seat contact gives **≈3–16 W/K (central ≈8)**, short by ~2.5× on the average and ~7× on the peak — so the interface is *designed*: the well bore is used as a deliberate contacting radial path (≈17× the flank area, 19–94 W/K even at poor contact conductance), the flanks and seat are ground and the **torque spec becomes a thermal requirement** (contact conductance rises with preload), and the peak is buffered by the kit's own metal while the interface is sized on the 90 s average `[P6]`. Second, the shell is a **long-time** sink: the thermal penetration depth in steel over a 90 s flight is only ≈30–65 mm, so the flight-time participating mass is the kit plus the shell's nose (≈6–8 kg, ≈25–35 K rise) and the 5.8 K is the asymptote `[P6]`. Neither refinement weakens the claim — both are measurements the rig is specified to take `[R7]`.

### 4. Feasibility — the things that decide it

**(a) The accuracy budget closes with margin.**

| Source | 1σ | Why |
|---|---|---|
| Navigation at impact | **5 m** allocation, **3.7 m derived** | GNSS 3.0 + IMU and filter residual 2.0 + time/lever-arm 1.0, **RSS 3.7 m — a ≈26 % margin**, and conditional on GNSS availability rather than on inertial grade `[N1, G4]` |
| Guidance and control | **17 m** | propagation and model error 13 m, ring angle 9 m, actuation and loop lag 6 m `[G4]` |
| Meteo residual over remaining flight | **5 m** | forecast error only, because the law re-solves continuously `[G4]` |
| Ballistic and aerodynamic model | **8 m** | coefficient uncertainty, carried explicitly `[G4]` |
| Fuze and detonation dispersion | **3 m** | small at this calibre `[G4]` |
| **RSS** | **20.3 m** | **→ CEP 23.9 m**, 20 % under the 30 m claim `[G4]` |

The muzzle-velocity residual is **absorbed into the navigation state** — under continuous impact-point prediction a velocity error already incurred is *measured*, not predicted `[G4]`. The campaign that turns this budget into a result is defined: **≈10,000 full-fidelity flights** — 5,000 at the design condition for a ±2.0 % (95 % confidence) headline, plus five envelope corners — with the **worst corner's 95 % upper bound supporting the claim** and the two model-error terms sampled with a stated correlation rather than assumed independent `[R5]`.

**The navigation line closes from below.** The 5 m allocation was set top-down before anything existed to check it against; the bottom-up budget is **3.7 m — GNSS 3.0, IMU and filter residual 2.0, time and lever-arm 1.0 — a ≈26 % margin** `[N1]`. It is **conditional on GNSS availability, not on inertial grade**: with aiding the IMU supplies attitude and fills gaps, and unaided the same IMU is two orders of magnitude worse than the allocation — 0.1° of attitude error mis-resolving a 5 g drag deceleration is ≈110 m over 50 s — so the outage tolerance is a bounded requirement `[N1, N4]`. And the 2 m IMU term is only available because the IMU rides the **de-spun ring** `[N1, N6]`.

**(b) Authority — the honest version.**

The 80 % capture fraction needs **407 m** of correction `[M7]`. A 20 N force on the 45.0 kg design mass over the 45 s terminal window delivers **450 m** — a margin of **1.11:1** `[M7]`. That is thin, and it is stated as thin. Because the force is not commandable and collapses near apogee, the requirement is really on the **minimum force over the guided window**: **≥ 18.1 N** `[C8]`. That figure sits **above the floor of the reference's own band**, and 15 N would capture only 67 % of the unguided population — so the design cannot inherit the reference canard sizing `[C8]`.

**(c) The torque margins, which are thinner still.**

Ring control is a torque balance, and both ends of the flight are constrained `[C9, C12]`:

- **Near apogee** the aerodynamic torque collapses to **0.1706 N·m** against a friction budget of 0.1 N·m — a **1.7:1** margin `[C12]`.
- **On descent** the aerodynamic torque reaches **2.119 N·m** while the alternator's available current has fallen to ≈5 A, giving an **11 % shortfall in transient authority** at the end of flight `[C9]`.

Combining the two criteria **closes the control-pair sizing window entirely above `Tf = 0.1567 N·m`** — so the friction budget is a **feasibility gate on the architecture**, not a preference `[C12, C13]`. Inside the gate the design has ≈±20 % of freedom on control-pair size `[C12]`. This is why the friction budget is specified as **≤ 0.10 N·m flat across the full speed and temperature envelope**, with flatness — a load-dominated rather than viscous-dominated bearing — as the actual specification `[C13]`. **And the budget is honest about its own provenance:** the reference's 0.1 N·m datum was measured at 83.8 rad/s, **19.4× below flight**, and if its viscous interpretation were a flight law it would fail C10 outright — so the flatness requirement is specified to be correct under either reading, and **the measurement is a test item** `[C13, risk 24, R7]`.

**(d) Structural, in-bore, and the air gap.**

The ring sees **73.5 kN** of setback at 15 000 g `[C26]`. **That load cannot pass through the flight bearings** — thin-section instrument bearings of this class carry static ratings an order of magnitude lower — so the design routes it around them through a dedicated launch load path `[C26]`. The 0.40 mm machine air gap splits that requirement in two `[C35]`: the **axial** case is a stiffness spec on the structural path (**≥ 367 N/µm**, comfortable for machined steel *provided nothing soft — no spring washer, elastomer or compliant potting — sits in the launch path*), and the **radial** case is a bearing stiffness spec (**≥ 122 N/µm on the pair**), which is achievable only with preload — the same knob that sets the friction budget. That tension has one owner and one resolution point: **C23 sets the preload against both** `[C23, C35, C13]`. Permanently exposed canards are held inside the bore by a **2 mm/side clearance budget**, capping the canard tips at **Ø151 mm** `[C31]`.

**(e) Stability.**

First-order gyroscopic stability across the declared envelope runs **Sg = 1.37 to 3.55**, with the design point at **1.83** `[S1]`. The conservative corner clears the customary 1.3 floor by only 5 %, and **that 5 % is the canard allowance** — the derived requirement is that the canards may raise the pitching-moment derivative by no more than **5 % at that corner, 40 % at the design point** `[S1, S2]`. Two useful results fall out: the ring and canards add **+5.4 %** to axial inertia, which *raises* Sg by ≈11 % and partly offsets their own destabilising effect `[P11]`; and because spin is set by the rifling twist, **muzzle stability is charge-independent** — a 3M and a 6M round leave the tube equally stable `[S6]`.

**(f) Energy and thermal — the design's second hard problem, answered.**

| Item | Value | ID |
|---|---|---|
| Generated power (mechanical) | **2.92 kW peak, ≈121 kJ per flight** | [C42] |
| Where it cannot go | storage (≈1.5 F at 400 V — excluded), the kit's own metal (134–179 K rise), the airstream (≈26 % of the integral, 12 % of the peak) | [W7] |
| Where it goes | conduction into the shell through the fuze-well threads — 121 kJ raises 45 kg of steel by **5.8 K** (long-time asymptote; ≈25–35 K on the flight-time participating mass) | [W7, P6] |
| Interface requirement | **≥ 58 W/K at the peak; ≥ 20–27 W/K on the flight average** | [W7, P6] |
| Bare-thread estimate | **≈3–16 W/K (central ≈8)** — the gap is closed by the well bore as a *contacting* path (19–94 W/K), a conductance-specified joint (ground flanks/seat, torque spec as a thermal requirement), and the peak/average split | [P6] |
| Dump stage | ≈0.15–0.30 kg resistive element, body-side, **no nose volume** | [W12] |
| Demand vs generation | ≈12 W peak avionics vs ≥240 W at the apogee floor — **≈20:1**; the surplus is the dump's | [W4] |

**And it cannot be traded away**: the 18.1 N guidance-force requirement sets cant ≥ 10°, and 10° cant is what produces the 2.92 kW `[C8, C43]`. The 121 kJ is the price of the authority the design is built on — which is the sentence to put in front of a reviewer who asks why a guidance kit carries a kilowatt-class thermal load. The trade against a **servo-actuated canard kit, which has no such load at all**, is stated rather than assumed away `[risk 32]`.

**(g) Cost and the retrofit economics.**

The fielded competitor in this product class is a **US$13,541** unit (FY2013, with a sub-US$10,000 objective and foreign-military-sales pricing of US$12.7–20k), and the 2026 production award for the class was **US$863 M** `[K4 benchmark, reference model §7]`. **Our published target: ≤ ₹6.5 lakh (≈ US$7,800) recurring, at 5,000 kits per year sustained** — "the fielded price minus 40 %" `[K4]`. The architecture attacks that from three directions: **one moving assembly**, no actuators, gearboxes or in-flight battery; fuze and guidance sharing processor, power and housing; and **no re-qualification of the shell** — the body, charge system and driving band are untouched `[P13]`. The target's evidence is the ranked-driver costing at that volume `[K5]`, with make-versus-buy `[C45]` and the axial-flux trade `[C44]` as the levers if the bill of materials does not close.

### 5. Validation methodology

1. **7-DOF trajectory simulation with the guidance loop in the loop**, in the body-fixed-plane frame, driven by a Mach × α × β coefficient set — not the reference's five-point Mach table, which produced non-physical jumps.
2. **Monte Carlo dispersion analysis that produces the CEP** — the claim is derived, not asserted `[R5]`: **≈10,000 full-fidelity flights**, 5,000 at the design condition (±2.0 % at 95 % confidence) plus five envelope corners; the model-error terms sampled with a stated correlation; target-location error switched separately (0 / 10 / 25 m); and the claim supported by the worst corner's 95 % upper bound.
3. **Hardware-in-the-loop**, closing ring angle back into flight parameters — the step the reference work never took.
4. **A rotating bench rig — specified now, built if the entry is shortlisted** `[R7]`. The specification is flight-representative, because the rig's job is to close the items argument cannot: **friction at up to ≈2,000 rad/s relative speed** (against the reference's 19.4×-low datum), **the machine as generator at the real 2.92 kW** into the dump and buffer, **closed-loop ring-angle tracking** with the disturbance observer and the state-dependent limits (overshoot ≤ 10 %, never past the guard band — this rig fixes that guard band's provisional value), **magnetometer coexistence at speed**, the **24 GHz spin-modulation test**, the **ring–body power/data interface**, a **setback-representative pulse** on the buffer, and the **fuze-well thermal interface measured in W/K** against the ≥58 / ≥20–27 requirement. The rig is presented as a **plan**, never as an existing asset, and the items it verifies are declared as open verifications rather than demonstrated results.

### 6. Growth module — the bounded option

The kit is designed with a defined mechanical and electrical interface for a future terminal seeker, and the baseline carries none of its mass, power or cost `[X1]`. The option is stated with its bound rather than as a capability: a target-referenced seeker's field of view contains the target only in the descent — the nose points up throughout the ascent — giving a **≈20 s window** `[X3]`, inside which the correctable miss is **≈59 m against M7's 407 m** `[X4, X5]`. So **348 m (85 %) of the correction still depends on GNSS/INS**, and the module narrows the GPS-denied error rather than closing it. The **primary GPS-denied answer is anti-jam GNSS with INS coasting** `[X17]` — the fielded counterpart's own answer, in the same envelope and cost class, and it rides the multi-element spin-axis aperture the design already has `[N3]`, so it costs no new antenna.

---

## SLIDE-READY CONTENT

### Slide 1 — Problem statement

- A conventional 155 mm round at maximum range lands with **CEP 267 m** `[M6]` — bracketed by public values of 259 m and 139 m.
- Neutralising a point target therefore needs volume fire: more rounds, longer engagements, more collateral.
- The requirement is **CEP ≤ 30 m** at maximum-range full charge `[M4]`, defined against the loaded aimpoint with target-location error stated separately `[M5]`.
- YIL manufactures the shell. **The missing capability is the guidance and fuze kit that bolts onto it.**

**Visual:** two impact patterns side by side — the wide unguided ellipse against a tight cluster — with rounds-per-target under each.

### Slide 2 — Proposed solution

- **Fuze-well retrofit** — replaces only the fuze and the ogive forward of it `[P13, P6]`.
- **Four fixed canards on a de-spun ring**, permanently exposed, no deployment mechanism `[C1, C31]`.
- **Steering pair makes the force, control pair aims it** — 2-D steering from one axis, no moving surfaces `[C1]`.
- **A frameless outrunner alternator that is both actuator and generator** — 12 slots / 14 poles, ≈79 mm gap, 400 V bus, ≈0.9 kg `[C34, C36, C41, C40]` — so the kit carries **no in-flight battery** `[W4]`.
- **Multi-mode fuze** — proximity **2–15 m** by **24 GHz RF Doppler**, time **0.1–199.9 s**, impact superquick / short delay / graze, set on the existing gun-line interface and re-synchronised in flight `[M2, F1, F2, F11]`.
- **Safety by construction** — out-of-line rotor on two independent launch stimuli; nothing can function in the bore `[F6]`.
- Mass stated honestly: the kit lands in the **1.4–1.7 kg class**, a net **+0.7–1.0 kg** (≈1.6–2.2 %) over the fuze it replaces, with the axial-flux trade and make-versus-buy as the open levers `[C40, P9, risk 33]`.

**Visual:** exploded kit view plus the canard force/torque diagram.

### Slide 3 — Technical approach

- **Continuous impact-point prediction** — the reference work for this airframe has no guidance law; this is new `[G1]`.
- **Target, met, charge state and GNSS ephemeris ride the existing gun-line setter** — the round computes its own solution in flight, and the setter reads back what it wrote `[F12]`.
- **The de-spun ring is the inertial platform** — 1107–1912 rad/s of spin removed from the measurement, with the body-side spin channel the limit laws already need `[N6]`.
- **The GNSS antenna is spin-invariant by geometry** — a symmetric aperture on the spin axis, combined not switched, so there is no 300 Hz modulation to track out `[N3]`.
- **Ring angle is the only command channel**; force magnitude is set by cant and dynamic pressure `[G2]`.
- **Coexistence is designed, not shielded** — the alternator's field is notched at its measured frequency and compensated against measured current; no new hardware `[F15]`.
- **State-dependent authority gate** — the apogee blackout is computed in flight, not scheduled `[G3]`.
- **Every limit closes the loop on itself**: DOB + state-dependent current and velocity limits, 1 kHz, FPGA/processor split `[G14, G15, G13]`.
- **Derived, not asserted**: RSS 20.3 m → **CEP 23.9 m** `[G4]`.
- **And the architecture's own hardest problem is stated and answered**: the ring costs 2.92 kW / 121 kJ to hold, and the energy leaves through the shell — a declared thermal interface, not a hidden loss `[C42, W7, W12, P6]`.

**Visual:** control block diagram and system layout.

### Slide 4 — Feasibility

| Item | Value | ID |
|---|---|---|
| Error budget RSS | 20.3 m → **CEP 23.9 m** | [G4] |
| Navigation at impact | **3.7 m derived** against a 5 m allocation (≈26 % margin), conditional on GNSS | [N1] |
| Authority margin | **1.11:1** (450 m available vs 407 m required) | [M7] |
| Minimum guidance force | **≥ 18.1 N** over the guided window | [C8] |
| Friction budget | **≤ 0.10 N·m flat**; feasibility gate **0.1567 N·m** | [C13, C12] |
| Stability | **Sg 1.37–3.55**, design point 1.83 | [S1] |
| Setback on the ring | **73.5 kN**, routed around the flight bearings | [C26] |
| Air gap / deflection | 0.40 mm gap → **367 N/µm structural, 122 N/µm bearing** | [C35] |
| Generated energy | **2.92 kW peak, ≈121 kJ** → dumped into the shell through a **≥ 58 W/K** declared interface | [C42, W7, W12, P6] |
| Electrical demand | **≈12 W** against ≥240 W at the worst generation point — **≈20:1** | [W4] |
| Cost | **≤ ₹6.5 lakh (≈US$7,800)** at 5,000/year — the fielded price minus 40 % | [K4] |

**Visual:** error-budget waterfall; canard force vs time with the guided window shaded.

### Slide 5 — Impact

- **CEP ≤ 30 m** `[M4]` turns a point target from a volume-fire problem into a first-round one — **4 rounds against ≈264** for a 90 % defeat probability at 30 m effective radius, on our derived figures `[M8]`.
- **No adjustment fire** — shorter engagements, less exposure, smaller signature.
- **Reduced collateral damage**, which matters operationally and politically.
- **Indigenous, at volume cost** — a published target of **≤ ₹6.5 lakh (≈US$7,800) at 5,000 units/year**, measured against a US$13,541 fielded competitor `[K4]`.
- **No new shell, charge or gun** — the existing stockpile becomes precision-capable `[P13]`.

### Slide 6 — References

Register-sourced: the METU actuation study for this airframe class; the impact-point-prediction guidance literature for dual-spin projectiles with fixed canards; the public M795/M549A1 platform and dispersion record; MIL-STD-333B; the DOT&E PGK report; the M1156 public specification; the SIH26098 problem statement.

---

## Track status — everything on the submission-critical track is now closed

**The submission-critical track holds 38 rows. All 38 are closed: DEFINED or DERIVED, with one hardware item parked by decision.**

Closed since the machine sizing of 2026-09-18, in the order decided:

| Row | ID | What closed |
|---:|---|---|
| 34 | C42 | Generated power — **2.92 kW peak, ≈121 kJ** — is the authority for W7/W12 |
| 35 | C43 | Cant angle buys guidance force **and** dissipation in equal measure — binding on C2/C3 |
| 36 | C40 + C34/C36 | The machine, concretely: frameless outrunner, 12 slots / 14 poles, ≈79 mm gap, **≈0.81–0.97 kg** |
| 37 | C35 | The air gap splits into a **367 N/µm structural** case and a **122 N/µm bearing** case |
| 38 | W12 | The dump stage: element mass, body-side location, **no nose volume** |
| 26 | N6 | **The IMU rides the de-spun ring** with the body-side spin channel (N7/N8 derived; N1's 2.0 m term back-filled) |
| 27 | W4 | **The demand never binds**: ≈12 W against 2.92 kW — ≈20:1 — and the surplus is routed to the dump; a supercapacitor buffer carries the fireset, hold-up and bursts |
| 29 | K4 | **≤ ₹6.5 lakh (≈US$7,800) at 5,000/year** — the fielded price minus 40 % |
| 30 | R5 | The **≈10,000-flight Monte Carlo**, with the worst-corner 95 % upper bound carrying the claim |
| 31 | R7 | The **bench-rig specification** — flight-representative, full-capability — **built only if shortlisted (P7)** |

Plus the two carry-ins from the previous session's findings: **P6 is now a thermal criterion** (the bare 2″-12 UNS thread delivers ≈3–16 W/K against the ≥58 W/K peak requirement, and the closing route is stated on the row), and the **C35 ↔ C13 preload tension has an owner (C23)**.

**What remains is not submission work.** 86 of the register's 178 criteria are still open, but none of them changes what the deck may claim — they are the P1b/P2/P3/P4 build-out (sub-system selections, qualification detail, budgets, simulation). The one thing the P5 writer must carry carefully is the **list of declared open verifications**:

- **Friction flatness at flight speed** (C25, and with it the C23 preload trade) — closed by test on the rig `[risk 24]`, not by argument.
- **The fuze-well thermal interface conductance** — measured on a representative joint `[P6, R7]`.
- **Coexistence and spin-modulation at speed** — F15 and F2/F3 verified on the rig.
- **The ring–body power/data interface and the buffer's launch survival** — risks 34 and 35.
- **Everything PARAMETRIC re-baselines at P6** against YIL's drawing and firing tables `[risk 20]`.

The submission says all of this plainly. A bid that names what it has not yet measured, and states how it will, is a stronger bid than one that presents an estimate as a result — and it is the same discipline the register itself is written to.
