# SIH26098 — Idea Presentation Format (6-slide template)

Content laid out for the SIH *Idea Presentation Format* PDF that must be uploaded with the submission. The portal caps this at **10 MB, PDF format**.

**Structure:** 1 Problem Statement · 2 Proposed Solution · 3 Technical Approach · 4 Feasibility Analysis · 5 Impact Assessment · 6 References

**Style rules SIH gives:** prefer points and diagrams over paragraphs, and keep to six slides. Each slide below carries the bullet text plus a note on the visual it needs — the diagrams do most of the scoring work on this sheet, so budget real effort for them.

---

## SLIDE 1 — Problem Statement

**Title:** 155 mm Artillery Is Unguided — and That Costs More Than Accuracy

**Header line (fix the bucket conflict here):** Problem Statement SIH26098 · Ministry of Defence / Yantra India Limited · **Category: Hardware.** *The technology bucket must be one value only — the drafts currently carry "Smart Vehicles" in one place and "Defence and Security" in another, and the analyst dataset a third. Pick one before the slide is laid out; the judge dossier calls this the #1 slide-1 trap.*

- Conventional 155 mm shells follow ballistic trajectories, and **dispersion scales with range.** The fielded record for the class: **94 / 125 / 150 m CEP at intermediate ranges rising to 267 m at maximum range** on a conventional M549A1 — against **30 m at every range** once a guidance kit is fitted.
- Neutralising a point target therefore needs volume fire: many rounds, long engagement time, and unavoidable collateral damage.
- The inefficiency compounds — adjustment fire requires observation and re-engagement, exposing the firing battery and revealing intent.
- YIL already manufactures the mechanical hardware of the 155 mm shell. **The missing capability is a guidance and fuze kit that bolts onto it.**
- The requirement: **CEP ≤ 30 m**, compatible with the existing shell, surviving launch and flight, at low Size, Weight, Power and Cost.

**Visual:** Two impact patterns side by side on a range map — the wide unguided dispersion ellipse versus a tight 30 m guided cluster, with rounds-per-target shown under each. Underneath, a small **dispersion-versus-range curve** plotting the four fielded conventional points against the flat 30 m guided line: dispersion growing with range *is* the argument, and one curve makes it in less space than the sentence does.

**Note on sourcing.** The four-point dispersion figures and the flat 30 m line are the **fielded programme's own published numbers** (Orbital ATK, NDIA 2015). Using them is stronger than quoting our single 267 m anchor, because they are checkable by the panel without leaving the room.

---

## SLIDE 2 — Proposed Solution

**Title:** DRISHTI-PGK — A De-Spun Canard Guidance Kit with an Integrated Multi-Mode Fuze

- **A fuze-well-mounted kit** that replaces only the fuze and forward ogive. The shell body, charge system and gun interface are untouched.
- **Four fixed canards on a de-spun ring**, isolated from the spinning shell by two bearings. No control surface moves.
- **Canard split:** a 0°/180° steering pair with equal cant produces a net guidance force with zero roll torque; a 90°/−90° control pair with opposite cant produces zero net force and a net roll torque. Rotating the ring aims the guidance force anywhere in the plane — **two-dimensional steering from one actuation axis**.
- **The alternator is the actuator.** Magnets on the ring, coils on the body: drawing current produces control torque; not drawing current generates power. No servos, no gearboxes, one moving assembly.
- **Multi-mode electronic fuze** — proximity, time and impact — sharing the nose with the guidance electronics and configured over the gun line's existing inductive fuze setter.

**Say this before the panel asks it — the architecture is the fielded one.** *"The de-spun canard assembly with fixed canards, no mechanical actuators, one moving part and self-generating power in flight is the **published specification of the M1156 Precision Guidance Kit** — the system this problem statement asks India to indigenise. Those are our design targets, not our inventions. What we contribute is the sizing, the thermal path and the sensing, and we will be specific about each."* Naming it converts the single largest trap on this slide into evidence that the homework was done.

**Two lines that must be stated precisely, because a specialist will check them:**

- **Power.** *"Flight power is self-generated — the alternator supplies the kit in flight, so no battery is required for flight. A reserve battery covers pre-launch and the safe state only, and a supercapacitor buffer carries hold-up and the actuator's motoring bursts."* **Do not claim battery-free parity with the fielded kit** — it is documented as *"no battery"* outright, and ours carries a reserve cell. State our version, and the reason: the reserve battery is what makes the arming path independent of the alternator.
- **The architecture's cost, stated by us first.** Holding the ring against the spinning shell costs **2.92 kW peak and ≈121 kJ per flight**, which leaves the kit through a declared thermal interface into the shell rather than a hidden loss. A servo-actuated canard design carries no such load — and it also carries actuators, gearboxes and a battery. Stating our hardest problem and its price is worth more than leaving it for the panel to find.

**Visual:** Exploded/annotated view of the kit — fuze module at the tip, canard ring on its bearings, alternator, GNC and power modules — plus the inset canard-force diagram showing the steering pair (net force) and control pair (net torque). If the exploded view can also show the **thermal path out through the fuze-well threads**, it does the work of the second line above.

---

## SLIDE 3 — Technical Approach

**Title:** Impact-Point-Prediction Guidance, Spin-Free Navigation, Adaptive Control

**Guidance and navigation**
- **Impact-point-prediction guidance law:** propagate the navigation state to predicted impact, compute the miss against the loaded target coordinates, and command a ring angle that nulls it. Recomputed continuously. **Credit it:** impact-point-prediction guidance for a dual-spin projectile with fixed canards is established in the published literature — say so, and claim only the **state-dependent authority gate** that makes the apogee collapse a designed constraint rather than a failure mode.
- **De-spun ring as the inertial platform.** With spin removed, the ring sees the projectile's coning motion rather than a 15,000–20,000 rpm rotation. This converts the hardest sensing problem in a spin-stabilised guided shell into a conventional low-rate navigation problem. **State it as a trade, not a triumph:** the fielded kit determines its roll angle from GNSS and carries **no inertial sensors at all**, so our IMU is a cost and complexity addition — justified because a kit entering service in this decade must not assume GNSS is always available.
- **Ring-angle sensing** defines the direction of the guidance force: a magnetic/inductive pickoff for the body-relative angle used by the control loop, and a magnetometer for the earth-referenced angle used by guidance.
- **Fusion:** GNSS + IMU + barometric altitude, with graceful degradation to inertial coasting under GNSS denial.
- **The GNSS-denied answer, and why it is on this slide:** the fielded programme is already fielding **anti-jam** as a mid-life upgrade, with production started in 2026 and first deliveries expected in early 2028, and its long-range variant is specified to *"operate in a near-peer GPS threat environment."* By the time a kit we design could enter service, **GNSS-denied operation is table stakes rather than a feature.** Our answer is anti-jam GNSS with INS coasting, riding the same spin-axis aperture — and the IMU above is what pays for it.

**Flight control**
- Cascade loop: **PI inner velocity, P outer position**, inner loop designed to settle ≥5× faster than the outer.
- **Disturbance observer** estimates the unmeasurable aerodynamic and friction torques and feeds them forward.
- **State-dependent saturation limits.** The aerodynamic torque varies by more than an order of magnitude over the flight and the alternator's available current falls with relative speed. Fixed limits lose control authority near apogee, so current and velocity limits are scaled continuously to the observed disturbance — authority loss becomes a designed constraint, not a failure mode.
- **1 kHz control loop** with clamping anti-windup.
- **Stability, including the mode the literature names.** Gyroscopic stability is held across the launch envelope with a stated margin. The **roll–coning resonance** that the fixed-canard dual-spin literature documents is a separate, angular-motion effect and is dispositioned rather than assumed away — and the disposition is the design's own configuration: a **span-capped canard with cant angle as the force lever**, which is exactly the span-reduction-and-deflection-increase fix that the 2026 resonance study proposes to raise the natural frequency clear of the canard disturbance.

**Fuze and power**
- Out-of-line safe-and-arm unit with **dual environmental interlocks (setback + spin)** — cannot arm in storage, handling, bore or ramming. **And its complement, which belongs in the same breath:** the kit's electro-explosive devices are qualified against ordnance electromagnetic hazards and ESD, so nothing can *make* the fuze initiate from outside either.
- Reserve battery for pre-launch and safe state; **alternator takes over in flight**; control energy managed by an active dissipation stage.
- **The predicted-miss question, answered in one line.** ⟨**DECISION REQUIRED — register criterion F16, see §6.5 of the form content.**⟩ The kit computes a predicted impact point continuously and holds the loaded target, so it can decide whether to detonate on a predicted miss; the fielded kit does exactly that, at a 150 m radius, so a battery can call precision fires near its own position. **State the chosen position — adopt the threshold, decline it with a reason, or log-and-report without withholding function — and state it here, on this slide.** A fuze-safety reviewer asks this within two questions and has no patience for a third.

**Visual:** Two panels — a control block diagram (guidance law → ring angle command → cascade PI/P → alternator current → plant, with the disturbance observer and adaptive limits drawn in), and a system layout showing sensor, actuator and power blocks. If the layout can carry the **fuze-safety chain — two independent stimuli, out-of-line rotor, no in-bore function** — as a small inset, it pre-empts the safety question before it is asked.

---

## SLIDE 4 — Feasibility Analysis

**Title:** The CEP Budget Closes, and the Hardware Concept Is Already Proven

**Accuracy closes on paper — the current budget**

| Error source | 1σ allocation |
|---|---|
| Navigation (GNSS/INS) at impact | 5 m — allocation; **3.7 m derived** (GNSS 3.0 + IMU/filter 2.0 + time/lever-arm 1.0), ≈26 % margin, conditional on GNSS |
| Guidance and control | 17 m — propagation 13, ring angle 9, actuation 6 |
| Meteorological and muzzle-velocity residual | 5 m |
| Remaining aerodynamic / model uncertainty | 8 m |
| Fuze and detonation dispersion | 3 m |
| **Root-sum-square** | **20.3 m** |
| **Implied CEP (1.1774 σ)** | **≈ 23.9 m** |

*The budget published an earlier split of nav 5 / guidance 15 / meteo 10 / aero 8 / fuze 3 (RSS 20.4 → CEP 24). That version is superseded: the guidance term now carries the dominant error it actually owns, and the meteo residual shrank because continuous impact-point prediction uses the forecast over the remaining flight rather than the whole trajectory. **Any slide still showing 20.4 / 24 is stale.** The two model-error terms (13 m and 8 m) overlap and are sampled with a stated correlation in the Monte Carlo rather than independently.*

**Guidance authority is not the limit**
- Canard force holds a ≈15–25 N band through mid-flight (±85 N in the launch transient, ≈0 at apogee). Minimum over the guided window: **≥ 18.1 N**.
- **Authority margin 1.11:1** — 450 m available against 407 m required to capture 80 % of the unguided population. Stated as a margin, not as comfort.
- **The binding constraints are navigation quality and impact-point-prediction accuracy, not canard force.** The design effort is placed accordingly.

**Technical feasibility**
- The de-spun-ring-with-alternator actuation concept, its torque-authority criteria and its control architecture have been **validated on hardware for the 155 mm class** in published research — including the low-torque near-apogee region where fixed control limits fail — and a **motor-generator test bench built specifically to emulate a fixed-canard dual-spin projectile** is published, which is the same architecture as our own rig.
- Aerodynamic coefficients: published 155 mm body data plus canard data, with CFD to fill gaps and verify canard interference. Coefficient uncertainty is carried explicitly into the Monte Carlo so its CEP contribution is quantified rather than assumed. **This is the acknowledged long pole**, and saying so is stronger than implying it is closed.

**Standards the kit is designed to** — name them, because "the applicable defence standards" reads as evasion: **MIL-STD-1316** (fuze safety design), **MIL-STD-331C** (fuze environmental and performance testing), **MIL-STD-810F** (environmental), **MIL-STD-461** (EMC), **AOP-22** (inductive setting of large-calibre fuzes), **STANAG 4369 / AOP-39** (fuze design and safety), **STANAG 4439** (insensitive munitions), **STANAG 9216 / MIL-STD-333B** (fuze interface).

**Validation methodology**
- 7-DOF trajectory simulation with the guidance loop in the loop, in a body-fixed-plane frame.
- **Monte Carlo dispersion analysis produces the CEP** — the claim is derived, not asserted — varying muzzle velocity, meteo, target location error, launch perturbation and coefficient uncertainty. Two tiers: 5,000 runs at the design condition and 1,000 at each of five envelope corners, with the **worst corner's 95 % upper bound** supporting the claim rather than the design-point estimate.
- Hardware-in-the-loop, closing ring angle back into flight parameters.
- Rotating dynamometer bench rig emulating aerodynamic torque and body spin, with a programmable load — **built only if the entry is shortlisted**, and presented here as a plan rather than as an asset.

**Cost and manufacturability**
- One moving assembly. No actuators, gearboxes, linkage electronics.
- Fuze and guidance share a processor, power supply and housing.
- Existing shell body, charge system and driving band unchanged — **no re-qualification of the shell**.
- **Range retention is a stated requirement, not an unexamined consequence:** the kit is specified to retain **better than 90 %** of the conventional round's maximum range, which is the figure the fielded kit publishes and which puts a price on the canards' drag and the kit's mass.
- **Mass, stated both ways.** Total mass is 1.0–1.21× the fielded kit's; the **net penalty over the fuze replaced is 1.55–2.2×** its +0.45 kg. The second ratio is the honest one to lead with.
- **Processes are chosen at a stated volume — 5,000 kits/year — and split into two tiers.** The production tier is mature: the ring and canards machined as **one datum structure** (cant angle *is* the guidance force, so it is held by the tooling, not by an assembly stack, and the 74 kN setback passes through continuous metal, not fasteners); a stator core traded between 0.1–0.2 mm laminations and a compacted soft-magnetic core on published **loss *and* strength** data; a conventional concentrated winding — at the machine's 2,130 Hz the copper skin depth is ≈1.4 mm, so printed copper is *not* needed on loss grounds; **grain-boundary-diffusion magnets**, buying the coercivity with heavy rare earth only at the grain boundaries; a **manufactured** fuze-well thermal joint (compliant contact + indium foil + cold-sprayed copper at 98 % IACS / 368 W/mK as-sprayed); an aluminium-nitride thick-film dump package; MIM for small fuze parts; and a **laser-direct-structured spin-axis aperture that is structure rather than an added antenna**.
- **The novel processes are declared, not implied.** Printed-copper windings, hybrid printed end-windings and additively manufactured iron cores are development and first-article tools, bounded by published numbers (79 % slot fill and 87 % IACS after heat treatment; ≈⅓ of the winding-head height removed in the hybrid) — **and their qualification cost is not hidden inside the recurring unit cost.** At this volume the governing process question is **tooling amortisation**, which is why every production process above needs no new tooling or a die shared across a part family.
- **The complex low-volume parts are built in a digital cell, not on a fixed line.** Robotic metal and polymer printing; the post-treatment chain that makes printed parts fit for gun launch — **HIP for porosity, heat treatment for residual stress, machining of bearing seats and sealing faces, surface finishing** — and automated placement and assembly, with a build record per part. Qualification follows the established shape — process control, coupons, testing, traceability — on the **defence certification route** (DoDI 5000.93's AM policy; the ASTM / UK-MoD *criticality-based* guide), not the spaceflight standard alone. **Boundary stated with it:** printed parts are non-primary structure and electronics carriers; the primary launch path stays conventional.
- **And the cell is why the design can keep improving.** **The printed parts carry no tooling**, so the post-selection re-baseline against YIL's drawings changes *their* geometry without a die programme, and a variant — another shell, a growth module — is a file, not a die. The conventional tier keeps its dies and its suppliers, which is what the two-tier split is for.
- **Modular sensor stack, targeted redundancy.** One module standard for every sensing channel; a second inertial and magnetic channel and a second, different-physics ring-angle pickoff add **≈5–15 g and under 0.5 W — about 1 % of the kit's mass** — affordable *because* printed structural electronics (components placed during the build, conductors printed to them) removes the connectors and boards that would otherwise host them. **And the principle is demonstrated, not proposed: printed conformal structural supports for circuit boards have been shown viable for gun-launch high-G survivability** — the residual is project-specific qualification. **Bounds:** the cell prints structure and signals, not power; the explosive train stays in the licensed, segregated line; and printing changes the shape of qualification, it does not remove it.
- Cost drivers are the machine, power electronics, bearings, fuze stack, navigation, dump and buffer, and housing — all conventional and volume-reducible.

**Visual:** The error budget as a waterfall or bar chart showing each contribution to the 20.3 m RSS, plus a small chart of available canard force versus time with the guided window shaded. The waterfall should mark the 13 m propagation term as the largest single bar — pointing at the problem is better than looking like we have not noticed it.

---

## SLIDE 5 — Impact Assessment

**Title:** First-Round Precision at Volume Cost, Built on Existing Indian Hardware

> **Why this slide is shaped like a business case.** The SIH 2026 guidelines state that *"if it has a business potential more weightage will be given."* So this slide answers **volume, unit economics, the production line, indigenous content and who pays** — and puts the capability claim second, not first.

**The business proposition**

- **What is being sold:** a kit that converts an existing 155 mm shell stockpile into a precision capability **without a new shell, new charge system or new gun**. The customer's capital equipment and logistics chain are unchanged.
- **Volume and price.** Target **≤ ₹6.5 lakh (≈ US$7,800) recurring unit cost at 5,000 kits per year sustained** — anchored to the fielded competitor's public **US$13,541** unit price, i.e. approximately the fielded price minus 40 %. Development and one-time tooling are excluded, so the number is comparable with a competitor's recurring price.
- **State the volume gap honestly, because the panel will see it.** The fielded programme has produced **over 100,000 units**; 5,000/year is two orders of magnitude below that. The volume assumption is therefore stated and its basis given (a sustained precision uptake within national consumption — the share is YIL's to confirm post-selection), **not left as an unexplained number**. The ranked cost drivers at that volume — machine, power electronics, bearings, fuze stack, navigation, dump and buffer, housing — are the evidence the target rests on.
- **Who pays, and why they would.** The buyer is the same organisation that already buys the shell: the kit is a consumable-class addition to an existing round, procured through the existing channel, **at a unit cost an order of magnitude below a guided projectile** and without a new platform, training burden or supply chain.
- **Indigenous content, made specific.** Manufacture sits on YIL's core competency — precision mechanical work: an integrally machined ring and canards, a compacted or laminated stator core, conventional winding, MIM fuze parts, a machined or cast housing. The bounded additions are the electronics, the magnets and the thermal joint — and the magnet's coercivity is bought through **grain-boundary diffusion**, which places heavy rare earth only at the grain boundaries, so the kit's most critical-element-intensive item is specified with *less* of the critical element rather than more.

**The operational payoff, quantified against the fielded record**

- **CEP ≤ 30 m** means first-round effects on point targets. The fielded programme's own published value proposition is the checkable anchor: **301 projectiles → 77** for the same effect (**74 % reduction**), and **959 → 208** charges. A competing fielded kit claims **up to 90 %** reduction in ammunition expenditure. **Our derived figure sits beside these, not instead of them**, and the scenario difference is stated rather than glossed.
- **No adjustment fire.** Shorter engagements, less exposure, smaller signature.
- **Reduced collateral damage** — operationally, politically and legally relevant.
- Rounds not fired are logistics not moved: a direct reduction in ammunition consumption and supply-chain burden.

**Future progression**

- Modular backbone allows subsequent anti-jam GNSS, an improved seeker or a different fuze module without redesigning the kit. **Anti-jam is not a hypothetical future option** — the fielded programme is fielding it now, so the growth path is alignment with a known direction rather than speculation.
- The same architecture extends to other calibres and to spin-stabilised rocket projectiles.

**Visual:** A three-block slide. **Left:** the unit-economics bar — our target against the fielded US$13,541, with the ranked cost drivers stacked underneath. **Centre:** before/after rounds-per-target, showing our derived figure and the fielded 301→77 anchor side by side. **Right:** the production-line and supply picture — what YIL already makes, what is added, what is unchanged. The capability claim stays to the bullet text; the slide's visual weight goes to the business case.

---

## SLIDE 6 — References

**Set in two columns; keep each entry to one line where possible. The list is deliberately built from the design's own lineage as well as its sources — crediting the prior art is part of the argument, not a concession.**

**Fielded systems and programmes**
1. Orbital ATK, *Precision Guidance Kit (PGK) Program Update*, NDIA Armament Systems Forum, 2015.
2. *M1156 Precision Guidance Kit* — public programme record, US Army PM Combat Ammunition Systems.
3. Elbit Systems, *Silver Bullet II* product brochure, 2026.
4. US Army DOT&E, *Precision Guidance Kit (PGK)*, FY2015 Annual Report.
5. Indian Army RFI — indigenous 155 mm electronic fuzes (three categories).

**Airframe, guidance and stability**
6. G. Günay, *Controller Design and Implementation for a Guidance Kit Used at Spinning Rockets and Projectiles*, M.Sc. thesis, Middle East Technical University, 2022.
7. X. Zhang, X. Yao and Q. Zheng, "Impact point prediction guidance based on iterative process for dual-spin projectile with fixed canards," *Chinese Journal of Aeronautics* 32(8), 2019.
8. J. Norris, A. Hameed, J. Economou et al., "A review of dual-spin projectile stability," *Defence Technology* 16(1), 2020.
9. R. Jaiswal, M. Kothari and A. Abhishek, "Design and aerodynamic characterization of canard guided fuze for dual-spin artillery projectiles," AIAA 2024-1105.
10. P. Wernert and S. Theodoulis, "Modelling and stability analysis for a class of 155 mm spin-stabilized projectiles with course correction fuze," AIAA Atmospheric Flight Mechanics Conference, 2013.
11. L. Wang, Z. Wang and Z. Yu, "Influence of control strategy on stability of dual-spin projectiles with fixed canards," *Defence Technology* 14(6), 2018.
12. "Investigation of flight stability for fixed canard dual-spin projectile," *Defence Technology*, 2025.
13. H. Guo, Z. Peng, W. Liu et al., "Resonance mechanism and aerodynamic optimization of a canard-type two-dimensional trajectory correction projectile," *Acta Armamentarii*, 2026.
14. G. Clancy, T. Bybee and D. Friedrich, "Fixed canard 2-D guidance of artillery projectiles," US Patent 6,981,672, 2006.

**Environment, thermal and safety**
15. A. K. J. Hasselström and U. E. Nilsson, *Thermal Contact Conductance in Bolted Joints*, Chalmers University of Technology / RUAG Space, 2012.
16. Naval Surface Warfare Center Indian Head Division, "High Shock Modeling of Fuze Components," 64th NDIA Fuze Conference, 2021.
17. "Establishment of the damage tolerance criterion of projectile-borne electronics under in-bore launch," *Defence Technology*, 2026.

**Standards**
18. NATO **AOP-22**, *Design Criteria and Test Methods for Inductive Setting of Large Calibre Projectile Fuzes*, Ed. B Ver. 1, 2018 (supporting STANAG 4369 / AOP-4369).
19. MIL-STD-1316 · MIL-STD-331C · MIL-STD-810F · MIL-STD-461 · STANAG 4439 · STANAG 9216 / MIL-STD-333B.
20. Problem statement SIH26098, Ministry of Defence / Yantra India Limited, Smart India Hackathon 2026.

**Note for whoever lays this out:** entries 6–14 are **work this design builds on**, not work it competes with, and they should read that way. A reference slide that lists the prior art it credits is strictly stronger than one that lists only what it borrowed a number from — and it is the same discipline that keeps `[criterion]` tags off the deck. **Do not carry the register's bracketed criterion IDs onto the slide; they belong in the register, and the dossier flags them as an AI-tell.**

---

## To generate the PDF

The portal's own template file is the exact layout to match. Download it from the form ("Download Template") and drop it in this folder — the six slides above then get laid out into it directly.
