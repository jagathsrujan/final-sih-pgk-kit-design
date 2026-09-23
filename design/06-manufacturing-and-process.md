# DRISHTI-PGK — Manufacturing and Process Dossier

**Purpose of this file:** the deep-dive research behind the submission's manufacturing and cost story. It answers three questions the register currently leaves dispersed: *which process makes each subsystem*, *what those processes cost at 5 000 kits/year*, and *what may not be claimed about them*.

**Status:** research pass, 2026-09-20. Sources are rated in the same scheme as `design/05-source-register.md` and are listed there under **section J**. **No register value is changed by this file.** The new rows and risks it proposes (§8) are proposals, and none of them is quoted in the submission until they are opened. **§7 is the advanced-manufacturing concept** — the digital print–post-treat–assemble cell, the post-treatment chain against each known AM weakness, printed structural electronics, and the modular/targeted-redundant sensor stack — and it is written to the same discipline: every claim carries a bound.

**Why this file exists:** K4's cost target (≤ ₹6.5 lakh at 5 000/yr) has no evidence under it — K5 is open and *is* the evidence the target needs. C45 (make-versus-buy) and C44 (radial versus axial flux) are open. C39 (stator lamination grade and iron loss) is open and now has three concrete process routes with published data. And slide 5 of the deck is scored as a business case (H1), where "manufacturable at volume" is a claim that has to be made of named processes, not of adjectives.

**The discipline this file follows:** every process claim is one of three things —
1. **production-mature** — in volume use today, citable to a vendor datasheet, a standard or a cost model;
2. **research-demonstrated** — a peer-reviewed result with numbers, confined to development or first-article use;
3. **declared** — a development item with its qualification cost named, never presented as ready.

No process is described as ordnance-qualified unless it is.

---

## 1. The manufacturing problem, decomposed against the criteria

Every row below is a *criterion the register already owns* — this dossier does not invent requirements, it supplies the process answer each one is waiting for.

| # | What must be made | Governing criteria | The manufacturing question |
|---|---|---|---|
| 1 | **Stator core** — 12 slots / 14 poles, Ø79 mm gap, 25–30 mm stack, 2 130 Hz electrical | C16, C36, C39 | Lamination, SMC compaction, or additively manufactured iron? |
| 2 | **Winding** — concentrated double-layer, `kw` 0.933, 7.5 A/mm² peak / 3 A/mm² continuous, 15.9 A rms | C17, C18, C39 | Needle-wound, pre-formed, hairpin, or printed copper? |
| 3 | **Rotor magnets** — NdFeB SH/UH, 1.5 mm radial, 736 N shear per 5 g magnet at 15 000 g | C38, C40 | Grade and grade *manufacture* (heavy-rare-earth content), segmentation, retention |
| 4 | **Rotor/ring structure** — backiron + retention carrier, **382 kN setback** (re-baselined 2026-09-23 from 74 kN on the CAD's measured 2.595 kg ring-side mass), 1 900 rad/s | C26, C32, C35, C40 | Machined one-piece, cast, or topology-optimised LPBF — and mass is the lever: **every 0.1 kg costs 14.7 kN of setback** |
| 5 | **Isolation bearings** — thin-section, `k_pair ≥ 635 N/µm` (**re-baselined 2026-09-23 from 122 — and at that load the radial case is a *bypass*, not a bearing requirement at all**), `Tf ≤ 0.10 N·m` flat to ≈1 900 rad/s | C22, C23, C25 | Sourcing and precision class; the friction budget is a surface/quality specification |
| 6 | **Fuze-well thermal joint** — ≥ 20–27 W/K flight average, ≥ 58 W/K peak into the shell | P6, W7, W12 | How to *manufacture* a conductance-specified joint rather than inherit a structural thread |
| 7 | **Dump stage** — 2.92 kW peak / 121 kJ per flight, H9's chopper + shunt | W12, H9 | Where the energy physically goes and what component class carries it |
| 8 | **Fuze parts** — S&A rotor, impact switch, timer, radome | F6, F7, F2 | Precision at 5 000/yr — MIM, investment casting, or machining |
| 9 | **Canards + ring** — cant angle is the force lever (C31/C43); permanently exposed, no mechanism | C31, C29, C30 | One-piece (integrity + cant-angle tolerance) versus assembled |
| 10 | **RF — the spin-axis aperture and the dual-band nose** | N3, F2, risk 27 | How the aperture becomes structure, and what the radome must pass |

---

## 2. Electrical machine — the three core routes

### 2.1 Thin laminations (the baseline)

- **0.1 mm non-oriented grades exist commercially** — Waelzholz supplies thin electrical steel strip from 0.1 mm for medium-to-high frequency duty (J2). So C39's "0.1–0.2 mm laminations" branch is a real, purchasable route, not a wish.
- **But thin laminations are hard to process**: cutting and handling below 0.23 mm demands small cutting clearances and tight tolerances, and the multi-layer shear-cutting study names it as a genuine manufacturing challenge (J3). This is a *cost and yield* consideration at 5 000/yr, not a physics problem.
- Stacking methods are mature and numerous — interlocking, bonding (backlack), laser welding, riveting, cleating (J3b). At 12 slots and a 25–30 mm stack the stack is short, which favors bonding or interlocking over welding.
- **Verdict: production-mature baseline.** It is the route the cost target should be priced against first, because it needs no new tooling beyond stamping dies and the supply is global.

### 2.2 Soft Magnetic Composites — powder compaction (the volume route)

SMC is the process where the *shape* freedom and the *volume* economics are both real:

- **Published material data at the frequencies this machine runs at** (J1, Somaloy 700 7P): core loss **83 W/kg at 1 T / 1 kHz** — with the paper's own comparison table showing the prior generation at 125 W/kg, i.e. the improvement is real and measured. The benefit is stated across **0–5 kHz**, which brackets our 2 130 Hz.
- **Process**: die compaction of coated iron powder + heat treatment. Net-shape 3D geometry (the paper explicitly enables 3D flux paths that laminations cannot make), no stacking operation, and die-wall lubrication raises density (7.63 vs 7.50 g/cm³) and lowers loss (78.3 vs 82.9 W/kg at 1 kHz).
- **The two honest cautions, both from the same source:**
  - **Mechanical strength is 60 MPa tensile (TRS)**, rising to ≈100 MPa with a tailored pre-oxidation heat treatment — an order of magnitude below steel. For a stator that must survive **15 000 g axial / 5 000 g radial** and hold the C35 air gap, the stator core's own structural role becomes a design question, not an assumption.
  - **Thermal aging is good but not free**: 0 % loss increase after 120 h at 150 °C, 1 % at 200 °C, 5 % at 260 °C. The nose thermal environment (W9) sits inside this, so SMC's ageing is acceptable *if* the nose temperature claim holds — an explicit coupling worth stating.
- **Verdict: production-mature for volume, with a strength/structural analysis required.** The die is the tooling investment; per-part cost falls steeply with quantity, which suits 5 000/yr far better than a bespoke lamination stack for a *non-standard* slot geometry.

### 2.3 Additively manufactured iron (development only)

LPBF Fe-Si is genuinely established in research — dense, crack-free builds at 3 and 9 wt% Si (J23), in-situ alloying of FeSi6.5 as a cost-effective powder route, and beam-profile control of magnetic properties. It enables the three-dimensional flux paths that motivate the research.

**But there is no volume motor-core production on this route**, and a flight-critical stator is the wrong place for a first production use. **Verdict: development/first-article tool only.** Useful for the R7 rig and for making a *single* experimental core to validate C39's loss model, never cited as the production plan.

### 2.4 The C39 decision the three routes force

C39's own text says the iron-loss figure "is not yet trustworthy." This dossier changes that from a hole into a **structured trade**:

| Route | Loss at 2 130 Hz | Strength | Tooling | Volume fit |
|---|---|---|---|---|
| 0.1–0.2 mm laminations | Lowest eddy, thin-gauge material cost | Steel (high) | Stamping dies | Good, but hard handling <0.23 mm |
| SMC compaction | ~83 W/kg at 1 kHz, measured; must be measured at 2 130 Hz | 60–100 MPa | Compaction die | Best for 5 000/yr |
| AM Fe-Si | Research numbers only | Build-dependent | None | Development only |

**Recommendation recorded for C39**: specify the loss **and** the strength and let the trade close on both; do not select SMC for shape freedom alone, and do not select laminations for strength alone. The register already owns the number; this table is the decision's shape.

---

## 3. Winding — an AC-loss result that changes the recommendation

### 3.1 The skin-depth arithmetic [derived]

Copper at ~20 °C: δ = 66.1 / √f mm.

- **At the 2 130 Hz fundamental: δ ≈ 1.43 mm.**
- **At the ≥100 kHz converter switching F15 specifies: δ ≈ 0.21 mm.**

C18's current density (7.5 A/mm² peak) puts the conductor at roughly 2 mm² — a round wire of about Ø1.6 mm, or a rectangular section of comparable area. **The conductor is smaller than the fundamental skin depth and larger than the ripple skin depth.** Consequences, both of which matter for C18/C39 and neither of which is currently recorded:

1. **The conventional winding route is technically defensible.** Fundamental-frequency skin and proximity effects in a single-layer concentrated winding are moderate, not prohibitive. Printed copper is therefore *not* required on loss grounds — which is the opposite of the assumption that usually motivates it.
2. **The conductor subdivision requirement is set by the converter, not the machine.** F15's ≥100 kHz switching (specified for L-band quiet) is what pushes strand-level design; a converter with slower edges would relax it and a faster one would tighten it. **The winding spec is coupled to the EMC spec** — a cross-domain coupling no criterion currently records.

### 3.2 The process options

**(a) Needle winding — the production baseline.** Out-slot needle winding machines exist precisely for externally wound stators (Elmotec, IMA, DETZO, J21); needle winding is the standard route for complex concentrated schemes. Its known limitation is slot fill.

**(b) Printed copper (LPBF) — the number, honestly.** The peer-reviewed winding study reports **~80 µm minimum feature spacing, 79 % slot fill for square conductors and 63 % for round, and 87 % IACS after heat treatment** (J4). Against a conventional needle-wound concentrated winding at roughly 45–55 % fill, that is a real gain — but:

- **Conductivity is process-dependent and must be specified, not assumed**: 73 % IACS in one 2022 LPBF study (J7), 87 % after heat treatment (J4), 91.7 % via electron-beam melting (J7b). A single "copper is copper" assumption is unsafe.
- **Insulation and surface finish are the hard part**: AM surfaces need smoothing before coating, and coating route changes breakdown behaviour (the Bristol study cited in J5's chain).
- **Cooling channels in printed parts are a trap**: the multi-material PBF stator-tooth study reported that intended cooling channels **could not be fully freed of powder** and that electrical testing found short-circuit currents involving coils and teeth (J6). This is the "do not inherit" result of this dossier.

**(c) The hybrid — printed winding heads on conventional conductors.** The Aachen study printed pure-copper hairpin winding heads onto conventional conductors and **removed 12.5 mm of a 37 mm winding-head height — about one third — and ≈0.564 kg of copper in that machine** (J5). For this kit, where the visible envelope above the seat is hard (≤95.25 mm, P12) and the whole machine is 0.81–0.97 kg (C40), a one-third end-winding reduction is a **direct lever on two budgeted quantities** (P12's envelope and C40's mass) rather than a laboratory curiosity.

**Recommendation recorded for the new winding row (§8)**: production = needle-wound or pre-formed conventional conductors; **development/derivative = hybrid printed end-winding, evaluated against the fact that it spends process risk to buy axial length and mass.** Full printed stators stay a development item.

---

## 4. Magnets, backiron and the launch-load chain

### 4.1 Magnet grade manufacture — a cost lever nobody has claimed

C38 specifies NdFeB **SH/UH grade for the W9 nose temperature**, and K4's target is "the fielded price minus 40 %." Heavy rare earth (Dy/Tb) is the principal cost driver of high-coercivity NdFeB. **Grain-boundary diffusion (GBD)** places the heavy rare earth only at the grain boundaries rather than throughout the bulk, and the review literature frames it explicitly as *cost reduction and high-efficiency use of critical elements* (J13), with a scalable dip-coating DyF₃ route published in 2025 (J13b).

**What this changes:** nothing about the design — the magnet still functions identically. It changes **what the cost target may assume**: the same coercivity class bought through a GBD-processed magnet rather than a uniformly Dy-alloyed one. That is a K5 evidence item, and it is exactly the kind of indigenous-process leverage the submission should name.

### 4.2 Segmented magnets — the loss mechanism at 2 130 Hz

The magnet eddy-current loss review (J12) and the high-speed-machine segmentation study (J12b) establish the mechanism: at high electrical frequency, harmonics in the stator field drive eddy currents in the magnets, and **segmentation with insulated interfaces is the standard mitigation**, with retention and validation as part of the same problem. Our relative field is 1 234–2 131 Hz (F15's own figure), so **magnet eddy loss is a real term in C42's ledger and a heat input into the ring** — which sits next to the apogee thermal margin. Record it; do not quantify it until C39's loss model is complete.

### 4.3 Retention and the one-piece ring

- **Retention is mechanical by requirement** (C38: 736 N shear on a 5 g magnet at 15 000 g). Manufacturing route: pockets or sleeves, magnet grinding to the 1.5 mm radial dimension, and a mechanical retention feature that is a CAD load case.
- **The ring assembly should be machined as a datum structure**: the canards' cant angle is the guidance-force lever (C31), and an assembled ring stacks tolerances precisely where the design's performance is most sensitive. The blisk precedent — a bladed disk milled from a single billet to remove joints and hold blade geometry (J22) — is the analogy: **integral machining buys both integrity under 85 N transient / 74 kN setback and cant-angle tolerance in the same setup.**
- **Mass is the multiplier**: at 14.7 kN per 0.1 kg of ring assembly (C26), every gram removed by a topology-optimised, LPBF-built carrier (the aircraft-bracket precedent, J14) pays twice — once in the kit mass budget (P9/C40) and once in the retention structure it no longer has to carry. This is the one place in the design where an additive part has a *systemic* argument rather than a shape argument.
- **Two materials in one rotating part**: the backiron must remain magnetic (steel); the structural carrier need not. The join between them (press/braze/shrink) and the final **balancing at 1 900 rad/s** are production steps to state, not to discover later.

---

## 5. The thermal path — manufacturing a conductance-specified joint

P6's closing route was recorded as *"a contacting radial path through the well bore, a conductance-specified joint and a peak/average split."* This section supplies the process content for each clause.

### 5.1 The contacting radial path

- **Compliant multi-point contact springs** (canted-coil spring / fingerstock class) are established hardware for consistent multi-point contact **under shock and vibration** (J10b) — the exact duty of a gun-launched joint. Their heritage is electrical/EMI; using them as a *thermal* path requires the contact conductance to be characterised rather than assumed, and P6 already brackets `h_c` at 1–5 kW/(m²·K) for a contacting interface — the spring is the mechanism that makes the contact *contacting*.
- **Indium foil** is the space-grade answer where a bolted joint must conduct: a 2025 study characterises smooth and **embossed** indium foil against graphite sheet specifically as a function of interface temperature, **contact pressure and surface roughness** (J10), and NASA's SmallSat thermal state-of-the-art documents the bolted-joint conductance framing (J10c). Embossed foil is the variant for non-ideal surfaces — which a well bore is.
- **Cold-sprayed copper on the kit's own spigot** is the third element: a solid-state deposition process producing **as-sprayed 98 % IACS and 368 W/mK** with bulk-like properties and no post-heat treatment (J9), used commercially for hybrid heat sinks and busbars. Spraying the *kit* to a controlled diameter creates the precision mating surface without touching the shell — which the retrofit constraint requires.
- **What this must not become**: a clearance fit. P6 already records that a 0.1 mm air film over the same area is only ≈5 W/K. The sleeve must be a *contacting* design with a stated contact pressure, and the thesis of the joint is that its conductance is **specified and tested** (R7 item 7).

### 5.2 The dump stage's component class

- **AlN thick-film power resistors** are the standard high-power-density package (Vishay RCP, IMS N-series, J20) — the resistor class for 2.92 kW peak exists off the shelf, and its datasheets state the design rule (heat leaves by conduction through substrate, terminations and joints).
- **Spreading, not rejecting, is the job**: the 121 kJ enters the kit's ≈400–450 J/K of metal (a ≈+40 K transient buffer, P6's own arithmetic) and then leaves through the well interface. So the dump stage is a *heat spreader* problem: cold-spray copper (J9) for the current-carrying spreader and **pyrolytic graphite sheet** — 700–1 000 W/mK standard, up to 1 950 W/mK in-plane, with compressible variants (J11) — for thin, conformal spreading. Note the anisotropy: PGS conducts in-plane, so it is a spreader, never a through-thickness interface.

---

## 6. Fuze parts, RF and the nose

### 6.1 Precision parts at 5 000/yr

- **Metal injection moulding (MIM)** is the class route for small, complex, high-precision metal parts in stable production (S&A rotor, switch bodies, small mechanisms); the cost guides frame the decision against CNC and die casting as a function of size, complexity and **volume** (J16). The honest statement: **tooling amortisation is the question at 5 000/yr**, and it is shared across all MIM-able parts in the kit and the fuze — which is an argument for consolidating part families rather than for avoiding MIM.
- **Investment casting** gives ±0.1 mm and Ra 1.6–3.2 µm with complex thin walls, but wax-pattern tooling ($2k–30k+) drives the low-volume economics (J16b). For a first production batch, machining-from-bar may beat casting; the crossover is a stated calculation, not a preference.

### 6.2 The spin-axis aperture — the antenna as structure

N3's requirement is a rotationally symmetric aperture on the spin axis with **elements combined rather than switched**. Two manufacturing facts support it:

- **Laser Direct Structuring (LDS)** — laser-activated conductive traces on an injection-moulded 3D part (LPKF process; production practice at Kyocera AVX and Taoglas, J17) — puts the array *on* the nose structure instead of beside it. Given that the nose has no volume to spare (risk 27), an aperture that is also structure is the only version that fits.
- **Sequential rotation** — the established array technique of rotating element feeds to control polarisation from combined elements (J18) — is the antenna-engineering practice behind "combined rather than switched". It converts N3's symmetry argument from an assertion into a construction method.

### 6.3 The dual-band radome

The nose tip must pass **L1/L5 (~1.2–1.6 GHz)** and **24 GHz** while being a structural, aerodynamically heated surface. The routes: quartz/cyanate-ester composite radomes with frequency-selective surfaces for dual-band transmission (the 2023 dual-band composite radome study, J19), quartz prepreg systems (Toray, J19b), and the classic missile-dome glass-ceramic (Corning Pyroceram, J19c). **A fourth route belongs to §7's cell:** *printed* dielectrics whose permittivity is set spatially by the print itself — demonstrated for graded-index lenses at 60 GHz and in Ka-band (J33) — which could make the radome and the aperture one printed part. **This is a declared development item** — a dual-band, load-bearing, heated radome is not something to claim as solved on a slide, and the register's F2 note (the radome must pass both L1 and 24 GHz) already carries it.

---

## 7. The advanced manufacturing concept — one digital cell, three capabilities

§2–§6 answer *which process makes each part*. This section answers the question the business case actually needs: **what kind of factory is this kit built in, and what does that factory let the design become?**

The proposal is a single **digital hybrid cell** with three capabilities — **print, post-treat, assemble** — organised around a per-part process record. It is *not* a proposal to print the whole kit: §3's skin-depth result already refuted printed copper on loss grounds, and §2's loss-versus-strength trade keeps the stator conventional at volume. The cell exists where additive manufacturing's specific advantages pay — **tooling-free geometry, part consolidation, embedded electronics, iteration speed** — and it is bounded by the qualification discipline of §7.3 and §7.5.

### 7.1 Why "on-demand" is the right frame at *this* volume

5 000 kits/year is the fact that makes this coherent rather than fashionable. The fielded programme's 100 000+ units justify hard tooling; 5 000 does not justify a tooling change for every design iteration, and this programme **already knows its geometry will move** — P6 re-baselines every parametric criterion against YIL's drawings after shortlisting, and the growth modules (X18's interface) and the seeker option each imply a variant. A tooling-free production route converts those known future changes from retooling programmes into design changes. **This is the strongest argument for the cell, and it is a programme argument, not a technology argument:**

- **Tooling-free first articles — for the printed subset** (the qualification this bullet needs, found in the validation pass): the P6 re-baseline changes the geometry of the **printed** parts without tooling lead time, which is a direct reduction of the schedule exposure that risks 20/21 carry. The stator core, windings, magnets and bearings keep their dies and their suppliers, which is what the two-tier split exists to make explicit — an unqualified "tooling-free" claim would be caught by J3 in the room.
- **Variants without retooling** — different 155 mm shell types, growth modules, and a future sensor variant are each a file, not a die. **R12's modularity stops being a document property and becomes a production property.**
- **Part consolidation** — a printed bracket or carrier that replaces a fastener stack removes joints, which in a 15 000 g environment is where the classic failure points live (J29).
- **Iteration speed** — the spiral from bench rig (R7) to first article to production is measured in prints, not in tooling programmes.

### 7.2 Print — four deposition routes, one cell

| Route | Used for | Anchor |
|---|---|---|
| **Metal LPBF** | Ring/retention carrier, fuze mechanism parts, magnet pockets; printed copper only where geometry beats loss. **The carrier prints; the magnetic backiron does not** — printed Fe-Si is research-grade and carries a loss penalty (J23), so the backiron stays laminated or compacted magnetic material and the printed part is the structure around it. Stated as a split because J3 will ask the magnetic question | J7, J14, J23 |
| **Robotic directed energy deposition (WAAM)** | Larger near-net metal preforms where deposition rate beats resolution; a robot-based hybrid WAAM + machining platform is demonstrated on aluminium, and multi-robot WAAM cells scale to metre-class parts | J30 |
| **Polymer SLS/MJF** | Radome, housings, potting shells, jigs, ground-support hardware | J34 |
| **Direct-write conductors** | Silver/dielectric printed simultaneously (multi-material electronics printing), aerosol-jet antennas, sensors and fine traces; components placed during a print pause | J31 |

### 7.3 Post-treat — the chain that converts as-built weakness into qualified property

The user's instinct is correct and it is the crux: **the additive route is only defensible because every known weakness has a named treatment.** Each row below is a stated deficiency with a stated countermeasure:

| As-built weakness | Treatment | Evidence |
|---|---|---|
| **Porosity** → fatigue crack initiation in AlSi10Mg is dominated by process porosity | **HIP** closes it; the strength loss from a classic ~500 °C / 100 MPa cycle is partly recoverable by subsequent heat treatment | J24, J25 |
| **Residual stress and distortion**; thin walls are hard to build | Stress-relief heat treatment, build-orientation and support design; thin-wall fabrication limits are parameter-controlled | J26b |
| **Surface roughness** (a named LPBF limitation) | Abrasive-flow machining for internal passages, electrolytic and chemical polishing, laser polishing, sandblasting — measured improvements on Ti-6Al-4V | J26 |
| **Feature tolerance** — geometry can fall outside the tolerance a demanding application needs | **Print near-net, machine critical**: bearing seats, magnet pockets and sealing faces are finish-machined; LPBF tolerance/reproducibility studies bound what may be left as-built | J26c |
| **Polymer SLS roughness and porosity** | Vapour smoothing brings SLS parts toward injection-moulded surface quality; dyeing and plating follow | J34 |
| **Data-poor qualification** | In-process melt-pool / optical monitoring plus CT plus per-build coupons — the part carries its build record | J27 |
| **The honest limit** | In-situ monitoring is advancing toward model-based qualification but **is not yet a substitute for testing** — coupons, CT and lot testing stay in the qualification chain | J27 |

**The qualification precedents that make this claimable at all — and the validation pass changed which one to lead with.** NASA-STD-6030 defines how additively manufactured parts are used in flight hardware — **process control, coupons, testing and traceability**, not "printed therefore approved" (J28). But for a *munitions* context the sharper authority is the **defence** set, found in the same pass: **DoDI 5000.93** governs the use of AM in the US DoD (J37), and **ASTM with the UK MoD (Project TAMPA)** has published a **criticality-based certification approach** for AM parts in defence (J38) — which is also the correct framing for our boundary, because it is *criticality* that decides how much evidence a printed part carries. **And the principle that printed structure can carry electronics through a gun launch is not ours to prove: printed conformal structural supports for circuit boards have been demonstrated as a viable route to high-G survivability in gun-launch applications (J39).** The residual we owe is project-specific qualification — which is exactly what risk 50 says.

### 7.4 Assemble — printed structural electronics, and the parts it removes

- **Print–pause–place–resume.** Components are placed into a part mid-build, conductors are printed to them, and a thermal cure completes the joint — demonstrated on a stereolithography platform with pick-and-place insertion followed by direct-write filling (J31).
- **What it buys this kit specifically:** the harness and the connectors disappear. Connectors are the classic failure point under launch acceleration and vibration, and a printed structural module — **the potting *is* the structure** — is exactly what H5's annular stack in the well spigot wants to be. **And the principle is demonstrated in this exact environment, which the validation pass established: printed conformal structural supports for circuit boards have been shown viable for high-G survivability in gun-launch applications (J39).** The claim therefore carries no speculative weight; the residual is project-specific qualification (risk 50).
- **Embedded sensing is demonstrated in metal too:** fibre Bragg gratings have been embedded in Inconel 718 during printing, and in aluminium by ultrasonic additive manufacturing with dynamic strain measured to 10 kHz (J32). **Honest scope:** this is a *qualification and ground-test* instrument in the baseline — the ring's thermal and load history measured during rig and flight trials — and an in-flight health channel is a growth option, never a baseline claim.
- **Robotic fitting and handling** — the cell's automation target is stated as a target: robot handling, placement and assembly with a small operator crew per shift, and a per-part digital record. It is a *level of automation*, not a headcount claim, and it is what makes the low-volume/high-variety proposition economic.

### 7.5 The honest boundaries — what the cell does *not* do

1. **Energetics are out of the cell.** The fuze's explosive train cannot share an automated line; it stays in the licensed, segregated assembly facility under the MIL-STD-1316 safety discipline (F6). The cell ends at the non-energetic subassembly and the fuze housing.
2. **Printed conductors carry signals, not power.** Optimised reactive silver inks reach near-bulk conductivity (J31b), but conventional nanoparticle inks sintered at low temperature sit at several times bulk resistivity. C18's **15.9 A rms** stays on conventional copper; printed traces carry sensing, RF and logic.
3. **Throughput is arithmetic, not aspiration [derived].** At ~0.3–0.5 kg of printed metal per kit, 5 000 kits/year is **1.5–2.5 t/year**. A mid-size multi-laser LPBF machine delivering ~200–400 g/h of effective metal over two shifts is **≈2–5 machines**, plus the post-treatment and assembly equipment. This is a **production asset with capex that K5 must price** — not a bench printer — and that number belongs in the cost case rather than in the pitch.
4. **AM does not repeal qualification.** See 7.3's qualification paragraphs and J27/J28/J37/J38 — and note that the right framework to quote for a munitions context is the *defence* one (criticality-based, per J38), not the spaceflight standard alone.
5. **Automation is pitched as repeatability, not headcount.** At a public-sector works this is a labour question before it is a technology question (judge dossier §4.8). The cell's argument is small-batch economics and process repeatability — the deck's word is "automated placement", never "unmanned".
6. **Machine prices are not quoted.** We have no rated source for a machine price; the capex belongs to K5 as a line item with the machine *class* named and the throughput chain shown (§7.5.3).

### 7.6 Modularity and targeted redundancy in the sensor stack

The user's second direction — modular sensing with redundancy — is right for this kit, and it is affordable **because** of 7.4: when the electronics are printed into structure, a second sensing channel costs grams, not boards.

- **The modular interface.** Define one module standard — mechanical envelope, datum, digital bus and power rail — covering the inertial unit, magnetometer, body-spin channel, ring pickoff, barometer and the GNSS front end. H7's connectorless ring–body link (rotary transformer power, optical data) is the same idea at the rotating interface, so the kit's **whole sensor chain becomes replaceable at module level** — which is R12 executed rather than declared.
- **Redundancy, targeted by failure effect — not blanket:**
  - **Dual inertial + magnetic channel** (two IMUs and two magnetometers, cross-checked and voted). Attitude and heading are the guidance-critical measurement; a MEMS-grade second unit is a 1–2 g device at tens of milliwatts.
  - **Dual ring-angle pickoffs of different physics** (inductive plus optical/magnetic). G5/G6's ring-angle line is the most error-sensitive in the whole budget — an independent second channel is the cheapest defence in the design.
  - **Already redundant by construction, and therefore not revisited:** the arming chain is triple-condition (F6), and the power rails are diode-OR across two domains (H12).
  - **Deliberately *not* proposed:** redundant bearings (mass and friction would break C13's feasibility gate), redundant detonation paths (the safety case forbids parallel function paths), and duplicated GNSS receivers (power and volume without a failure effect that justifies them).
- **The cost, stated [derived]:** the policy adds roughly **5–15 g and under 0.5 W** across the kit — about **1 % of the 1.4 kg budget** (P9) — and it is only that cheap because printed structural electronics removes the connectors and boards that would otherwise host the second channels.
- **The honesty:** redundancy is bought with K4 and P9. The policy therefore names *which functions* get it and *why*, rather than claiming "high redundancy" as a property.

---

## 8. Proposed register changes (the user's to open)

None of these is quoted anywhere until opened. Each follows the register's own rule: a finding from an external source that owns something no row owns.

| Proposal | Type | What it would own | Basis |
|---|---|---|---|
| **K7 — Manufacturing process plan** | Chosen | The two-tier strategy (production vs development processes), the tooling-amortisation statement at 5 000/yr, and the make/buy decision matrix feeding C45 | This dossier §2–§6; K5's evidence |
| **C46 — Winding process route and slot-fill specification** | Chosen / Derived | Needle/pre-formed vs printed vs hybrid; the slot-fill *definition* that makes C18 auditable; and the derived coupling of conductor subdivision to F15's switching spectrum (§3.1) | J4, J5, J21; derived skin-depth arithmetic |
| **K8 — Digital hybrid cell** | Chosen | The print–post-treat–assemble capability of §7: which parts are printed, the post-treatment chain, the automation level, the throughput arithmetic, and the claim that variants and the P6 re-baseline are tooling-free | §7; J24–J34 |
| **C47 — Additive/post-treatment chain for primary structure** | Chosen / Derived | Which structural parts are printed (ring/retention carrier, fuze mechanism parts), and the HIP + heat-treatment + finish-machining + NDE chain that makes them gauntlet-passable at 15 000 g; the derived [allowables] rule that printed parts carry orientation-based design values | §7.3; J24–J28 |
| **H14 — Sensor-stack module interface** | Chosen | One mechanical/digital/power standard for every sensing module (IMU, magnetometer, spin channel, ring pickoff, barometer, GNSS front end), so variants, upgrades and redundant units swap at module level — R12 and X18 made executable | §7.6; H5, H7, X18 |
| **H15 — Targeted redundancy policy** | Chosen | Which functions are dual-redundant (inertial + magnetic channel; ring-angle pickoff) and which are not (bearings, detonation path, GNSS), with the mass/power/cost quantified — ~5–15 g, <0.5 W [derived] | §7.6; P9, K4 |
| **Risk 47 — Novel-process qualification burden** | Risk | LPBF carriers, cold-spray copper, printed windings and AM cores are not ordnance-qualified; adopting any of them in *production* adds qualification cost and schedule that K4's recurring-cost target does not include | J5, J6, J7, J28 |
| **Risk 48 — Process-dependent properties** | Risk | Printed-copper conductivity spans 73–92 % IACS by process and post-treatment; SMC tensile strength is 60–100 MPa; a property that moves after design freeze moves loss, mass, or both | J1, J4, J7 |
| **Risk 49 — AM design allowables and anisotropy** | Risk | A printed part's static and fatigue allowables are orientation-, process- and machine-dependent; qualification must be per orientation and per machine, and in-situ monitoring is not yet a testing substitute — so a printed flight part carries a heavier evidence chain than a machined one | J26, J27, J28 |
| **Risk 50 — Printed/embedded electronics under launch loads** | Risk | Sintered silver and printed dielectrics have not been qualified through 15 000 g / 5 000 g; adhesion, CTE mismatch and via integrity are the specific unknowns, and they must be proven before the harness is deleted | J31, J31b; D1/D2 (E-domain's own high-g evidence chain) |

*(Numbering checked against the register 2026-09-20: risks 40–46 exist — 46 being the C42 reference-speed reconciliation — so these take 47–50.)*

---

## 9. Integration plan — where this lands in the submission

| Artefact | Change | Section |
|---|---|---|
| `design/05-source-register.md` | New **section J** with the rated sources; a manufacturing claims note in §3 | Done in this pass |
| `submission/SIH26098-form-content.md` | §12 *Manufacturability and cost optimisation* rewritten around the two-tier strategy, the named processes, and — second pass — the digital cell, tooling-free iteration and the modular/redundant sensor stack as a **bounded** paragraph | Done in this pass |
| `submission/SIH26098-template-slides.md` | Slide 4 "Cost and manufacturability" sharpened; slide 5's indigenous-content bullet made concrete | Done in this pass |
| `submission/SIH26098-draft-from-register.md` | §4 feasibility and slide 4/5 content aligned | Same pass |
| `design/00-design-criteria-register.md` | §8's proposals, if the user opens them | **Not done — proposal only** |
| `design/ROADMAP-and-prompts.md` | Carried item 16 extended to cover the §8 proposals (H14, H15, C47, K8, risks 49/50) | Done in this pass |

**What the deck may now say that it could not before** (all production-mature, all citable):

- The machine's core has three real routes with published data, and the volume route (SMC compaction or thin lamination) is chosen on a stated loss-versus-strength trade.
- The winding route is conventional for production, with the printed/hybrid option bounded by its own published numbers and its own cautionary result.
- The thermal joint is a *manufactured* interface — compliant contact + indium foil + cold-sprayed copper — specified by contact pressure and conductance, not inherited from a thread.
- The magnets' coercivity is bought through a process (GBD) that reduces the critical-element cost driver.
- The spin-axis aperture is manufactured into the nose structure (LDS) and combined by an established array technique (sequential rotation).
- **§7's advanced concept, in bounded form:** the kit is built in a digital cell whose parts carry their own process record; each known AM weakness has a named countermeasure (HIP for porosity, heat treatment for residual stress, machining for critical features, polishing for roughness); the qualification route follows NASA-STD-6030's shape (process control + coupons + testing); tooling-free first articles de-risk the P6 re-baseline; and the sensor stack is modular with **targeted** redundancy at ~1 % of the mass budget.

**What the deck still may not say:** that any of the novel processes is qualified for ordnance; that printed copper is required for loss reasons (the skin-depth arithmetic says the opposite); that the dual-band radome is solved; that the cell removes the need for qualification (it changes its *shape*, per J28); that printed conductors carry power (they carry signals — C18's 15.9 A stays on copper); that the energetic train is inside the automated cell (it is not, and cannot be); that in-situ monitoring replaces testing (J27); or that the cost target includes the qualification of any new process (risk 47, proposed).

---

## 10. Open questions

1. **Does SMC's 60–100 MPa strength close the launch case** at the stator, or does the stator core need the lamination route for structural reasons alone? Answered with C35's load path at P4.
2. **What is the magnet eddy loss at 2 130 Hz** as a fraction of C42's 121 kJ? Belongs to C39's loss model.
3. **Is a hybrid printed end-winding worth its process risk** for the 12.5 mm / 0.56 kg class of saving, given this machine's harder axial envelope? A C46/R7 development item.
4. **Which parts consolidate into MIM families** at 5 000/yr, and what is the tooling amortisation per kit?
5. **India-specific sourcing** for thin electrical steel, SMC powder, GBD magnets and LDS-capable moulders — a post-selection question for YIL, stated as such.
6. **Which structural parts actually print** (§7.2): the ring/retention carrier is the candidate, but the decision needs the CAD mass properties (C21's route) and C47's allowables before it can be taken — and the answer may be "none of the flight structure, cell for electronics and first articles only", which is a perfectly good answer.
7. **Do printed traces survive the gun?** Risk 50 is the gate: adhesion, CTE mismatch and via integrity through 15 000 g must be proven before the harness is deleted, and the fallback (printed traces for ground-test articles, conventional harness in flight) is cheap and should be stated as the fallback.
8. **What does the sensor-stack module standard actually constrain?** H14 must fix the mechanical envelope, the digital bus and the power rail without freezing the sensor choice — the interface is the criterion; the silicon is not.
9. **The cell's automation level** — how many operators per shift, and which steps (powder handling, QA disposition, magnet handling) remain manual — is a target to be set at P4/P7 with YIL, not asserted here.

---

## 11. Sources

Rated in `design/05-source-register.md` **section J** (J1–J34). All numbers quoted above trace to that list. The one cautionary source — J6, powder retention in printed cooling channels with an observed short-circuit outcome — is recorded deliberately: this project's practice is to state the failure mode it will not inherit, and this is the manufacturing pass's contribution to that list.
