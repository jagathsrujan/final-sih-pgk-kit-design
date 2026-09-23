# Wang 2015 — what it changes for DRISHTI-PGK

**Source.** Yi Wang, Wei-dong Song, Dan Fang, Qing-wei Guo, *Guidance and Control Design for a Class of Spin-Stabilized Projectiles with a Two-Dimensional Trajectory Correction Fuze*, International Journal of Aerospace Engineering, Vol. 2015, Article ID 908304, 15 pp. Open access, `http://dx.doi.org/10.1155/2015/908304`.
**File in the workspace.** `Guidance_and_Control_Design_for_a_Class_of_Spin-St.pdf` (repo root).
**Read depth.** Full — text plus every figure, read from pages rendered at 300 dpi. The PDF's text layer OCRs the equations badly (§6 below), so **no number in this note is quoted from the text layer**; each one is read off a rendered page, and the crop each came from is listed in §7 and reproducible via `notes/figures/wang2015/extract.py`.
**Rated.** `design/05-source-register.md` row **C11** — Cite 4, Adopt 5.
**Tag.** `[C11]` in the register means *measured on their airframe by them, taken as evidence — never our own result*. It is the same discipline as `[ref]` (the METU thesis): another projectile, another canard set, another aero model.

---

## 1. Why this is the closest external paper the project has

- **The airframe is our class.** 45.5 kg, muzzle velocity 897 m/s, fired at 45°, apogee ≈8.8 km and impact at ≈27 km, spin-stabilized 155 mm. Our reference model is 45.0 kg at 546–943 m/s — the paper's single flight condition sits inside our declared envelope.
- **The architecture is our C1.** Two sets of fixed canards on a roll-decoupled correction part: steering canards (equal cant → net guidance force) and rotation canards (opposite cant → net roll torque). The correction part is held at a commanded roll angle relative to the ground frame with zero roll rate (their eq. (8)). That is our C1 two-pair split and our G2 "the ring angle is the sole command channel", published, and arrived at independently of the thesis the architecture came from.
- **The vehicle model is our P3 vehicle.** Their eqs. (1)–(8) are a 7-DOF dual-spin formulation — three translational plus four rotational (pitch, yaw, correction-part roll, body roll) — in a **quasi-body frame whose x–y plane is fixed in the vertical plane**. That is the body-fixed-plane frame the P3 toolchain decision already chose.
- **One real difference, and it is our hardest problem.** The paper asserts the correction part is held at the commanded angle and never says what holds it or what powers the electronics. There is **no generator, no bus, no dump and no thermal ledger anywhere in it**. C42 → W7/W12 → P6 (2.92 kW, 121 kJ, ≥58 W/K) gets nothing from this paper. It is silent on exactly the thing that separates our architecture from theirs.

---

## 2. The four things it gives us

### 2.1 The swerve-response phase — new criterion **G16**

A spin-stabilized body does not swerve in the direction the control force points. The paper computes the dynamic equilibrium angle caused by the control (eq. (21)) and then the swerve response of the deviation motion (§3.2, eqs. (22)–(29)), and shows the response is rotated relative to the command by a large, slowly-varying phase.

Read from their Figures 4 and 5 `[C11]`:

- the **phase shift** between command angle and response direction is **≈170–172° at launch, falls to a minimum of ≈146–149° at t ≈ 42–45 s, and is back to ≈162–163° by t ≈ 85 s**;
- the four command angles (0°, 90°, 180°, −90°) give curves **within ≈3° of each other** at every instant, so for a given trajectory state the phase shift is a single number — which is what makes it compensable;
- with **Mach** as the argument the shift runs from **≈149° at Ma 1.0 to ≈167° at Ma 1.65** (their Fig. 6 fit; the raw data extends to Ma ≈1.45), fitted with a fourth-order polynomial;
- their command law is then the miss direction minus that phase: **φ_C = −arctan(DL/DH) − φ_d** (eq. (38)), i.e. the force must be aimed *ahead* of the direction the round should go.

**Why this matters to us more than the number does.** Our G4 already states the failure form — *"a systematic misdirection is not self-correcting under IPP, because the law's own propagation model assumes the commanded direction was realised"* — and it currently has no line for this effect. Two consequences, and they are different:

1. **Propagator fidelity (G1, risk 8, risk 18).** If our IPP propagator applies the ring command as a lateral acceleration rather than reproducing the airframe's angular-motion response, the law's model of its own command is wrong in direction, at first order, permanently. The always-on steering force (risk 18) is already a stated modelling obligation for *magnitude*; this makes it an obligation for **direction** as well.
2. **A compensation requirement (G2).** The ring angle is the only command channel, so the compensation has to be inside the ring-angle command, as in their eq. (38).

**Scope of the claim, stated honestly.** The phase is a property of the airframe's angular motion (its roll–coning / epicyclic response to a force applied ahead of the CG — the mechanism is Ollerenshaw & Costello, their ref. [16]), **not** of the correction part's rotation. It therefore does not disappear because our ring is de-spun. But the *magnitude* is theirs, on their canards and their coefficients: it is a **method** to adopt and a **reason to expect the effect is large**, never a number to port. And the value is convention-laden — their γ_f definition ("0° when the steering canards are horizontal and give upward force; positive direction of the correction part is left, looking from nose to base") and their complex-angle definition both enter it. Re-derive; do not copy.

### 2.2 Correction authority versus correction start time — risk 10's missing method

Their Figure 14 sweeps the instant correction begins, 30 s → 80 s, and plots the reachable impact points as closed curves in the impact plane; the command angle moves the point around the curve, and the curve **shrinks hard** as the start is delayed. The 30 s curve spans ≈540 m between its 0° and 180° command points (their summary: **≈260 m "from far to target", ≈300 m "from near to target"**, lateral "about 260 m"), the 40 s curve ≈460 m, the 50 s ≈330 m, the 60 s ≈230 m, and by 80 s the reachable set is a point. The labelled 0°/90°/180°/−90° rays also show the curve is **tilted relative to the downrange/lateral axes**, which is the same swerve phase seen geometrically.

**Why this matters.** Our M7 margin of **1.11:1 assumes full force across a continuous 45 s window**; G3's gate makes that form unavailable and risk 10 records the true margin as *"worse than 1.11:1 and unquantified until the loop is in the loop in R5"*. This is the analytical route to quantify it now: authority as a function of the instant correction starts, computed from our own swerve-response magnitude (their eq. (29)) over G3's two-segment window instead of a ½aT². Their 260–300 m at a 30 s start is a same-class order-of-magnitude companion to our 407 m requirement — not a verdict on our design (different canards, different authority), but the first external number that says what a windowed correction of this class actually buys.

**Their strategy also splits the flight**, and the split is worth carrying as an option at G3:

- **ascent — lateral only**, φ_C = ±90° − φ_z, with a deadband S_z (eq. (39)). Their reason: the downrange prediction is not accurate early, while the lateral prediction still reads the **sign** of the lateral deviation before it reads the magnitude, and the sign is enough to spend authority in the right direction.
- **descent — the full phase-compensated command** (eq. (40)).

That is the same shape as our G1 apogee blackout and G3 gate, arrived at from prediction confidence rather than from authority collapse. The two explanations are complementary, not competing, and both are true of our trajectory.

### 2.3 A cheap perturbation impact-point predictor — a cross-check, not a replacement

Their §4 predicts the impact point from **perturbation theory** rather than by propagating: pre-load the nominal trajectory and its partial derivatives against impact point, then multiply the current state deviation by the Jacobian (eqs. (31)–(33)).

Numbers read from their §4.2 and Figures 9–11 `[C11]`:

- **75 rows of nominal trajectory and 20 rows of first-order partials**, occupying **no more than 5 kB of RAM** — the paper's own suitability argument for a fuze processor;
- finite-difference steps: **velocity step 2 m/s, position step 5 m**; 20 rows of partials is enough (more rows buy no accuracy);
- **first-order derivatives beat second-order** in their study — the second-order result has larger amplitude and slower convergence;
- interpolation error alone (nominal trajectory used as its own disturbance): **<0.8 m downrange, <0.1 m lateral** with 75 rows;
- against a **real disturbance** (0.5° elevation error, i.e. a genuine trajectory perturbation): predictive error **≤2 m downrange**, and lateral **≤15 m**, with lateral convergence reached by **t ≈ 40 s** — and their real deviation in that case is a constant ≈30 m downrange, ≈20 m lateral (Fig. 11).

**Why this matters.** Our G1 propagates to impact roughly 300 times a flight at 5–20 ms each (G10, H4). This is not a replacement for that — **their demonstrated deviations are tens of metres and ours is 407 m**, and the linearisation is only as good as its local validity — but it is a cheap, independent second estimate of the same quantity, which is what risk 8's propagation model and P3's two-implementation rule both want. If the propagator and the perturbation predictor diverge, the propagator (or its coefficient set) is wrong, and that is precisely the 13 m term G4 cannot currently check.

Two smaller things come with it: a **10 Hz (0.1 s) GPS-fed prediction loop**, which is the same order as our ~6 Hz guidance update (G10); and a **second-order fading-memory filter** with a single gain (eq. (34): H = (1−β)², G = 1−β²) to take GPS measurement noise out of the deviation estimate.

### 2.4 The coefficient list and the Monte Carlo precedent

- **Magnus.** Their force and moment expressions carry **Magnus force coefficients for both parts (C_zf, C_za) and Magnus moment coefficients for both parts (C_npaf, C_npaa)** — four terms, active at our spin rate. Our risk 8 names the gap only as *"a Mach × α × β coefficient set"*, and no S row owns Magnus, though it is a first-order driver of the slow drift our S7 (yaw of repose) exists to absorb. **The coefficient list should name Magnus explicitly** so the set that eventually gets sourced or computed carries it.
- **The disturbance set** (their Table 2) is a citable precedent for R5's input distributions: mass ±0.5 kg, length ±5 mm, moment of inertia ±4 %, muzzle velocity ±5 m/s, launching elevation ±0.06°, launching azimuth ±0.02°, wind velocity ±2 m/s, wind direction ±15°.
- **Result under that set: CEP ≤ 30 m at ≈27 km** (their §5.3.2; Fig. 20 shows the unguided cloud spread mostly ±250 m downrange with the guided cluster collapsed toward the origin). This is a **published 30 m-class CEP for our architecture on a comparable airframe** — useful support for M4, subject to the project's standing rules: scenario-match before comparing (the register's two-ratio discipline), and never claim accuracy superiority over the fielded kit (source-register A2's guard).

---

## 3. What it corroborates for free (no change, worth a citation)

| Our row | What the paper supplies |
|---|---|
| **C1** | An independent published instance of the two-pair fixed-canard roll-decoupled arrangement, and of the ring/correction-part roll angle as the only command channel. C1 currently rests on the METU thesis `[ref]` plus the fielded M1156. |
| **C9 / C10 / C12** | The roll-decoupling torque balance written out: their eq. (3) carries the separate front/aft roll inertias and moments and the reaction between the two parts, and the roll-damping terms of both parts — the published form of the coupling our control pair and friction budget live in. |
| **G2 / G3** | "Authority is a window, not a constant", from the authority-versus-start-time sweep — the register's own slide-3 claim, with an external curve behind it. |
| **S4 / S5** | Their Fig. 18 measures the **sideslip dither the control force itself induces: magnitude ≈10°, declining late in flight**, on a design with no gyroscope and therefore no angular feedback. Our S4 caps yaw at **≤3°** and we have the ring IMU, the DOB and state-dependent limits — so either we hold the tighter bound and say why, or S4's bound needs re-examination against the force we are deliberately keeping on (risk 18). It is a tension to resolve, not a number to adopt. |
| **P3** | A published 7-DOF dual-spin formulation in the body-fixed-plane frame, as an independent cross-check on our own model's structure. |

---

## 4. What we do not take from it

- **The phase-shift number itself** — convention-laden, their canards, their coefficients (§2.1).
- **The printed phase-shift polynomial** (their eq. (30)) — see §6, it is defective as printed.
- **The perturbation predictor as the primary IPP.** Their case is tens of metres; ours is 407 m, where the linearisation's validity is unproven. Cross-check only.
- **Anything about power, thermal, the machine or the dump** — outside the paper's scope entirely.
- **Their control-loop design.** No gyro, no observer, no state-dependent limit; their accepted 10° sideslip is exactly what our G11/G14/G15 stack exists to prevent.

---

## 5. Where it landed in the register — the change set of 2026-09-23

| Paper item | Register change |
|---|---|
| The swerve-response phase and its compensation | **New criterion G16** (OPEN, provisional on the P3 vehicle); **new risk 51** (the phase is uncovered and unquantified); a **modelling obligation added to G4** alongside the 2026-09-19 phasor-wobble obligation; cross-refs at G1, G2 and risk 18 |
| Authority versus correction start time | **Risk 10** gains the quantification route and the same-class data point; **G3** gains the two-segment ascent/descent option and the authority-curve method |
| The induced sideslip of the always-on force | **S4** gains the ≈10° external datum and the question it raises; **S5** cross-referenced; **risk 18** extended |
| Magnus force and moment terms | **Risk 8**'s coefficient list now names Magnus |
| The disturbance set and the CEP result | **R5** gains the citable disturbance-set precedent (scenario-matched, no superiority claim) |
| The perturbation predictor and fading-memory filter | Recorded as a cross-check route for G4/H4 and a filter form for the prediction loop — decision-log entry only, no value moved |
| The paper as a source | **Source register C11** — Cite 4 / Adopt 5, read depth full |

**Nothing decided was reopened.** The pass adds one criterion, one risk and citations; no closed value moved, and no submission claim changes except by gaining support (M4's CEP) and one caution (S4's yaw bound).

---

## 6. Defects and cautions — read before quoting anything from this paper

1. **Their eq. (30) as printed does not reproduce their Fig. 6.** Evaluating the printed polynomial, φ_d = −285Ma⁴ + 1638Ma³ − 3157Ma² + 3352Ma − 1032, over Ma 1.0–1.7 returns ≈435–980°, where the figure and the text both show ≈149–168°. The coefficients must not be transcribed; if we want the closed form, refit from Fig. 6 (or from our own P3 phase data, which is the better answer anyway).
2. **The text's lateral authority figure does not reconcile exactly with Fig. 14's geometry.** The text says "about 260 m" lateral at a 30 s start; the figure's −90°/90° command points span ≈640 m, i.e. roughly ±300 m about the nominal impact. Quote the text and the figure together, or quote the figure's shape rather than either number alone.
3. **The text layer is not usable for equations.** The extraction interleaves symbols and mis-assigns the matrices and equation numbers around eqs. (4)–(15) and (27)–(31). Every number in this note was read from a rendered page.
4. **Their simulator has no angular feedback** (their §5.3.1 says so explicitly) and accepts ≈10° of sideslip. Their stability conclusions are therefore not evidence about a design that closes a 1 kHz loop around the ring angle.
5. **Their authority numbers are their canards'.** Read as class evidence, never as our capability.

---

## 7. Figures extracted from the paper

All in `notes/figures/wang2015/`, regenerable with `python3 notes/figures/wang2015/extract.py` (needs `poppler-utils` and Pillow).

| File | What it shows |
|---|---|
| `p7-fig3-projectile-with-fixed-canards.jpg` | Their projectile and canard arrangement — the C1 corroboration |
| `p7-fig4-5-phase-angle-and-phase-shift.jpg` | **The headline pair.** Fig. 4: the response direction for the four command angles, curves separated rigidly by the command separation. Fig. 5: the phase shift itself — ≈172° at launch, minimum ≈146–149° at t ≈ 42–45 s, ≈163° at the end |
| `p8-fig6-phase-shift-mach-polynomial-fit.jpg` | Phase shift against Mach, ≈149° at Ma 1.0 rising to ≈167° at Ma 1.65, with the fit that eq. (30) fails to reproduce |
| `p10-fig9-10-predictive-results-and-fading-memory-filter.jpg` | Prediction error against the number of nominal-trajectory rows (<0.8 m / <0.1 m at 75 rows) and the fading-memory filter with and without GPS noise |
| `p11-fig11-12-filter-at-45deg-and-gnc-process.jpg` | The filter against a real 0.5° firing-elevation error (constant ≈30 m downrange, ≈20 m lateral), and their guidance-and-control process block diagram |
| `p12-fig13-14-predictive-derivation-and-correction-authority.jpg` | The downrange/lateral / φ_D geometry, and the authority curves for correction starting at 30–80 s |
| `p13-fig15-16-range-vs-altitude-and-cross-range.jpg` | The controlled trajectory against nominal — apogee ≈8.8 km, impact ≈27 km, ≈1 km of lateral to remove |
| `p13-fig17-19-predictive-results-sideslip-and-command-angle.jpg` | Predictive deviation through the flight, the **≈10° induced sideslip**, and the command-angle history |
| `p14-table2-and-fig20-disturbances-and-monte-carlo.jpg` | The disturbance set R5 can cite, and the Monte Carlo result behind the ≤30 m CEP |

---

## 8. Open items this opens

1. **G16's derivation at P3** — our own φ_d(Ma) on the named vehicle, the compensation's residual, and the propagator's fidelity to the angular response. Gates nothing in the submission; it is a P3 exit item and a P2 modelling obligation.
2. **Risk 10's quantification** — authority versus correction start time on our airframe, replacing the unquantified "worse than 1.11:1". This one *does* touch the submission: it is the honest form of the authority claim on slide 3/5.
3. **S4's 3° bound versus the induced sideslip** — resolve deliberately, in writing, either way.
4. **Risk 8's coefficient list** — Magnus added to what must be sourced or computed.
5. **The perturbation predictor** — decide at P3 whether it is built as the propagator's cross-check (cheap, ≤5 kB, no propagation) or left as a documented alternative.
