# SIH26098 — Idea Submission Form Content

**Problem statement (official):** *Development of a Low-Cost Precision Guidance and Smart Electronic Fuze System for a 155 mm Artillery Shell*
**Organisation:** Ministry of Defence (MoD) — **Department:** Yantra India Limited, Ambajhari, Nagpur
**Category:** Hardware · **Theme:** Smart Vehicles · **Submission deadline:** 30 September 2026
**PS number:** SIH26098

This file holds every field the portal asks for, in paste-ready form. Character counts are verified at the bottom.

---

## FIELD 1 — Technology Bucket

**Select: `Smart Vehicles`**

SIH26098 is registered under the *Smart Vehicles* theme (17 themes exist in SIH 2026; the PS belongs to this one). If the dropdown on your form is a different list, pick the closest **hardware / embedded-systems** option and keep it consistent with the PS theme.

---

## FIELD 2 — Idea Title (max 100 characters)

Pick one. All three are under the limit.

| # | Title | Chars |
|---|---|---|
| **A** | DRISHTI-PGK: De-Spun Canard Guidance Kit with Multi-Mode Smart Fuze for 155 mm Shells | 85 |
| **B** | TRINETRA-PGK: Alternator-Actuated De-Spun Canards with Multi-Mode Fuze for 155 mm | 81 |
| **C** | Low-Cost De-Spun Canard PGK with Multi-Mode Electronic Fuze for 155 mm Artillery | 80 |

**Recommendation: A.** "DRISHTI" (vision / sight) carries the precision-guidance idea, "PGK" states the product class, and the rest echoes the PS vocabulary — *low-cost*, *canard*, *multi-mode*, *155 mm*. Judges skim titles against the problem statement; mirroring its words helps.

---

## FIELD 3 — Abstract / Summary (max 10,000 characters)

```
Conventional 155 mm artillery shells fly unguided ballistic trajectories. At long range their dispersion is large, so neutralising a point target demands volume fire — consuming ammunition, extending exposure and risking collateral damage. YIL already manufactures the mechanical hardware of these shells. What is missing is a kit that converts them into precision munitions without altering the shell itself.

We propose DRISHTI-PGK: a fuze-well-mounted precision guidance kit built around a de-spun canard ring. Four fixed-incidence canards are carried on a ring isolated from the projectile body by two bearings and free to rotate about the roll axis.

The canard arrangement is the basis of the control concept. Two canards at 0°/180° carrying equal cant angles produce codirectional aerodynamic forces: their roll torques cancel, leaving a net guidance force equal to twice one canard's force. Two canards at 90°/-90° carrying opposite cant angles produce opposing forces: zero net force, but a net roll torque about the body axis. Rotating the ring therefore aims the guidance-force vector anywhere in the plane normal to the shell axis — full two-dimensional steering from a single actuation axis, with no moving control surfaces.

The actuation is the key economy of the design. The ring carries the permanent magnets of an alternator and the body carries the stator coils, so the same machine that generates electrical power also generates control torque whenever its coils are loaded. There are no servo actuators, gearboxes or control-surface linkages, and no in-flight battery is required. This directly attacks the Size, Weight, Power and Cost constraint that governs the problem statement and removes the least reliable components of a conventional guided shell.

Guidance is by impact-point prediction: the flight computer propagates the current state to predicted impact, computes the miss, and commands a ring angle that nulls it, using a GNSS/INS solution, a barometric altitude channel and an onboard aerodynamic model. The de-spun ring also solves the hardest sensing problem in a spin-stabilised guided shell: with spin removed it is the natural mounting platform for the inertial sensor, so the navigation system sees the projectile's flight dynamics rather than a 15,000-20,000 rpm rotation that no flight-representative MEMS gyroscope can measure.

The nose assembly carries a multi-mode electronic fuze supporting proximity, time and impact modes, with an out-of-line safe-and-arm unit interlocked on setback and spin so it cannot arm in bore. All modes, the time-of-flight setting and the target data are written before firing over the gun line's existing inductive fuze setter, so the kit integrates with current firing procedure.

Verification follows three layers: a seven-degree-of-freedom trajectory simulation with a guidance loop in the loop and Monte Carlo dispersion analysis that derives CEP rather than asserting it; a hardware-in-the-loop bench with a rotating dynamometer rig that emulates aerodynamic torque and body spin; and a proof-of-concept assembly demonstrating ring-angle tracking under load.

Our design target is CEP of 30 m or better, carried by an error budget in which navigation and impact-point prediction — not canard authority — are the critical terms. Simulations of the 155 mm class show the canard control authority available is worth several hundred metres of impact correction, comfortably more than the dispersion being trimmed.
```

---

## FIELD 4 — Idea Description (max 50,000 characters)

```
====================================================================
1. PROBLEM UNDERSTANDING AND DESIGN DRIVERS
====================================================================

A 155 mm unguided shell at long range carries a circular error probable measured in hundreds of metres. Correcting this conventionally requires adjustment fire — observe, evaluate, re-engage — which consumes time, reveals the firing position and reduces the probability of destroying the target.

The problem statement sets out exactly what must be added: a Canard Actuation Assembly for in-flight trajectory correction; a Guidance, Navigation and Control system; a multi-mode electronic fuze with proximity, time and impact modes; embedded electronics and real-time flight-control software; power management for high-g launch and flight; and a pre-fire programming interface. The integrated system must reach CEP of 30 m or better while remaining compatible with the existing 155 mm shell and surviving launch and flight.

The governing design drivers we extracted are:

- Accuracy: CEP of 30 m or better at full charge and long range.
- Retrofit compatibility: the shell body, charge system and gun interface must not change. The kit occupies the fuze well and the forward ogive.
- Launch survival: high axial acceleration, radial shock, and spin in the 10,000-20,000 rpm band, followed by aerodynamic heating and 90 s of flight.
- SWaP-C: the problem statement explicitly asks for low Size, Weight, Power and Cost. Cost is the competitive premise of this product class.
- Safety and reliability: the fuze must be safe in storage, on the gun line, in bore and during ramming, and must arm only after launch.
- Modularity: clean interfaces so a future anti-jam GNSS or a different fuze module can be substituted without redesigning the kit.

====================================================================
2. SYSTEM ARCHITECTURE
====================================================================

The kit replaces the shell's fuze and forward ogive and comprises four modules on a common mechanical and electrical backbone:

  (a) Fuze module — nose tip. Proximity antenna, impact switch, safe-and-arm unit, fuze electronics and detonation train.
  (b) Canard Actuation Assembly — a de-spun ring carrying four fixed-incidence canards, mounted on two isolation bearings, carrying the alternator rotor magnets.
  (c) Guidance, Navigation and Control module — inertial measurement, GNSS receiver, barometric sensor, flight computer and the control loop.
  (d) Power module — alternator stator, rectifier and conditioning, reserve battery, energy management and the external programming interface.

The kit body is rigidly attached to the shell and spins with it. The canard ring is isolated by bearings and free to rotate about the roll axis, so the canard assembly is de-spun relative to the projectile body while remaining fully coupled to the airflow.

====================================================================
3. CANARD ACTUATION ASSEMBLY — DEPLOYMENT AND ACTUATION
====================================================================

3.1 Canard geometry and control concept

Four canards are mounted on the ring in two functional pairs:

- Steering pair at 0 deg and 180 deg, carrying equal cant angles. Their aerodynamic forces are parallel and codirectional, so their roll torques cancel while their forces add. The result is a net guidance force equal to twice a single canard's force, with no net roll torque.
- Control pair at 90 deg and -90 deg, carrying opposite cant angles. Their forces oppose, so there is no net force, but there is a net roll torque about the body axis.

Because the ring is free to rotate, the direction of the steering force in the plane normal to the shell axis is set by the ring's roll angle. Commanding that angle is therefore equivalent to commanding a two-dimensional guidance-force vector. This gives full planar steering from one actuation axis and eliminates the servo actuators, linkages and gearboxes that a conventional actuated-canard layout requires.

3.2 Actuation: the alternator as actuator

The ring carries permanent magnets; the body carries the stator coils. When the flight computer draws current from the coils it produces a reaction torque on the ring that opposes the aerodynamic torque. When it does not, the machine generates electrical power. One machine therefore performs both functions.

This yields three advantages that map directly onto the constraints:

- No control actuators — the least reliable and most expensive components of a guided projectile are removed.
- Recovered in-flight power — no battery has to carry the guidance load through a 90 s flight, which reduces weight and removes a large launch-survival risk.
- Only one moving assembly — the ring — which simplifies assembly, tolerance stack-up and qualification.

3.3 Torque balance and the ring design criterion

Three torques act on the ring: the aerodynamic torque from the control canards, which opposes the body spin and is unavoidable and flight-dependent; the bearing friction torque, which acts with the body spin; and the alternator reaction torque, which is the control input.

The design criterion is that control authority must be symmetric in both directions and must remain positive throughout flight:

- Symmetric authority requires the peak aerodynamic torque to be no more than half the sum of the maximum alternator torque and the friction torque.
- Minimum controllability requires the aerodynamic torque to exceed the friction torque at all times.

For a 155 mm shell the aerodynamic torque on the canard assembly rises to a few newton-metres over the flight while the bearing friction must be held to a fraction of a newton-metre. This makes bearing selection, preload and contamination control first-order design decisions, not details — the margin is thinnest near apogee where the aerodynamic torque collapses.

3.4 Deployment mechanism

The canards must be stowed flush within the kit envelope for magazine storage, ramming and in-bore travel, then deployed and positively locked after muzzle exit. The deployment is a one-shot mechanism and is distinct from the continuous ring actuation:

- Stowed flush and mechanically locked for in-bore safety, so the assembly cannot foul the bore or the rammer.
- Released by launch environment — setback and spin — with a spring-driven deployment.
- Positively locked at the deployed position by a detent so aerodynamic load cannot fold the canard back.
- A redundant lock ensures a canard cannot deploy partially, which would create an asymmetric force.

3.5 Launch survival

The isolation bearings and the ring retention carry the full setback load of the ring and canard assembly during launch, which is the governing structural load case for the CAA and the primary input to the bearing specification and the CAD structural analysis.

====================================================================
4. GUIDANCE AND NAVIGATION METHODOLOGY
====================================================================

4.1 Guidance law — impact point prediction

The flight computer runs an impact-point-prediction guidance law:

- Propagate the current navigation state forward to impact using the onboard aerodynamic and gravity model.
- Compare the predicted impact point with the target coordinates loaded before firing.
- Compute the required correction and convert it into a commanded ring angle, i.e. a direction for the guidance-force vector.
- Recompute continuously; the loop converges as the trajectory becomes better determined.

This is the correct law for this architecture for two reasons. First, the single controlled variable — ring angle — maps directly to a force direction, so the law's output is naturally the azimuth of the correction vector. Second, the available guidance force scales with dynamic pressure, so authority is high early and late in flight and vanishes at apogee. An impact-point-prediction law exploits the high-authority windows and does not demand control where none exists.

4.2 Navigation

The navigation solution fuses:

- GNSS position and velocity, for absolute accuracy and for the target-relative solution.
- An inertial measurement unit, for attitude, angular rate and continuity through GNSS outage or jamming.
- A barometric sensor, for altitude, which also improves the aerodynamic model's density estimate.
- Ring-angle sensing, which is the single most important measurement in this architecture because it defines the direction of the guidance force.

4.3 Solving spin-rate sensing — the de-spun ring as sensor platform

The hardest sensing problem in a spin-stabilised guided shell is that the body rotates at 10,000-20,000 rpm. No flight-representative MEMS gyroscope measures that rate, and a body-fixed inertial sensor either saturates or requires heavy compensation.

Our architecture resolves this structurally rather than by sensor specification. The canard ring is already isolated from body roll, so it rotates slowly relative to inertial space. Mounting the inertial sensor on the ring means it measures the projectile's coning and pitch/yaw motion with the spin removed — a conventional, low-rate attitude signal that a standard IMU can provide. The ring's own rotation is measured separately:

- Relative to the body, by a magnetic or inductive pickoff, which gives the ring angle used by the control loop.
- Absolutely, by a magnetometer referenced to the Earth's field, which gives the earth-referenced direction of the guidance force.

This combination is a genuine architectural advantage of the de-spun ring, and it converts the problem's largest sensing risk into a solved item.

4.4 GNSS under spin

A body-fixed antenna rotating at the shell's spin rate modulates the received signal amplitude and phase at the spin frequency. The antenna arrangement is therefore a first-class design item: either a spin-tolerant antenna pattern, an array with combined outputs, or an antenna mounted on the de-spun ring. GNSS denial is handled by graceful degradation — the navigation solution coasts on inertial data, and the guidance law continues to reduce dispersion to the limit of inertial drift.

====================================================================
5. FLIGHT CONTROL ALGORITHMS
====================================================================

5.1 Cascade structure

Ring angle is controlled by a cascade loop: an outer position controller sets a reference ring angular velocity, and an inner velocity controller commands alternator current.

- Inner velocity loop: proportional-integral, which provides zero steady-state error to a step and drives the effect of disturbance torques to zero.
- Outer position loop: proportional. The plant already contains an integrator, so proportional control is sufficient and avoids unnecessary phase lag.
- The inner loop is designed to settle at least five times faster than the outer loop, so disturbances are rejected before they reach the outer loop.

5.2 Disturbances and their rejection

Two disturbances act on the ring: the aerodynamic torque from the control canards and the spin of the projectile body, which is imposed through bearing friction. Both enter the plant and are rejected by the inner loop. Since they are not directly measurable with simple sensors, they are estimated with a disturbance observer and fed forward into the control law.

5.3 Adaptive limits — the key robustness measure

A fixed saturation limit is unsafe in this application, because the aerodynamic torque varies by more than an order of magnitude over the flight and the alternator's available current itself falls as relative speed changes. With fixed limits, control authority is lost in the low-torque region of the trajectory; the ring then overshoots badly and can enter a runaway rotation.

We therefore make every limit state-dependent rather than constant:

- The current limit is scaled to a multiple of the observed disturbance current, so the controller always has authority over the actual disturbance.
- The velocity limit is scaled proportionally to the same estimate, so the commanded ring velocity never exceeds what the alternator can achieve at the current operating point.
- Both limits are recomputed continuously from the measured relative velocity and the disturbance estimate.

This turns authority loss from a failure mode into a designed-in constraint, and it is the single most important robustness feature in the control design.

5.4 Anti-windup

Because output saturation is unavoidable and the dynamic limits change continuously, the integral term is protected by clamping anti-windup, so the controller leaves saturation immediately and without overshoot.

5.5 Control rate

The control loop runs at 1 kHz, which is well above the position-loop bandwidth required for guidance (a few hertz). Control bandwidth of this order is sufficient because guidance corrections are needed only while the projectile is off-trajectory, and near impact the ring may be allowed to free-wheel.

====================================================================
6. MULTI-MODE ELECTRONIC FUZE DESIGN
====================================================================

6.1 Modes

- Proximity mode: an RF Doppler proximity sensor with a selectable burst height, giving airburst effects against personnel and soft targets.
- Time mode: a crystal-controlled timer, programmable before firing, giving airburst at a computed time of flight and scoring against targets in defilade or under cover.
- Impact mode: a crush/inertial switch with selectable delay, for point and hardened targets and for graze function.

6.2 Safe-and-arm

The fuze uses an out-of-line safe-and-arm unit in which the detonator is mechanically misaligned from the explosive train until arming. Arming requires two independent environmental interlocks — the setback of launch and the spin of the projectile — so the fuze cannot arm in storage, during handling, in the bore or during ramming. A pyrotechnic or electromechanical delay after muzzle exit provides an arming distance. If either interlock is absent the fuze remains safe and the round functions as a non-guided shell.

6.3 Pre-fire programming interface

All configuration is written before firing over the gun line's existing inductive fuze setter, with no tools and no modification to existing firing procedure. The data package carries:

- Fuze mode (proximity, time or impact) and the associated setting.
- Time of flight for time mode.
- Target coordinates, muzzle velocity and meteorological data for the guidance solution, since an impact-point-prediction law must know where it is trying to arrive.

The interface is also the software upload and built-in-test port for maintenance.

6.4 Coexistence with the guidance system

The proximity sensor, the magnetometer used for ring-angle measurement and the alternator share one nose assembly, so electromagnetic compatibility is designed in rather than tested in: shielded and partitioned compartments, separated frequency planning for the proximity and setter channels, and a shared timing reference so that the alternator's switching does not appear as a false target to the proximity sensor. The fuze and guidance electronics share a processor and a power rail, which reduces part count and cost.

6.5 Dormancy and function

The fuze has no single-point electronic failure that prevents the round from functioning: loss of guidance, loss of GNSS or loss of the setter write all degrade accuracy but leave a live, functioning fuze.

====================================================================
7. SENSOR SELECTION
====================================================================

  Function                  Sensor                      Rationale
  ------------------------  --------------------------  ------------------------------------------
  Guidance force direction  Ring angle pickoff          Defines where the steering force points
                            (magnetic/inductive) +      and is the primary control feedback
                            magnetometer                variable
  Attitude and rate         IMU mounted on the          Spin removed by the de-spun ring, so a
                            de-spun ring                conventional IMU suffices
  Absolute position,        GNSS receiver with          Absolute accuracy and target-relative
  velocity                  spin-tolerant antenna       solution
  Altitude and air density  Barometric sensor           Improves the aerodynamic model and the
                                                        impact prediction
  Body spin rate            Magnetic or optical         Needed for the control limit scheduling
                            pickoff on ring relative    and for fuze arming interlock
                            to body
  Burst height              RF Doppler proximity        Standard, robust in weather and
                            sensor                      obscurants
  Impact                    Crush / inertial switch     Independent of all electronics
  Temperature               Board and external          Aerodynamic heating and thermal
                            thermistors                  compensation of sensors

Sensors are selected for availability in the domestic supply chain, for rated shock, and for operation over the storage and flight temperature range. The inertial and barometric sensors are mounted in a shock-isolated, potted module.

====================================================================
8. EMBEDDED HARDWARE ARCHITECTURE
====================================================================

8.1 Processing

A dual-domain architecture separates hard real-time control from navigation and guidance:

- A microcontroller core runs the 1 kHz control loop, the alternator current loop, the safe-and-arm logic and the fuze timing. This path must be deterministic and is written as bare-metal or on a real-time operating system with fixed priorities.
- A second core or a small FPGA handles the navigation filter, the guidance law and the impact-point prediction, which need floating-point throughput but tolerate longer latency.

8.2 Signal chain

  - IMU and magnetometer on the ring: synchronous serial interface with a slip-free or short-range coupling across the bearing.
  - GNSS receiver: serial interface, with time synchronisation to the flight computer.
  - Barometric sensor and thermistors: analogue to digital conversion.
  - Alternator: three-phase rectification followed by a controlled current sink driven by the velocity loop output.
  - Fuze: firing discretes, arming interlocks, and the inductive setter interface.
  - Power: regulated rails with monitoring and brown-out protection.

8.3 Software architecture

  - Deterministic control task at 1 kHz with fixed execution budget.
  - Navigation and guidance task.
  - Disturbance observer and limit scheduling.
  - Fuze manager: mode selection, timing, arming logic, firing decision.
  - Built-in test, health monitoring, watchdog and flight-event logging for post-flight analysis and for evidence in trials.

====================================================================
9. POWER SUPPLY AND ENVIRONMENTAL PROTECTION
====================================================================

9.1 Generation in flight

The alternator provides electrical power throughout flight, because the shell is still spinning at a substantial rate at impact. Rated continuous power, winding resistance, inductance and the torque constant are set by the same sizing exercise as the actuation requirement, so power generation and control authority are designed together rather than traded against each other.

9.2 Pre-launch and safe state

The kit must be inert and safe before launch, so it is unpowered in storage and on the gun line. A reserve battery, activated by the launch environment, provides power for the fuze, the safe-and-arm logic and the boot sequence until the alternator takes over. This is also the safety enabler: no power means no arming path.

9.3 Energy management

The control torque on the ring is produced by dissipating electrical energy. In flight there is no load bank to absorb it, so the control power is managed explicitly by an active dissipation stage, with the option to recover part of it to charge the reserve battery or a supercapacitor.

9.4 Environmental protection

- Shock and acceleration: electronics potted and encapsulated with no free mass; the inertial module shock-isolated; all leaded or large components avoided.
- Vibration: conformal coating, staked components, and a packaging scheme qualified by test rather than analysis alone.
- Thermal: aerodynamic heating at the nose is the driving case; thermal mass, a potting compound with a defined conductivity, and thermal compensation of sensor biases. Storage and operating temperature ranges are stated and verified.
- Humidity, salt fog and corrosion: sealed assembly with a controlled internal environment.
- Electromagnetic: designed to standard electromagnetic compatibility practice for a fuze and a switching power stage in one volume.
- Qualification approach: environmental and shock testing against the applicable defence standards for artillery fuzes, with a shock-sled or air-gun test for launch-survival verification.

====================================================================
10. SIMULATION AND VALIDATION METHODOLOGY
====================================================================

10.1 High-fidelity trajectory model

A six-degree-of-freedom model of the shell is extended to seven degrees of freedom to represent the de-spun ring as an independent roll body. The model is written in a body-fixed plane reference frame in which the Euler roll is identically zero, which keeps the guidance and control formulation clean and avoids the long simulation times caused by resolving the high-frequency roll motion. The model includes aerodynamic forces and moments, Magnus effects, pitch and yaw damping, roll damping, gravity, and the additional force and torque terms generated by the canards.

10.2 Aerodynamic data

Aerodynamic coefficients for the shell body and for the canard assembly are compiled as functions of Mach number and angle of attack and sideslip, not as a sparse table, because the guidance law depends on accurate force and moment prediction throughout the flight. The coefficient set is assembled from published 155 mm data for the body and from canard data for the kit, with computational fluid dynamics used to fill gaps and to verify the canard interference case. Coefficient uncertainty is carried explicitly so that its contribution to CEP can be quantified.

10.3 Monte Carlo dispersion analysis

This is how the CEP claim is produced. The simulation is run over a statistical population in which the following are varied according to their expected distributions:

- Muzzle velocity and charge temperature.
- Meteorological conditions: wind profile, air density, temperature.
- Target location error and survey error.
- Launch perturbations: elevation, azimuth and initial angular rates.
- Aerodynamic coefficient uncertainty and sensor noise.

Each run produces an impact point; the resulting two-dimensional distribution gives the CEP directly. This allows every error source to be traced to its contribution, so the budget can be actively managed rather than asserted.

10.4 Hardware-in-the-loop

The ring control loop is exercised against a live trajectory: the simulated flight state generates the aerodynamic torque and the body spin rate, the controller acts on the real ring hardware, and the ring's measured angle is fed back into the trajectory. This closes the loop that pure simulation leaves open and is where authority losses and limit-scheduling errors appear.

10.5 Bench dynamometer rig

A rotating test rig reproduces the two loads that matter on the bench: aerodynamic torque on the ring, applied by a torque motor, and body spin, applied by a speed motor, with a programmable load absorbing the control power. This allows the actuation concept, the disturbance observer, the adaptive limits and the anti-windup behaviour to be verified on hardware before flight, and it produces the measured alternator constant and friction data used to close the design.

====================================================================
11. PERFORMANCE ESTIMATION — PATH TO CEP OF 30 m OR BETTER
====================================================================

11.1 Guidance authority is sufficient

The guidance force available from the canard pair scales with dynamic pressure. For the 155 mm class the control force reaches approximately 85 N in the launch transient and holds a band of approximately 15 to 25 N through mid-flight, falling towards zero at apogee and returning to approximately 20 N during descent.

Taking 20 N on a 43 kg shell gives a lateral acceleration of approximately 0.47 m/s^2. Applied over the available guided window this corresponds to a velocity change of the order of 18 m/s, and an impact displacement of the order of several hundred metres. The dispersion being corrected is of a comparable order. Guidance authority is therefore not the limiting factor.

11.2 The CEP budget

Accuracy is budgeted in one-sigma radial terms and combined in root-sum-square, with CEP related to the radial standard deviation by the standard circular relationship.

  Error source                                         1-sigma allocation
  ---------------------------------------------------  ------------------
  Navigation (GNSS/INS) at impact                            5 m
  Guidance and control (prediction, ring angle, force)      15 m
  Meteorological and muzzle-velocity residual               10 m
  Remaining aerodynamic and model uncertainty                8 m
  Fuze and detonation dispersion                              3 m
  ---------------------------------------------------  ------------------
  Root-sum-square                                            20.4 m
  Implied CEP (1.1774 x sigma)                             ~24 m

The budget closes with margin against the 30 m requirement.

11.3 Where the margin comes from, and where the risk sits

The budget makes clear that the dominant term is guidance and control, not raw navigation and not canard force. The three measures that protect it are: an accurate aerodynamic model so that impact prediction is trustworthy; the adaptive, state-dependent limits so that authority is never lost; and the ring-angle measurement, because an error in ring angle is a direct error in the direction of the guidance force.

11.4 Graceful degradation

With GNSS degraded, the navigation solution coasts on inertial data and the correction accuracy degrades smoothly towards the inertial drift limit rather than failing. With guidance unavailable, the round remains a functioning ballistic shell with a working fuze. There is no failure mode in which the kit makes accuracy worse than the unguided baseline.

====================================================================
12. MANUFACTURABILITY AND COST OPTIMISATION
====================================================================

This architecture is deliberately chosen to be cheap to make, because cost is the competitive premise of the problem statement and because YIL's advantage is precision mechanical manufacturing at volume.

- No control actuators, no gearboxes, no servo electronics and no control-surface linkages. The single moving assembly is the canard ring on two bearings.
- The alternator is the only electromechanical machine, and it is built from standard magnet and winding fabrication.
- The fuze and guidance electronics share a processor, a power supply and a housing, so the part count is well below that of a conventional guided projectile.
- No in-flight battery to qualify for a 90 s high-vibration flight, and no battery thermal management.
- The kit occupies the fuze well and forward ogive only, so YIL's existing shell body, charge system, driving band and gun interface are untouched and no re-qualification of the shell is required.
- The design is dimensionally parametric in kit mass and centre of gravity, so it can be matched to the full family of 155 mm shells YIL produces without redesigning the control concept.

The dominant cost drivers are therefore the bearings, the magnets and windings, and the electronics — all of which are conventional, sourced, and reducible by volume.

====================================================================
13. CONSTRAINT COMPLIANCE
====================================================================

  Compatibility with existing 155 mm shell
    The kit is a fuze-well and ogive replacement only. Kit mass, centre of
    gravity and axial inertia are treated as design variables and are held
    within the limits that preserve the shell's gyroscopic stability across
    the charge and temperature envelope. The canards are stowed flush for
    ramming and in-bore travel.

  High launch acceleration, vibration, spin and environment
    Structural load cases are taken from the launch environment. Bearings,
    ring retention and the stowage locks are designed for the governing
    setback and spin cases. Electronics are potted and the inertial module
    is shock-isolated. Verification is by bench rig, shock sled and
    environmental test.

  Low Size, Weight, Power and Cost
    Single moving assembly, no actuators, no in-flight battery, shared
    processor and power supply, and unchanged shell hardware.

  High reliability and safety
    Out-of-line safe-and-arm unit with dual environmental interlocks,
    no arming path without launch power, independent impact switch, and
    graceful degradation in every electronic failure mode.

  Modularity and future upgrade
    Four modules on a common mechanical and electrical backbone: fuze,
    canard actuation assembly, GNC and power. A future anti-jam GNSS, an
    improved seeker or a different fuze can be substituted at module level.

====================================================================
14. PROOF OF CONCEPT PLAN
====================================================================

The preferred deliverable is a prototype or proof of concept. Our plan builds it in three steps, in order of information gained per rupee spent:

  Step 1 - Simulation (no hardware). Seven-degree-of-freedom trajectory
  model with the guidance loop in the loop, and the Monte Carlo dispersion
  analysis that produces the CEP estimate and the error budget. Delivers
  the trajectory-correction demonstration, the guidance and control
  algorithm, and the performance estimation.

  Step 2 - Bench demonstrator. A reduced rotating dynamometer rig: the
  canard ring on its bearings, an alternator, a motor to impose relative
  spin, a torque motor to impose the aerodynamic torque profile, a
  programmable load, and a magnetometer and pickoff for ring-angle
  measurement. Demonstrates closed-loop ring-angle tracking under applied
  disturbance, the disturbance observer, the adaptive limits and the
  anti-windup behaviour. This is the proof of concept that the constraints
  are achievable in hardware.

  Step 3 - Integration demonstrator. Fuze module and GNC module integrated
  on the common backbone, with the inductive programming interface
  exercised end to end, mode selection verified, and the safe-and-arm
  logic functionally demonstrated under simulated setback and spin.

  Deliverables produced along the way: system architecture document,
  CAD model of the canard actuation assembly with structural analysis
  under the launch load case, electronics block diagram, guidance and
  control algorithm with simulation results, and the performance
  estimation.

====================================================================
15. SUMMARY OF NOVELTY
====================================================================

- Actuation and power generation by a single machine: the alternator
  reacts against the ring to steer it and generates the kit's electrical
  power, removing all control actuators and the in-flight battery from a
  guided artillery projectile.
- Full two-dimensional guidance from one actuation axis, using fixed
  canards in a steering pair and a control pair, so no control surface
  moves.
- The de-spun ring used as the inertial sensing platform, converting the
  spin-rate measurement problem into a conventional low-rate navigation
  problem.
- Impact-point-prediction guidance law synthesised for a control channel
  whose authority varies by more than an order of magnitude over the
  flight, with state-dependent saturation limits that make authority loss
  a designed constraint rather than a failure mode.
- A three-mode electronic fuze integrated into the same nose assembly as
  the guidance kit and configured over the gun line's existing inductive
  fuze setter, so no change to firing procedure is required.

====================================================================
16. REFERENCES
====================================================================

1. G. Gunay, "Controller Design and Implementation for a Guidance Kit
   Used at Spinning Rockets and Projectiles," M.Sc. thesis, Middle East
   Technical University, 2022.
2. X. Zhang, X. Yao and Q. Zheng, "Impact point prediction guidance based
   on iterative process for dual-spin projectile with fixed canards,"
   Chinese Journal of Aeronautics, vol. 32, no. 8, 2019.
3. P. Wernert and S. Theodoulis, "Modelling and stability analysis for a
   class of 155 mm spin-stabilized projectiles with course correction
   fuze," AIAA Atmospheric Flight Mechanics Conference, 2013.
4. L. Wang, Z. Wang and Z. Yu, "Influence of control strategy on stability
   of dual-spin projectiles with fixed canards," Defence Technology,
   vol. 14, no. 6, 2018.
5. G. Clancy, T. Bybee and D. Friedrich, "Fixed canard 2-D guidance of
   artillery projectiles," US Patent 6,981,672, 2006.
6. J. Robinson and F. Berefelt, "On Guidance and Control for Guided
   Artillery Projectiles," FOI, Sweden, 2011.
7. G. Khalil, A. Abdalla et al., "Dispersion analysis for spinning
   artillery projectile," 2009.
8. R. Spagni, S. Theodoulis and P. Wernert, "Flight control for a class of
   155 mm spin-stabilized projectile with reciprocating canards," AIAA
   Guidance, Navigation and Control Conference.
9. US Army DOT&E, "Precision Guidance Kit (PGK)", FY2015 Annual Report.
10. NATO STANAG 4369 / AOP-39 guidance for fuze design, safety and
    insensitive munitions assessment.
```

---

## Character count verification

| Field | Limit | Actual | Headroom | Status |
|---|---|---|---|---|
| Idea Title (A) | 100 | 85 | 15 | OK |
| Idea Title (B) | 100 | 81 | 19 | OK |
| Idea Title (C) | 100 | 80 | 20 | OK |
| Abstract / Summary | 10,000 | 3,491 | 6,509 | OK |
| Idea Description | 50,000 | 34,769 | 15,231 | OK |

Counts are measured from the text inside the code fences above, not estimated.

---

## Note on the template PDF

The portal's **Download Template** produces the SIH *Idea Presentation Format* — a six-page (six-slide) PDF with these sections:

1. Problem Statement
2. Proposed Solution
3. Technical Approach
4. Feasibility Analysis
5. Impact Assessment
6. References

Download that file from the form and drop it into this repo so the PDF can be laid out to match exactly. The slide-by-slide content is drafted in `SIH26098-template-slides.md`.
