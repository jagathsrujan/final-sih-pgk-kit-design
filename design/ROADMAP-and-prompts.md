# DRISHTI-PGK — Roadmap and Session Prompts

The phase plan from here to a complete design and a submitted entry, plus the prompt to drive it. Use this file as the entry point for every design session from now on — it locates itself, so the same prompt works at every stage.

---

## Ground rules (established 2026-09-17)

These constrain everything below. Do not re-litigate them in a session.

- **Submission deadline is 30 September 2026** — confirmed. Thirteen days from 2026-09-17.
- **YIL will not release the shell drawing, firing tables or any technical document before the idea submission is shortlisted.** This is not a delay, it is the process. **Do not plan around receiving YIL data, and never treat unavailable data as a blocker or as a reason to stop.**
- **Therefore the platform and stability domains are designed parametrically.** Values we cannot obtain become *bounded assumptions over a declared envelope*, supported by public data, with a sensitivity showing the design closes across that envelope. Criteria formerly marked `OPEN-BLOCKED` on YIL become `PARAMETRIC`.
- **Public data is the substitute.** A **reference 155 mm HE model** is built from open sources — M795 / M549A1 mass and geometry class, the standardised fuze-well interface, published dispersion. It is the design's stand-in platform until selection and is re-baselined in P6.
- **The kit is specified as a parametric product** — kit mass, CG shift and inertia change stated as *limits of the design* rather than values inherited from one shell. This is how a supplier defines a retrofit kit, and it converts a data gap into a specification.
- **Nothing published in the submission may imply access to YIL technical data we do not have.** Where a number is an assumption, say so explicitly.

---

## Phase dependency graph

The phases are **not** strictly linear. The submission has its own short path so it is not held up by the design phases.

```
P0  Context                                  ✅ complete
     │
P1  Design criteria
     ├── P1a  Submission-critical track  ─────────────►  P5  Idea submission  (30 Sep)
     │                                                         │
     └── P1b  Remaining criteria                               │
              │                                                │
              ├── P2  Budget reconciliation / closure          │
              │        → design/01-design-definition.md        │
              ├── P3  Simulation & verification  ──────────────┤
              │        → derived CEP, trajectory correction    │
              └── P4  Hardware definition  ────────────────────┤
                       → CAA CAD, electronics diagram,         │
                         envelope, fuze definition             │
                                                               ▼
                                                        P7  Proof of concept
                                                            (bench rig)

P6  Post-selection re-baseline → replace the reference shell with YIL's actual
    shell → re-confirm P and S → affects P2, P3, P4
```

**Two consequences worth holding onto:**

- **P5 depends only on P1a.** The idea submission needs criteria and argument — not CAD, not hardware, not the full simulation. Roughly 30 criteria unlock it.
- **P3 depends on the aerodynamic coefficient set**, which is the only gap with no cheap workaround. It is the long pole and should be attacked early even though it is not on the submission path.

---

## Phase status

*Update at the end of every session.*

| Phase | Name | Status | Last updated | Note |
|---|---|---|---|---|
| P0 | Context | ✅ Complete | 2026-09-17 | Thesis distilled, design brief written |
| P1a | Submission-critical track | ✅ **Complete** | 2026-09-18 | **38 rows — all 38 closed.** This session closed the last five in order: **N6** (the IMU on the de-spun ring, with N7/N8 derived and N1's 2.0 m term back-filled), **W4** (demand ≈12 W against 2.92 kW — ≈20:1 — plus the supercapacitor buffer for the fireset reservoir, hold-up and actuator bursts), **K4** (≤ ₹6.5 lakh at 5,000/yr — the fielded price minus 40 %), **R5** (the two-tier ≈10,000-flight Monte Carlo, worst-corner 95 % upper bound carrying the claim) and **R7** (the flight-representative bench rig, **built only if shortlisted — P7**), with the two carry-ins closed first: **P6 is now a thermal criterion** (the bare 2″-12 UNS thread delivers ≈3–16 W/K against the ≥58 W/K peak; the closing route is on the row) and the **C35 ↔ C13 preload tension has an owner (C23)**. Rows 34–38 had closed earlier the same day: C42 (2.92 kW / 121 kJ — the authority for W7/W12), C43 (cant ↔ power, binding on C2/C3), C40+C34/C36 (machine identity and mass), C35 (air gap splits: 367 N/µm structural, 122 N/µm bearing), W12 (dump stage). The growth-module decision (X1, X3–X6, X17) sits outside the numbered track but gated what the deck may claim. **Open output carried into P1b: W8/C17 inherit a converter requirement from G7** — the machine reaches `E = V_bus` at the launch condition, i.e. at peak load |
| P1b | Remaining criteria | 🔄 In progress | 2026-09-18 | **33 DEFINED · 34 DERIVED · 25 PARAMETRIC · 86 OPEN, of 178.** (The earlier "of 146" predated the 19-criterion X block and the 13 machine rows — the register's counts are authoritative) |
| P2 | Budget reconciliation | ⬜ Blocked on P1b | | |
| P3 | Simulation & verification | ⬜ Blocked on P1b + aero data | | Long pole |
| P4 | Hardware definition | ⬜ Blocked on P1b *(reference shell model **now built**)* | | Envelope parametric and declared in `02-reference-155mm-model.md` — not YIL-gated |
| P5 | Idea submission | 🔄 **Draft refreshed** | 2026-09-18 | **Deadline 30 Sep 2026.** `submission/SIH26098-draft-from-register.md` **refreshed 2026-09-18** against everything closed since the machine sizing: the machine (C34/C36/C40/C41), the energy path and its thermal interface (C42, W7/W12, and P6's check that the bare thread does not deliver it), the air-gap/preload split (C35, C23), the power budget and the supercapacitor buffer (W1–W4), the ring-mounted IMU (N6–N8), the cost target (K4), the Monte Carlo campaign (R5) and the rig specification with its post-selection build gate (R7). **The submission-critical track is closed, so P5 is no longer gated on P1a** — what the deck must carry carefully is the **list of declared open verifications** (friction at flight speed, the fuze-well thermal interface, coexistence at speed, the ring–body interface, the buffer's launch survival) and the P6 re-baseline. **The deck itself is not built yet** |
| P6 | Post-selection re-baseline | ⬜ After shortlisting | | YIL data arrives only post-selection |
| P7 | Proof of concept | ⬜ Blocked on P4 | 2026-09-18 | For the finale. **Rig specification now set (R7): flight-representative — friction at up to ≈2 000 rad/s, the 2.92 kW generation path into the dump and buffer, closed-loop tracking with the DOB and state-dependent limits, coexistence, spin modulation, the ring–body interface, and the fuze-well thermal joint in W/K — and the build is gated on shortlisting** |

---

## Carried items — outstanding work between sessions

Work that has been decided or identified but not yet executed. **Check this list at the start of every session and clear anything still open before starting new phase work.** Remove items once closed.

| # | Item | Phase | Why it matters | Status |
|---|---|---|---|---|
| 1 | **Re-baseline M6 and re-derive M7.** M6 holds a bare `500 m class (range-direction 1σ)` assumption — roughly 2.2× pessimistic against the public anchor (unguided M549A1 CEP 267 m at max range → circular σ ≈ 227 m). Re-derive M7 as a capture-fraction problem, A = σ·sqrt(−2·ln(1−P)), and split range vs deflection. | P1b | M6 is the root of the sizing chain — canard area, `Taero`, alternator, bearing, mass and cost all inherit its error | ✅ Closed 2026-09-17 — M6 on the cited M549A1 anchor (267 m CEP → σ 227 m); M7 re-derived as a capture fraction (80% → 407 m, 19.5 m/s); Decision Log and risk 12 updated |
| 2 | **Amend `START-HERE-session-prompt.md`** — replace strict dependency-order with unblocked-first (G, C, F, N, W, R on declared `[ref]` placeholders; leave P and S until YIL data arrives). Without this the session stalls on ~20 consecutive placeholders. | P1a | Ordering | ✅ Closed 2026-09-17 — unblocked-first protocol now in `START-HERE-session-prompt.md` |
| 3 | **Build the "Submission-critical track" section** in the register — ~30 criteria that actually change what can be claimed in the idea submission. Becomes the priority order for P1a. | P1a | Gates P5 | ✅ Closed 2026-09-17 — 33-criterion track built in the register; P1a priority order set |
| 4 | **Set git identity and commit** — repo has 0 commits; `notes/`, `submission/` and `design/` are untracked | — | Nothing is versioned yet | ✅ Closed 2026-09-17 — repo-local identity (`jagath-srujan` + noreply); first commit `a0db1c8` (28 files) |
| 5 | **Reclassify the YIL-dependent criteria from `OPEN-BLOCKED` to `PARAMETRIC`** — M3, M4, M6, P1–P14, S1–S7, F11. Each becomes a bounded assumption over a declared envelope, with a public-data basis and a sensitivity showing the design closes across it. Rewrite the register's "Requests outstanding from YIL" section as **"Data required post-selection"** — it is a statement of what to request after shortlisting, not a live request. | P1a | Unblocks ~25 criteria that would otherwise sit idle until after selection, and stops sessions from treating them as blockers | ✅ Closed 2026-09-17 — 25 criteria reclassified (M3, M4, M6, P1–P14, S1–S7, F11); `PARAMETRIC` added to the status vocabulary and `OPEN-BLOCKED` retired; tracker rewritten as **"Data required post-selection"** with 7 documents, what each re-baselines, and the interim basis in use for each. The submission-critical track now has **no blocked entries** |
| 6 | **Build the reference 155 mm HE model** from public sources — mass, CG, Ixx and Iyy class, ogive contour, the standardised fuze-well interface, published dispersion. Then declare the envelope the design must close over. | P1a + P4 | Replaces the YIL shell drawing; on the critical path for stability (S1) and the kit envelope drawing | ✅ Closed 2026-09-17 — `design/02-reference-155mm-model.md`. M795 / M549A1 class, **MIL-STD-333B** interface (2″-12 UNS-2A thread), fielded **M1156 PGK** as the kit envelope benchmark, mass properties derived from published geometry and calibrated on the one published 155 mm CAD set, envelope declared. Produced two results: first-order **Sg 1.37–3.55** (design point 1.83) with a **≤ 5 % ΔC_Mα canard allowance**, and the finding that the `[ref]` Iyy is 28 % high on stability optimism |
| 7 | **Update the risk register for the parametric design basis** — the design now rests on a reference shell, not YIL's. Record it as a named risk with the P6 re-baseline as its mitigation. | P1a | The largest single assumption in the project must be visible rather than implicit | ✅ Closed 2026-09-17 — risk **20** (reference shell: accepted, mitigated by the P6 re-baseline, envelope declared openly) and risk **21** (the `[ref]` inertia divergence: conservative value adopted, model uncertainty stated). Risk **3** updated from "Open" to "quantified — governs the canard allowance" |
| 8 | **Commit the 9 closed criteria** — register and roadmap modified since `a0db1c8` | — | Housekeeping | ✅ Closed 2026-09-17 — committed with the parametric reclassification, the reference model and the C-domain work |
| 9 | **Decide the terminal seeker / growth module — the new X block.** Added to the register 2026-09-17 from the team's proposal to add laser/EO terminal guidance and visual odometry for GPS-denied operation. 19 criteria, all open, entirely gated by **X1**. Four of them — **X1, X3, X4, X17** — change what the submission may claim the moment a seeker is mentioned. The load-bearing finding: the nose points up throughout the ascent, so no target-referenced seeker can see the target pre-apogee, and terminal-only guidance corrects only **≈35–90 m** against **407 m** of baseline dispersion. **A seeker narrows the GPS-denied error; it does not close it.** Full detail in the register's X section, the track note above, and risks 29–31. | P1a | Either it appears in the deck with a bounded and honest claim, or it is left out entirely. Naming a seeker with X1–X4 undecided is the one way this submission could lose credibility | ✅ Closed 2026-09-18 — **X1 DEFINED: optional growth module, out of the baseline. X17 DEFINED: anti-jam GNSS with INS coasting is the primary GPS-denied answer, the seeker only the secondary** (and it rides N3's multi-element aperture, so it costs no new antenna). **X3–X6 derived in the same pass, and X4 *corrects* the finding this row carried:** the correctable miss is **≈59 m at the design point (N = 3), bounded above by 89 m (N = 2)** — the old "≈35–90 m" pair mixed two guidance gains — so **348 m (85 %, X5) of the 407 m requirement still depends on GNSS/INS**. N5 is promoted from future upgrade to baseline requirement as a consequence. Register: X1–X6 and X17 rows, Decision Log (2 rows), risks 29–31 |
| 10 | **Confirm the CAA machine sizing, and re-size W7 against it.** `design/03-caa-machine-sizing.md` sizes the frameless outrunner: 12 slots / 14 poles, ≈79 mm gap diameter, L 25–30 mm, 400 V bus, ≈0.9 kg. Outputs marked *await confirm*: C14–C16, C18–C20, C34, C36, C41. **The load-bearing finding is C42** — the machine is a *loaded generator* delivering **2.92 kW peak and ≈121 kJ over the flight**, ×2.4 the reference's rating, invisible until now because the bench rig ran body spin 21.6× slower. Three follow-ons: W7 must be sized against that number rather than treated as a dissipation detail; C43's cant-angle ↔ power coupling must enter the C8/C2/C3 trade; and the C35 air-gap deflection requirement (0.20 mm at 15 000 g) becomes the governing bearing **stiffness** spec, not just friction. | P1a / P2 | The kilowatt-class energy load has no owner in W yet, and the nose is already over-subscribed for volume (risk 27). Recorded as risk 32. | ✅ Closed 2026-09-18 — **sizing confirmed**: C14–C16, C34, C36, C41 `DEFINED`; C18–C20, C35, C40, C42, C43 `DERIVED`. **W7 and W12 derived, and the answer is the shell:** 121 kJ cannot be stored, cannot be held in the kit's own 1.5–2.0 kg (134–179 K rise), and is only ≈26 % rejectable to the airstream — but it raises the **45 kg shell body by 5.8 K** through the fuze-well threads, so the spec is a **thermal interface ≥ 58 W/K**, not a radiator, and it takes **no nose volume** (risk 27 relieved). It is **not avoidable**: C8's 18.1 N sets cant ≥ 10°, which produces the 2.92 kW. C35 splits into a `367 N/µm` structural case under setback and a **`122 N/µm` bearing case radially — the preload tension against C13**. **Two corrections fell out:** G7's recorded basis was wrong (the back-EMF ceiling is `V_bus/Kv` = 1914 rad/s, 61× the ±31.42 rad/s ring limit, so the rate limit is not bus-dependent), and the real bus condition — the machine reaching `E = V_bus` at launch spin, i.e. at peak load — is handed to W8/C17. **W7 and W12 were confirmed by the team the same day**, so the thermal path stands as a declared interface requirement rather than a provisional derivation |
| 11 | **P6 thermal check (carry-in from the W12 finding).** The fuze-well thread is a thermal interface with a ≥ 58 W/K peak requirement, and that figure sits close to what a 2″-12 UNS thread actually delivers. Estimate the flank and seat contact conductance, and state what closes the gap if the thread alone does not. Record the answer on P6. | P1a | The 121 kJ path is the architecture's defining cost; a requirement that *assumes* an interface exists is not the same as one that shows the interface works | ✅ Closed 2026-09-18 — **the bare joint does not close it: flank + seat ≈ 3–16 W/K (central ≈ 8)**, against ≥ 58 W/K at the peak and ≥ 20–27 W/K on the flight average — ≈7× and ≈2.5× short. **Closing route recorded on P6:** the well bore as a *contacting* radial path (18.8e-3 m², ≈17× the flank area → 19–94 W/K; a clearance fit does not count — its 0.1 mm air film is ≈5 W/K), a conductance-specified joint (ground flanks and seat; **the torque spec is now a thermal requirement**), the peak/average split with the kit's metal buffering the launch transient, and rig verification (R7). **Also derived: the 45 kg shell is a long-time sink** — 90 s penetration depth ≈30–65 mm, so the flight-time participating mass is the kit plus the shell's nose (≈6–8 kg → ≈25–35 K) and 5.8 K is the asymptote. Cross-referenced from W7/W12; risk 32 extended; decision-log entry added |
| 12 | **Preload-trade ownership (carry-in from C35/C13).** The 122 N/µm bearing-pair stiffness and the friction budget pull in opposite directions through preload — more preload buys air-gap stiffness and costs friction, and the friction budget is already the tightest gate in the design. Neither criterion owns the trade. Give it an owner and record where it is resolved. | P1a | A tension split between two rows can be lost between them: each row can look satisfied while the pair is not | ✅ Closed 2026-09-18 — **owner: C23 (bearing preload).** One preload value must hold `k_pair ≥ 122 N/µm` (radial, launch) while keeping `Tf ≤ 0.10 N·m` flat across the speed envelope, on C22's load-dominated bearing; resolved at C23 with C22, verified by C25 by test and on the rig. Recorded in C13, C23, C35, risk 1 and the decision log |

---

## Phase definitions

### P1a — Submission-critical track
**Purpose:** close the criteria whose answers actually change what can be claimed in the idea submission.
**Inputs:** the register's "Submission-critical track" section.
**Work:** the same one-question-at-a-time interview, restricted to those criteria.
**Exit criteria:** every shortlisted criterion is `DEFINED` or `DERIVED`, or explicitly parked with a stated reason.
**Output:** the number set and argument that P5 is written from.

### P1b — Remaining criteria
**Purpose:** complete the register for the design phases.
**Work:** unblocked-first, per the amended protocol in `START-HERE-session-prompt.md`.
**Exit criteria:** all non-blocked criteria `DEFINED` or `DERIVED`; every blocked criterion carries a declared placeholder and a named dependency.
**Output:** a complete register.

### P2 — Budget reconciliation / design closure
**Purpose:** the criteria are defined individually; they must now be reconciled against each other. Designs rarely close on the first pass.
**Work:** mass budget vs mass limit; torque authority vs `Taero` envelope; power demand vs alternator generation; energy dissipation path; CEP error budget vs the 30 m requirement. Iterate the trades — canard area against alternator mass against unit cost — until every budget closes.
**Exit criteria:** every budget closes with a stated margin, and each margin is recorded against the criterion that sets it.
**Output:** `design/01-design-definition.md` — the consolidated, self-contained design definition, with every number traceable to a criterion ID.

### P3 — Simulation and verification
**Purpose:** convert defined criteria into verified performance.
**Work:** 7-DOF trajectory model with the guidance law in the loop; the aerodynamic coefficient set; Monte Carlo dispersion analysis. Derive the CEP rather than restating it, and verify the error budget.
**Exit criteria:** a Monte Carlo campaign produces a CEP with stated confidence, and the trajectory-correction demonstration the PS asks for exists as a result.
**Output:** simulation results, the derived CEP, the validated error budget.
**Gating risk:** the aero coefficient set. Source it from published 155 mm data, fill gaps with CFD, and carry uncertainty explicitly.

### P4 — Hardware definition
**Purpose:** turn the sizing into hardware.
**Work:** CAD of the canard actuation assembly with structural analysis under the launch load case; kit envelope drawing inside the ogive and fuze well; electronics block diagram; fuze design definition.
**Exit criteria:** the CAD survives the governing load case, and the assembly fits the declared envelope.
**Output:** the PS's hardware deliverables.

### P5 — Idea submission
**Purpose:** submit.
**Work:** write the six-slide Idea Presentation Format and the form fields **from the register**, not from the generic drafts. The existing `submission/` files give the structure and the section coverage; every number must come from a criterion ID.
**Exit criteria:** submitted before the deadline.
**Deadline:** 30 September 2026 — confirmed 2026-09-17.

### P6 — Post-selection re-baseline
**Purpose:** replace the reference shell with YIL's actual shell, once the entry is shortlisted and the documents are released.
**Work:** re-baseline every parametric criterion (M3, M4, M6, P1–P14, S1–S7) against the real drawing and firing tables. Re-run the sizing chain and re-confirm every number derived on a public-data or `[ref]` basis. Expect the canard sizing, alternator sizing and the kit envelope to move.
**Exit criteria:** no criterion remains `PARAMETRIC` — every value traces either to a YIL document or to analysis performed on one.
**Note:** deliberately last. It is not a blocker and must never be used to justify pausing work.

### P7 — Proof of concept
**Purpose:** demonstrate the concept in hardware for the finale.
**Work:** reduced rotating dynamometer rig — ring on its bearings, alternator, imposed relative spin, applied torque load, ring-angle sensing. Demonstrate closed-loop ring-angle tracking under disturbance, the disturbance observer, and the adaptive limits.
**Exit criteria:** ring-angle tracking demonstrated under an applied aerodynamic torque profile.
**Output:** the PS's "prototype or proof-of-concept (preferred)".

---

## Master session prompt

Copy the block below to start any design session from this point on. It works at every phase — it reads the state, tells you where you are, and does the next right thing.

```
Read these files in full, in this order:
  1. design/ROADMAP-and-prompts.md          — the phase plan and its exit criteria
  2. design/00-design-criteria-register.md  — current state of the criteria
  3. design/START-HERE-session-prompt.md    — the working protocol
  4. notes/02-PGK-SIH-design-brief.md       — context

Then locate us:
  - Determine which phase we are in using the register's Status column, its
    "Progress at a glance" table, and the "Requests outstanding from YIL"
    tracker. Cross-check against the phase status table in the roadmap.
  - Tell me in a few lines: the phase, the evidence you used, what is
    complete, what is blocked, and what the next action is. Say so if the
    roadmap's phase status table and the register disagree.

Then clear the carried items:
  - Read the "Carried items" section of the roadmap. Close every item still
    marked Open, in the order listed, before starting new phase work. Each
    item describes what it needs.
  - When an item is done, mark it Closed in the roadmap table and say so.
  - Do not skip a carried item because it looks like it belongs to another
    phase — the items are listed separately precisely because they fall
    between phases.

Then execute the next action of that phase.

  - If the phase is P1a or P1b, follow START-HERE-session-prompt.md exactly:
    one question at a time, never batched, and edit the register after
    every single answer — value, status, Decision Log, progress table, risk
    register. Do not defer edits.
  - If the phase is P2, P3, P4 or P7, say what you are about to produce and
    what it depends on, flag any dependency that is not yet satisfied, and
    then proceed.

Before advancing to a new phase, verify that every exit criterion of the
current phase is met and state explicitly which ones you checked. If any
exit criterion is unmet, do not advance — tell me which one and what it
needs.

Rules:
  - Only create or edit files inside design/. Never modify notes/ or
    submission/ unless I explicitly ask.
  - Never mark a criterion DEFINED on my behalf. DEFINED means I confirmed
    it; DERIVED means you computed it.
  - Never invent a number without labelling it an assumption and naming
    what would verify it.
  - Any criterion derived on top of a placeholder must be marked
    provisional and must name the placeholder it depends on.
  - **Resolve coupled criteria together.** If a criterion is coupled to one
    in another domain, say so before asking and do not close either without
    the other. The register now carries several, all created by the machine
    sizing of 2026-09-18:
      · **C43 ↔ C2/C3** — cant angle buys guidance force and costs
        dissipated power in equal measure, so the cant decision cannot be
        taken without C42.
      · **C42 ↔ W7 / W12** — the generated power (2.92 kW peak, ≈121 kJ per
        flight) is what the dump must shed, so W7 and W12 are downstream of
        C42, not independent.
      · **C35 ↔ C22 / C32** — the 0.40 mm air gap sets a 0.20 mm maximum
        relative deflection at 15 000 g, which is a stiffness spec on the
        bearing pair and the ring retention.
      · **C9 / C12 ↔ C13** — the friction budget is the feasibility gate for
        whether a control pair exists at all.
    Ask the coupled questions as one question where they cannot be separated.
  - When the September deadline and a design-phase task compete, prioritise
    the submission path: P1a then P5.
  - At the end of the session, update the phase status table in
    design/ROADMAP-and-prompts.md so the next session can locate itself.

Start with the location report.
```

---

## Quick reference — which prompt do I use?

| Situation | Use |
|---|---|
| Normal design session, any stage | The master prompt above |
| First time, before anything is defined | `design/START-HERE-session-prompt.md` (the master prompt supersedes it once phases are in motion) |
| Just want to see where things stand | Say: *"Read design/ROADMAP-and-prompts.md and design/00-design-criteria-register.md and give me a status report only — do not start work."* |
| The September deadline is close and the design work has stalled | Say: *"Prioritise P1a then P5 only. Nothing else."* |
