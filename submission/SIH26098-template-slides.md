# SIH26098 — Idea Presentation Format (6-slide template)

Content laid out for the SIH *Idea Presentation Format* PDF that must be uploaded with the submission. The portal caps this at **10 MB, PDF format**.

**Structure:** 1 Problem Statement · 2 Proposed Solution · 3 Technical Approach · 4 Feasibility Analysis · 5 Impact Assessment · 6 References

**Style rules SIH gives:** prefer points and diagrams over paragraphs, and keep to six slides. Each slide below carries the bullet text plus a note on the visual it needs — the diagrams do most of the scoring work on this sheet, so budget real effort for them.

---

## SLIDE 1 — Problem Statement

**Title:** 155 mm Artillery Is Unguided — and That Costs More Than Accuracy

- Conventional 155 mm shells follow ballistic trajectories. Dispersion grows with range, reaching hundreds of metres at long range.
- Neutralising a point target therefore needs volume fire: many rounds, long engagement time, and unavoidable collateral damage.
- The inefficiency compounds — adjustment fire requires observation and re-engagement, exposing the firing battery and revealing intent.
- YIL already manufactures the mechanical hardware of the 155 mm shell. **The missing capability is a guidance and fuze kit that bolts onto it.**
- The requirement: **CEP ≤ 30 m**, compatible with the existing shell, surviving launch and flight, at low Size, Weight, Power and Cost.

**Visual:** Two impact patterns side by side on a range map — the wide unguided dispersion ellipse versus a tight 30 m guided cluster, with rounds-per-target shown under each. This one image frames the entire problem.

---

## SLIDE 2 — Proposed Solution

**Title:** DRISHTI-PGK — A De-Spun Canard Guidance Kit with an Integrated Multi-Mode Fuze

- **A fuze-well-mounted kit** that replaces only the fuze and forward ogive. The shell body, charge system and gun interface are untouched.
- **Four fixed canards on a de-spun ring**, isolated from the spinning shell by two bearings. No control surface moves.
- **Canard split:** a 0°/180° steering pair with equal cant produces a net guidance force with zero roll torque; a 90°/−90° control pair with opposite cant produces zero net force and a net roll torque. Rotating the ring aims the guidance force anywhere in the plane — **two-dimensional steering from one actuation axis**.
- **The alternator is the actuator.** Magnets on the ring, coils on the body: drawing current produces control torque; not drawing current generates power. **No servos, no gearboxes, no in-flight battery.**
- **Multi-mode electronic fuze** — proximity, time and impact — sharing the nose with the guidance electronics and configured over the gun line's existing inductive fuze setter.

**Visual:** Exploded/annotated view of the kit — fuze module at the tip, canard ring on its bearings, alternator, GNC and power modules — plus the inset canard-force diagram showing the steering pair (net force) and control pair (net torque).

---

## SLIDE 3 — Technical Approach

**Title:** Impact-Point-Prediction Guidance, Spin-Free Navigation, Adaptive Control

**Guidance and navigation**
- **Impact-point-prediction guidance law:** propagate the navigation state to predicted impact, compute the miss against the loaded target coordinates, and command a ring angle that nulls it. Recomputed continuously.
- **De-spun ring as the inertial platform.** With spin removed, the ring sees the projectile's coning motion rather than a 15,000–20,000 rpm rotation. This converts the hardest sensing problem in a spin-stabilised guided shell into a conventional low-rate navigation problem.
- **Ring-angle sensing** defines the direction of the guidance force: a magnetic/inductive pickoff for the body-relative angle used by the control loop, and a magnetometer for the earth-referenced angle used by guidance.
- **Fusion:** GNSS + IMU + barometric altitude, with graceful degradation to inertial coasting under GNSS denial.

**Flight control**
- Cascade loop: **PI inner velocity, P outer position**, inner loop designed to settle ≥5× faster than the outer.
- **Disturbance observer** estimates the unmeasurable aerodynamic and friction torques and feeds them forward.
- **State-dependent saturation limits.** The aerodynamic torque varies by more than an order of magnitude over the flight and the alternator's available current falls with relative speed. Fixed limits lose control authority near apogee, so current and velocity limits are scaled continuously to the observed disturbance — authority loss becomes a designed constraint, not a failure mode.
- **1 kHz control loop** with clamping anti-windup.

**Fuze and power**
- Out-of-line safe-and-arm unit with **dual environmental interlocks (setback + spin)** — cannot arm in storage, handling, bore or ramming.
- Reserve battery for pre-launch and safe state; **alternator takes over in flight**; control energy managed by an active dissipation stage.

**Visual:** Two panels — a control block diagram (guidance law → ring angle command → cascade PI/P → alternator current → plant, with the disturbance observer and adaptive limits drawn in), and a system layout showing sensor, actuator and power blocks.

---

## SLIDE 4 — Feasibility Analysis

**Title:** The CEP Budget Closes, and the Hardware Concept Is Already Proven

**Accuracy closes on paper**

| Error source | 1σ allocation |
|---|---|
| Navigation (GNSS/INS) at impact | 5 m |
| Guidance and control (prediction, ring angle, force) | 15 m |
| Meteorological and muzzle-velocity residual | 10 m |
| Remaining aerodynamic / model uncertainty | 8 m |
| Fuze and detonation dispersion | 3 m |
| **Root-sum-square** | **20.4 m** |
| **Implied CEP (1.1774 σ)** | **≈ 24 m** |

**Guidance authority is not the limit**
- Canard force holds a ≈15–25 N band through mid-flight (±85 N in the launch transient, ≈0 at apogee).
- ≈20 N on a 43 kg shell → ≈0.47 m/s² lateral. Over the guided window that is ≈18 m/s of velocity change, worth several hundred metres of impact correction — comfortably more than the dispersion being trimmed.
- **The binding constraints are navigation quality and impact-point-prediction accuracy, not canard force.** The design effort is placed accordingly.

**Technical feasibility**
- The de-spun-ring-with-alternator actuation concept, its torque-authority criteria and its control architecture have been **validated on hardware for the 155 mm class** in published research, including the low-torque near-apogee region where fixed control limits fail.
- Aerodynamic coefficients: published 155 mm body data plus canard data, with CFD to fill gaps and verify canard interference. Coefficient uncertainty is carried explicitly into the Monte Carlo so its CEP contribution is quantified rather than assumed.

**Validation methodology**
- 7-DOF trajectory simulation with the guidance loop in the loop, in a body-fixed-plane frame.
- **Monte Carlo dispersion analysis produces the CEP** — the claim is derived, not asserted — varying muzzle velocity, meteo, target location error, launch perturbation and coefficient uncertainty.
- Hardware-in-the-loop, closing ring angle back into flight parameters.
- Rotating dynamometer bench rig emulating aerodynamic torque and body spin, with a programmable load.

**Cost and manufacturability**
- One moving assembly. No actuators, gearboxes, linkage electronics or in-flight battery.
- Fuze and guidance share a processor, power supply and housing.
- Existing shell body, charge system and driving band unchanged — **no re-qualification of the shell**.
- Cost drivers are bearings, magnets/windings and electronics — all conventional and volume-reducible.

**Visual:** The error budget as a waterfall or bar chart showing each contribution to the 20.4 m RSS, plus a small chart of available canard force versus time with the guided window shaded.

---

## SLIDE 5 — Impact Assessment

**Title:** First-Round Precision at Volume Cost, Built on Existing Indian Hardware

**Operational**
- **CEP ≤ 30 m** means first-round effects on point targets: the rounds-per-target figure falls by roughly an order of magnitude against unguided fire.
- **No adjustment fire.** The engagement is shorter, the battery is exposed for less time, and the firing signature is smaller.
- **Reduced collateral damage**, which matters both operationally and in the political and legal context of employment.
- Rounds not fired are logistics not moved — a direct reduction in ammunition consumption and supply-chain burden.

**Strategic and indigenous**
- The kit converts an existing shell stockpile into a precision capability **without a new shell, new charge system or new gun**.
- Manufacture is aligned with YIL's core competency — precision mechanical hardware — with electronics and sensing added as a defined, bounded scope.
- Addresses a capability currently available only through import, at a fraction of the unit cost of imported precision guidance kits.

**Future progression**
- Modular backbone allows subsequent anti-jam GNSS, an improved seeker or a different fuze module without redesigning the kit.
- The same architecture extends to other calibres and to spin-stabilised rocket projectiles.

**Visual:** Before/after comparison — rounds required per target and resulting collateral radius — plus an indication of unit cost relative to an imported kit.

---

## SLIDE 6 — References

1. G. Günay, *Controller Design and Implementation for a Guidance Kit Used at Spinning Rockets and Projectiles*, M.Sc. thesis, Middle East Technical University, 2022.
2. X. Zhang, X. Yao and Q. Zheng, "Impact point prediction guidance based on iterative process for dual-spin projectile with fixed canards," *Chinese Journal of Aeronautics*, vol. 32, no. 8, 2019.
3. P. Wernert and S. Theodoulis, "Modelling and stability analysis for a class of 155 mm spin-stabilized projectiles with course correction fuze," *AIAA Atmospheric Flight Mechanics Conference*, 2013.
4. L. Wang, Z. Wang and Z. Yu, "Influence of control strategy on stability of dual-spin projectiles with fixed canards," *Defence Technology*, vol. 14, no. 6, 2018.
5. G. Clancy, T. Bybee and D. Friedrich, "Fixed canard 2-D guidance of artillery projectiles," US Patent 6,981,672, 2006.
6. J. Robinson and F. Berefelt, *On Guidance and Control for Guided Artillery Projectiles*, FOI, Sweden, 2011.
7. G. Khalil, A. Abdalla et al., "Dispersion analysis for spinning artillery projectile," 2009.
8. R. Spagni, S. Theodoulis and P. Wernert, "Flight control for a class of 155 mm spin-stabilized projectile with reciprocating canards," *AIAA GNC Conference*.
9. US Army DOT&E, *Precision Guidance Kit (PGK)*, FY2015 Annual Report.
10. Problem statement SIH26098, Ministry of Defence / Yantra India Limited, Smart India Hackathon 2026.

---

## To generate the PDF

The portal's own template file is the exact layout to match. Download it from the form ("Download Template") and drop it in this folder — the six slides above then get laid out into it directly.
