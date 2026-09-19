# DRISHTI-PGK — Rated Source Register

**Problem statement:** SIH26098 — *Development of a Low-Cost Precision Guidance and Smart Electronic Fuze System for a 155 mm Artillery Shell*
**Purpose of this file:** every external source the project leans on or could lean on, rated on **how hard we may cite it** and **how much it should change the design** — with the change written down. The companion file is `submission/SIH26098-verified-source-audit.md`, which records *what each source says*. This file records *what each source is worth*.

**Relationship to the audit.** The audit (2026-09-19) fetched and read 13 sources and produced the ✅⚠️❌➕ verdict ledger. Its verdicts are carried here unchanged and extended. It found four things that change what the deck may claim; this register adds three more, one of which **reverses a claim the audit had marked as ours**.

---

## 1. The rating scheme

**Cite (1–5)** — how hard the submission may lean on the source.

| | Meaning |
|---|---|
| **5** | Carries a **headline number** on a scored slide (1 or 5), or is an authority we are measured against |
| **4** | In-text support for a claim a judge will test |
| **3** | Reference-slide entry, or background that shapes framing |
| **2** | Read and understood, but **not cited** |
| **1** | **Do not cite** — unretrievable, vendor marketing, or too weak to carry a claim |

**Adopt (1–5)** — how much the register or design changes because of it.

| | Meaning |
|---|---|
| **5** | **Creates or corrects a criterion, risk or decision** — a register row must change |
| **4** | Changes a value, a budget, a margin, or a criterion's stated basis |
| **3** | Confirms a basis already in use — the row gains a citation, no value moves |
| **2** | Worth a risk-register or decision-log note |
| **1** | No design consequence |

**Read depth** — `full` · `partial` · `abstract` · `indexed` · `✗` (not retrievable). Recorded honestly per row.

**The four rules.**
1. **Nothing may be cited at Cite ≥ 4 on an abstract-only read** unless the abstract itself states the number being cited. Everything else is provisional (`†`) until the full text is read.
2. **Cite and Adopt are independent.** A source can be worth citing hard and changing nothing; a source can change a criterion and never appear on the slide.
3. **Every row with Adopt ≥ 4 must produce a visible change** in the criteria register, the risk register or the decision log. An orphan rating is a defect.
4. **A source found to be wrong is still a source.** Its row is kept, marked with what it defeated, so no later session re-imports it.

---

## 2. The sources

### A — Fielded systems and programmes

| # | Source | Cite | Adopt | Read | What it moves |
|---|---|---|---|---|---|
| A1 | Orbital ATK, *Precision Guidance Kit (PGK) Program Update*, NDIA Armament Systems Forum 2015 ([pdf](https://ndia.dtic.mil/wp-content/uploads/2015/armament/wed17409_Hunter.pdf)) | 5 | 4 | full | **Slide 1's four-point dispersion evidence** (94 / 125 / 150 / 267 m CEP conventional vs 30 m with PGK); the **301→77 rounds / 74 %** impact anchor for slide 5; the **>90 % range-retention** requirement that becomes M10; corroborates M6's 267 m; and the "no mechanical actuators / one moving part / no battery / de-spun canard assembly" list that **retires our novelty claim** |
| A2 | M1156 PGK — [Wikipedia](https://en.wikipedia.org/wiki/M1156_precision_guidance_kit) + [US Army PM CAS](https://www.cpeae.army.mil/Project-Offices/PM-CAS/Organizations/Precision-Fires-Mortars/Products/PGK/) | 4 | 3 | full | Mass 1.4 kg / net +0.45 kg; intrusion ≤124.7 mm, visible ≤95.25 mm; modes PD + HOB; **the dud-on-miss failsafe** (F16); **sub-10 m median demonstrated accuracy** — the "never claim accuracy superiority" guard |
| A3 | Northrop Grumman PGK E5 / Long Range PGK + production coverage | 4 | 3 | indexed | **GNSS-denied is table stakes**: E5 anti-jam production September 2026, first deliveries early 2028; M1156E2/A1 10 m at 30–40 km; LR-PGK 70 km for a near-peer GPS threat. Justifies N6's IMU as a trade, not a triumph |
| A4 | Elbit *Silver Bullet II* brochure 2026 ([pdf](https://www.elbitsystems.com/sites/default/files/2026-06/silver_bullet_ii_2026_7_web.pdf)) | 5 | 4 | full | **Mode-set parity**: PD + PDD + AB — so "wider mode set" is true only against the US kit. **Adaptive canards** (a genuine architectural contrast that favours us). CEP 20 m; GNSS-degraded guidance; "up to 90 %" expenditure reduction; **MIL-STD-810F / MIL-STD-331C**; a firing computer that uploads mission data — so F12's setter package is **fielded practice, not an invention** |
| A5 | IAI TopGun | 1 | 1 | ✗ | **Do not cite.** Bot-protected, only a search-indexed description; the manufacturer-stated 20 m CEP is unverified |
| A6 | US Army DOT&E, *Precision Guidance Kit (PGK)*, FY2015 | 3 | 2 | abstract | Threshold 50 m / objective 30 m CEP — the requirement pair behind M4 |
| A7 | DRDO 155 mm guided projectile (Aero India 2025); Army ADITI-4 terminally-guided munition | 3 | 2 | indexed | The funded national alternative. Shapes slide 5's "why this kit and not a seeker" |
| A8 | Indian Army RFI — indigenous 155 mm electronic fuzes, three categories | 4 | 3 | full | **Our F1 mode set maps 1:1 onto a live, named requirement** — the strongest single framing sentence available for the fuze half of the project |

### B — Reference architecture, airframe and stability

| # | Source | Cite | Adopt | Read | What it moves |
|---|---|---|---|---|---|
| B1 | Günay, *Controller Design and Implementation for a Guidance Kit Used at Spinning Rockets and Projectiles*, M.Sc. thesis, METU 2022 (full text extracted at `notes/01-thesis-full-text-extracted.txt`) | 5 | 5 | full | The reference architecture. Source of every `[ref]` value in the register: the de-spun ring with the alternator as actuator, the cascade PI/P loop, the DOB, the fixed-limit loss of control between 30 s and 50 s (→ G15), the 83.8 rad/s rig datum (→ risk 24) |
| B2 | Zhang, Yao & Zheng, *Impact point prediction guidance based on iterative process for dual-spin projectile with fixed canards*, Chinese Journal of Aeronautics 32(8), 2019 | 4 | 4 | abstract | **The IPP law is published prior art for this airframe.** `draft-from-register.md:216` still calls it "new" — ❌ |
| B3 | Jaiswal, Kothari & Abhishek, *Design and Aerodynamic Characterization of Canard Guided Fuze for Dual-Spin Artillery Projectiles*, AIAA 2024-1105 | 4 | 4 | abstract | Closest published relative of our CAA: four fixed canards at **4°**, two rolling + two lifting, and a **minimum design torque of 0.8 N·m** for a 155 mm projectile. Independently validates the two-pair split; the 0.8 N·m figure needs a written distinction against our 0.17–2.12 N·m aerodynamic envelope |
| B4 | *Investigation of flight stability for fixed canard dual-spin projectile*, **Defence Technology 2025** | 4 | 5 | abstract | CFD+RBD virtual flight, and it **"reproduces the characteristic resonance instability"** — a named failure mode of our own architecture that the register does not currently name |
| B5 | Guo, Peng, Liu et al., *Resonance Mechanism and Aerodynamic Optimization of a Canard-Type Two-Dimensional Trajectory Correction Projectile in the Uncontrolled Flight Phase*, **Acta Armamentarii (兵工学报) 2026**, DOI 10.12382/bgxb.2026.0534 | 4 | 5 | partial | **The single most corroborating paper found.** Complex-angle-of-attack theory shows canard disturbance resonating with the projectile's natural frequency; the proposed fix is **reduce canard span and increase deflection angle**, which raises the pitching-moment derivative and natural frequency. That is **exactly this design's C31 span cap + C43 "cant, not area, is the lever"** — arrived at independently. Also supplies the Norris review citation and a cluster of further directly-relevant work (see B7, B11–B13) |
| B6 | *Aerodynamic and angular motion characteristics of a fixed-canard dual-spin projectile*, Chinese Journal of Aeronautics 2025 | 3 | 4 | abstract | Forebody spin rate changes the angular motion; a stationary or reverse-rotating forebody **improves** dual-spin stability. Supports S1/S8 |
| B7 | Norris, Hameed, Economou et al., *A review of dual-spin projectile stability*, **Defence Technology 16(1), 2020, pp. 1–9** | 4 | 5 | indexed | The standalone review of the field: how classical stability factors are modified for a controlled dual-spin projectile, and how airframe and canard properties affect flight stability. This is the section someone will hand a judge who asks "is it stable?" |
| B8 | *Robust Velocity Control of a Fixed Canard Decoupled Dual-Spin Projectile*, **IEEE 2024** ([10663247](https://ieeexplore.ieee.org/document/10663247)) | 4 | 5 | abstract | **A motor-generator test bench built to emulate the dual-spin system**, with sliding-mode velocity control. Published precedent for R7's rig architecture *and* for four-quadrant operation — which is risk 37's ring-hold-duty trade, currently the design's largest open lever |
| B9 | *Flight Stability of Canard-Guided Dual-Spin Projectiles with Angular Rate Loops* | 3 | 3 | abstract | Coning-motion stability conditions derived analytically for angular-rate loops; supports G11/G15's loop design |
| B10 | Zhu, *Flight stability of a dual-spin projectile with canards*, J. Aerospace Engineering 2014 | 3 | 3 | abstract | A stability criterion that accounts for nose-applied side forces — the correct frame for our canards-ahead-of-CG case in S1 |
| B11 | † Wang, Shen, Wang et al., *Analysis and compensation of inertial navigation external gimbal arm error for the fuze of double spin ballistic correction projectile*, Acta Armamentarii 46(6), 2025 | 4 | 4 | indexed | **Directly on N1's "time/lever-arm 1.0 m" term**, which is currently the register's least-supported error line. A published treatment of exactly the lever-arm problem on exactly this airframe |
| B12 | † Luo, Zhang, Deng et al., *Integrated optimization of de-spin actuator design and operating parameters*, Aerospace Science and Technology 167, 2025 | 4 | 4 | indexed | Integrated de-spin **actuator** design optimisation — the C-domain's own optimisation problem, published. Feeds C44/C45 and risk 37 |
| B13 | † Ramteke & Kothari, *Accessibility analysis and robust control design of dual-spin projectiles*, J. Guidance, Control and Dynamics 48(3), 2025, pp. 575–590 | 4 | 4 | indexed | **Accessibility analysis** — a formal reachability treatment of what a dual-spin projectile can and cannot achieve. The rigorous form of M7's authority question |
| B14 | † Shi, Zhang & Liu, *Analysis of spin rate and correction ability of two-dimensional trajectory correction fuze for 155 mm fixed-canard dual-spin projectiles*, Acta Armamentarii 40(8), 2019, pp. 1587–1595 | 4 | 4 | indexed | Forebody spin rate ↔ correction capability for **our exact calibre and configuration**. Bounds C8/M7 |
| B15 | † Zhao, Shi, Wang et al., *Dynamic stability and influence factors of the whole trajectory of fixed canard dual-spin projectiles*, Chinese J. Theoretical and Applied Mechanics 54(5), 2022 | 3 | 4 | indexed | Full-trajectory dynamic stability — the whole-flight counterpart to S1's muzzle-point evaluation, which is S1's known weakness |

### C — Course-correction fuze, guidance and control

| # | Source | Cite | Adopt | Read | What it moves |
|---|---|---|---|---|---|
| C1 | Wernert & Theodoulis, *Modelling and stability analysis for a class of 155 mm spin-stabilized projectiles with course correction fuze*, AIAA AFM 2013 | 3 | 3 | indexed | The CCF stability modelling lineage; the register's S-domain framing |
| C2 | Gagnon & Lauzon, *Course Correction Fuze Concept Analysis for In-Service 155 mm Spin-Stabilized Gunnery Projectiles*, AIAA 2008-6997 | 4 | 4 | abstract | Compares **drag brake, spin brake and the roll-decoupled four-canard configuration** head to head, with guidance and control tuned for each. The comparative evidence base for C1's "why four fixed canards" |
| C3 | *Efficiency Analysis of Canards-Based Course Correction Fuze for a 155-mm Spin-Stabilized Projectile*, J. Aerospace Engineering 29(6), 2016 | 4 | 4 | indexed | Quantifies **how much correction a canard CCF actually buys** — the published counterpart to M7's 407 m and C8's 18.1 N |
| C4 | Wang, Wang & Yu, *Influence of control strategy on stability of dual-spin projectiles with fixed canards*, Defence Technology 14(6), 2018 | 3 | 3 | indexed | Control strategy ↔ stability coupling; supports G3/G15's state-dependent limit argument |
| C5 | Robinson & Berefelt, *On Guidance and Control for Guided Artillery Projectiles*, FOI Sweden 2011 | 3 | 2 | indexed | Background framing for the G domain |
| C6 | Spagni, Theodoulis & Wernert, *Flight control for a class of 155 mm spin-stabilized projectile with reciprocating canards*, AIAA GNC | 3 | 2 | indexed | The **mechanism we rejected** (reciprocating canards) — the counterfactual in C1's trade |
| C7 | *Robust gain-scheduled autopilot design for spin-stabilized projectiles with a course correction fuze*, Aerospace Science and Technology 2015 | 4 | 3 | abstract | A q-LPV autopilot for a nose-positioned CCF. The rigorous alternative to our cascade+DOB; supports G14's filter-bandwidth defence |
| C8 | Khalil, Abdalla et al., *Dispersion analysis for spinning artillery projectile*, 2009 | 3 | 3 | indexed | M6's dispersion modelling lineage |
| C9 | Clancy, Bybee & Friedrich, *Fixed canard 2-D guidance of artillery projectiles*, **US Patent 6,981,672**, 2006 | 4 | 2 | abstract | **The canonical fixed-canard 2-D geometry.** Cite it to credit it — it defeats the "2-D steering from one actuation axis" novelty claim, so it belongs in the adopted-and-credited list |
| C10 | † *Trajectory parameter identification and impact point prediction*, Chinese Journal of Aeronautics 2025 | 3 | 4 | abstract | Nonlinear coupling of geometric and aerodynamic effects in IPP — a refinement path for G1's propagation model and G4's 13 m propagation term |

### D — Launch environment and survivability *(new coverage — E1/E2/E4/H5 have a bare `[ref]` today)*

| # | Source | Cite | Adopt | Read | What it moves |
|---|---|---|---|---|---|
| D1 | † *Establishment of the damage tolerance criterion of projectile-borne electronics under in-bore launch*, **Defence Technology 2026** | 4 | 5 | abstract | Establishes a **damage-tolerance criterion** for projectile-borne electronics in a high-g launch environment. This is E1/E2's missing method: the criterion is the deliverable, not the g-number |
| D2 | † *Survivability of embedded microelectronics in precision guided projectiles*, Int. J. Impact Engineering 2021 | 3 | 4 | abstract | Multiphysics shock loading through launch and muzzle exit. Supports H5's board-partition and launch-survival argument |
| D3 | † *Survivability of MEMS packages at high-g loads* (gas gun to 60 000 g), Springer | 3 | 4 | abstract | MEMS IMU survivability to 20 000 g demonstrated; 60 000 g by gas gun. Directly supports N7's ±2 000 °/s standard-MEMS claim and E1's margin |
| D4 | Cao, *High Shock Modeling of Fuze Components*, NSWCIH, 64th NDIA Fuze Conference 2021 ([pdf](https://ndia.dtic.mil/wp-content/uploads/2021/fuze/Cao1.pdf)) | 4 | 4 | **full** | The **method** behind E1/E2/E4: material characterisation (Split Hopkinson Bar + 4-point bend) → explicit FEM (DYSMAS/ParaDyn) → very-high-g test with a **potted accelerometer**. Also confirms **MEMS S&A with setback lock + command lock is established practice** (F6), and that a national lab runs guns to 21″ at >2 000 ft/s — so the E-domain test path exists and is nameable |
| D5 | *A miniature, gun-hard MEMS IMU for guided projectiles, rockets and missiles*, IEEE | 3 | 4 | indexed | Gun-hard MEMS IMU specified against 10 000–20 000 g with a >5 ms long-duration shock component — the shock *shape* E1 says the register is missing |
| D6 | OTS, *High-G Testing Overview* white paper | 2 | 2 | indexed | Test-house framing; background only |
| D7 | GuideNav — gun-hard MEMS IMU product page | 1 | 1 | indexed | **Do not cite.** Vendor marketing |

### E — Power, thermal, bearings and energy *(new coverage — C13/C23/C25, P6/W7 and risk 35 currently rest on single estimates)*

| # | Source | Cite | Adopt | Read | What it moves |
|---|---|---|---|---|---|
| E1 | Hasselström & Nilsson, *Thermal Contact Conductance in Bolted Joints*, Chalmers / RUAG Space, Diploma work 85/2012 ([pdf](https://publications.lib.chalmers.se/records/fulltext/159027.pdf)) | 4 | 5 | **full** | **P6's missing evidence base, and it is quantitative.** Vacuum experiments on aluminium bolted joints: total joint conductance **≈0.52 / 0.79 / 0.89 W/K** at 0.8 / 1.1 / 1.4 N·m bolt torque, rising to **19.6 / 20.8 / 21.2 W/K with a thermal interface material — a 24×–38× lever**. Three findings that bear directly on the register: (i) the bare-joint order of magnitude matches our first-order 3–16 W/K; (ii) **heat flow concentrates within a short radius of each fastener and large areas of the joint carry essentially no flux** — which is why "a clearance fit does not count" is correct; (iii) **a thin interstitial material is the closing lever, not more clamping force**. Also: available analytical models disagree strongly, so an application-specific measurement is the recommended route — i.e. exactly R7's item (7) |
| E2 | *Estimation of thermal contact conductance of spacecraft heat sink bolted joints*, Applied Thermal Engineering 2023 | 3 | 4 | abstract | Non-intrusive inverse estimation of the conductance distribution across a bolted joint; and a companion result on **non-conformal** joints where contact occurs only over the real contact patches. Supports the same P6 closing route |
| E3 | † *High-g impact survivability of thermal batteries: gas-gun experiments and a validated 3D FEM design guidelines*, **Defence Technology 2026** | 4 | 5 | abstract | **Risk 35's exact question**, answered for an adjacent storage technology: cells must survive launch deceleration while delivering power, characterised by gas-gun experiment plus a validated 3-D FE model. Gives W4's buffer a method and a test route — and the precedent that this class of part is qualified, not assumed |
| E4 | † *Sensing-in-Energy microdevice for high-g shock via supercapacitor*, Nano Research 2025 | 2 | 2 | abstract | A supercapacitor surviving extreme-g shock events. Weak (different duty, different scale) but worth a decision-log note that the part class has been demonstrated at high g |
| E5 | *Friction torque in miniature ball bearings*, **MDPI Lubricants 13(1):12, 2025** | 4 | 5 | abstract | **C13/C25's missing literature.** Decomposes friction torque into rolling, sliding, pivoting, cage–ball and cage–race losses. Our whole feasibility gate (`Tf* = 0.1567 N·m`) and risk 24's 19.4× speed scaling rest on a single reference datum; this is where a published model comes from |
| E6 | † *Influence of the cage on the friction torque in miniature ball bearings*, MDPI Lubricants 14(4):145, 2026 | 3 | 4 | abstract | Fits **Houpert's model** to modified cage configurations — the analytical route to scaling `Tf` from the reference's 83.8 rad/s to 1 900 rad/s |
| E7 | † *Experimental friction torque in miniature ball bearings, grease lubricated*, 2026 | 3 | 4 | abstract | Grease-lubricated measurements across speed and load; gives the shape of the Tf(ω) curve the register needs to show is flat |
| E8 | Miniature bearing speed, friction, torque and heat generation — manufacturer technical guide | 3 | 5 | **full** | **Creates a new risk.** Three things: (i) `Q ∝ M_friction × ω`, so a "flat" 0.10 N·m budget is **≈160 W of heat** at the ring's own speed — the register's number, now with a stated mechanism; (ii) **thermal-preload runaway**: friction → heat → clearance loss → preload rise → friction rise, explicitly called out as a high-speed failure mode, and our own C23 trade *buys stiffness with preload at 1 900 rad/s*; (iii) low temperature raises starting and running torque, which is the cold corner of R5's Monte Carlo. Also: contact seals are a large friction share (so open/shielded), grease *quantity* is a first-order variable in a miniature bearing, and cage instability is a speed limit. Cite 3 — it is a vendor guide, not authority — but it changes the design |
| E9 | Supercapacitor review, J. Energy Storage 2025 | 2 | 1 | indexed | Background only |

### F — Fuze, setter and safety standards

| # | Source | Cite | Adopt | Read | What it moves |
|---|---|---|---|---|---|
| F1 | **NATO AOP-22**, *Design Criteria and Test Methods for Inductive Setting of Large Calibre Projectile Fuzes*, Edition B Version 1, May 2018 (supporting STANAG 4369 / AOP-4369) | 5 | 5 | **full** | **F11 has no named standard today; this is it.** And it does three more things. **It closes the setter interface with numbers**: carrier 100 ± 0.01 kHz; forward bit rate 1 000 ± 10 bit/s; rise/fall ≤ 50 µs; FMW 275 ± 5 ms; PUP 1–1000 ms; 36.2–48.2 V p-p induced into the receive coil. **It defines the window the mission package must fit** — ≈275 bits per FMW, and the two registered **course-correction** fuzes (XM7, XM8) use **2 FMWs**, so ≈550 bits is the standard's own budget for a CCF. **It documents the XM8 doing in-flight time correction** (see §3.4 — this reverses a claim). And §3.3 makes our F12 read-back the *standard* error-detection mechanism, not a design feature. §3.6(c) also allows the fuze to **calibrate its time base against the setter's precision time base** — the natural home for H6/N15 |
| F2 | STANAG 4369 / AOP-39 (fuze design, safety and insensitive munitions assessment) | 4 | 3 | indexed | The parent standard AOP-22 supports; E11's IM assessment route |
| F3 | MIL-STD-1316 (fuze design safety criteria) | 5 | 4 | indexed | F6's authority; the out-of-line rotor requirement |
| F4 | MIL-STD-333B (fuze interface; 2″-12 UNS-2A) | 4 | 4 | indexed | P6/P7/P12's interface authority |
| F5 | MIL-STD-810F / **MIL-STD-331C** / MIL-STD-461 | 4 | 4 | indexed | **E10's named list.** MIL-STD-331C for fuze environmental and performance testing is the piece the submission omits today — the audit's ⚠️ "vague standards" |
| F6 | Elbit M910 inductive electronic time fuze datasheet — *STANAG 9216 (MIL-STD 333B)*, 105–203 mm | 3 | 3 | indexed | A fielded fuze declaring STANAG 9216 / MIL-STD-333B / MIL-STD-1316 / MIL-STD-331 compliance — the observed naming convention for F's standards list |
| F7 | *EPIAFS — Enhanced Portable Inductive Artillery Fuze Setter*, NDIA Fuze Conference 2006 | 3 | 3 | indexed | The fielded setter our F11/F12 emulate; establishes that the gun-line setter is existing procedure |
| F8 | *Method and system for inductive programming of a fuze*, US20210310778A1 | 2 | 2 | indexed | Patent background for the setter link; not cited |
| F9 | **UNCLASSIFIED tooling find:** the AOP-22 Annex E registered-fuze tables | 5 | 4 | full | Same source as F1, listed separately because it has a separate use: it is the **registry of what a setter must already talk to**, including two course-correction fuzes. If our kit claims to use "the existing setter", this is the list it must not break |

### G — Simulation toolchain

| # | Source | Cite | Adopt | Read | What it moves |
|---|---|---|---|---|---|
| G1 | RocketPy documentation v1.13.0, technical section, and repository (MIT) | 3 | 4 | partial | Confirms risk 38's boundary by naming the limits: the documented aerodynamics are **elliptical fins** and **individual fins**, with the equations-of-motion derivations v0/v1, and the documentation states it is incomplete. There is **no canard model, no de-spun ring degree of freedom, and no in-bore phase** — so the register's "harness only, never the model" rule holds, and the version pin is now 1.13.0 under MIT |

### H — Competition, cost and market

| # | Source | Cite | Adopt | Read | What it moves |
|---|---|---|---|---|---|
| H1 | SIH 2026 Guidelines (official PDF, via the DTU SPOC notice) | 5 | 4 | indexed | The nine-term rubric; **"if it has a business potential more weightage will be given"** → slide 5 becomes a business case; six-slide cap; PDF only; prototype preferable but not mandatory; 30 September deadline; the abstract is read standalone |
| H2 | DTU SPOC notice | 2 | 1 | indexed | Corroboration only |
| H3 | `srkself26-cmd/sih26098-guidance-sim` — competitor repository | 3 | 2 | full | Competitor archetype C1: a 3-DOF/ZEM simulation claiming sub-4 m CEP. Shows the field's default answer and where the honest-claim discipline differentiates |
| H4 | Stout, *Very Affordable Precision Projectile System*, NDIA 2011 | 3 | 3 | indexed | The affordability thesis and its cost structure — the class's precedent for K4/K5 |
| H5 | *High maneuverability projectile flight using low cost components*, Aerospace Science and Technology | 3 | 3 | indexed | Algorithms compensating for poor actuator performance; relevant to K4's "low-cost parts" hypothesis |
| H6 | PGK / Excalibur market notes and market-research reports | 1 | 1 | indexed | **Do not cite.** Analyst estimates with no method disclosed |

### I — Explicitly excluded

Recorded here so no later session re-imports them as sources.

| Excluded | Why |
|---|---|
| IAI TopGun product page | Not retrievable (bot protection). Only a search-indexed claim; unusable |
| Kratos, GAJT-AE3 and other anti-jam vendor pages | Marketing; no method. Used only as context for X17, never cited |
| Analyst field-size models and competitor-count estimates | Unattributable method |
| Scribd re-hosts of NDIA presentations | The primary PDF exists; cite the primary |
| The predecessor workspace at `~/Documents/smart india hackathon/` | **In-house analysis, not a public source.** Values from it are labelled cross-checks, never citations — the rule already stated in the register's Related-files table |

### J — Manufacturing, materials and process

Added 2026-09-20 with the manufacturing dossier (`design/06-manufacturing-and-process.md`). These sources supply the process evidence behind K5 (the cost target's ranked drivers), the open trades C39/C44/C45, and P6's joint. Rows rated **Adopt ≥ 4** appear in §3.6.

| # | Source | Cite | Adopt | Read | What it moves |
|---|---|---|---|---|---|
| J1 | Höganäs (Ye, Jonsson et al.), *A new generation of sustainable SMC materials with low core loss*, powder-metallurgy technical paper | 4 | 4 | full | **C39's compaction route with numbers**: Somaloy 700 7P core loss **83 W/kg at 1 T / 1 kHz** (against 125 W/kg for the prior generation), TRS **60 MPa** rising to ≈100 MPa with tailored heat treatment, thermal aging **0 / 1 / 5 %** loss increase after 120 h at 150 / 200 / 260 °C, benefit stated **0–5 kHz**. Also the strength caution a gun-launched stator must answer |
| J2 | Waelzholz, *Thin electrical steel strip: NO grades for medium to high frequency ranges* | 3 | 3 | indexed | **C39's lamination branch is purchasable** — 0.1 mm thin-gauge NO strip is a catalogue product, not a development item |
| J3 | *Multi-layer shear cutting of thin non-oriented electrical steel sheets*, ScienceDirect 2026 | 3 | 3 | abstract | The lamination route's process cost: small cutting clearances and handling below **0.23 mm** are named manufacturing challenges — a yield/cost input to C39 and K5 |
| J3b | Motor-core lamination stacking process references (interlocking, bonding, welding, riveting) | 2 | 2 | indexed | Stacking methods for the 25–30 mm stack; background for the stator process plan |
| J4 | † *On the Fabrication of High-Performance Additively Manufactured Copper Winding*, **Materials 16(13):4694, 2023** | 4 | 4 | indexed | **Printed-copper windings with numbers**: ~80 µm minimum feature spacing, **79 % slot fill** (square conductor) / **63 %** (round), **87 % IACS after heat treatment** — the upper bound of the printed route for the new winding row |
| J5 | † RWTH Aachen, printed pure-copper winding heads on conventional conductors (BHM 2023, DOI 10.1007/s00501-023-01420-w) | 4 | 4 | indexed | **The hybrid route with numbers**: end-winding height cut **12.5 mm of 37 mm (≈1/3)** and **≈0.564 kg** of copper saved in that machine; roughness ≈32 µm Sa, lower productivity and insulation testing still owed. A direct lever on P12's axial envelope and C40's mass |
| J6 | † Oel et al., multi-material PBF-LB stator tooth with integrated cooling, **Additive Manufacturing Letters, 2023** (DOI 10.1016/j.addlet.2023.100165) | 4 | 4 | indexed | **The cautionary result this dossier will not inherit**: printed cooling channels could not be fully freed of powder and testing found short-circuit currents involving coils and teeth. Printed cooling is not a plan until depowdering, cleanliness and leakage are independently evidenced |
| J7 | Robinson et al., *Materials* 15(21):7563, 2022 (LPBF Cu/Ag: 88 % density, **73 % IACS** max) + EBM copper-winding study, Procedia CIRP 2025 (**91.7 ± 1.8 %** of pure copper) | 3 | 3 | abstract | **Conductivity is process-dependent** — 73 → 92 % IACS across AM processes and post-treatments. Any printed-copper claim must specify process, heat treatment and measured phase resistance |
| J8 | Additive Drives (Germany) — 3D-printed coil and stator product pages | 2 | 3 | full | **The commercial state of printed windings**: single coils, OptiSlot, NextPin, quoted for >500 Hz fundamental duty; vendor claims only (25 kW/kg, 100 kW/litre) — cited for the strategy, never for a number |
| J9 | IEEE 2024, *Advanced cooling of power electronics with copper cold sprayed…* (doc 10754883) | 4 | 4 | abstract | **Cold-spray copper for P6 and W12**: as-sprayed **98 % IACS and 368 W/mK**, used for hybrid heat sink and busbar duty. The route to a precision, high-conductance mating surface on the kit's own spigot |
| J10 | *Selection of high-performance thermal interface materials for space…*, ScienceDirect 2025 (S2214157X25004630) | 4 | 4 | abstract | **P6's joint characterised**: smooth and **embossed** indium foil against graphite sheet as a function of interface temperature, **contact pressure** and **surface roughness** (ASTM D-5470). The measured basis under P6's `h_c` bracket |
| J10b | Bal Seal canted-coil spring — electrical/EMI shielding and contact engineering | 2 | 3 | indexed | **The compliant multi-point contact mechanism**: consistent contact force under shock and vibration. Heritage is electrical/EMI — thermal use must be characterised, not assumed |
| J10c | NASA SmallSat Technology State-of-the-Art, **7.0 Thermal Control** (2024) | 3 | 3 | indexed | The bolted-joint thermal contact conductance framing the P6 route follows; the practice standard for a conductance-specified joint |
| J11 | Panasonic pyrolytic graphite sheet (PGS) / G-TIM datasheets (via Digi-Key white paper and Danfoss-hosted datasheet) | 3 | 3 | indexed | **W12's spreader**: 700–1 000 W/mK standard, up to 1 950 W/mK in-plane, 10 µm-class thicknesses, **compressible variant** available. Anisotropic — a spreader, never a through-thickness interface |
| J12 | MDPI *Energies* 15(17):6116, 2022 (magnet-loss review) + IET *Power Electronics* 2021 (segmentation model, DOI 10.1049/pel2.12009) | 3 | 3 | abstract | **Magnet eddy loss at our 1 234–2 131 Hz relative field is a real term in C42's ledger**; segmentation with insulated interfaces and retention is the standard mitigation. Feeds C38 and the machine's loss model |
| J13 | *Significant progress of grain boundary diffusion for cost…*, ScienceDirect 2021 (S0264127521005591) + DyF₃ dip-coating GBD, Springer 2025 (DOI 10.1007/s10853-025-11721-9) | 3 | 3 | abstract | **K4/K5 cost lever without a design change**: GBD buys coercivity with heavy rare earth placed only at grain boundaries — cost reduction and high-efficiency use of the critical element — matching C38's SH/UH grade need |
| J14 | Topology optimization + LPBF aircraft-bracket studies: Springer 2025 (DOI 10.1007/s12046-025-02810-1) and MDPI *Applied Sciences* 13(24):13218 | 3 | 3 | abstract | **The mass-reduction route for the ring**: topology-optimised LPBF carriers with verified examples. At 14.7 kN per 0.1 kg (C26), mass removed pays twice — P9/C40 and the retention structure |
| J15 | Thin-section bearing supply: RBC *Thin Section Ball Bearings* catalogue (2025) + Schatz custom-bearing pages | 3 | 3 | indexed | **C22/C23 are procurable**: standard and custom thin-section radial/angular contact bearings, ABEC 5–7 classes, preload control — the `k_pair ≥ 122 N/µm` / `Tf ≤ 0.10 N·m` pair is a specification to a bearing house, verified by C25 by test |
| J16 | DFMA cost-estimating guides — metal injection moulding and investment casting | 3 | 3 | indexed | **The 5 000/yr tooling question for F-domain parts and the housing**: per-part economics vs CNC as a function of size, complexity and volume; wax-pattern and MIM tooling amortisation stated rather than assumed |
| J17 | Laser Direct Structuring: LPKF (process) + Kyocera AVX / Taoglas (production practice) | 3 | 3 | indexed | **N3's aperture as structure**: 3D conformal conductive traces on an injection-moulded part, at volume. The version of the spin-axis aperture that costs no separate antenna volume (risk 27) |
| J18 | *Sequential Rotation of Antenna Array Elements*, Advances in Radio Science 20:17, 2023 | 3 | 3 | indexed | **The established array technique behind N3's "elements combined rather than switched"** — rotated element feeds control polarisation from combined elements; converts the symmetry argument into a construction method |
| J19 | Dual-band radome: Springer *J. Electronic Materials* 2023 (DOI 10.1007/s11664-023-10679-1) + Toray quartz radome prepreg systems + Corning Pyroceram missile domes | 3 | 3 | indexed | **F2/N3's radome is a declared development item with real precedents**: quartz/cyanate composite with FSS for dual-band transmission, quartz prepreg systems, and the classic glass-ceramic dome |
| J20 | AlN thick-film power resistors: Vishay RCP series and IMS N-series | 3 | 3 | indexed | **W12/H9's dump resistor class exists off the shelf** at the required power density, with its own conduction-out design rule stated in the datasheet |
| J21 | Needle winding machine practice: Elmotec Statomat, IMA Automation, DETZO | 2 | 3 | indexed | **The production winding baseline**: out-slot needle winding is the standard route for concentrated schemes with high type variety — the process the printed option must beat |
| J22 | Integral (one-piece) 5-axis machining of bladed disks — blisk practice | 2 | 2 | indexed | **The ring/canard integrity precedent**: one-piece machining removes joints and holds blade geometry in a single setup — corresponds to C31's cant-angle-as-lever and C26's 74 kN |
| J23 | LPBF Fe-Si soft magnetic studies: ScienceDirect 2023 (S026412752300758X), *Sci. Rep.* 2025 beam-profile study, in-situ alloying FeSi6.5 (Springer 2025) | 3 | 3 | abstract | **AM iron is real research and not a production route**: dense crack-free builds at 3–9 wt% Si, but no volume motor-core production — a development/first-article tool for C39's loss model and the R7 rig |

**Added the same day, for §7 of the dossier (the digital-cell concept).** These carry the advanced-manufacturing claims — the post-treatment chain, in-process monitoring, robot cells, printed/embedded electronics — and each one exists to *bound* a claim as much as to support it.

| # | Source | Cite | Adopt | Read | What it moves |
|---|---|---|---|---|---|
| J24 | † *Hot isostatic pressing of laser powder bed fusion AlSi10Mg*, Springer *J. Materials Science* 2022 (DOI 10.1007/s10853-022-07027-9); and *Effect of HIP treatment on microstructure and fatigue strength of SLM AlSi10Mg*, MDPI *JMMP* 3(1):16, 2019 | 4 | 4 | abstract | **The porosity countermeasure, with its cost stated**: fatigue crack initiation in as-built LPBF AlSi10Mg is dominated by process porosity; HIP is the reduction route; a classic ~500 °C / 100 MPa cycle causes a strength loss that is **partly recoverable by heat treatment**. Both halves are needed — quoting only "HIP closes porosity" would be the incomplete form |
| J25 | † *Effects of heat treatment and hot isostatic pressing on microstructure and fatigue of SLM Ti-6Al-4V*, Materials Letters 2024 (S0167577X24007791) | 3 | 3 | abstract | The Ti-6Al-4V counterpart of J24 — heat treatment vs HIP compared on fatigue; supports the chain's ordering (HIP, then heat treatment, then finish) |
| J26 | † *Surface roughness in laser powder bed fusion* ScienceDirect 2020 (S2214860420308095); *Effect of post-processing methods on the surface quality of LPBF Ti6Al4V* Frontiers in Materials 2023; post-processing polishing review (mechanical, laser, abrasive flow, electrochemical, chemical) | 4 | 4 | abstract | **Roughness is a named LPBF limitation** and the treatment set is measured, not assumed: abrasive-flow machining, electrolytic and chemical polishing, laser polishing, sandblasting. This is the "post-treatment to overcome the disadvantage" claim, in its citable form |
| J26b | † *Exploring the fabrication limits of thin-wall structures in LPBF*, Springer IJAMT 2020 (DOI 10.1007/s00170-020-05827-4) | 3 | 3 | abstract | Thin walls, residual stress and shrinkage are parameter- and build-controlled limits — the design rule behind "print near-net" for thin sections |
| J26c | † *Geometric feature reproducibility for LPBF* ScienceDirect 2021 (S2214860421004632); *Understanding dimensional and geometrical tolerances of metal PBF*, MDPI 2026 | 4 | 4 | abstract | **Why critical features are machined, not printed**: feature reproducibility is machine- and orientation-dependent, and geometrical requirements "may prevent these technologies from being employed in more demanding applications". The bound on what may be left as-built |
| J27 | † Predictive qualification of LPBF with multi-modal in-situ monitoring, UT Austin 2025; melt-pool radiation monitoring, ScienceDirect 2025; NIST AMS 100-35 thermal calibration of melt-pool sensors | 3 | 4 | abstract | **The honest limit on "the part carries its record"**: in-situ monitoring (optical tomography, melt-pool monitoring, photodiodes, IR) is advancing toward model-based qualification but **is not yet a substitute for testing** — so coupons, CT and lot testing stay in the chain |
| J28 | NASA-STD-6030, *Additive Manufacturing Requirements for Spaceflight Systems*, 2021 | 4 | 4 | indexed | **The qualification shape this kit would follow**: AM flight hardware is approved through process control, coupons, testing and traceability — not because the process is additive. Also the ceiling on any "printed therefore modern" argument |
| J29 | † Additive Manufacturing in the Aerospace Industry, *Am. J. Eng. Applied Sci.* 2024 — part consolidation, lead-time reduction, **on-demand production with reduced inventory**; aerospace DFM part-count guidance | 3 | 3 | abstract | The part-consolidation and on-demand claims (§7.1): printed assemblies remove fasteners and joints — the classic 15 000 g failure points |
| J30 | † Robot-based hybrid WAAM + machining platform, Springer IJAMT 2023 (DOI 10.1007/s00170-023-12517-4) — aluminium parts, machining quality and mechanical properties satisfactory; scalable multi-robot WAAM, ScienceDirect 2023 (S2772369023000634); MX3D robotic WAAM practice | 3 | 4 | abstract | **The robotic cell exists in production form**: robot deposition, robot machining and robot handling in one platform. This is the §7 claim's anchor — a stated industrial practice, not a concept drawing |
| J31 | † *3D printed structural electronics: embedding and connecting electronic components into freeform electronic devices*, Plastics, Rubber and Composites 2017 — print interrupted to **pick and place** components, then direct-write/squeegee conductive filling and thermal cure; Nano Dimension DragonFly IV (simultaneous silver + dielectric); Optomec Aerosol Jet (printed resistors, capacitors, antennas, sensors) | 3 | 4 | abstract | **The print–pause–place–resume sequence, demonstrated** — the mechanism behind "integrated electronics placement while printing" and "printed electrical traces", with components embedded rather than mounted |
| J31b | † *Approaching the practical conductivity limits of aerosol jet printed silver*, ACS AMI / arXiv 2020; *Highly conductive circuits from aerosol jet printed silver inks*, *Sci. Rep.* 2021; electroplating of printed silver for solderable traces, *Adv. Eng. Mater.* 2021 | 3 | 3 | abstract | **The conductivity bound**: optimised reactive inks reach near-bulk conductivity at ~80 °C treatment, while conventional low-temperature-sintered nanoparticle inks sit several times bulk — so printed traces carry **signals, RF and logic, not power**, and the ink/process must be qualified per application |
| J32 | † *Spectral behaviour of fibre Bragg gratings during embedding in 3D printed metal*, MDPI *Sensors* 24(12):3919, 2024 (Inconel 718 by LPBF); FBG sensors embedded by ultrasonic additive manufacturing, IEEE 2023 (dynamic strain 1–10 kHz); LPBF-embedded fibre-optic sensors, Silicon Austria Labs | 3 | 3 | abstract | **Embedded sensing in metal is demonstrated** — the qualification/ground-test instrument of §7.4. Also the bound: an in-flight health channel is a growth option, not a baseline claim |
| J33 | † 3D-printed graded-index dielectric lenses: 60 GHz printed Luneburg lens, IEEE 2019; six-zone printed Luneburg lens, MDPI *Electronics* 15(12):2537, 2026; printed-lens review | 3 | 3 | abstract | **Printed dielectrics as a radome/lens manufacturing route** — spatially varying permittivity by printing, demonstrated at mmWave. Supports F2/N3's radome as a *printed* development item; the dual-band structural radome remains declared, not solved |
| J34 | † SLS vapour smoothing: Formlabs/AMT white papers — surface and mechanical improvement on Nylon 11 toward injection-moulded quality; dyeing and plating as secondary steps | 2 | 3 | indexed | **The polymer-SLS post-treatment**: roughness and porosity addressed by vapour smoothing — the reason a printed radome/housing can be an end-use part rather than a prototype |

**Added the same day, for the validation pass (§4.8 of the judge dossier).** These are the sources that answer the question a defence panel will actually ask — *is this how munitions are made now, and is a printed part legal in a gun-launched fuze?*

| # | Source | Cite | Adopt | Read | What it moves |
|---|---|---|---|---|---|
| J35 | US Army CCDC ARL, **Science of Additive Manufacturing for Next Generation Munitions (SAMM)** programme | 4 | 4 | indexed | **AM for munitions is a funded US Army research direction**, not a vendor pitch — tailored alloys and, in their own words, printing custom munitions. The precedent that a panel cannot dismiss the approach as naive |
| J36 | US Army, *Additive manufacturing to provide Soldiers with cutting-edge munitions* (2019); and the Picatinny Armaments Center additive-manufacturing facility (2025) | 3 | 4 | indexed | The Army's own statement that AM *"has potential to improve the performance of munitions, electronic sensors and fuzes"* — the fuze/electronics relevance stated by the customer class itself, plus a standing AM facility at the armaments centre |
| J37 | **DoDI 5000.93, *Use of Additive Manufacturing in the DoD*** | 4 | 4 | indexed | **The policy basis**: the US DoD has an instruction governing AM implementation. Useful precisely because it shows the question "is AM allowed in defence?" has an institutional answer, not a cultural one |
| J38 | **ASTM + UK MoD, Project TAMPA** — *strategic guide to support certification of additively manufactured parts in defence* | 4 | 5 | indexed | **The defence-specific qualification framework**: a common, **criticality-based** approach to qualifying and certifying AM parts. Stronger and more on-point than NASA-STD-6030 alone for a munitions context, and the direct answer to "show me the qualification route" |
| J39 | **DTIC AD1023960** — *Method for designing electronic assemblies* : **additively printed conformal structural supports for printed circuit boards, demonstrated as a viable method for ensuring high-G survivability of electronics in gun launch applications** | 4 | 5 | abstract | **The single most valuable find of this pass.** Printed structural electronics surviving **gun launch** is a demonstrated principle, not a proposal — which converts risk 50 from "unproven" into "principle demonstrated, project-specific qualification owed". It also validates the §7.4 claim that the potting *is* the structure |
| J40 | Times of India, *Yantra India fast-tracks custom-made ammo hardware for foreign companies* (2026) | 2 | 3 | indexed | **The host's own direction**: YIL is already moving toward custom and short-run ammunition hardware. The digital-cell argument lands on a strategy the PS owner is pursuing, rather than reading as a student novelty. Press source — context, never a number |

† — read via indexed/secondary summary rather than the full text; the numbers quoted are as reported by the source and are provisional until the full text is read (the same convention as section B). J1 is a full-text read; J9 and J10's quoted figures are stated in the papers' own abstracts. **The §7 rows above (J24–J34) are at that provisional level by construction** — they support a *concept* whose qualification is declared, not a production commitment.

---

## 3. The adopt list — what each source changes

Every row rated **Adopt ≥ 4** appears here with its change. Rows rated Adopt ≤ 3 are citation-only and are not repeated.

### 3.1 New criteria

| Source | New criterion | Why |
|---|---|---|
| A2, A1 | **F16 — Predicted-miss failsafe (dud-on-miss behaviour)** | The fielded kit decides, five seconds after launch, whether it expects to land close enough to detonate. F6 guarantees *no premature function*; nothing guarantees *no function at the wrong place*. A fuze-safety judge asks this within two questions |
| A1 | **M10 — Range retention (>90 % of the conventional round)** | The fielded kit's own published requirement, and no criterion owns the range cost of our canards and mass. A kit that buys accuracy with range may not be accepted |
| B4, B5, B7 | **S8 — Resonance instability disposition** | A named failure mode of this exact architecture, reproduced in the literature, which an `Sg`-only treatment does not cover |
| A2, F3 | **E12 — HERO / EMR / ESD** | Absent from E10/E11; the standard ordnance electromagnetic-hazard set |

### 3.2 New risks

| Source | New risk | Why |
|---|---|---|
| A2 → F16 | **Risk 40 — the dud-on-miss decision cuts both ways** | Withholding detonation is safer for the supported force but converts a usable near-miss into a dud and changes the terminal effect the user buys |
| B4, B5, B7 → S8 | **Risk 41 — resonance instability is unnamed in our stability case** | The literature for our own configuration reproduces it; S1 evaluates `Sg` at the muzzle only |
| F3, A2 → E12 | **Risk 42 — HERO/EMR/ESD absent from the qualification set** | A fuze-safety gap that MIL-STD-1316 and the IM assessment do not cover |
| A1 → M10 | **Risk 43 — range retention unbounded** | Canards and kit mass are a drag and trim penalty; no criterion owns it |
| **F1 → F12/H11** | **Risk 44 — the setter mission package has never been sized against the standard's window** | F12 lists target coordinates, met, charge/muzzle-velocity, time reference, **GNSS ephemeris and keys**, mode, parameters and round ID. AOP-22 allows ≈275 bits per forward message window at 1000 bit/s and the two registered course-correction fuzes use two windows — ≈550 bits for a whole CCF mission package. Ephemeris alone is of that order. **The package must be counted and cut, or the claim narrowed to what fits.** H11 owns the count |
| **E8 → C23** | **Risk 45 — thermal-preload runaway across the bearing pair** | C23 deliberately buys air-gap stiffness (122 N/µm) with preload, and the ring runs at up to ≈1 900 rad/s. At that speed the friction → heat → clearance → preload feedback is a known runaway path and nothing in C13/C22/C23/C35 owns the transient |

### 3.3 Basis hardening — citation added, **no value moves**

| Source | Row(s) | Change |
|---|---|---|
| F1, F7 | **F11** | The setter interface gains a **named standard** (AOP-22) and its numbers, plus EPIAFS as fielded practice. A PARAMETRIC row stops being generic |
| F1 | **H6, N15** | AOP-22 §3.6(c) permits the fuze to calibrate its time base against the setter's precision time base — an external anchor for a criterion that currently closes on itself |
| E5, E6, E7 | **C13, C23, C25** | The friction budget and the preload trade gain published torque models to scale against, replacing a single reference datum (risk 24) |
| E8 | **C13, W12** | `Q ∝ M_f ω` stated as the mechanism; the ≈160 W bearing-friction figure becomes derivable rather than asserted |
| E1, E2 | **P6, W7, W12** | The bare-joint conductance estimate gains a quantitative, measured basis and a stated closing lever |
| E3 | **W4, risk 35** | The buffer's high-g question gains a method and a precedent that the part class is qualified |
| D1, D2, D3, D4 | **E1, E2, E4, H5** | 15 000 g stays `[ref]`, but the **damage-tolerance criterion** and the test method become citable — this is the rows' path to closure |
| D4 | **F6** | MEMS S&A with setback lock and command lock is established practice — F6's design direction is validated, not invented |
| B8, B13 | **R7** | A published motor-generator bench for a fixed-canard dual-spin projectile, plus an accessibility analysis — R7's architecture and authority question both have precedent |
| B3 | **C9, C12** | The 0.8 N·m distinction recorded: theirs is an *actuator design requirement*, ours is the *aerodynamic* torque the ring must hold |
| B11 | **N1** | The lever-arm error term gains a published treatment on this airframe |
| B5, B14, B15 | **C31, C43, C8, M7, S1** | Independent corroboration of the span-cap-plus-cant architecture, and published correction-capability bounds |
| A1, A4 | **M8** | The derived rounds figure sits beside the fielded **301→77 (74 %)** and Elbit's *up to 90 %* |
| A2, A4 | **R5, G4** | The "never claim accuracy superiority" guard: fielded sub-10 m median and 20 m CEP |
| G1 | **risk 38, carried item 14** | Version pin 1.13.0, MIT licence, and the named limits — fin-based aerodynamics, no canard model, no ring DOF, no in-bore phase |

### 3.4 Claim corrections

These change **what the submission may say**. Sharpest first.

| # | Claim as it stands | Verdict | Action |
|---|---|---|---|
| 1 | *"In-flight re-synchronisation of the time setting from the navigation solution"* — presented as a contribution, and the audit recorded it as *"✅ Ours, and no fielded equivalent found"* (`audit §3`) | **❌ Wrong, and the audit's own method defeats it** | **AOP-22 Annex E.16 registers the XM8 — "FUZE, COURSE-CORRECTION, ELECTRONIC TIME FUZE" — and states: "In course correction mode, the time is also corrected in flight to improve accuracy."** A NATO-registered, fielded course-correction fuze already does this. The claim joins the M1156 list: **adopted and credited, never claimed.** This is the register's most important correction and it was found by reading the standard rather than the article |
| 2 | *"The setter reads back what it wrote"* (F12), presented as a design feature | **⚠️ Standard practice** | AOP-22 §3.3: the setter transmits, the fuze repeats, the setter compares — the standard's own error-detection mechanism. Keep the sentence, retire the implication |
| 3 | *"Wider mode set than the fielded competitor"* | **❌ Only true against the US kit** | Silver Bullet II offers PD + PDD + AB. The genuine differentiators are a true **programmable time** mode and in-flight re-synchronisation — and #1 above removes the second one unless narrowed to *impact/proximity* time re-synchronisation |
| 4 | *"Continuous impact-point prediction … this is new"* (`draft:216`) | **❌ Still uncorrected in the draft** | Published prior art (B2). The deck's honest novelty is the authority gate and the ring-as-inertial-platform |
| 5 | De-spun ring, fixed canards, no actuators, one moving part, no in-flight battery | **❌ Not novel; partially fixed** | `form-content.md` §15 was rewritten 2026-09-19; the fielded kit must still be **named**, and `template-slides.md` slide 2 still carries the implication |
| 6 | *"There is no failure mode in which the kit makes accuracy worse than the unguided baseline"* and *"loss of guidance … leaves a live, functioning fuze"* | **❌ Answers the wrong question** | Both are about *accuracy*; the panel will ask about *where the round lands*. Requires F16's decision to be stated |
| 7 | Mass: *"a net +0.7–1.0 kg"* | **⚠️ One-sided** | Total mass is 1.0–1.21× the fielded kit; **net penalty is 1.55–2.2×**. State both |
| 8 | *"The ring-mounted IMU"* | **⚠️ A trade, not a triumph** | The fielded design determines roll angle from GPS with **no inertial sensors**. Our IMU is a cost and complexity addition — justified by the GNSS-denied requirement (A3), and it must be priced |
| 9 | *"4 rounds vs ≈264"* (M8) | **⚠️ Unanchored** | Sit it beside the fielded 301→77 and explain the scenario difference |
| 10 | Standards: *"the applicable defence standards for artillery fuzes"* | **⚠️ Vague** | Name MIL-STD-1316, **MIL-STD-331C**, MIL-STD-810F, MIL-STD-461, **AOP-22**, STANAG 4369/AOP-39, STANAG 4439, STANAG 9216 |
| 11 | HERO / EMR / ESD | **❌ Absent** | E12 |
| 12 | Resonance instability | **❌ Not named** | S8 |

### 3.5 Submission actions

1. The **F16 dud-on-miss position**, stated in one line, either way — `form-content.md` §6.5 and §11.4, `draft-from-register.md`, slide 3.
2. The **fielded kit named** in the adopted-and-credited list, and the **XM8's in-flight time correction** added to it.
3. The **two honest mass ratios**, in one sentence.
4. **Range retention >90 %** as a stated requirement (M10).
5. The **mode-set nuance** — parity in count, differentiation in *time*, and no claim the XM8 does not also make.
6. **Resonance instability**, named and dispositioned (S8).
7. The **named standards**, including AOP-22 and MIL-STD-331C.
8. **Slide 5 as a business case**, because business potential carries extra weight (H1).
9. The **fielded impact anchor** 301→77 / 74 % beside our derived figure.
10. The **GNSS-denied alignment argument** — PGK E5 in production, LR-PGK for the near-peer GPS threat; our IMU-on-ring a deliberate, priced departure.
11. The **slide-4 error budget refreshed** to RSS 20.3 m → CEP 23.9 m (the template still shows the superseded 20.4/24 with nav 5 m).
12. The **400 V bus** replaced by H8's ≈150–200 V everywhere it still appears.

### 3.6 Manufacturing adopt list (section J)

Added 2026-09-20. These **do not change a decided value**; they supply the process evidence the cost target (K4/K5) and three open trades (C39, C44, C45) have been resting on without citation.

| Source | Row(s) | Change |
|---|---|---|
| J1, J2, J3 | **C39** | The stator-core trade gains three real routes with data — SMC compaction (83 W/kg @ 1 T/1 kHz, TRS 60–100 MPa), 0.1 mm laminations (purchasable, hard to process below 0.23 mm), and AM Fe-Si (research only). No value moves; the criterion's missing number now has a decision shape |
| J4, J5, J7, J21 | **new winding row (C46, proposed)** | The winding route gains bounded options: conventional needle winding (production), printed copper at 79 %/63 % fill and 87 % IACS after HT, the hybrid at −1/3 end-winding height and −0.564 kg — plus the process-dependent-conductivity caution (73–92 % IACS) |
| J6 | **R7, W12** | **A stated non-inheritance**: printed cooling channels were not fully depowdered and produced short-circuit currents in test. Printed cooling is not a plan until depowdering/cleanliness/leakage are evidenced |
| J9, J10, J10b, J10c, J11 | **P6, W7, W12** | The joint's closing route becomes manufacturable and measured: cold-sprayed copper (98 % IACS / 368 W/mK as-sprayed) for the kit-side surface, compliant multi-point contact, indium foil characterised against pressure/roughness, PGS for spreading — with NASA's bolted-joint conductance framing as the practice standard |
| J12 | **C38, C42** | Magnet eddy loss at 1 234–2 131 Hz enters the loss ledger by mechanism; segmentation is the mitigation and retention joins it |
| J13 | **K4, K5** | The coercivity C38 requires can be bought through GBD — heavy rare earth at the grain boundaries — which is a cost lever with no design change. This is K5 evidence |
| J14 | **C26, C32, C40** | Mass removed from the ring pays twice (P9/C40 and the 14.7 kN per 0.1 kg retention chain); topology-optimised LPBF is the demonstrated route |
| J15 | **C22, C23, C25** | The bearing spec is procurable (thin-section, ABEC 5–7, preload control); confirmation stays with C25 by test |
| J16 | **K5, F-domain** | Tooling amortisation at 5 000/yr becomes a stated calculation (MIM, investment casting vs machining) rather than an assumption |
| J17, J18, J19 | **N3, F2, risk 27** | The spin-axis aperture is manufacturable as structure (LDS) and combinable by an established array technique (sequential rotation); the dual-band radome is a declared development item with precedents |
| J20 | **W12, H9** | The dump's resistor class exists at the required power density (AlN thick-film); the design rule is conduction out of the package |
| J22 | **C31, C26** | One-piece machining precedent for the ring/canards: joints removed, cant geometry held in one setup |
| J8, J23 | strategy only | Commercial state of printed windings; AM iron as development tool — cited to bound what may be claimed, never for a number |
| **J24–J28** | **K8, C47 (proposed)** | The post-treatment chain in citable form: HIP for porosity *with its strength cost* (J24/J25), roughness treatments measured (J26), thin-wall and tolerance limits bounded (J26b/J26c), in-situ monitoring's honest ceiling (J27), and the qualification shape itself (J28). This is what converts "we will 3D print it" into a defensible sentence |
| **J30** | **K8 (proposed)** | The robotic print–machine–handle cell is an industrial platform, not a concept drawing |
| **J31, J31b, J32** | **K8, H14/H15 (proposed), H5** | Print–pause–place–resume structural electronics; the conductivity bound that keeps power on copper; embedded FBG sensing as a qualification instrument. These carry the modular/redundant sensor-stack claim's *affordability* argument |
| **J29, J33, J34** | **K8, F2/N3, R12** | Part consolidation and on-demand production; printed graded dielectrics as a radome route; SLS post-treatment that makes a printed part end-use |
| **J35–J38** | **K8, C47 (proposed)** | The **defence** precedent set, found in the validation pass: funded US Army AM-for-munitions research, the Army's own statement on munitions/sensors/fuzes, the DoD's AM instruction, and a **criticality-based defence certification guide** (ASTM/UK-MoD). This is what turns "we will print it" into "this is how our industry qualifies printed parts" |
| **J39** | **K8, risk 50, H5** | **The upgrade that matters**: printed structural supports for circuit boards demonstrated for gun-launch high-G survivability. The printed-electronics claim moves from *proposal* to *demonstrated principle with project-specific qualification owed* — and it is now cited on the deck |
| **J40** | **K8 (proposed)** | The host's own direction — YIL fast-tracking custom ammunition hardware — so the low-volume cell argument lands on the PS owner's strategy rather than reading as a student novelty |

**The pass's own cautionary note, in the register's style:** the manufacturing dossier's most useful result is a *negative* one — at 2 130 Hz the copper skin depth is ≈1.4 mm, so printed copper is **not** required on AC-loss grounds; the conductor subdivision requirement comes from F15's ≥100 kHz converter switching (δ ≈ 0.21 mm), not from the machine. A cross-domain coupling (winding ↔ EMC) that no criterion owned until this pass.

---

## 4. The claim ledger

Every number the deck may put on a slide, and the source that owns it. `Cite` is the best available; where the best is ≤ 2 the claim is listed in §5 instead.

**Slide 1 — Problem statement**

| Claim | Owner | Cite |
|---|---|---|
| Unguided 155 mm CEP 267 m at max range (bracketed 259 / 139) | A1 (94/125/150/267 m), B1 | 5 |
| Dispersion grows with range — four points, not one | A1 | 5 |
| The requirement is CEP ≤ 30 m | A6 (threshold 50 / objective 30), H1 | 5 |
| The fielded kit reaches 30 m at every range and sub-10 m median | A1, A2 | 4 |

**Slide 2 — Proposed solution**

| Claim | Owner | Cite |
|---|---|---|
| Fuze-well retrofit: replaces the fuze and forward ogive only | A2 (intrusion 124.7 mm, visible 95.25 mm), F4 | 4 |
| De-spun canard assembly, fixed canards, no actuators, one moving part, no battery | **A1 — credited to the fielded kit, never claimed** | 5 |
| Two-pair canard split (steering + control), 2-D steering from one axis | B3, C9 — **credited** | 4 |
| Kit mass 1.4–1.7 kg; net +0.7–1.0 kg = 1.55–2.2× the fielded penalty | A2, A1 | 4 |
| Multi-mode fuze (proximity, time, impact) mapping to the Army RFI's three categories | A8 | 4 |
| Safe-and-arm: out-of-line rotor on setback + spin, no in-bore function | F3, D4 | 5 |
| Predicted-miss failsafe — **stated position** | A2 → F16 | 4 |

**Slide 3 — Technical approach**

| Claim | Owner | Cite |
|---|---|---|
| Impact-point-prediction guidance for a fixed-canard dual-spin airframe | **B2 — credited as published prior art** | 4 |
| The machine as both actuator and generator, no in-flight battery | A1 — credited; ours is the *sizing* | 5 |
| Ring as inertial platform (spin removed mechanically from the measurement) | B1 (names ring-angle feedback as the airframe's largest open problem), A3 (fielded design has no IMU) | 4 |
| Spin-invariant GNSS aperture on the spin axis | B1, A3 | 3 |
| State-dependent authority gate | B1 (the fixed-limit loss of control it answers), C4 | 4 |
| Cascade PI/P with DOB and clamping anti-windup | B1 | 5 |
| Coexistence by notch + current compensation | A3 (anti-jam fielding), B1 | 3 |
| Standards named (MIL-STD-1316 / 331C / 810F / 461, AOP-22, STANAG 4369 / AOP-39 / 4439 / 9216) | F1–F6 | 5 |

**Slide 4 — Feasibility**

| Claim | Owner | Cite |
|---|---|---|
| Error budget RSS 20.3 m → CEP 23.9 m | Own derivation (G4); method anchored in A6 | 3 |
| Navigation 3.7 m against a 5 m allocation | Own derivation (N1); lever-arm term now supported by B11 | 4 |
| Authority margin 1.11:1 (450 m available vs 407 m) | Own derivation (M7); bounded by B13, B14 | 4 |
| Minimum guidance force ≥ 18.1 N | Own derivation (C8); bounded by C3 | 4 |
| `Tf* = 0.1567 N·m` feasibility gate | E5, E6, E7 — **the row's weakest link, now supported** | 4 |
| Stability `Sg` 1.37–3.55, design point 1.83; canard ΔC_Mα ≤ 5 % | Own derivation (S1); frame from B7, B10, B15 | 4 |
| Span cap Ø151 mm + cant as the lever | **B5 — independently corroborates** | 4 |
| Resonance instability disposition | B4, B5, B7 | 4 |
| Setback 73.5 kN; air gap 0.40 mm → 367 / 122 N/µm | Own derivation (C26, C35); method from D4 | 3 |
| 2.92 kW peak / ≈121 kJ → ≥ 58 W/K interface | Own derivation (C42, W7, W12, P6); conductance basis E1 | 4 |
| Demand ≈12 W vs generation ≈20:1 | Own derivation (W4) | 3 |
| Cost ≤ ₹6.5 lakh at 5,000/yr | Own claim (K4), anchored to A2's US$13,541 and A4's class pricing | 4 |
| Monte Carlo ≈10 000 flights, worst corner 95 % bound | Own definition (R5); statistical basis stated | 3 |
| Bench rig capability | Own spec (R7); architecture precedent B8 | 4 |
| Range retention >90 % | A1 | 5 |
| Stator-core route traded on published loss **and** strength data (SMC 83 W/kg @ 1 T/1 kHz, TRS 60–100 MPa; 0.1 mm laminations purchasable) | J1, J2, J3 | 4 |
| Winding route bounded: printed copper 79 %/63 % fill and 87 % IACS after HT; hybrid end-winding −1/3 height, −0.564 kg | J4, J5 | 4 |
| Thermal joint is *manufactured*: cold-spray copper 98 % IACS / 368 W/mK as-sprayed; indium foil characterised against pressure and roughness | J9, J10 | 4 |
| Ring mass lever: topology-optimised LPBF precedent; 14.7 kN per 0.1 kg (C26) | J14, own derivation | 3 |

**Slide 5 — Impact (business case)**

| Claim | Owner | Cite |
|---|---|---|
| Rounds per target fall ≈74 % (fielded) — our derived figure beside it | A1, A4 | 5 |
| No adjustment fire | A4 | 4 |
| Unit cost ≈₹6.5 lakh vs a US$13,541 fielded competitor | A2, A1 | 4 |
| 100 000+ units produced fielded; our 5 000/yr is two orders smaller — **state the gap** | A2 | 4 |
| Business potential (§ weight) — volume, unit economics, ranked drivers, indigenous content, who pays | H1, H4, K5 | 4 |
| Magnet coercivity bought through grain-boundary diffusion — less heavy rare earth for the same SH/UH class | J13 | 3 |
| Tooling amortisation at 5 000/yr stated (MIM / investment casting vs machining), part families consolidated | J16 | 3 |
| Production-mature processes named for every subsystem; novel processes confined to development and declared | J1–J23 (section J) | 4 |

**Slide 6 — References.** Cite ≥ 3 only. Expected set: A1, A2, A4, A8, B1–B5, B7, B8, B11–B14, C2, C3, C9, D1, D4, E1, E3, E5, E8, F1–F5, G1, H1, H4. **If the manufacturing claims above are kept on slides 4–5, add J1 (SMC), J4/J5 (printed and hybrid windings), J9/J10 (cold-spray copper and the thermal joint) and J13 (grain-boundary-diffusion magnets)** — they carry those claims and nothing else does.

---

## 5. The gap list

Claims and rows with **no source at Cite ≥ 3**, with what would close them.

| # | Gap | Where | Closing route |
|---|---|---|---|
| 1 | **The 5 000 kits/year volume assumption** behind K4 | `register K4`, slide 5 | A2 gives the fielded volume (100 000+); the *share of national consumption* is YIL's to confirm post-selection. State the assumption, don't defend it as derived |
| 2 | **The ₹6.5 lakh build-up** (K5's ranked drivers at volume) | `register K5` | H4 (affordability class), A2/A4 (price anchors). The register already concedes K5 is the evidence; the gap is real and correctly stated |
| 3 | **`r_eff` = 30 m effective radius** behind M8 | `register M8` | Lethality data. Currently unverified; the claim is a sensitivity band, which is the honest form |
| 4 | **CG envelope spread 0.55–0.62 L** | `draft:100`, `dossier:329` | Needs a public source or a stated own analysis |
| 5 | **The reference model's mass properties** (calibrated on one published CAD set) | `02-reference-155mm-model.md`, risk 21 | Already declared as risks 20/21 with the P6 re-baseline as mitigation. Correctly bounded |
| 6 | **Bare-thread 3–16 W/K**, our own first-order estimate | `P6`, slide 4 | E1 gives the order of magnitude and the mechanism; the kit's *specific* joint still needs R7 item (7). Declared |
| 7 | **Aero coefficient set** | risk 8, P3 | The acknowledged long pole. Sources exist for the class (C3, B14) but not for our canard geometry; CFD gap-filling is the stated plan |

**No gap on this list may be silently filled.** Each is either cited, derived with a named assumption, or stated as a declared open verification — which is exactly the discipline the submission already follows for the five verifications it declares.

---

## 6. Cross-references

| File | Relationship |
|---|---|
| `submission/SIH26098-verified-source-audit.md` | What the sources **say** — the read-and-report record. This file is the value judgment on top of it |
| `design/06-manufacturing-and-process.md` | The manufacturing dossier — section J's consumer, and where the K5 process evidence lives |
| `design/00-design-criteria-register.md` | Where every Adopt ≥ 4 row lands: criteria, risks, decision log |
| `design/ROADMAP-and-prompts.md` | Carried item 15 tracks this register's follow-through into P5 |
| `submission/SIH26098-form-content.md`, `-template-slides.md`, `-draft-from-register.md` | The three files §3.4 and §3.5 change |
