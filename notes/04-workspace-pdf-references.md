# References inside the workspace PDFs — full list, relevance, harvest

**Written** 2026-09-27. Purpose: extract every reference from the two source PDFs held in this
workspace, judge each one against the SIH26098 design, and download the ones that are legally
retrievable. Downloads live in `notes/references/`.

**The two libraries, and why there are two.** The repo root holds the **source library** — files
under the names the publishers gave them, fetched one at a time (`US6981672.pdf`,
`Impact_point_prediction_guidance_based_on_iterativ.pdf`, `1-s2.0-…-main.pdf`), alongside the two
original sources. `notes/references/` holds the **catalogued subset** this file indexes: the same
family of work, renamed so the register row is readable from the filename, with the citation
attached. Where a file exists in both, the root copy is authoritative and is not duplicated here.
Section 6 is the reconciliation.

**Companion files:** `design/05-source-register.md` (what each source is worth) and
`submission/SIH26098-verified-source-audit.md` (what each source says). This file is the third
leg: *what is actually on disk*.

---

## 1. The three PDFs in the workspace

| PDF | What it is | Register row | References |
|---|---|---|---|
| `10463953.pdf` | Günay, *Controller Design and Implementation for a Guidance Kit Used at Spinning Rockets and Projectiles*, M.Sc. thesis, METU, April 2022 — 169 pp, LaTeX, no text layer (extracted with `pdftotext`) | **B1** — the reference architecture (5/5) | **23** |
| `Guidance_and_Control_Design_for_a_Class_of_Spin-St.pdf` | Wang, Song, Fang & Guo, *Guidance and Control Design for a Class of Spin-Stabilized Projectiles with a Two-Dimensional Trajectory Correction Fuze*, Int. J. Aerospace Engineering 2015, Art. 908304, 15 pp, open access | **C11** — the swerve-response phase (Adopt 5) | **26** |
| `submission/SIH2026-IDEA-Presentation-Format.pdf` | The official SIH 2026 six-slide idea template | **H1** (guidelines) | **0** — template only, no references |

**Total: 49 reference entries, 46 unique works** (three appear in both lists).

---

## 2. Relevance key

| Tag | Meaning |
|---|---|
| **CORE** | Directly on this project's airframe, control problem or fuze — dual-spin, fixed canards, course-correction fuze, swerve/phase, impact-point prediction, control authority, guidance-integrated fuzing. Should be read in full. |
| **SUPPORT** | A method or sub-system the design borrows (cascade/PID tuning, disturbance observers, BLDC cascade control, trajectory filtering). Worth having. |
| **BACKGROUND** | General flight dynamics, or a mechanism this design explicitly rejected. Cite only. |
| **NOT RELEVANT** | Generic control textbook or off-topic work. Not downloaded. |

---

## 3. Günay 2022 thesis — the 23 references

| # | Reference | Tag | Status |
|---|---|---|---|
| T1 | Wang, Wang & Yu, *Influence of control strategy on stability of dual-spin projectiles with fixed canards*, Defence Technology 14(6):709–719, 2018 | **CORE** (register **C4**) | ✅ on disk at repo root — see §6.1 |
| T2 | Spagni, Theodoulis & Wernert, *Flight control for a class of 155 mm spin-stabilized projectile with reciprocating canards*, AIAA GNC 2012 | **CORE** (register **C6** — the rejected mechanism) | ⛔ AIAA paywall |
| T3 | Barton, *155-mm M795 aerofuze test at the Kofa range, Yuma Proving Ground, 19 May 2015*, ARDEC/METC tech. rep. 2017 | **CORE** — a live-fire dual-spin test report | ⛔ not located publicly |
| T4 | Robinson & Berefelt, *On Guidance and Control for Guided Artillery Projectiles, Part 1: General Considerations*, FOI, 2011 | **CORE** (register **C5**) | ✅ **downloaded** |
| T5 | Clancy, Bybee & Friedrich, *Fixed canard 2-D guidance of artillery projectiles*, US Patent 6,981,672, 2006 | **CORE** (register **C9** — credited prior art) | ✅ **downloaded** |
| T6 | Zhang, Li, Xiao & Tian, *Research on control scheme of dual-spin projectile with fixed canards*, IEEE ICMA 2016, pp. 144–148 | **CORE** | ⛔ IEEE paywall |
| T7 | Yin, Jia & Yu, *Research on roll control system for fixed canard rudder of the dual-spin trajectory correction projectile*, Wireless Personal Communications 103(1):83–98, 2018 | **CORE** — roll control of exactly this rudder | ⛔ Springer paywall |
| T8 | Costello, *Modeling and simulation of a differential roll projectile*, AIAA MST 1998 | **CORE** — the differential-roll lineage | ⛔ AIAA paywall |
| T9 | Wernert, Theodoulis & Morel, *Flight dynamics properties of 155 mm spin-stabilized projectiles analyzed in different body frames*, AIAA AFM 2010 | **CORE** — body-frame framing | ⛔ OA copy exists at EPFL Infoscience but the site refuses non-browser fetches |
| **T10** | **Zhang, Yao & Zheng, *Impact point prediction guidance based on iterative process for dual-spin projectile with fixed canards*, Chinese J. Aeronautics 32(8):1967–1981, 2019** | **CORE — the register's B2, Cite 4 / Adopt 4, currently an abstract-only read** | ✅ on disk at repo root — see §6.1. **Rule 1 of the register makes reading it the highest-value next action** |
| T11 | Ogata, *Modern Control Engineering* | NOT RELEVANT | — |
| T12 | Åström & Hägglund, *Advanced PID Control* | NOT RELEVANT | — |
| T13 | Åström & Hägglund, *PID Controllers* | NOT RELEVANT | — |
| T14 | Visioli, *Practical PID Control* | NOT RELEVANT | — |
| T15 | Smith, Crawford & Moore, *Marine Auxiliary Machinery* | NOT RELEVANT | — |
| T16 | Soares, Calil & Stephan, *Cascade control vs full-state feedback*, IEEE COBEP/SPEC 2019 | SUPPORT — justifies B1's cascade form | ⛔ IEEE paywall |
| T17 | Karapinar, Esen, Şahin & Kanburoğlu, *Cascaded controller algorithm design for a BLDC motor…*, SIU 2013 | SUPPORT — the alternator's own control | ⛔ IEEE paywall |
| T18 | Wernert & Theodoulis, *Modelling and stability analysis for a class of 155 mm spin-stabilized projectiles with course correction fuze (CCF)*, AIAA AFM **2013** | **CORE** (register **C1**) | ⛔ AIAA paywall |
| T19 | Same title, AIAA AFM **2011** — duplicate entry in the thesis | **CORE** (same as C1) | ⛔ AIAA paywall |
| T20 | Sinha & Ananthkrishnan, *Advanced Flight Dynamics with Elements of Flight Control* | NOT RELEVANT | — |
| T21 | Li, Yang, Chen & Chen, *Disturbance Observer-Based Control: Methods and Applications* | SUPPORT — the DOB in B1 | ⛔ CRC textbook |
| T22 | Guan & Yi, *Modeling of dual-spinning projectile with canard and trajectory filtering*, Int. J. Aerospace Engineering 2018, Art. 1795158 | **CORE** — 7-DOF dual-spin model + UKF | ✅ **downloaded** |
| T23 | Khalil, Abdalla & Kamal, *Dispersion analysis for spinning artillery projectile*, 13th Int. Conf. Aerospace Sciences & Aviation Technology (ASAT-13), MTC, 2009 | **CORE** (register **C8**) | ⛔ publisher (EKB) rate-limits this network |

---

## 4. Wang et al. 2015 — the 26 references

| # | Reference | Tag | Status |
|---|---|---|---|
| W1 | Clancy, Bybee & Friedrih, *Fixed canard 2-D guidance of artillery projectile*, US 6981672 B2 | = T5 (register **C9**) | ✅ **downloaded** |
| W2 | Costello, *Modeling and simulation of a differential roll projectile*, AIAA MST 1998 | = T8 — **CORE** | ⛔ AIAA paywall |
| W3 | Wernert & Theodoulis, *Modeling and stability analysis … CCF*, AIAA AFM 2011, pp. 1–13 | = T19 (register **C1**) | ⛔ AIAA paywall |
| **W4** | **Theodoulis, Gassmann, Wernert, Dritsas, Kitsios & Tzes, *Guidance and control design for a class of spin-stabilized fin-controlled projectiles*, JGCD 36(2):517–531, 2013** | **CORE — the canonical 155 mm G&C design paper; ONERA/ISL, absent from the register** | ⛔ AIAA paywall |
| W5 | Gagnon & Lauzon, *Course correction fuze concept analysis for in-service 155 mm spin-stabilized gunnery projectiles*, AIAA GNC 2008 | **CORE** (register **C2**) | ⛔ AIAA paywall |
| W6 | Fresconi, Cooper, Celmins, DeSpirito & Costello, *Flight mechanics of a novel guided spin-stabilized projectile concept*, J. Aerospace Eng. 226(3):327–340, 2012 | **CORE** | ⛔ paywall (the Georgia Tech author copy is a dead link) |
| W7 | Gross, Costello & Fresconi, *Impact point model predictive control of a spin-stabilized projectile with instability protection*, AIAA AFM 2013 | **CORE** — IPP + the instability question | ⛔ AIAA paywall |
| **W8** | **Costello & Peterson, *Linear theory of a dual-spin projectile in atmospheric flight*, JGCD 23(5):789–797, 2000** | **CORE — the foundational linear theory for this exact configuration; absent from the register** | ✅ **downloaded** (ARL-CR-448 / ADA375201) |
| W9 | Yang, Lin, Chopper et al., *Analysis and evaluation of guidance integrated fuzing*, AIAA 93-3786CP, 1993 | **CORE** — the guidance-integrated-fuze programme, i.e. the fuze half of this PS | ⚠️ reference itself not located; a **related NSWCDD report on the same GIF programme is downloaded instead** |
| W10 | Corriveau, Berner & Fleck, *Trajectory correction using impulse thrusters for conventional artillery projectiles*, 23rd Int. Symp. Ballistics, 2007 | SUPPORT — the impulse-thruster counterfactual | ⛔ not located publicly |
| **W11** | **Corriveau, Wey & Berner, *Thrusters pairing guidelines for trajectory corrections of projectiles*, JGCD 34(4):1120–1128, 2011** | SUPPORT — the correction-authority counterpart to M7 | ✅ **downloaded** (DTIC ADA581953) |
| W12 | Calise & El-Shirbiny, *An analysis of aerodynamic control for direct fire spinning projectiles*, AIAA GNC 2001 | BACKGROUND | ⛔ AIAA paywall |
| W13 | Calise, El-Shirbiny & Kim, *An adaptive guidance approach for spinning projectiles*, AIAA GNC 2004 | BACKGROUND | ⛔ AIAA paywall |
| W14 | Frost & Costello, *Control authority of a projectile equipped with an internal unbalanced part*, JDSMC 128(4):1005–1012, 2006 | BACKGROUND — a rejected control mechanism, useful for the authority trade | ⛔ paywall |
| W15 | Rogers & Costello, *Control authority of a projectile equipped with a controllable internal translating mass*, JGCD 31(5):1323–1333, 2008 | BACKGROUND — same reason | ⛔ paywall |
| **W16** | **Ollerenshaw & Costello, *On the swerve response of projectiles to control input*, JGCD 31(5):1259–1265, 2008 — and the ARL-CR-0604 report version** | **CORE — the register's B16, the swerve-response phase, Adopt 5** | ✅ **downloaded** (ARL-CR-0604) |
| W17 | Fresconi & Plostins, *Control mechanism strategies for spin-stabilized projectiles*, AIAA 2009 / ARL-TR-4611 | **CORE** — the control-mechanism trade for this airframe | ✅ **downloaded** (DTIC ADA494194) |
| W18 | Fresconi & Ilg, *Model predictive control of agile projectiles*, AIAA AFM 2012 | SUPPORT — MPC alternative to B1's cascade+DOB | ⛔ AIAA paywall |
| W19 | Letniak & Costello, *A nonlinear model predictive observer for smart projectile applications*, AIAA AFM 2007 | SUPPORT | ⛔ AIAA paywall |
| W20 | Slegers, *Predictive control of a munition using low-speed linear theory*, JGCD 31(3):768–775, 2008 | SUPPORT — trajectory prediction for G1/G4 | ⛔ paywall |
| **W21** | **Hainz & Costello, *Modified projectile linear theory for rapid trajectory prediction*, JGCD 28(5):1006–1014, 2005** | **CORE — the propagation model behind G1's impact-point prediction and G4's 13 m term** | ⛔ paywall |
| **W22** | **Cooper, Fresconi & Costello, *Practical assessment of real-time impact point estimators for smart weapons*, AIAA AFM 2008** | **CORE — the direct evaluator of the G4 error budget** | ⛔ AIAA paywall |
| W23 | Ghosh & Prakash, *Neural models for predicting trajectory performance of an artillery rocket*, J. Aerospace Computing 1(2), 2004 | BACKGROUND | ⛔ paywall |
| W24 | Kramer & Stubberud, *Impact time and point predicted using a neural extended Kalman filter*, IEEE ISSNIP 2005 | SUPPORT — a filter route for N1 | ⛔ IEEE paywall |
| **W25** | **Robinson & Strömbäck, *Perturbation based guidance for a generic 2D course correction fuze*, AIAA GNC 2013** | **CORE — the direct antecedent of C11's perturbation IPP, i.e. of G4/G16** | ⛔ AIAA paywall; no FOI report version located |
| **W26** | **Murphy, *Free flight motion of symmetric missiles*, BRL Report 1216, July 1963** | **CORE — the classical yaw-of-repose/angular-motion theory the swerve phase descends from** | ✅ **downloaded** (ADA442757) |

---

## 5. What was downloaded — 11 files in `notes/references/`

| File | Ref | Pages | Source route |
|---|---|---|---|
| `B16-Ollerenshaw-Costello-2008-ARL-CR-0604-Swerve-Response.pdf` | W16 / register B16 | 30 | GovInfo (GPO D101 collection) |
| `C5-Robinson-Berefelt-2011-FOI-R-3291-Guidance-Control-Guided-Artillery.pdf` | T4 / register C5 | 33 | FOI REST API (`foi.se/rest-api/report/FOI-R--3291--SE`) |
| `T22-Guan-Yi-2018-IJAE-Dual-Spinning-Canard-Filtering.pdf` | T22 | 8 | Open access (CC BY), Semantic Scholar mirror |
| `W8-Costello-Peterson-2000-JGCD-Linear-Theory-Dual-Spin-Projectile.pdf` | W8 | 62 | GovInfo — ARL-CR-448, DTIC ADA375201 |
| `W9-Yang-2001-GIF-Guidance-Integrated-Fuze.pdf` | W9 — *same programme, not the same paper* | 12 | Internet Archive — DTIC ADA394578 (NSWCDD, 2001) |
| `W11-Corriveau-Wey-Berner-2011-Thrusters-Pairing-Guidelines-Trajectory-Correction.pdf` | W11 | 10 | Internet Archive — DTIC ADA581953 |
| `W17-Fresconi-Plostins-2009-Control-Mechanism-Strategies-Spin-Stabilized-Projectiles.pdf` | W17 | 34 | Internet Archive — DTIC ADA494194 (ARL-TR-4611) |
| `W26-Murphy-1963-ARL-1216-Free-Flight-Symmetric-Missiles.pdf` | W26 | 237 | Internet Archive — DTIC AD0442757 |
| `W-ARL-ADA441073-2006-Swerving-Motion-Dual-Spin-Lateral-Pulse-Jets.pdf` | **adjacent — not in either list** | 30 | Internet Archive — Burchett, Peterson & Costello, ARL-CR-570, 2005 |
| `W-ARL-ADA607104-2014-Impact-Point-Prediction-Thrusting-Projectiles-Wind.pdf` | **adjacent — not in either list** | 31 | Internet Archive — Yuan, Bar-Shalom & Willett, IEEE TAES 2013 (ARO-funded) |
| `W-Act-ADA462961-2006-Gas-Generator-Actuator-Arrays-Spinning-Body-Projectiles.pdf` | **adjacent — not in either list** | 6 | Internet Archive — English, Gadiraju, Rinehart, Glezer & Allen, 2006 |

**The register's C9 patent is not in this folder.** It is at the repo root as `US6981672.pdf`, and the
copy taken during this pass is byte-identical to it (md5 `b2ea7cd1…`), so the duplicate was dropped.
`notes/references/` and the root library carry the same file once each, in one place only.

**The three "adjacent" rows are flagged deliberately.** They are *not* references of either PDF;
they were surfaced while resolving the reference lists on the same repositories and they address
the same problems (dual-spin swerve, impact-point prediction under wind, actuation of a spinning
body). They are kept because they are free, on-topic, and sit in the same family as B16 — but they
must not be cited as if the source PDFs pointed at them.

**Eight of the eleven are literal references** from the two bibliographies: W16, T4, T22, W8, W11,
W17, W26, and the W9-adjacent GIF report.

---

## 6. Reconciliation with the root source library

### 6.1 Fetched separately, now on disk at the repo root

These arrived in commit `90a94eb` ("Add the source library…") while this pass was running. They are
the files this pass could not reach, plus two more. **They are on disk — do not re-fetch them.**

| Root file | Ref | What it is |
|---|---|---|
| `Impact_point_prediction_guidance_based_on_iterativ.pdf` | **B2 / T10** | Zhang, Yao & Zheng 2019, Chinese J. Aeronautics 32(8):1967–1981 — the iterative-process IPP law. **This is the one the register holds at Cite 4 / Adopt 4 on an abstract-only read.** Its `†` can now be retired by reading the file |
| `Influence_of_control_strategy_on_stability_of_dual.pdf` | **C4 / T1** | Wang, Wang & Yu 2018, Defence Technology 14(6):709–719 — control strategy ↔ stability coupling |
| `1-s2.0-S2214914725001722-main.pdf` | **B4** | Wang, Zhang, Lin, Lin & Xi, *Investigation of flight stability for fixed canard dual-spin projectile via CFD/RBD coupled method*, Defence Technology 53 (2025) 1–18 — the paper that reproduces the **resonance instability** and forces criterion S8 |
| `1-s2.0-S2214914723003227-main.pdf` | **new — not in either reference list** | Karimi, Rajabi, Sadati & Hosseini, *Multidisciplinary design optimization of a dual-spin guided vehicle*, Defence Technology 37 (2024) 133–148. Multidisciplinary sizing of a dual-spin airframe — the C-domain's own optimisation problem, adjacent to **C44/C45** |
| `US6981672.pdf` | **C9 / T5 = W1** | The Clancy fixed-canard 2-D patent (byte-identical to this pass's copy, which was dropped) |

**Consequence for the register.** §7's point 1 is now satisfied for B2 by possession rather than by
access, and B4 — the row that created S8 and risk 41 — is readable in full instead of at abstract.
Reading these three files is the highest-value next action this pass leaves open; nothing in them has
been read yet.

### 6.2 Still not retrievable from this machine

| Ref | Paper | Why it failed | Route to use instead |
|---|---|---|---|
| **T9** | Wernert, Theodoulis & Morel 2010, *Flight dynamics properties…* | OA deposit at <https://infoscience.epfl.ch/entities/publication/4089b44d-fda5-448d-b707-23c797709764> answers HTTP 405 to non-browser fetches | EPFL Infoscience page, normal browser |
| **T23 / C8** | Khalil, Abdalla & Kamal 2009, *Dispersion analysis…*, ASAT-13 | Publisher (<https://journals.ekb.eg/article_23740.html>) rate-limits this network with HTTP 429 | Retry the EKB page later |

**Note on ScienceDirect.** The two open-access articles that defeated this pass (B2, C4) were
retrieved by hand without difficulty, which confirms the block was environmental rather than
licensing — this network gets an HTTP 403 and a Cloudflare captcha, a normal browser does not. Any
future ScienceDirect OA target is worth one manual attempt before it is written off.

The remainder — every AIAA, IEEE, Springer, SAGE and CRC item in §3 and §4 — is a **paywall**, not a
blocked open-access file. There is no legitimate download for those from here.

**Two paywalled items are worth buying or requesting**, because the register's own Rule 1 makes them
blocking: **W4** (Theodoulis et al. 2013, JGCD — the canonical 155 mm G&C paper) and **W21/W22**
(Hainz & Costello 2005, Cooper/Fresconi/Costello 2008 — the trajectory-prediction and IPP-estimator
pair behind G1's propagation and G4's error term).

---

## 7. What this changes for the register

1. **B2's `†` can be retired — by reading, not by fetching.** Zhang 2019 is CC-licensed and now on
   disk at the root. The register has held it at "abstract" only because nobody opened it; Rule 1
   says Cite 4 is not allowed on an abstract read, so **reading this one file is the single highest-
   value action this pass leaves open.**
2. **B4's `†` likewise.** Wang et al. 2025 is now on disk in full. B4 is the row that *created*
   criterion **S8** and risk **41** — the resonance instability — and it has never been read past its
   abstract.
3. **Six references in these two PDFs are absent from `design/05-source-register.md`** and are all
   direct hits on open G-domain rows — worth adding as new rows or as basis-hardening:
   **W4** (Theodoulis 2013), **W8** (Costello & Peterson 2000 — the dual-spin linear theory),
   **W17** (Fresconi & Plostins — control-mechanism trade), **W21** (Hainz & Costello — trajectory
   prediction), **W22** (Cooper/Fresconi/Costello — real-time IPP estimators) and **W25**
   (Robinson & Strömbäck — perturbation guidance for a 2D CCF).
   W8 and W21/W22 relate to **G1/G4**; W25 relates to **G4/G16**; W17 relates to **C1's** mechanism trade.
4. **The register's C5 row** (Robinson & Berefelt) can now carry a full-text read tag — the report is
   on disk.
5. **One root file is not in either reference list** — Karimi et al. 2024, multidisciplinary design
   optimisation of a dual-spin guided vehicle. It touches the open trades **C44/C45** and has no
   register row. Decide whether it is cited or merely held.
6. **Nothing here turns into a slide-number change.** These are basis-hardening rows, not new
   headline values.

---

## 8. Reproduction

The two source bibliographies were extracted with:

```bash
pdftotext -layout "10463953.pdf" /tmp/10463953.txt                  # thesis, refs at line 3896
pdftotext -f 14 -l 15 "Guidance_and_Control_...Spin-St.pdf" -      # Wang, references page
```

`10463953.pdf` has no text layer for one page (p. 11) only; both bibliographies extract cleanly.
