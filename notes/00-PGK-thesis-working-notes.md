# Working Notes — "Controller Design and Implementation for a Guidance Kit Used at Spinning Rockets and Projectiles"

**Source:** `10463953.pdf` — MSc thesis, Görkem Günay, Mechanical Engineering, METU (Middle East Technical University), April 2022. Supervisors: Prof. Dr. Raif Tuna Balkan, Assist. Prof. Dr. Hakan Çalışkan. 169 pages (26 front matter + 143 body/appendix), LaTeX/pdfTeX.

**Why this document is in this folder:** it is the closest engineering reference to a **PGK (Precision Guidance Kit)** for spin-stabilized artillery — M.Sc.-level, fully instrumented, with a physical test rig, flight dynamics simulation, controller design, and validation data. It gives us a validated *architecture*, a *control-authority criterion*, and a *hard number set* we can design against.

**Status of these notes:** everything below is extracted from the PDF text layer + visual inspection of the figures. Derived numbers I computed myself are marked **[derived]**. Numbers that the thesis quotes but does not source (aero coefficients) are marked **[not in thesis]**.

---

## 1. TL;DR — the ten things that matter

1. **The guidance method is "fixed canards on a de-spun ring."** Four fixed-incidence canards sit on a ring that is *free to rotate about the roll axis, isolated from the body by bearings*. There are **no moving control surfaces**. The single actuation axis is the ring's roll angle.
2. **The actuator is the alternator itself.** Rotor magnets on the ring, stator coils on the body. By loading the alternator you generate a reaction torque. The same machine also **generates electrical power** — no battery needed (a stated advantage over canard-actuator designs).
3. **Steering comes from cant angle, not deflection.** Two canards at 0°/180° (= *steering canards*, same cant angle) produce **equal, codirectional forces** → their roll torques cancel, and they leave a **net translational force** (guidance force). Two canards at 90°/−90° (= *control canards*, opposite cant angles) produce **opposing forces** → **zero net force, net roll torque**. Rotating the ring aims the steering-force vector, which is 2-D guidance.
4. **Torque balance is the whole design problem.** On the ring: `Taero` (−X, unavoidable, flight-dependent) vs `Talt + Tf` (+X, controllable + friction). Position control = keeping the ring angle while these fight each other.
5. **Control-authority criteria (the key design rule, Ch. 6):**
   - Symmetric control in ± directions: `Taero ≤ (Talt_max + Tf) / 2` → their number: `(5.76 + 0.1)/2 = 2.93 N·m`
   - Minimum controllable: `Taero > Tf` → their number: `0.1 N·m`
   - **At apogee `Taero` collapses to 0.17 N·m while `Tf = 0.1 N·m` — only 1.7× margin. Friction budget and low-torque behavior dominate the design.**
6. **Control architecture: cascade PI(velocity, inner) + P(position, outer).** Velocity loop `0.29 + 7.82/s`, position loop gain `29.7`. Achieved 33.6 Hz velocity / 6.2 Hz position bandwidth (requirements were 20 Hz / 4 Hz).
7. **The discovered failure mode:** with fixed saturation limits, control is *lost between 30 s and 50 s* of flight (near apogee) — low `Taero` can't slow the ring, so it makes large overshoots and can run away into full rotation (non-linear instability).
8. **Fix = disturbance observer + dynamic saturation limits.** A frequency-domain DOB `û_d = Q(s)·(Ĝ⁻¹·y − u)` feeds a *dynamic current limit* (2× observed disturbance current) and a *dynamic velocity limit* (`26 rad/s per A`). Combined solution → no overshoot, symmetric response. Verified on hardware.
9. **Flight envelope from their 155 mm simulation:** spin 1623 → ~1050 rad/s over ~87 s; `Taero` 1.8 N·m at launch → 0.17 N·m at apogee (t≈41 s) → 2.12 N·m at t≈86 s; control forces ≈ ±15–25 N.
10. **What the thesis deliberately does NOT do: any guidance law.** It is an *actuation/feasibility* study only. Trajectory shaping, impact-point prediction, guidance law, HIL — all left as "future work." **That is the space our design occupies.**

---

## 2. The architecture, in detail

### 2.1 Three mechanical assemblies

| Colour in Fig. 2.2 / 2.3 | Part | Behaviour |
|---|---|---|
| **Green** | Guidance kit body + projectile body | Rigidly attached to the projectile; **rotates with the body** (up to ~20 000 rpm) |
| **Orange** | Nose / ogive | **Fixed to the green part** — it spins with the body |
| **Blue** | Canard ring ("rotor of the alternator") | Carries the 4 fixed canards and the alternator **magnets**. Isolated by **two bearings**; free to rotate about X relative to the body |

Because *both* halves rotate, the thesis explicitly notes the classical rotor/stator convention does not apply: **"the part with the permanent magnets = rotor; the part with the coils = stator."** The stator is bolted to the spinning body; the rotor carries the canards.

*Figure: `figures/p36-fig2.1-2.2-projectile-with-gk-and-preliminary-design.jpg` and `figures/p37-fig2.3-gk-section-view.jpg`*

### 2.2 Canard arrangement (the clever bit — Fig. 2.4)

Looking down the X axis, ring viewed from the front:

| Positions | Name | Cant angles | Force result | Torque result |
|---|---|---|---|---|
| 0° and 180° (on Z axis) | **Steering canards** | **same** | Forces are **parallel and codirectional** → **net force = 2 × F_aero** | Roll torques cancel → **no net torque** |
| 90° and −90° (on Y axis) | **Control canards** | **opposite** | Forces are **opposed** → **no net force** | **Net torque about X** |

- Geometry symbols — **quoted verbatim from the thesis, and I think there is a typo in it**:
  - `r` = *"the distance from the center of pressure of the control canard to the X-axis"*
  - `R` = *"the distance of the center of pressures of control canards"* → most likely the **separation** between the two control-canard centres of pressure, i.e. `R ≈ 2r`. Worth re-deriving from our own geometry rather than trusting this line.
- **Naming caution:** the prior art this concept comes from (US Patent 6,981,672, ref [5], Fig. 1.3) calls the torque pair **"rotation canards"**; this thesis calls them **"control canards"** and adds a *separate* `C_Nδ` control-coefficient model. Same idea, two vocabularies — keep them straight when reading sources.
- The *net translational force* from the steering pair is the **guidance force** — its direction in the earth frame is set by the ring's roll angle `θgk`.
- The *net roll torque* from the control pair is `Taero`, deliberately opposing body spin, so the alternator can work against it.

**Operational concept:** the ring is de-spun (rotates slowly relative to earth, not with the body). The controller commands `θgk` (ring angle) so that the steering force points where the guidance law wants. Hold `θgk` = hold the steering vector. That is the entire actuation problem, reduced to **one axis**.

### 2.3 Torques on the ring (Figs. 2.5 / 5.1)

| Symbol | Direction | Nature | Depends on |
|---|---|---|---|
| `Taero` | **−X** | Total aerodynamic torque from the control canards | Projectile velocity **and altitude** (air density) — *not controllable* |
| `Tf` | **+X** (with body spin) | Bearing friction torque | Relative velocity, radial & axial load |
| `Talt` | **+X** (with body spin) | Alternator reaction torque from drawing current | **Load on the alternator — this is the control input** |

```
T(+X) = Talt + Tf − Taero
T(−X) = −Talt − Tf + Taero
```

→ **To have any control authority in the −X direction, `Tf < Taero`.** This single inequality drives the bearing spec.

---

## 3. Why a ground test rig was built (Ch. 2)

The thesis's core contribution is a **rotating dynamometer rig** that reproduces, on the bench, the two flight loads that matter — **aerodynamic torque** and **body angular velocity** — so the alternator-as-actuator concept could be de-risked before flight.

### 3.1 Signal / power flow (Fig. 2.6)

```
                ┌─ Torque Motor ──────►| Torque Motor Driver |◄── torque input
relative pos →  ├─ Encoder ───────────► (index/A/B) ──────────►| Microcontroller |
encoder↔stator  ├─ Alternator ──AC──►| AC/DC Converter |─►| Filter Capacitor |─DC─►| Programmable DC Load |
                │                        (Vishay VS-36MT140)      (50 µF, 800 V)     (Aim TTi LD400P)
                ├─ Slip Ring
                └─ Speed Motor ──────►| Speed Motor Driver |◄── body velocity input
```

**Mechanical stack, top → bottom:** *Torque Motor → Coupling → Holding Part → Alternator (rotor magnets / body / magnets) → Speed Motor* (Figs. 2.10, 2.11). Parts 1–4 of the actuator stack and their inertias are tabulated (Table 2.2). The **torque motor plays the role of `Taero`**; the **speed motor plays the role of `p_body`**.

### 3.2 Component list (as-built)

| Function | Part | Key specs |
|---|---|---|
| Speed motor (simulates body spin) | Kollmorgen **AKM63M** | 480 VAC, Kt 1.23 N·m/A, 4.95 kW, 4500 rpm, 10.5 N·m, rotor inertia 24 kg·cm² |
| Torque motor (simulates `Taero`) | Kollmorgen **AKM-33H** | 240 VAC, Kt 0.51 N·m/A, 1.31 kW, 5500 rpm, 2.27 N·m, rotor inertia 0.85 kg·cm² |
| Speed motor drive | Kollmorgen **AKD-P02407** | 24 A cont. / 48 A peak, 16 kW |
| Torque motor drive | Kollmorgen **AKD-P02207** | 12 A cont. / 30 A peak, 8 kW |
| Position sensor | **FENAC** optical incremental | 2500 CPT + index |
| **Actuator under test** | **Volt Defence alternator** | Kt **0.716 N·m/A**, Kv **0.749 V/(rad/s)**, **7 pole pairs**, R 6.2 Ω ph-ph, L 8.8 mH ph-ph, 1.2 kW continuous, magnet inertia 1.485 kg·cm² |
| Rotary-to-static | **Senring** slip ring | **12 circuits, 5 A max**, 5000 rpm max |
| Filter | TDK capacitor | **50 µF**, 800 V |
| Rectifier | Vishay **VS-36MT140** | 25 A DC cont., 1400 V VRRM |
| Programmable load | Aim TTi **LD400P** | **80 A / 80 V / 400 W (600 W short)** |
| Logic supply | Aim TTi **CPX 400D** | 60 V / 20 A / 420 W |
| Controller | NI **cRIO-9063** + **NI-9205** (AI), **NI-9264** (AO), **NI-9411** (DI, encoder) | |

### 3.3 Test software — two-part architecture

- **Host (PC, LabVIEW):** operator input + data presentation. Fig. 2.12.
- **FPGA target (cRIO-9063), real-time:** encoder decode → velocity & position of the ring (relative to the body, using encoder + speed-motor position) → run control law → drive DC electronic load, speed-motor drive, torque-motor drive.
- **Sample rates / filtering:** control loop **1 kHz**; velocity measured over **1 ms** windows; **30 µs** line filter on encoder A/B, **45 µs** on index.
- **Velocity resolution [derived check]:** `δV = (1/2500)·1000·2π = 2.513 rad/s = 24 rpm` — quoted in the thesis as 24 rpm. *This quantization is one of the stated causes of the residual position oscillation seen when the ring is stationary, together with non-linear (Coulomb) friction.*
- Controller runs with **saturation + "minimum control effort" logic**: it computes which rotation direction needs less travel (shortest-way angle wrap) before commanding position.

*Figures: `figures/p41-fig2.6-2.7-test-setup-schematic-and-photo.jpg`, `figures/p44-fig2.10-test-setup-section-view.jpg`, `figures/p45-fig2.11-actuator-part-zoom.jpg`*

---

## 4. Mathematical model of the rig (Ch. 3)

- Physics mapped to a **linear graph** (Fig. 3.2); graph parameters: **N = 7 nodes, Nd = 2, B = 11 branches, tree = 5 branches, links = 6**.
- Physical model (Fig. 3.1): alternator = voltage source + `Ra` + `La`; filter cap `Cf` in parallel; viscous friction = damper `b`; `Iload` = current source; `p_body` = speed source (because a speed-controlled motor imposes body spin).
- **States:** `x = [p_gk , V_Cf , I_La]ᵀ` — ring angular velocity, capacitor voltage, alternator current.
- **Inputs:** `u = [p_body(t) , T_aero(t) , I_load(t)]ᵀ`.

**State matrix (Eq. 3.4):**

```
A = [ -b/Jgk        0       Kt/Jgk   ]
    [  0           0       1/Cf     ]
    [ -Kv/La     -1/La    -Ra/La    ]

B = [ b/Jgk      1/Jgk      0   ]
    [  0           0      -1/Cf ]
    [ Kv/La        0        0   ]
```

**Transfer functions (derived in App. B, units cross-checked in App. B):**

| TF | Form |
|---|---|
| `G_Iload→Pgk` | `β₀ / (s³ + σ₂s² + σ₁s + σ₀)` — β₀ = Kt/(LaCfJgk) |
| `G_Taero→Pgk` | `(β₂s² + β₁s + β₀) / (σ₃s³ + σ₂s² + σ₁s + σ₀)` |
| `G_pbody→Pgk` | `(β₂s² + β₁s + β₀) / (σ₃s³ + σ₂s² + σ₁s + σ₀)` |

**Numerical plant (App. F):**

```
G_Iload→Pgk = 1.367e9 / (s³ + 705.6 s² + 2.325e6 s + 2.418e6)
poles: -1.04 ,  -352.28 ± 1483.20i        (electrical pair ≈ 242.6 Hz, ζ ≈ 0.231)
```

**Inertia stack [derived sum]:** coupling 4.069e-5 + holding 1.678e-4 + alternator body 7.55e-4 + magnets 1.485e-4 + motor rotor 0.85e-4 → **Jgk = 1.197e-3 kg·m²**

**Friction [derived]:** the design code uses `b = 0.2 N·m @ 1500 rpm` → **b ≈ 1.273e-3 N·m·s/rad** (mechanical time constant `Jgk/b ≈ 0.94 s`). Flight chapter instead quotes a measured **Tf = 0.1 N·m at 800 rpm relative speed**.

**Consistency check [derived]:** DC gain `Kt/b = 565.5`; reduced TF DC gain `588.4/1.04 = 565.8`; numeric TF DC gain `1.367e9/2.418e6 = 565.3`. All three agree → the reduced first-order model is faithful, and it tells us:

> **Open-loop, the ring speed is ≈ 565 rad/s per amp of load current, and the mechanical pole is at only ≈ 1.04 rad/s.** Physics is not the bandwidth limit — the electrical dynamics and the load hardware are.

**Model validation (Tables 3.1, 3.2):** open-circuit (`Iload = 0`) and closed-circuit (`Iload` varied 0.5–2.5 A) tests at 10.5–83.8 rad/s. Simulation matches test well; `Kv` shows a slow drift with relative speed (0.74 → 0.80 V/(rad/s)) and `Kt` drifts with current (0.70–0.77 N·m/A) — attributed to measurement offset/non-linearity. Both treated as constant for control purposes.

---

## 5. Controller design (Ch. 4)

### 5.1 Structure: cascade

```
θgk_ref ──►( Σ )──► Gpc(s) ──► pgk_ref ──►( Σ )──► Gvc(s) ──► Iload ──►┌ Plant ────────┐──► 1/s ──► θgk
            ▲ −                          ▲ −                            │ Gd1: Taero    │
            └──── θgk_f ──────────────────┴──── pgk_f ───────────         │ Gd2: pbody    │
                                                                         │ Gu : Iload    │
                                                                         └───────────────┘
```

Rationale for cascade: only one variable is truly *controlled* (position), but there are two measured states; the inner loop kills `Taero` and `p_body` disturbances **before** they reach the outer loop. Inner loop must be **≥5× faster** than the outer.

### 5.2 Requirements → results

| Loop | Requirement | Achieved |
|---|---|---|
| **Position (outer)** | ≥ 4 Hz cut-off; `Kp = ∞`; `Ts ≤ 0.1 s`; `Mp ≤ 5 %` | **6.2 Hz**, ∞, 0.1 s, **0 %** |
| **Velocity (inner)** | ≥ 20 Hz cut-off; `Kp = ∞`; `Ts(5 %) ≤ 0.05 s`; `Mp ≤ 25 %` | **33.6 Hz**, ∞, 0.05 s, **9.57 %** |

- 4 Hz was chosen because guidance is only needed while the projectile is off-trajectory; near impact the ring may be allowed to free-wheel. Settling-time target 0.1 s comes from ref [10].
- **Velocity loop:** free integrator required for zero steady-state error to step, and it also drives disturbance error → 0 at steady state for both `Taero` and `p_body` steps. Chosen as **PI** with zero at `-26.98`, gain 0.29:

```
Gvc = 0.29 + 7.82/s            (= 0.29·(s + 26.98)/s)
closed-loop poles: -33.17 , -144.78 , -263.82 ± 1468.48i
```
- **Position loop:** the free integrator is already present (from `1/s`), so **P-only** is enough — no disturbance check needed since the inner loop handles it. Gain **29.7**:

```
Golp = Gpc · Gcl_v · (1/s)
closed-loop poles: -21.03 , -78.00 ± 26.7i , -264.29 ± 1466.71i
```
  Behaviour is **first-order-like** because the dominant pole sits near the imaginary axis → zero overshoot, hence the 0 % measured.

- **Anti-windup:** output saturation is unavoidable (source/actuator limits), so **clamping-type integral windup** is implemented (chosen over back-calculation for simplicity).

### 5.3 Bench test conditions (Table 4.5)

| Input | Value |
|---|---|
| `p_body` | 83.8 rad/s (800 rpm) |
| `p_gk` limits | ±20.9 rad/s (±200 rpm) |
| `Iload` limits | 0 → 1.9 A |

**Step test:** simulation and test agree; residual **position oscillation when stationary** (encoder noise + non-linear friction) that simulation does not show.
**Chirp test:** amplitude π/8 rad, π offset, 0.01 → 7.5 Hz over 15 s. Response attenuated to the −3 dB amplitude at **6.23 Hz**, matching the 6.2 Hz design value. The *velocity* traces differ more between test and sim than position does — inner loop is absorbing model uncertainty (Coulomb friction, misalignment of torque/velocity motor centrelines).

---

## 6. Flight dynamics (Ch. 5)

### 6.1 Frame choice — important design decision

Three options were weighed:
1. **Body frame** — rolling with the projectile → the high-frequency roll content forces very long simulation times.
2. **Body Fixed Plane (BFP) frame** ✅ *chosen* — **zero Euler roll** (`φ = φ̇ = 0`), enforced by `p_F = −r·tan θ`. Its advantage: **the Y axis always stays parallel to the Earth's surface**, which is exactly what guidance/control wants. This is also the frame the French work (Wernert/Theodoulis [9][18]) uses.
3. **Body non-spinning frame** (`p_F = 0`) — simpler/cheaper, less faithful.

**Equations used (BFP):**

```
Angular:  [ṗ, q̇, ṙ]ᵀ = I⁻¹ ( [L, M, N]ᵀ − Ω_BFP× I [p, q, r]ᵀ ),   Ω_BFP× skew = [0 −r q; r 0 r tanθ; −q −r tanθ 0]
Linear:   [u̇, v̇, ẇ]ᵀ = [X,Y,Z]ᵀ/m − Ω_BFP× [u, v, w]ᵀ
Kinematics:  θ̇ = q ,  ψ̇ = r / cos θ
Earth:    [ẋE, ẏE, żE]ᵀ = G [u, v, w]ᵀ   (G from App. D.15)
```

### 6.2 6-DOF → 7-DOF

Adding the ring's independent roll DOF requires (App. E):
- **Inertia matrix grows** to carry two independent X inertias: `I = diag(I_xgk , I_xbody , I_y , I_z)`
- **Moment vector gains a row**: `M7DOF = [L_gk−7DOF , L_b−7DOF , M , N]ᵀ`
- **Angular-velocity vector gains a row**: `ω7DOF = [p_gk , p_body , q , r]ᵀ`
- **Skew matrix's first row is duplicated** (so `p_body` and `p_gk` are both multiplied by *the same* row — required for a correct derivative in the non-inertial frame):
```
Ω_BFP× = [0   0     −r      q     ]
         [0   0     −r      q     ]
         [0   r      0    r tanθ  ]
         [0  −q  −r tanθ     0    ]
```

### 6.3 Projectile & aero model (Table 5.1 + App. G)

| Parameter | Value |
|---|---|
| Diameter d | 155 mm |
| Mass | 43 kg |
| Ixx | 0.144 kg·m² |
| Iyy = Izz | 1.216 kg·m² |
| Initial velocity | 800 m/s |
| Initial `[p,q,r]` | **[1600, 0, −3.5] rad/s** (≈ 15 280 rpm) |
| Firing elevation | 63° |

Assumptions used: flat earth, gravity constant with altitude, **aero coefficients vary with Mach only** (α, β dependence dropped) — acceptable for finding `Taero` and body speed, *not* acceptable for guidance work.

**Aero forces/moments (App. G, 6-DOF):** Lift `L`, Drag `D`, Magnus `K`, Pit/Yaw moment `M_PY`, Magnus moment `M_m`, Pitch/Yaw damping `M_pyd`, Roll damping `M_rd`, Gravity `Fg`. Standard coefficient set `C_Lα, C_D, C_ypα, C_Mα, C_npα, C_mq, C_lp`. **Numerical values are taken from refs [23] (body) and [1] (guidance kit) and are NOT printed in the thesis.**

**Guidance-kit terms (7-DOF):**

```
Control force:    Fc  = (ρSV²/2)·C_Nδ · ( δs·[0, cos θgk, sin θgk]ᵀ + [0, α, β]ᵀ )
Control moment:   Mc  = (ρSV²·l_CG/2)·C_Nδ · ( δs·[0, −sin pF, cos pF]ᵀ + [0, −β, α]ᵀ )
Aero torque on GK : Taero = ½·ρV²·S·l_gk·C_rc          (opposes body spin)
Damping torque    : Tad   = ½·ρS·d²·V·p_gk·C_rdgk      (opposes ring rotation)
Total on ring     : L_gk−7DOF = Taero + Tad
α = tan⁻¹(w/u) ,  β = tan⁻¹( v/√(u²+w²) )
```

### 6.4 Flight envelope results (the numbers to design against)

**Fig. 5.10 — `Taero` vs time for 4 elevation angles (0.8378, 0.925, 1.0123, 1.0996 rad):**
`Taero` starts ≈ −1.8 to −2.0 N·m, has a dip/bump around 5–10 s, **rises to ≈ 0 at apogee (t ≈ 40–55 s)**, falls again to −1.5 … −2.2 N·m at t ≈ 90 s. → **working range of `|Taero|` is 0 → ≈2.2 N·m.**

**Fig. 5.11 — `Tad`:** +1.8 N·m at launch → ~0 at apogee (45–55 s) → +2.1 N·m at 100 s.

**Fig. 5.8 — control forces (body-fixed-plane):** ≈ ±15–25 N peak early, → 0 at apogee, back to ≈ ±20 N late. Oscillatory because the de-spun ring sweeps relative to the body-fixed frame.

**Fig. 6.1 / 6.2 — the flight scenario actually replayed on the rig (elevation 0.925 rad):**
- `Taero`: 1.8 N·m at t=0 → minimum **0.1706 N·m at t = 41.16 s** → **2.119 N·m at t = 86.5 s**
- `p_body`: 1623 rad/s (≈ 15 500 rpm) decaying to ≈ 1050 rad/s (right axis); scaled 83.7 → ~52 rad/s for the rig

> **Non-physical discontinuities in Figs. 5.10/5.11** are caused by the sparse aero Mach table (coefficients only at **M = 0.9, 0.95, 1.1, 1.5, 2.0**). A gap we must not inherit.

---

## 7. The problem found, and the fix (Ch. 6) — most valuable part for us

### 7.1 Control-authority arithmetic

```
Talt_max  = Kt × 8 A = 0.72 × 8 = 5.76 N·m      (8 A = load capacity; the thesis used 8 A)
Tf        = 0.1 N·m                              (measured at 800 rpm relative speed)

Symmetric ± authority:  Taero_max = (Talt_max + Tf)/2 = 2.93 N·m
Minimum authority:      Taero_min =  Tf               = 0.10 N·m
```

**Failure mode with fixed limits (Fig. 6.3, 6.4):** replaying the real flight profile with fixed saturation (velocity-loop output saturated at 8 A, position-loop at 31.42 rad/s), control is **lost between t = 30 s and 50 s**: near apogee `Taero` is too small to decelerate the ring, so the ring overshoots badly, and the velocity loop cannot respond in the `Taero` direction. Large overshoots risk **full rotation → non-linearity → instability**.

### 7.2 Disturbance observer

Frequency-domain DOB chosen because *voltage and current at the DC load cannot be measured simultaneously* → full-state time-domain approach impossible. Block diagram (Fig. 6.5) is the standard:

```
û_d(s) = Q(s) · [ Ĝ⁻¹(s)·y(s) − u(s) ]
```

- Plant reduced since the complex pole pair is **338.7× farther** from the imaginary axis (App. F): residues r₁ = 588.4, and `Ĝ = 588.4/(s + 1.04)`.
- Filter `Q = 1/(0.5s + 1)` — deliberately slow (rise time ≈ 1.1 s) to reject measurement noise; acceptable because `Taero` and `Tf` have no high-frequency content.
- **Discretised for the FPGA (1 ms, `c2d` + first-order hold):**
```
G_observer(z) = (0.003397 z − 0.003394) / (z − 0.998)
Q(z)          = (0.0009993 z + 0.0009987) / (z − 0.998)
```

### 7.3 Three solutions, all simulated then built

| # | Idea | Rule | Simulated outcome | Hardware outcome |
|---|---|---|---|---|
| **1** | **Dynamic current limit** | Set velocity-loop upper saturation = **2 × observed disturbance current** | Controllable through the whole flight; **still overshoots** (35–55 s) because the *velocity* limit is untouched | Fixes instability; **overshoot remains** — rejected for real use |
| **2** | **Dynamic velocity limit** | Position-loop limits scaled by observed current: **V_SF = 5.2 rad/s ÷ 0.2 A = 26 rad/s per A** → `VL = 26·Î(A)`, capped at 31.4 rad/s | **No overshoot** anywhere; but **asymmetric** response ± (different current demand for identical angle steps) | Works, but the asymmetry is undesirable; **still applicable to a real projectile** because there `p_body ≫ p_gk` |
| **3** | **Combined (current + velocity limits)** | Both of the above | **No overshoot AND symmetric** — best | ✅ **Verified: best solution.** Also keeps the alternator below its limit because current is limited w.r.t. `Taero` |

**Interesting engineering note:** solution 2's overshoot problem *only appears on the rig*, because the rig scales `p_body` down (so the ratio `p_gk/p_body` becomes unrealistically large). On a real projectile body spin dominates, so the alternator/limit issue does not bite the same way. **Test-rig fidelity artifacts can create or hide failure modes — we need to be aware of this in our own rig design.**

### 7.4 Hardware lessons (Ch. 7)

The single most useful graph is **Fig. 7.4 — "Alternator Saturation Points and Velocity Controller Results":**
- **Available alternator current falls with relative speed**: from ≈ **10 A** at t=0 → ≈ **5 A** around apogee (40–50 s) → ≈ **6–7 A** at 85 s.
- Wherever the blue (controller demand) exceeds the orange (available limit), the filled regions mark **lost control authority** → the large overshoots seen in Fig. 7.7 (spikes to ≈5.5 rad against a 2.4–3.9 rad reference).
- **Recommended fix (thesis):** also saturate the controller output to the alternator's speed-dependent limit, *which is computable from the measured relative velocity* — i.e. make the limit a **state-dependent** constraint, not a constant.

Other test findings:
- Unmodified controller loses control over a **larger** portion of the flight on hardware than in simulation — causes: DC load dynamics, continuous-vs-discrete differences, non-linear friction, and **fixed-point quantization** in the FPGA (transfer functions and analog I/O in fixed point).
- The disturbance observer matches simulation **well at low `Taero`**, diverges at high `Taero`.

---

## 8. Master data sheet (all numbers in one place)

### Actuator / plant
| Quantity | Value |
|---|---|
| Alternator Kt | 0.716 N·m/A (design code uses 0.72) |
| Alternator Kv | 0.749 V/(rad/s) (design code uses 0.75) |
| Pole pairs | 7 |
| R ph-ph / L ph-ph | 6.2 Ω / 8.8 mH |
| Continuous power | 1.2 kW |
| Ring inertia `Jgk` [derived] | 1.197e-3 kg·m² |
| Viscous friction `b` [derived] | ≈ 1.273e-3 N·m·s/rad (0.2 N·m @ 1500 rpm) |
| Measured friction | 0.1 N·m @ 800 rpm relative |
| Filter cap `Cf` | 50 µF |
| Plant TF | `1.367e9/(s³ + 705.6s² + 2.325e6s + 2.418e6)` |
| Reduced TF | `588.4/(s + 1.04)` |
| Open-loop gain [derived] | ≈ 565 rad/s per A |
| Mechanical time constant [derived] | ≈ 0.94 s |

### Controller
| Quantity | Value |
|---|---|
| Velocity loop | PI: `Kp = 0.29`, `Ki = 7.82` (zero at −26.98) |
| Position loop | P: `Kp = 29.7` |
| Anti-windup | clamping |
| Bandwidths | velocity 33.6 Hz, position 6.2 Hz |
| DOB | `Ĝ = 588.4/(s+1.04)`, `Q = 1/(0.5s+1)` |
| DOB discrete | `(0.003397z − 0.003394)/(z − 0.998)`; `Q(z) = (0.0009993z + 0.0009987)/(z − 0.998)` |
| Current limit rule | `I_lim = 2 × Î_disturbance` |
| Velocity limit rule | `VL = 26 rad/s per A × Î`, cap 31.4 rad/s |
| Loop rate | 1 kHz |

### Limits used
| Quantity | Value |
|---|---|
| `Iload` | 0 → 8 A (1.9 A in step/chirp tests) |
| `p_gk` | ±20.9 rad/s (200 rpm) in bench tests; ±31.42 rad/s (300 rpm) = 80 V / Kv |
| DC load voltage | 80 V → `p_rel,max = 106.6 rad/s` |
| Slip ring | 5 A, 5000 rpm ⚠️ *(8 A was drawn in the flight-replay test — worth noting as a design tension)* |
| Speed scaling factor | C = 1623/75.18 = **21.6**, re-scaled to hold max body speed at 800 rpm |

### Projectile / flight
| Quantity | Value |
|---|---|
| 155 mm, 43 kg, Ixx 0.144, Iyy=Izz 1.216 kg·m² | |
| Launch spin | 1600 rad/s sim; 10 000–20 000 rpm over charge 3M–6M |
| Charge table | 3M: 546.4 m/s / 176.3 Hz → 128.2 Hz; 6M: 943.5 m/s / 304.4 Hz → 221.3 Hz |
| Gun launch loads | **15 000 g axial, 5 000 g radial** |
| Flight spin | ~270 Hz (ref [3]) |
| Flight time in sim | ~90–95 s, apogee ≈ t = 41 s |

---

## 9. Gaps, limitations, and things I do NOT want to inherit

**Stated by the author:**
1. **No guidance law at all** — pure actuation feasibility. The ring-angle command is an open-loop square wave in the fight-replay tests.
2. Earth curvature, gravity variation with altitude, and α/β dependence of aero coefficients are all neglected.
3. No **HIL**: the ring's position does not feed back into the flight parameters, and the guidance algorithm is not in the loop.
4. Body spin is **scaled down** on the rig; `p_body` was never applied at true magnitude.
5. Aero coefficient table is very sparse in Mach (0.9, 0.95, 1.1, 1.5, 2.0) → non-physical jumps in torque.
6. Aero coefficients `C_Nδ`, `C_rc`, `C_rdgk`, `l_CG`, `C_lp`, `C_mq`, `C_Mα` … **are not printed numerically** — they are imported from refs [1] and [23].

**Things I noticed that they do not flag:**
7. **Slip ring rated 5 A but 8 A was used** — a real integration constraint if we copy this architecture.
8. Harnessing **`p_gk` feedback in flight** is never addressed (they use a lab encoder; refs [6] used a gyro, ref [7] a geomagnetic + hall combination). This is our biggest open sensor question.
9. No thermal/power budget is given: the alternator is simultaneously the actuator and the avionics power source, and the load bank dissipates the *control* power — in flight that energy has nowhere to go except losses. Worth thinking about.
10. No discussion of the **launch/setback survival of the bearings** despite the 15 000 g / 5 000 g environment.

---

## 10. What I would carry into our PGK design

**Adopt as-is (validated):**
- **Fixed-canard de-spun ring + alternator-as-actuator** concept, and the steering/control canard split (same cant → force; opposite cant → torque).
- **Cascade control**: PI inner (velocity) + P outer (position), inner ≥5× faster, clamping anti-windup, shortest-way rotation logic.
- **DOB + dynamic saturation limits** — this is the thesis's real result. The *combined* solution (dynamic current limit + dynamic velocity limit) is the one to implement.
- The **control-authority criteria** as a *sizing equation*: `Taero ≤ (Talt_max + Tf)/2` and `Taero > Tf`.

**Take with caution / improve:**
- **Aero data:** we need a proper Mach × α × β coefficient set, not a 5-point Mach table.
- **Sensor for `θgk`:** lab encoder won't fly. Options: gyro (Zhang [6]), geomagnetic + hall (Yin [7]), or a hybrid.
- **Friction budget is the binding constraint near apogee** (1.7:1 margin at `Taero_min = 0.17 N·m`). Bearing selection, preload, and contamination matter more than control tuning here.
- **Make the saturation limit state-dependent everywhere** (both current and voltage) so authority losses are handled by construction.

**Open questions to answer next (design phase):**
1. **Our projectile class and envelope** — bore, mass, muzzle velocity, spin at launch/apogee, elevation. Everything above scales from this.
2. **Our aero dataset** — where do we get `C_Mα, C_lp, C_mq, C_Nδ, C_rc, C_rdgk`? (CFD? published datasets? refs [1]/[23]?)
3. **Ring radius and canard sizing** — `R`, `r`, planform, cant angles, and the resulting `F_steer` and `Taero` at the extremes of the envelope.
4. **Alternator sizing** — do we size for the worst-case `Taero` (symmetric criterion) or accept asymmetric authority and schedule?
5. **Guidance law** — since the thesis leaves it open: this is our real novelty space (impact-point prediction / trajectory shaping using the ring-angle channel at ~6 Hz command bandwidth).
6. **Bench rig for us** — do we replicate their speed-motor + torque-motor + load-bank architecture, or go lighter (motor-loaded ring without full spin emulation)?
7. **Power/thermal path** — where does the control energy go in flight if there is no load bank?

---

## 11. Figure index (images copied into `notes/figures/`)

| File | Content | Thesis figs |
|---|---|---|
| `p30-fig1.3-1.4-fixed-canard-orientation-and-example.jpg` | Prior art (US Patent 6,981,672 [5]): **steering canards** (red, net force `Fc` ↑) + **rotation canards** (orange, net torque), with projectile angular velocity marked; photo of a real fixed-canard assembly | 1.3, 1.4 |
| `p32-fig1.6-1.8-zhang-testset-and-costello-schematic.jpg` | Zhang et al. test platform; Costello's dual-spin schematic (ΦF/ΦA) | 1.6, 1.8 |
| `p36-fig2.1-2.2-projectile-with-gk-and-preliminary-design.jpg` | Projectile with GK + axis convention; preliminary GK design (green/blue/orange) | 2.1, 2.2 |
| `p37-fig2.3-gk-section-view.jpg` | **Section view**: nose, isolation bearings, alternator rotor/stator, canard ring | 2.3 |
| `p38-fig2.4-steering-and-control-canards.jpg` | **Canard arrangement**: 0°/180° steering (yellow, net force) vs 90°/−90° control (red, net torque) | 2.4 |
| `p39-fig2.5-torques-on-canard-structure.jpg` | `Taero`, `Tf`, `Talt` on the ring | 2.5 |
| `p41-fig2.6-2.7-test-setup-schematic-and-photo.jpg` | **Test rig signal/power schematic + photograph of the stand** | 2.6, 2.7 |
| `p44-fig2.10-test-setup-section-view.jpg` | Rig section: torque motor → actuator stack → speed motor | 2.10 |
| `p45-fig2.11-actuator-part-zoom.jpg` | Actuator stack zoom (1) coupling (2) holding part (3) alternator body (4) magnets | 2.11 |
| `p55-fig3.1-physical-model.jpg` | Physical model: alternator source+R+L, filter cap, friction damper, current source | 3.1 |
| `p70-fig4.1-cascade-control-structure.jpg` | **Cascade control block diagram** (position P → velocity PI → plant) | 4.1 |
| `p93-fig5.1-torques-on-guidance-kit.jpg` | Torques on the guidance kit | 5.1 |
| `p103-fig5.7-5.8-velocities-and-control-forces.jpg` | Earth-frame velocities; **control forces ±15–25 N** | 5.7, 5.8 |
| `p105-fig5.10-5.11-aero-torque-and-damping-vs-flight.jpg` | **`Taero` for 4 elevations (0 → 2.2 N·m); `Tad`** | 5.10, 5.11 |
| `p109-fig6.1-6.2-flight-scenario-aero-torque-and-body-spin.jpg` | **Flight scenario: `Taero` min 0.1706 @ 41.16 s, 2.119 @ 86.5 s; `p_body` decay** | 6.1, 6.2 |
| `p112-fig6.5-disturbance-observer-block-diagram.jpg` | **DOB block diagram** + `Ĝ` and `Q` | 6.5 |
| `p124-fig7.4-7.6-alternator-saturation-and-observer.jpg` | **Alternator current limit 10 A → 5 A vs controller demand**; DOB test vs sim | 7.4, 7.6 |
| `p126-fig7.7-7.8-test-results-velocity-limit-and-combined.jpg` | Hardware overshoots from alternator limit; combined solution discussion | 7.7, 7.8 |

*Page numbers are PDF pages (body page = PDF page − 26).*

---

## 12. References from the thesis worth chasing

| Ref | Why we want it |
|---|---|
| **[5]** Clancy, Bybee, Friedrich — *Fixed canard 2-D guidance of artillery projectiles*, **US Patent 6,981,672** (2006) | The origin of the architecture; likely has concrete geometry/cant-angle guidance |
| **[22]** Guan & Yi, *Modeling of dual-spinning projectile with canard and trajectory filtering*, Int. J. Aerospace Eng., 2018 | The 7-DOF model derivation source (App. E cites it) |
| **[23]** Khalil, Abdalla et al., *Dispersion analysis for spinning artillery projectile*, 2009 | **Source of the 155 mm aero coefficients** |
| **[1]** Wang, Wang, Yu, *Influence of control strategy on stability of dual-spin projectiles with fixed canards*, Defence Technology 14(6), 2018 | **Source of the guidance-kit aero coefficients** (`C_Nδ`, `C_rc`, `C_rdgk`) |
| **[10]** Zhang, Yao, Zheng, *Impact point prediction guidance … dual-spin projectile with fixed canards*, Chinese J. Aeronautics 32(8), 2019 | **The guidance law** the thesis leaves out — impact-point prediction |
| **[9][18]** Wernert, Theodoulis, Morel — 155 mm spin-stabilized flight dynamics in different frames | Frame selection rationale + CCF modelling |
| **[2]** Spagni, Theodoulis, Wernert — *Flight control for a class of 155 mm spin-stabilized projectile with reciprocating canards* | Alternative actuation concept worth knowing |
| **[21]** Li, Yang, Chen, Chen — *Disturbance observer-based control* | DOB design reference |
| **[4]** Robinson & Berefelt, *On Guidance and Control for Guided Artillery Projectiles*, FOI Sweden, 2011 | Systems-level guidance/control overview (also the bandwidth-vs-spin argument in Ch. 1) |

---

*Notes compiled from the full PDF: all 169 pages of text layer read; 18 key pages rendered and visually inspected. Everything above cross-referenced to figure/page.*
