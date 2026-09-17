# DRISHTI-PGK — Reference 155 mm HE Model and Declared Envelope

**Purpose of this file:** to replace the YIL shell drawing as the design's platform basis. It states what the design is sized against *now*, from public sources, and the envelope it must close over. Every parameter carries its provenance. It is the input to the P-domain and S-domain criteria, and it is re-baselined in P6 when YIL's documents arrive.

**Roadmap item:** carried item 6 ("Build the reference 155 mm HE model from public sources").

**Standing — read this first.** Nothing here is YIL data. Nothing here is an assumption that YIL's shell behaves this way. It is a *public-record proxy* for the 155 mm HE class, declared as an envelope, so that the platform and stability domains can be designed rather than parked. The design is a parametric product: it is specified as a set of limits it satisfies across the envelope, which is how a supplier defines a retrofit kit. Post-selection, P6 re-baselines every value below against YIL's actual drawing and firing tables.

---

## 1. Sources and their standing

| # | Source | What it provides | Standing |
|---|---|---|---|
| S1 | GD-OTS, *155 mm M795 HE Artillery Projectile* product datasheet (2024) | M795 mass 103 lb (46.7 kg), 23.8 lb TNT / IMX-101 fill, gilding-metal rotating band, charge compatibility 3W–8S (M3A1–M203A1) | Manufacturer public datasheet |
| S2 | *M795 projectile* — Wikipedia, citing Jane's Ammunition Handbook and GD-OTS | 46.7 kg as fired, 840 mm with fuze, 154.89 mm body diameter, range 22.5 km (39 cal), **CEP 139 m at maximum range (39 cal)** | Public record; CEP figure traces to Milner, NDIA Precision Strike Annual Review 2012 |
| S3 | *M549* — Wikipedia, citing Jane's and TM 43-0001-28 | M549A1 43.6 kg **without fuze**, 873.5 mm fused, 154.89 mm body diameter, 30.1 km from M198/M109A6 (39 cal), **CEP 259 m at max range (39 cal)** | Public record; CEP figure traces to the same NDIA 2012 presentation |
| S4 | *M1156 precision guidance kit* — Wikipedia, citing Jane's | **CEP 267 m for an unguided M549A1 at maximum range**; PGK mass 1.4 kg, 220.2 mm overall, 95.25 mm visible, 124.7 mm intrusion; four fixed canards; alternator, no battery; PD + proximity; unit cost US$13,541 (FY2013) | Public record — **this is the M6 anchor already in the register** |
| S5 | DOT&E, *Precision Guidance Kit (PGK) FY2015* | PGK is a combined fuze + GPS guidance module for M795 **and** M549A1; threshold 50 m CEP, objective 30 m CEP | US DoD test report |
| S6 | Balon & Komenda, "Analysis of the 155 mm ERFB/BB Projectile Trajectory", *Advances in MT* 1/2006 | A **complete published mass-property set for a 155 mm projectile**: 47.5 kg fuzed, Ixx 0.161 kg·m², Iyy 2.1061 kg·m², CG 0.6287 m from nose, overall length 0.9487 m (ogive 0.7714 / cylinder 0.0683 / tail 0.1090), base Ø140.9 mm, spin-vs-burn data | Peer-reviewed, PRODAS/I-DEAS derived — **the calibration case for our own computation** |
| S7 | Ferfouri et al., *J. Serbian Soc. Comp. Mech.* 17(2), 2023 | M107 geometry in calibers: overall 4.5097, nose 2.4129, base Ø0.869, rotating band Ø1.01935, CG at 2.9572 cal from the fuze; C_D0 and component drag | Peer-reviewed CFD/semi-empirical validation study |
| S8 | M557 mechanical PD fuze datasheet (MKE USA) | **Thread 2″-12 UNS-2A**, mass ≈975 g, total height 151.6 mm max | Manufacturer public datasheet |
| S9 | MIL-STD-333B, *Fuze, Projectile and Accessory Contours for Large Caliber Armaments* (1 May 1989) | The standardised nose fuze **thread, contour and projectile cavity** interface for gun projectiles ≥75 mm — "to insure physical interchangeability and that no special aiming corrections are required" | US military standard — the interface authority |

**What these sources do not give us:** YIL's shell. They give the class. That is the point.

---

## 2. The reference platform

Two projectiles bracket the class. Both are 155 mm HE, both are the M1156 PGK's own qualified platforms (S5), and together they span the mass, length and dispersion range the design must survive.

| Quantity | M795 HE | M549A1 HERA | Reference model (design point) |
|---|---|---|---|
| Mass as fired, with fuze | 46.7 kg (103 lb) | 43.6 kg (96 lb) without fuze → ≈44.6 kg with a 975 g fuze | **45.0 kg** |
| Length, fused | 840 mm (858 mm in the GD-OTS infobox) | 873.5 mm | **855 mm** |
| Body diameter | 154.89 mm | 154.89 mm | **154.89 mm** |
| Fill | 10.8 kg TNT / IMX-101 | 6.8 kg TNT | — |
| Max range (39 cal) | 22.5 km | 30.1 km | — |
| Unguided CEP at max range | **139 m** (S2) | **259 m** (S3) / **267 m** (S4) | **267 m — the M6 anchor** |
| Charge compatibility | 3W–8S (M3A1–M203A1) | top zones incl. 8S | covers the PS's 3M–6M band |

**Note the dispersion spread.** The public record puts unguided CEP at maximum range between 139 m (M795, 22.5 km) and 267 m (M549A1, 30.1 km). Dispersion grows with range and the rocket-assisted round is the worse of the two. The register's M4 decision claims CEP ≤ 30 m at the **maximum-range, full-charge** condition, so the **267 m / σ 227 m end governs the design**; 139 m is carried as the optimistic envelope edge. This is the sensitivity M7's authority budget is tested against — see §8.

---

## 3. Mass properties — method and result

The published ERFB/BB dataset (S6) is the only complete public mass-property set for this class, so it is used to **calibrate** a simple model, and the calibrated model is then applied to the M795/M549A1 geometry. This is stated as a method, not presented as measurement.

**Method.** Model the projectile as a body of revolution — tangent-ogive nose (tip truncated at the standard fuze diameter, Ø50.8 mm), cylindrical body, truncated-cone boattail to the published base diameter — with **uniform density**, the density set to reproduce the published mass. Integrate numerically:

```
m    = ρ ∫ A dx                     A = π r(x)²
x_cg = ρ ∫ x A dx / m
Ixx  = ½ ρ π ∫ r⁴ dx
Iyy  = ρ ∫ [ (x − x_cg)² + r²/4 ] A dx
```

**Calibration on the published ERFB/BB case** (uniform-density model vs. published CAD values):

| Quantity | Uniform-density model | Published (S6) | Factor |
|---|---|---|---|
| Mass | 47.50 kg | 47.50 kg | by construction |
| CG from nose | 0.6150 m (0.648 L) | 0.6287 m (0.663 L) | — |
| Ixx | 0.1149 kg·m² | **0.161 kg·m²** | **1.401** |
| Iyy | 2.2678 kg·m² | **2.1061 kg·m²** | **0.929** |

The CG and Iyy agree within 8 %. **Ixx is 29 % low** — expected, because the real projectile concentrates mass in the steel wall at full radius rather than uniformly across the section. The two factors (kx = 1.401, ky = 0.929) are applied to the M795/M549A1 results below and are **class correction factors, not measurements**; they carry the model's uncertainty into P4/P5 and are the reason those criteria are stated as bands.

**Result for the reference model.** Across nose-length variants (ogive occupying 45 % / 53.5 % / 65 % of the fused length — the M107 class nose fraction is 53.5 %, S7):

| Case | m | CG from nose | Ixx (corrected) | Iyy (corrected) |
|---|---|---|---|---|
| M795, nose 45 % | 46.7 kg | 0.482 m | 0.167 kg·m² | 1.81 kg·m² |
| **M795, nose 53.5 %** | **46.7 kg** | **0.497 m** | **0.165 kg·m²** | **1.73 kg·m²** |
| M795, nose 65 % | 46.7 kg | 0.517 m | 0.162 kg·m² | 1.66 kg·m² |
| M549A1 class, nose 53.5 % | 45.0 kg | 0.517 m | 0.159 kg·m² | 1.80 kg·m² |

**Cross-check against the register's existing `[ref]` values.** The thesis platform is 43 kg, Ixx 0.144, Iyy 1.216 kg·m².

- **Ixx agrees.** Scaling the M795 result to 43 kg gives 0.152 kg·m² against the `[ref]` 0.144 — a 5 % divergence, inside the model's own uncertainty.
- **Iyy does not agree.** The public-calibrated band is **1.66–1.81 kg·m²** for the M795 class; the `[ref]` value is **1.216 kg·m²**, some **28 % lower** and outside the band. The ERFB/BB projection (2.1061 kg·m² at 0.9487 m, scaled by L² and mass to the M795's 0.840 m) independently gives **1.62 kg·m²** — it does not support 1.216 either.
- **Consequence:** the `[ref]` pair (0.144 / 1.216) is **not adopted as the design case**. It sits at the optimistic end. Because **Sg ∝ Ixx²/Iyy**, a low Iyy flatters the stability result, and taking a flattering value for the one criterion that can veto the whole architecture is not defensible. The design is therefore sized on the **public-calibrated band, with the design point at Ixx 0.155 / Iyy 1.75 kg·m²**, and P4/P5 are declared as bands. This divergence is recorded as risk 21.

> **Design point adopted:** m = 45.0 kg · Ixx = 0.155 kg·m² · Iyy = 1.75 kg·m² · CG 0.50 m from the nose · L = 855 mm · d = 154.89 mm.
> **Envelope:** m 43–47 kg · Ixx 0.144–0.167 · Iyy 1.22–1.81 · CG 0.55–0.62 L from the nose.

---

## 4. The standardised fuze-well interface

This is the strongest public anchor in the whole model, because it is the interface our kit must mate with and it is fixed by a military standard rather than by any one projectile.

| Element | Value | Source |
|---|---|---|
| Interface standard | **MIL-STD-333B** — nose fuze threads, fuze contours and projectile cavities, gun projectiles ≥75 mm | S9 |
| Fuze thread | **2″-12 UNS-2A** | S8, on an in-service 155 mm PD fuze |
| Standard fuze mass (the thing we replace) | **≈975 g** | S8 (M557) |
| Standard fuze height above the seat | 151.6 mm max | S8 |
| **Kit intrusion into the fuze well** | **≤ 124.7 mm** | S4 — M1156 PGK, qualified on both M795 and M549A1 |
| Kit length above the fuze seat | **≤ 95.25 mm** | S4 |
| Kit overall length | 220.2 mm | S4 (as a check: 124.7 + 95.25 = 219.95 mm ✓) |
| Kit mass | **1.4 kg** — 0.45 kg more than a standard fuze | S4 |

**Why the PGK's dimensions are the right anchor and not a guess.** The M1156 is a fielded kit that screws into the same MIL-STD-333B interface and is qualified on exactly the two projectiles in §2 (S5). Its intrusion depth of 124.7 mm is therefore *evidence of how much axial room the standard well actually offers*, published by a source with no reason to understate it.

**Net mass penalty.** The kit does not add 1.4 kg to the projectile; it **replaces** a ≈0.98 kg fuze. The marginal mass is **≈0.42 kg**, or **0.9 % of a 45 kg projectile**. That reframing is a feasibility statement in its own right and it is what makes P9 answerable now.

---

## 5. Ogive envelope — maximum kit diameter at each station

The kit's outer contour forward of the fuze seat is bounded by the shell's ogive. The ogive is modelled as a tangent ogive through the published nose length (S7: fused length 4.5097 cal, nose 2.4129 cal → nose fraction 0.535), truncated at the standard fuze diameter Ø50.8 mm. For the reference model (L = 840 mm, nose 449 mm):

| Station aft of the fuze seat | Shell diameter at that station | Available for the kit |
|---|---|---|
| 0 mm (seat) | 50.8 mm | — |
| 20 mm | 61.9 mm | — |
| 40 mm | 72.4 mm | — |
| 60 mm | 82.2 mm | — |
| 80 mm | 91.4 mm | — |
| **95 mm (end of the kit's visible length)** | **97.9 mm** | **canard span must exceed this to be effective** |
| 120 mm | 107.9 mm | — |
| 160 mm | 121.8 mm | — |
| 200 mm | 133.2 mm | — |
| 250 mm | 144.1 mm | — |
| 300 mm | 151.2 mm | — |
| 370 mm (full diameter) | 154.9 mm | — |

**Two consequences the design must respect:**

1. **The kit has only Ø98 mm of shell to work with at the forward end of its visible length.** Any aerodynamic surface that is to generate a useful normal force must extend beyond Ø98 mm — a stowed-canard design has to deploy *outward as well as outward-forward*. This is a hard constraint on C4/C5, and it is fixed by the shell, not by us.
2. **In-bore, nothing may exceed Ø155 mm.** The ogive table is the outside bound for stowage; the bore is the inside bound for the deployed state. C31 (in-bore stowage and safety) is written against both.

**Method caveat.** The real contour is a secant-ogive variant of the same nose length, not exactly a tangent ogive; the divergence is confined to the forward ~300 mm and is within a few millimetres of diameter. The table is a design bound, not a drawing, and is superseded by YIL's drawing at P6.

---

## 6. Published dispersion

| Condition | Unguided CEP | Equivalent circular 1σ (CEP/1.1774) | Source |
|---|---|---|---|
| M549A1 at 30.1 km, 39 cal | **267 m** | **227 m** | S4 — **the M6 anchor in use** |
| M549 at max range, 39 cal | 259 m | 220 m | S3 |
| M795 at 22.5 km, 39 cal | **139 m** | **118 m** | S2 |

**The M6 anchor is confirmed, not merely asserted.** Two independent citations of the same class of round give 259 m and 267 m — the register's 227 m σ sits between them and is the conservative of the pair. The third data point (139 m for the M795 at a shorter range) shows how strongly the number is range-dependent and is the reason the anchor is tied to M4's maximum-range condition rather than quoted bare.

**Sensitivity to be carried into M7 and R5:** the correction authority M7 derives is A = σ·√(−2·ln(1−P)). At P = 80 %: σ 227 m → **407 m** (the M7 design value); σ 118 m → **212 m**. The design must close at the 227 m end; the 118 m end is the lower bound of the envelope and is reported, not claimed.

---

## 7. The kit benchmark — what the fielded analogue establishes

The M1156 PGK is the fielded answer to the same problem statement. It sets the performance bar and the cost bar, and it is the only public evidence that this architecture works.

| Quantity | M1156 PGK (public) | Source |
|---|---|---|
| Accuracy | Threshold < 50 m CEP, objective < **30 m CEP** | S5 |
| Demonstrated | Median < 10 m in lot acceptance testing; 90 % of rounds within 5 m in a German DM111 demonstration at 27 km | S4 |
| Mass | 1.4 kg, +0.45 kg over a standard fuze | S4 |
| Steering | **Four fixed canards** | S4 |
| Power | Internal **alternator, no battery** | S4 |
| Fuzing | Point-detonating + proximity airburst | S4 |
| Unit cost | **US$13,541** (FY2013); <$10,000 target; FMS pricing US$12.7k–20k per kit | S4 |
| Production | >100,000 units | S4 |

**Three things this benchmark settles for our submission:**

1. **The 30 m CEP claim is not ambitious — it is exactly the objective specification the US Army set for this class of kit, and it has been met.** The claim is therefore a known-achievable target, which is a stronger statement than an aspirational one.
2. **The cost lane is real and it is quantified.** The fielded competitor is a **$13.5k unit**, and the 2026 production award for this product class was **$863 M**. An indigenous kit at a stated volume is measured against that number, which is what K4 needs.
3. **Two capabilities in the problem statement are *not* in the fielded competitor.** The PGK offers PD + proximity only. The PS requires **proximity, time and impact**, and requires navigation and guidance that work without GPS. Both are genuine differentiators, and both are scoreable.

---

## 8. The declared envelope the design must close over

Every P- and S-domain criterion is answered against this table. Values marked *public* are sourced above; values marked *derived* are computed in this document.

| Envelope quantity | Design point | Envelope (design must close across) | Basis |
|---|---|---|---|
| Projectile mass, fuzed | 45.0 kg | 43–47 kg | public (S1–S4) |
| Overall length, fuzed | 855 mm | 840–874 mm | public (S2, S3) |
| Body diameter | 154.89 mm | 154.89 mm (fixed by calibre) | public |
| CG from nose | 0.50 m (0.585 L) | 0.55–0.62 L | derived (kx/ky-calibrated model) |
| Ixx | 0.155 kg·m² | 0.144–0.167 kg·m² | derived, band |
| Iyy = Izz | 1.75 kg·m² | 1.22–1.81 kg·m² | derived, band — includes the `[ref]` 1.216 |
| Unguided CEP at max range | 267 m (σ 227 m) | 139–267 m (σ 118–227 m) | public (S2–S4) |
| Muzzle velocity, charge 3M–6M | — | 546–943 m/s | PS + `[ref]` |
| Spin at launch | — | 1108–1912 rad/s (176–304 Hz) | `[ref]`, **confirmed by the 1:20 cal rifling check below** |
| Moment of inertia of the flight state | — | Ixx 0.144–0.167, Iyy 1.22–1.81 | — |
| Launch load | 15 000 g axial / 5 000 g radial | stated | `[ref]` |
| **Kit mass** | **1.4 kg (0.42 kg net over the fuze replaced)** | **≤ 1.4 kg total, ≤ 0.5 kg net** | public benchmark (S4) |
| **Kit intrusion into the well** | — | **≤ 124.7 mm** | public benchmark (S4) |
| **Kit length above the seat** | — | **≤ 95.25 mm** | public benchmark (S4) |
| Kit diameter in the well | — | Ø50.8 mm (2″-12 UNS-2A) | S8, S9 |
| Shell diameter at the kit's forward station | 97.9 mm | 97.9 mm | derived, ogive table |
| In-bore diameter limit (stowed) | — | Ø155 mm | bore |

**Kit mass and CG effect on the platform (derived).** With the kit's CG at ≈0.115 m from the nose and the projectile CG at 0.497 m:

- As added mass: CG shift **11.5 mm forward**.
- **Net of the fuze it replaces** (≈0.98 kg at ≈0.075 m): **2.6 mm forward — 0.31 % of the projectile length**.
- Ixx contribution from the in-well electronics (≈1.4 kg at r_eff ≈0.03 m): **+0.4 %**.
- Ixx contribution from a ring and canards at the body radius (≈1.4 kg at r ≈0.0775 m): **+5.4 %**, which *raises* Sg by ≈11 %.

So the mass and inertia consequences of the retrofit are **second-order against the platform's own spread across the envelope**. The first-order stability question is not the kit's mass — it is the aerodynamic effect of canards ahead of the CG. That is stated next.

---

## 9. Stability sensitivity — the first-order answer S1 needs

This is not S1. It is the bounded sensitivity that makes S1 a **PARAMETRIC** criterion rather than a blocked one, and it identifies what actually governs.

**Gyroscopic stability factor** (Murphy form):

```
Sg = Ixx² p² / (4 Iyy M_α)          M_α = C_Mα · q · S · d,   S = πd²/4
```

**The rifling check — and a result worth keeping.** Fixing the twist at the standard 155 mm **1 turn in 20 calibres** predicts the launch spin exactly for both charges:

| Charge | Muzzle velocity | Predicted spin (1:20 cal) | `[ref]` spin |
|---|---|---|---|
| 3M | 546.4 m/s | 1107.5 rad/s (176.3 Hz) | 176.3 Hz ✓ |
| 6M | 943.5 m/s | 1912.3 rad/s (304.4 Hz) | 304.4 Hz ✓ |

Because p = 2πV/twist exactly, **p/V is a constant of the gun and Sg at the muzzle is charge-independent** — a 6M round and a 3M round leave the tube with the same stability factor. The charge sweep is therefore not a stability driver at the muzzle, and the governing case is the **maximum-density** one (low altitude, muzzle exit), not a particular charge.

**Sg across the envelope** (ρ = 1.225 kg/m³, C_Mα bracketed 3.7–4.8 — the published 155 mm ERFB/BB range, S6):

| Ixx | Iyy | C_Mα 3.7 | C_Mα 4.3 | C_Mα 4.8 |
|---|---|---|---|---|
| 0.144 | 1.216 | 2.64 | 2.27 | 2.04 |
| 0.144 | 1.81 | 1.78 | 1.53 | **1.37** |
| 0.155 | 1.75 *(design point)* | 2.12 | **1.83** | 1.64 |
| 0.167 | 1.81 | 2.39 | 2.05 | 1.84 |

**The envelope spans Sg = 1.37 to 3.55.** The design point sits at **Sg = 1.83**, comfortably above the customary 1.3–1.5 margin. The conservative corner (Ixx 0.144, Iyy 1.81, C_Mα 4.8) sits at **Sg = 1.37** — clearing 1.3 by only 5 %.

**The canard allowance — the number that actually constrains the architecture.** Canards ahead of the CG increase C_Mα; since Sg ∝ 1/C_Mα, the allowable increment is:

| Case | Sg (no canards) | Max ΔC_Mα/C_Mα for Sg ≥ 1.3 | for Sg ≥ 1.5 |
|---|---|---|---|
| Conservative corner | 1.37 | **+5.3 %** | already below |
| **Design point** | **1.83** | **+40.8 %** | +22.0 % |
| Optimistic corner | 3.55 | +173 % | +137 % |

**What this means, stated plainly.** At the design point there is ample room for the canard set — a 20–40 % increment in the pitching moment derivative is available, which is a normal canard allowance. But **at the conservative corner of the envelope the entire stability margin is 5 % of C_Mα**, and the `[ref]` inertia pair (which the register has been carrying) would have made the picture look better than it is.

**Therefore S1's governing requirement is: the canard installation shall not increase C_Mα by more than 5 % at the conservative envelope corner, and the design shall be re-checked once P4/P5 are re-baselined.** Whether that is achievable is a canard-sizing question (C4/C5) and a P6 question. It is now **a stated requirement with a number**, which is what the parametric treatment is for. Logged as risk 3 (escalated) and risk 21.

---

## 10. What each parametric criterion takes from this model

| Criterion | Value taken | Status of the value |
|---|---|---|
| M3 | Charge/velocity envelope 546–943 m/s across 3M–6M; full functional envelope, CEP claim banded to M4 | Parametric |
| M4 | Max-range, full-charge; numeric range 22.5–30.1 km class | Parametric |
| M6 | CEP 267 m → σ 227 m, bracketed 139–267 m | Cited anchor, confirmed |
| P1 | Any MIL-STD-333B-compliant fuzed 155 mm HE in the M795/M549A1 class | Parametric |
| P2 | 45.0 kg design point, 43–47 kg envelope | Public |
| P3 | CG 0.55–0.62 L from the nose | Derived band |
| P4 | Ixx 0.144–0.167 kg·m² (design 0.155) | Derived band |
| P5 | Iyy 1.22–1.81 kg·m² (design 1.75) | Derived band |
| P6 | MIL-STD-333B, thread 2″-12 UNS-2A | Public standard |
| P7 | ≤ 124.7 mm available axial envelope forward of the fuze seat | Public benchmark |
| P8 | Ogive table §5; Ø97.9 mm at the kit's forward station | Derived |
| P9 | Kit ≤ 1.4 kg total, ≤ 0.5 kg net of the fuze replaced | Public benchmark |
| P10 | ≤ 0.31 % of length net CG shift forward at the design point | Derived |
| P11 | Kit ΔIxx ≤ +5.4 % (ring) / +0.4 % (electronics) — stability-positive | Derived |
| P12 | Ø50.8 × 124.7 mm intrusion + ≤95.25 mm visible | Public benchmark |
| P13 | Driving band and rifling untouched — the kit sits forward of the ogive | By architecture |
| P14 | Stowed envelope inside Ø155 mm; ramming load carried by the kit body | Derived from §5 |
| S1 | Sg envelope 1.37–3.55; design point 1.83; canard allowance ≤ 5 % ΔC_Mα at the corner | **Derived — parametric** |
| S2 | Canard ΔC_Mα is the binding term, bounded by S1's allowance | Parametric |
| S3–S5, S7 | Re-checked at P2/P3 against the P4/P5 bands | Parametric, deferred to analysis |
| S6 | 1108–1912 rad/s at launch, 1:20 cal twist confirmed from the `[ref]` charge table | **Confirmed from public rifling practice** |
| F11 | The setter interface is the standard gun-line interface; the PGK precedent shows PK/modern fuzes are inductively set | Parametric |

---

## 11. What changes at P6

Every value in §8 is replaced by a YIL-sourced value. Specifically, the following re-baselining is expected to move design numbers:

| Post-selection input | Re-baselines | Expected effect |
|---|---|---|
| Shell drawing: mass, CG, Ixx, Iyy | P2–P5, S1–S7 | **Sg re-run; the canard allowance recomputed** — this is the single largest re-baseline |
| Ogive contour and fuze-well drawing | P6–P8, P12, C31 | Kit outer contour and stowage envelope redrawn |
| Firing tables: dispersion and its range/deflection split | M3, M4, M6, M7, M8 | The M7 authority budget moves off the 407 m anchor |
| Fuel/charge compatibility list | M3, M9, E1, E2 | Launch load case fixed |
| Setter interface | F11, F12 | Setter data package fixed |

**Until then, this model is the design basis, and it is declared rather than hidden.**

---

## 12. Related files

| File | Purpose |
|---|---|
| `design/00-design-criteria-register.md` | The criteria this model answers; carries the PARAMETRIC values and the post-selection data list |
| `design/ROADMAP-and-prompts.md` | Phase plan; P6 is the re-baseline that retires this model |
| `notes/00-PGK-thesis-working-notes.md` | The `[ref]` values, including the Ixx/Iyy pair this model diverges from |
| `notes/02-PGK-SIH-design-brief.md` | Problem mapping and architecture decisions |
