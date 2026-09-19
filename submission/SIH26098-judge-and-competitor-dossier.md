# SIH26098 — Judge Simulation, Competitor Prediction and Differentiation Dossier

Written 2026-09-19. Companion to `SIH26098-form-content.md`, `SIH26098-template-slides.md` and `SIH26098-draft-from-register.md`. It does not replace them — it tells you which parts of them will win, which parts will be attacked, and what to change before 30 September.

**Three kinds of statement appear below, and they must not be confused:**

| Tag | Meaning |
|---|---|
| **[fact]** | Sourced from the public record. URLs in §10. |
| **[ours]** | A number or claim from our own register/brief. |
| **[predicted]** | Inference. Labelled so nobody quotes it back as evidence. |

---

## 0. The one-page version

Six findings change what you should do:

1. **The idea round is won on six slides read by someone who will never see your work.** No jury, no demo, no code. Roughly five teams per problem statement advance, out of a cap of 500 submissions. The deck is the entire game. **[fact]**
2. **The official rubric is published and is nine words long:** novelty, complexity, clarity and details in the prescribed format, feasibility, practicability, sustainability, scale of impact, user experience, potential for future work progression. The deck should be re-read against those nine words before anything else. **[fact]**
3. **Three of our five declared novelty claims have direct prior art, and two of the prior-art items are on our own references slide.** A dual-spin/domain judge will see this in the first two minutes. This is the single most fixable, most damaging defect in the current submission. (§6)
4. **The three PS deliverables that actually differentiate — trajectory-correction simulation, CAA CAD, electronics block diagram — do not exist yet.** Every competitor will be weak here too, which is precisely why shipping them is the cheapest large score available. (§7, move 1–3)
5. **AI-assisted evaluation is likely, the tools refuse to design weapons, and 2026 juries now ask "how much of this did AI write".** A refusal-prone screener falls back on keyword coverage, specificity and checkable claims — all three of which we can control. (§5)
6. **Our real moat is not the mechanism. It is that we are the only entry that has done the arithmetic and found the hard problem.** Nobody else will arrive with a declared 121 kJ thermal interface and a 1.11:1 authority margin stated honestly. That is the differentiator. Lead with it. (§7)

---

## 1. The evaluation machine — what actually happens to our deck

### 1.1 The two gates

| | Idea screening (Oct–Nov) | Grand finale (Nov–Dec) |
|---|---|---|
| Who | Experts / ministry + industry evaluators, possibly an AI first pass | Panel at a nodal centre: PS-owner officer + domain expert + academic/innovation evaluator |
| What they see | **Six slides. Nothing else.** No presentation, no demo, no link they will click | 36 hours of build, evaluators visiting the table 3–4 times, then a pitch |
| Volume | Up to 500 ideas per PS; ~5 teams advance | 1 winner per PS, ₹1.5 L |
| Decided by | Reading comprehension of our deck | Visible delta between visits + demo + answers under pressure |

**[fact]** The screening gate is the one that matters for the next 11 days. The playbook that documents it is blunt: *"the round deciding it never sees your code, your demo or your team. It reads six slides and nothing else."*

### 1.2 The published rubric, and what each word actually scores in a defence deck

**[fact]** SIH 2026 Guidelines, verbatim: *"the ideas will be evaluated by experts. Evaluation criteria will include novelty of the idea, complexity, clarity and details in the prescribed format, feasibility, practicability, sustainability, scale of impact, user experience and potential for future work progression."*

| Rubric word | What a MoD evaluator reads it as | Our current standing |
|---|---|---|
| **Novelty** | "Have I seen this before?" — and for a defence PS, they have seen a lot | **At risk.** Three claims are literature. §6. |
| **Complexity** | Is this trivially easy or genuinely hard? A hard problem *solved* scores; hard problem *described* does not | Strong — the torque balance, the energy path, spin-rate sensing |
| **Clarity and details in the prescribed format** | Did they use the template, is it readable, are the numbers specific | **At risk.** Our content is register-grade: dense, tag-laden, 3,500-character abstract. §5.3 |
| **Feasibility** | Can this be built by someone, even if not by a student team? | Strong on paper, **unproven** — no sim, no CAD, no rig |
| **Practicability** | Does it fit the gun line, the supply chain, the magazine, the doctrine? | Good — setter interface, no shell change. Thin on production and HERO/EMI |
| **Sustainability** | Will it survive contact with a real programme — maintenance, upgrade, obsolescence | Good — modular backbone, growth interface |
| **Scale of impact** | How many rounds, how many guns, how much logistics removed | Strong — but currently asserted, not quantified with a source |
| **User experience** | For a fuze: the gun crew and the maintainer. Is procedure unchanged? | Strong and under-sold — the inductive setter is a UX story |
| **Future work progression** | Is there a path from here to a product | Strong — but the seeker module must stay bounded (X1) |

### 1.3 The real size of the field

- **[fact]** Hardware statements draw roughly half the field of software ones; MoD/strategic-body statements draw the smallest fields of all. A third-party analyst model puts this PS at **65–150 teams expected**, "#32 of 240 by expected field".
- **[fact]** The same analyst's automated review scored this PS **acceptance 1/5, feasibility 1/5** and concluded: *"every submission will therefore be a paper architecture with no build and no test data, which is a weak position against a panel that develops this hardware professionally."*
- **[fact]** A tracker snapshot shows **0/500 ideas registered** for this PS at the time it was scraped. You report six submitted. Either way the field is early and small.
- **[predicted]** Consequence: the field is populated by (a) teams who read "MoD" and self-deselected, (b) teams who submitted early with AI-generated decks, and (c) one or two serious teams. We are aiming at a five-seat gate against roughly 30–80 genuine attempts, not 500.

### 1.4 Two administrative defects to check today

1. **Theme/bucket inconsistency across our own files.** `form-content.md` says *Smart Vehicles*; `draft-from-register.md` says *Defence and Security*; the analyst dataset classifies the PS domain as *Miscellaneous*; your paste of the PS says *Smart Vehicles*. **One of these is wrong and it appears on slide 1.** Copy the ID, title, theme and category off the portal character-for-character. A wrong theme is the cheapest mark lost in the whole process. **[fact — the playbook lists this as the #1 slide-1 trap]**
2. **Deadline discrepancy.** Our register records 30 September 2026. One tracker snapshot shows a **20 September 2026** submission deadline for this PS. Treat 20 September as real until the portal says otherwise. **[fact — conflicting sources]**

---

## 2. The seven judges

Not seven people — seven *lenses*. Any real panel holds three or four of them at once, and the finale adds the ones that ask the questions nobody prepares for. For each: what they optimise, what they already know, the question that ends a weak answer, and whether our deck currently answers it.

### J1 — The YIL manufacturing host
*Likely: a senior works/D&D manager from Ordnance Factory Ambajhari, Nagpur — the unit that makes the shell hardware, cartridge cases and fuzes.*

- **Optimises:** "Can I build this on the line I already have, with people I already employ, without a capital case?"
- **Knows:** the shell's fuze well better than we do; the real cost of a machined part; that a precision guidance kit is a supply-chain problem before it is a control problem.
- **Killer question:** *"Your stator has 12 slots and your rotor has 14 magnets. What machine winds it, what does that machine cost, and how many do I need to buy for 5,000 kits a year?"*
- **Our current deck:** says "standard magnet and winding fabrication" and "cost drivers are bearings, magnets and windings". That is a materials statement, not a manufacturing plan. **Gap.**
- **Fix:** one slide-4 line naming the production route — frameless outrunner wound on a conventional concentric winder, magnets in a retained sleeve, stack laminated from standard electrical steel, assembly by bearing preload fixture — plus the two capital items if any, and a make-vs-buy note for the winding.

### J2 — The fuze safety engineer
*Likely: a YIL/OFAJ fuze specialist, a DGQA quality representative, or a DRDO armament-safety person. This is the most dangerous seat in the room, because a fuze question answered badly is a public-safety story.*

- **Optimises:** "Nothing functions in the bore; nothing functions in the magazine; nothing functions on the gun line; and it still goes off when it should."
- **Knows:** MIL-STD-1316, STANAG 4369, AOP-39, the difference between an out-of-line rotor and an electronic interlock, and the fact that a failed guided round must still be a functioning round.
- **Killer questions:** *"What is your dud rate?"* / *"You have a bus, a kilowatt-class dump resistor and a 24 GHz emitter next to your firing circuit — where is your HERO assessment?"* / *"What happens on a misfire with the round half-way into the tube?"* **Updated 2026-09-19: the bus is now ≈150–200 V (180 V nominal) per H8/H12, superseding the 400 V of the earlier sizing pass; the HERO question is now answered by register criterion E12, but the answer should be rehearsed because the question is the useful part.** / *"If the guidance fails and the round lands 400 m from the target, does it still detonate?"* — **the predicted-miss question, register criterion F16, and the one the answer sheet below still lacks.**
- **Our current deck:** excellent on the out-of-line rotor and the two environmental interlocks; silent on HERO/EMR, ESD, insensitive-munitions and dud rate. **Gap, and it is the gap a fuze judge instinctively probes.**
- **Fix:** add three lines — HERO/EMR zoning and the shielded fireset reservoir; ESD and RF hazard management to the fuze standards we already cite; and a dud statement (a conservative number with the reason, not a claim of zero).

### J3 — The DRDO armament scientist
*Likely: ARDE/HEMRL-adjacent, or an aerospace/GNC academic who has read the dual-spin literature.*

- **Optimises:** "Is this new, and is it right? Show me the derivation."
- **Knows the literature cold:** the Chinese dual-spin fixed-canard corpus, Wernert/Theodoulis, Spagni, the METU thesis, US Patent 6,981,672, and — critically — that **DRDO unveiled its own 155 mm guided projectile prototype at Aero India 2025** and that the Army launched an indigenous terminally-guided-munition programme under ADITI-4 in March 2026 targeting sub-metre CEP with a hybrid laser/IIR/MMW seeker. **[fact]**
- **Killer question:** *"The impact-point-prediction law for a dual-spin projectile with fixed canards is a 2019 paper, the fixed-canard 2-D geometry is a 2006 patent, and the de-spun ring with the alternator as the actuator is a 2022 thesis. Which part of this is yours?"*
- **Our current deck:** cannot answer this cleanly, because it claims those three things as novelty *and* cites all three in the references. **This is the defect to fix first.**
- **Fix:** §6 and §8.

### J4 — The user's representative
*Likely: a Directorate of Artillery officer or a DGQA user-rep, if present.*

- **Optimises:** "Does this drop into a real battery's routine, and what does it cost me in training, storage and logistics?"
- **Knows:** that the Army has a live **RFI out for indigenous 155 mm electronic fuzes in exactly three categories — electronic percussion, electronic proximity and electronic time** — and that India is partly dependent on imported fuzes for ATAGS, Dhanush, K9 Vajra and MGS. **[fact]** This PS is not academic; it is a routed business requirement.
- **Killer question:** *"Your fuze is one box with three modes. Our RFI is three separate fuze types. Are you bidding into that, and does one unit replace three stock lines or add a fourth?"*
- **Our current deck:** mentions the three modes and the setter, but never connects to the RFI or to inventory logic. **Gap, and an easy win.**
- **Fix:** add the mapping — one multi-mode unit covering all three RFI categories, one stock line instead of three, unchanged gun-line procedure, and a stated shelf-life/storage argument.

### J5 — The feasibility/innovation evaluator
*Likely: an academic or an industry innovation panellist on the screening panel.*

- **Optimises:** "Is the risk honest and is the path real?" Their playbook is explicit: *the feasibility slide is the one that separates two decks with the same idea, and a slide with no risks on it reads as a team that has not thought past the demo.* **[fact]**
- **Killer question:** *"What have you not solved, and what will you do about it?"*
- **Our current deck:** unusually strong here — five declared open verifications, a named risk register. **But it is buried.** The honesty is spread across 35,000 characters instead of being three bullets with mitigations on slide 4.
- **Fix:** promote it. Three risks, each with the mitigation and the date. This is our strongest single slide and it is currently invisible.

### J6 — The AI screener (if used)
*Increasingly likely at screening, where volume makes human reading expensive.*

- **Optimises:** coverage of the PS bullets, internal consistency, specificity, and non-duplication against the other submissions and against the public web.
- **Behavioural fact:** general-purpose models **refuse to produce weapons design content for this statement** — one published AI analysis of SIH26098 returned "Not provided" for its build spec and wrote that producing actuation, sensor or control design content would be "producing weapons design content regardless of the hackathon framing." **[fact]**
- **Predicted consequence:** an automated screen on this PS degrades to keyword coverage and similarity scoring, not deep technical judgement. That is *good news for us* if we make our slide text dense with the PS's own vocabulary and bad news if our claims are unverifiable.
- **Killer behaviour:** flagging unsourced precision, unresolved internal codes, or text that resembles generated filler.
- **Full treatment in §5.**

### J7 — The AI-disclosure question (now standard)
**[fact]** 2026 evaluators expect teams to be explicit about which parts of the build are AI-assisted, and the standard finale question is *"How much of this did AI write?"* with the documented trap answer being *"we wrote everything ourselves."*

- **Our answer must be prepared, short and true** — and ours is genuinely a good story: AI was used for literature synthesis and drafting; every number came from our own derivation chain with a named criterion; the open verifications are ours. Say the proportion. Do not say "none".

---

## 3. The six who already submitted — plus the sleeper

**[predicted]** Archetypes, not identifications. Each is the shape a team lands in when it optimises for the deck rather than the problem. One of these is confirmed real, with evidence.

### C1 — "The Vibe-Coded Trajectory" *(confirmed real — evidence found)*

**Evidence.** A public GitHub repository for this exact PS: a Python 3-DOF simulation with ZEM guidance, a Flask web dashboard, a Dockerfile and a Vercel/Render deploy. Its README is written for a layperson, includes a definitions glossary, and was built inside an AI tool's scratch directory. It states in-scope items as 3-DOF physics, stochastic Monte Carlo and "canard actuator limits (5–10 g)", and out-of-scope items as 6-DOF dynamics, the fuze, HIL and GNSS jamming. Its sensitivity table claims that under guidance **"CEP stays under 4 metres unless the error exceeds fin steering limits."** **[fact]** (It also recommends activating a venv at a path under a home directory named for a Gemini/antigravity scratch folder — the AI provenance is not hidden.)

- **Its deck will say:** GPS-guided canard package, Monte Carlo CEP in single digits, a live dashboard link, a "trajectory correction demonstration" screenshot.
- **Where it scores:** *clarity* (the README is genuinely readable) and *complexity* (there is running code). It has the artifact we do not.
- **Where it dies:** the CEP claim. A requirement of 30 m answered with 4 m reads as someone who has never seen a real dispersion budget. The fielded system achieves 30–50 m and cost a US$863 M production award; a 3-DOF model with no spin, no fuze and no launch environment cannot beat it by 7×.
- **The killing question:** *"Your CEP is 4 metres. The US M1156 is 30 and the requirement is 30. What in your model makes you 7× better than the fielded system?"*
- **What we learn from it:** it will be *deployed and clickable*. Deck-vs-deck, a clickable simulation beats a promised one. This is the strongest argument for shipping our simulation before 30 September.

### C2 — "The Quadcopter in a Shell"

**Likely content:** four servo-actuated canards, a drone flight controller (often literally a Pixhawk-class IMU), PID loops, a CAD nose with servos, lithium battery, sometimes a small bench demo of a canard deflecting.
**[predicted]** This is the most common naive answer, because it is the answer a control-systems student gives for any guided vehicle.

- **Where it scores:** it looks like a real build; the control diagram is familiar to a general evaluator.
- **Where it dies — three ways at once:**
  1. **Spin.** The airframe rotates at 1,100–1,900 rad/s. A body-fixed servo canard on a spinning shell produces a rotating force vector that averages to approximately nothing; the classic answer is a de-spun section, and they will not have one. **[ours: 1107–1912 rad/s]**
  2. **Launch.** 15,000 g makes a servo a projectile inside its own housing. **[ours: 73.5 kN on the ring]**
  3. **The PS's own words.** The statement asks for a *canard actuation assembly* with *low SWaP-C* and *survivability*. Servos, gearboxes and a battery are the three items we removed for exactly those reasons.
- **The killing question:** *"Show me the servo that survives 15,000 g, and tell me what your rotating canard force averages to over one revolution."*

### C3 — "The Wikipedia M1156"

**Likely content:** a clean, correct description of the M1156 PGK — GPS guidance, four fixed canards, combined fuze — with a block diagram, a plausible CEP of 30 m, and a cost target quoting a public figure. No derivation, no CEP budget, no launch analysis.
**[predicted]** This is what an AI-assisted deck produces for this PS if the model is willing to write at all, because the M1156 is the canonical answer and it is thoroughly documented.

- **Where it scores:** *clarity* and *practicability*. It reads like a product.
- **Where it dies:** the only question that matters — *"How are you different from the thing you just described?"* — plus the cost case, which collapses because they are describing a US$13,541 import rather than attacking it.
- **Our advantage:** we are the anti-M1156. Same class of capability, different materials budget, and a stated mechanism for why it is cheaper.

### C4 — "The Fuze Lab"

**Likely content:** a serious electronics submission — proximity sensing (often 24 GHz radar or IR), a programmable timer, an impact switch, safe-and-arm logic, a proper PCB block diagram, maybe a bench demo of a radar module detecting a moving target. Weak or absent guidance.
**[predicted]** Electronics-heavy teams gravitate here because the fuze is the part that looks like normal embedded work.

- **Where it scores:** *feasibility* and *complexity* — and if they demo a proximity sensor on a bench, they have an artifact.
- **Where it dies:** the deck answers maybe one third of the PS. No CAA, no GNC, no CEP, no trajectory. The rubric scores the statement, not the best third of it.
- **Their best move (which we should pre-empt):** claiming their fuze is the "hard part" of a guided shell. It is not; the guidance is.
- **The killing question:** *"Where is the guidance?"*

### C5 — "The MATLAB Thesis"

**Likely content:** a 6-DOF simulation, well-produced plots, a CEP derived from Monte Carlo, a literature review, references to the Chinese dual-spin papers and possibly the METU thesis. Little or no hardware, no fuze, no CAD, no cost.
**[predicted]** This is the competitor most likely to resemble us — and the one most likely to *out-score us on artifact* if they ran their simulation and we only budgeted ours.

- **Where it scores:** *novelty* and *complexity* if their model is real.
- **Where it dies:** typically on spin (their model frequently omits the dual-spin degree of freedom), on the fuze gap, and on launch survival.
- **Our counter:** our model is 7-DOF with the ring as an independent body, and our register holds the torque and authority criteria that a 6-DOF model cannot express. But **we must actually run it.** A rival with plots beats us with a table.

### C6 — "The Excalibur Dream"

**Likely content:** a seeker (laser semi-active, EO, or "AI-based target recognition"), thrusters or reaction jets, an anti-jam GNSS, sometimes a swarm or network-enabled round. Ambitious, and often the most visually exciting deck in the room.

- **Where it scores:** *novelty* and *scale of impact* with a non-specialist evaluator.
- **Where it dies:** *feasibility* and *practicability*. It breaks the PS constraint — compatible with the existing shell at low SWaP-C — and a knowledgeable panel knows that DRDO's own terminally-guided-munition programme with a hybrid laser/IIR/MMW seeker targeting sub-metre CEP under ADITI-4 is the funded answer to *that* problem, not this one. **[fact]** A student deck claiming a seeker is claiming a programme.
- **The killing question:** *"Your canards have to point a seeker at the target. Your nose points up for the whole ascent. When exactly does your seeker see anything?"*
- **Why this matters to us:** our register already answers that question — a ~20 s descent window, ≈59 m of correctable miss against 407 m of need, 85 % of the correction still on GNSS/INS **[ours, X3–X6]**. That paragraph is worth more than a seeker claim and it is currently buried in §6 of the draft.

### C7 — The sleeper: "The Cheap Drag Brake"

**Likely content:** a 1-D range-correction fuze using deployable drag brakes, with the muzzle-velocity correction computed on the gun line and set into the fuze — the SPACIDO concept (GPS-free, low cost, 1-D). **[fact — SPACIDO is a real fielded product using exactly this: muzzle-velocity radar plus air brakes, explicitly GPS-independent and low cost]**
**[predicted]** This is the most dangerous competitor, and the one nobody expects. It is genuinely cheap, genuinely GPS-free, genuinely simple, and it hits the two adjectives the problem statement actually leads with: *low-cost* and *30 m*.

- **Where it scores:** *feasibility*, *practicability*, *sustainability* — a real product exists, so it reads as achievable.
- **Where it dies:** it is a **1-D range correction**, so 2-D deflection error survives; and it does not deliver the fuze-mode set or the canard actuation the PS explicitly requires. It also caps its improvement: trimming range error alone does not reach a 30 m circular figure from a 267 m unguided CEP. **[ours, M6]**
- **Our counter, and it must be on slide 2 or 3:** the PS asks for *canard actuation* and *2-D* correction. Drag brakes answer one axis of the problem. We should also state the lesson honestly: the reason to compare against the air-brake family is that *they* are the low-cost incumbent, so our cost claim has to beat a brake, not only a US$13,541 kit.

---

## 4. Cross-examination — the questions, the trap, and the answer that wins

Format: what they ask → why → what our deck currently invites → the answer that lands → the edit.

### 4.1 Accuracy and the CEP claim

**Q1. "Where does 23.9 m come from?"**
*Why:* the whole submission rests on it, and 30 m is the PS's number.
*Invites:* silence. Our budget is in the draft, not the deck, and the deck's feasibility slide shows acceptance bands rather than our design point.
*Wins:* "A 1σ radial budget, RSS 20.3 m, converted by CEP = 1.1774σ → 23.9 m, leaving about 20 % under the claim. Every line has a source, and the dominant line is guidance and prediction, not hardware."
*Edit:* put the CEP table on slide 4 complete with RSS and the conversion.

**Q2. "Is that a measured number?"**
*Wins:* "No. It is a derived budget with declared allocations, and the campaign that converts it to a result is specified — about 10,000 full-fidelity flights, 5,000 at the design condition for ±2.0 % at 95 % confidence, plus five envelope corners, with the claim carried by the worst corner's 95 % upper bound. The breach fraction above 30 m is reported per condition, because the requirement is a tail statement."
*Edit:* this is already in the draft; it needs to be one visible bullet, not a paragraph.

**Q3. "Why should I believe the guidance-and-control term is 17 m and not 40?"**
*Wins:* name the three sub-terms and what bounds each — propagation and model error 13 m (bounded by coefficient uncertainty, which is carried explicitly), ring angle 9 m (from a 1.28° RSS attitude-and-pickoff error), actuation and loop lag 6 m (from a 6.2 Hz outer loop against a 6 Hz guidance update).
*Edit:* the sub-term breakdown is our credibility. Show it.

**Q4. "The M1156 does 30 m with a much bigger programme, and TopGun advertises 20 m at any range. Why is yours different?"**
*Why:* they know the competitor set. **[fact — IAI TopGun claims 20 m CEP at any range; Elbit Silver Bullet II is a fielded 2-D CCF; the Yugoimport CCF also states 20 m]**
*Wins:* "Both are correct and both are priced accordingly. TopGun and Silver Bullet are the reason a 30 m kit has to justify itself on cost rather than on accuracy — the accuracy is not the differentiator, the unit cost and the indigenous supply chain are. Our claim is the same class of accuracy at a target of ₹6.5 lakh, and the mechanism that gets us there is removing the actuator, the gearbox and the in-flight battery."
*Edit:* **add a comparison table to slide 4 or 5.** M1156 / TopGun / Silver Bullet II / SPACIDO / our kit, across: guidance, actuation, fuze modes, dependence on GNSS, unit cost, and what it does not do. Pre-empting this question is worth more than any other single slide change.

**Q5. "You exclude target-location error from your claim. Isn't that the biggest term?"**
*Wins:* "It is, and that is exactly why it is stated rather than hidden. The kit cannot fix a wrong coordinate, and any submission claiming 30 m *including* target-location error is claiming the crew's survey is perfect. Ours is published as a sensitivity. The honest version: the design delivers 23.9 m against the aimpoint it is given."
*Edit:* already strong. Keep.

### 4.2 Architecture and actuation

**Q6. "Two fixed canard pairs and a rotating ring. Why is this not a servo-driven canard kit?"** *(the "it's not really an actuation assembly" challenge)*
*Wins:* "Because a servo cannot survive 15,000 g and a spinning airframe — and because a battery is the least reliable item in a fuze. The ring *is* the actuation assembly: 2-D force vectoring from a single rotation axis with no moving control surface and no gearbox. **Flight power is self-generated — the alternator supplies the kit in flight, so no battery is required for flight; a reserve battery covers pre-launch and the safe state only.** The machine that aims the ring is the same machine that generates the kit's power." **Note (2026-09-19): say "no battery is required for flight", not "no in-flight battery" and never battery-free parity — the fielded M1156 is documented as having *no battery at all*, while our design carries a reserve cell. The distinction is the point of honour here.**
*Edit:* slide 2's canard diagram is already the best asset we have. Make it bigger and label the two torques.

**Q7. "What stops the ring rotating forever?"**
*Invites:* hand-waving about control.
*Wins:* a torque balance with numbers — aerodynamic torque from the control pair 0.17–2.12 N·m across the flight, friction budget ≤ 0.10 N·m flat, an alternator reaction torque as the control input, and a hard feasibility gate at 0.157 N·m above which the control-pair sizing window closes entirely.
*Edit:* the gate number belongs on slide 4. It is the most "this team actually did the work" number in the pack.

**Q8. "What is the canard authority? Show me."**
*Wins:* ≥ 18.1 N minimum over the guided window; 450 m of terminal correction available against 407 m required — a **1.11:1 margin, stated as thin**. Plus: "a cheaper design would have quoted the mid-flight band and hidden the margin. Ours is bounded by the minimum."
*Edit:* state the margin as thin on the slide. Thin-and-known reads as engineering; 3:1 reads as fiction.

**Q9. "Your canards are permanently exposed. What happens in the bore?"**
*Wins:* "Nothing deploys, so nothing can deploy wrongly. In-bore safety becomes a static clearance question rather than a mechanism-safety argument: a 2 mm per side clearance budget caps the canard tips at Ø151 mm inside a 155 mm bore. This also matches the fielded PGK's four fixed external canards." **[fact — the M1156 is fielded with exposed canards]**
*Edit:* already excellent, and it is a *simplification win*. Lead with it — judges reward removing a failure mode.

**Q10. "Where is the CAD?"**
*Why:* it is a named PS deliverable and a screening evaluator checks the deliverable list.
*Invites:* our current answer is "new work, not yet done". That is the honest answer and it is a scoreable zero.
*Wins:* an assembly section view with the ring, bearings, stator, magnets, dump stage and fuze train, dimensioned against the fuze-well envelope — even without FEA.
*Edit:* **highest-value artifact after the simulation.** See §7, move 2.

### 4.3 Navigation under spin

**Q11. "Everything on the shell is rotating at 15,000 rpm. How do you navigate?"**
*Wins:* the two-part answer we already own — the IMU rides the **de-spun ring** so it sees coning motion instead of 1,107–1,912 rad/s of spin, and the ring's own angle is measured relative to the body by pickoff and absolutely by magnetometer.
*Edit:* keep. This is our strongest architectural argument and it is unique in the field.

**Q12. "Your GNSS antenna is rotating at 300 Hz. How does it track?"**
*Wins:* "It does not have to. A rotationally symmetric aperture on the spin axis with elements combined rather than switched is pattern-invariant under rotation, so there is no 176–304 Hz modulation to track out. The alternative — putting the aperture on the ring — is refuted by our own architecture, because the ring angle is the guidance command channel."
*Edit:* this refutation-of-our-own-alternative is a maturity signal. Keep it visible.

**Q13. "What about GPS jamming?"**
*Wins:* "Primary answer is anti-jam GNSS with INS coasting in the same envelope and cost class as the fielded counterpart; the seeker is secondary and bounded. With GNSS degraded, correction accuracy degrades smoothly to the inertial drift limit rather than failing." Plus the honest negative: unaided, 0.1° of attitude error mis-resolving a 5 g drag is ≈110 m over 50 s — so outage tolerance is a bounded requirement.
*Edit:* keep the honest negative. It pre-empts Q14.

**Q14. "You have a magnetometer sitting next to a kilowatt alternator. Be serious."**
*Why:* this is the question a domain judge most expects to break us.
*Wins:* "The interference is at 1,234–2,131 Hz — seven pole pairs times the measured relative rotation — and it is removed by a coherent notch locked to that measured frequency, with the current-proportional part compensated against measured coil current. Both signals already exist for the control limit laws, so coexistence costs no new hardware. And the honest negative: shielding cannot help a magnetometer, because the interference and the Earth's field share both band and space — so it must be calibrated in flight."
*Edit:* this is the best technical paragraph in our pack. It belongs on slide 3, not in a register.

### 4.4 Fuze

**Q15. "You have three modes. Our RFI is three separate fuze types. Are you one product or three?"** *(J4's question)*
*Wins:* "One unit covers electronic percussion, proximity and time — the three categories in the Army's own fuze RFI. That is one stock line instead of three, one setter procedure, and no change to the gun line." **[fact — the RFI categories are exactly these three]**
*Edit:* add to slide 5. It is the single most India-relevant sentence in the pack and it is currently missing.

**Q16. "How does the fuze arm?"**
*Wins:* "Out-of-line rotor to MIL-STD-1316, released only by two independent environment stimuli — setback and spin — with the electronics' arm command as a third independent condition. The rotor cannot complete travel while setback is sustained, so no in-bore function is possible by construction rather than by timer. A misfire leaves the fuze safe, and dead electronics give a dud, never a premature burst."
*Edit:* already strong. Keep verbatim.

**Q17. "Dud rate?"** *(the gap)*
*Invites:* nothing in our pack.
*Wins:* a defensible figure with its basis, plus the design features that bound it: independent impact switch (so it functions without electronics), the fallback to a pre-set time, and the fact that loss of guidance degrades accuracy but never liveness.
*Edit:* **add a dud line.** A fuze judge will notice its absence in a way they will not notice its imprecision.

**Q18. "HERO — hazards of electromagnetic radiation to ordnance. You are putting a kilowatt-class switching machine in the same body as an electro-explosive device."** *(the gap)*
*Invites:* nothing.
*Wins:* a stated hazard assessment — fireset reservoir isolated and charged only under the arming interlock; setter and proximity channel frequency planning and partitioning; the arming command required as a third independent condition; and a named verification item on the rig.
*Edit:* **add two lines to slide 3 or 4.** This is the most likely question to expose a real gap.

**Q19. "Why 24 GHz and not laser or IR?"**
*Wins:* "RF Doppler is standard for artillery, is robust in weather and obscurants, and puts no optical window on the kit — so there is no line of sight to foul, obscure or heat. A laser or IR window on a shell nose is a thermal and contamination problem for no gain."
*Edit:* keep. It also implicitly dismisses C6's seeker window idea.

**Q20. "The time setting is written before firing. A guided round's flight time is not the one in the firing table. Now what?"**
*Wins:* "The time setting is re-synchronised in flight from the navigation solution, so the airburst follows the guided round's actual time of flight. The fuze stays autonomous: the correction interface is one-way and bounded, and with no correction it falls back to its pre-set time."
*Edit:* this is a genuinely novel detail and it should be on slide 2 with a different colour. It is the one fuze-side thing nobody else will say.

### 4.5 Power, thermal and mass — our hardest territory, and our best ammunition

**Q21. "A guidance kit with a kilowatt thermal load. Why?"**
*Wins:* "Because the architecture is the low-cost one. Holding the ring against aerodynamic torque at full spin absorbs 2.92 kW peak and about 121 kJ per flight. That is the price of having no servo and no gearbox. A servo-actuated kit has no such load and costs more; this is the trade and we state it." **Note (2026-09-19): quote the reference speed with the figure.** The register's own duty table carries a 2.36 N·m hold torque, which at the launch spin of 1 623 rad/s gives a higher figure than 2.92 kW (register risk 46), so the two must be reconciled before this number is defended — and it is the number the fuze-well thermal interface is sized on, so a reviewer who checks the arithmetic will find the discrepancy.
*Edit:* this answer converts our biggest liability into evidence of rigour. Put a one-line version on slide 3 and the full version on slide 4.

**Q22. "Where does 121 kJ go?"**
*Wins:* "Not into storage — that would be about 1.5 F at 400 V, and about 7.5 F at the 180 V nominal bus we actually adopted, so it is excluded either way. Not into the kit's own metal — that is a 134–179 K rise. Only about 26 % reaches the airstream. So it leaves through the shell: a resistive dump stage conduction-coupled to the fuze-well threads, where 121 kJ raises 45 kg of steel by 5.8 K in the long-time limit." **Note (2026-09-19): the capacitance figure is bus-dependent — quote the 180 V one, since the bus is now H8/H12's ≈150–200 V, 180 V nominal. The argument gets stronger at the lower bus, not weaker.**
*Edit:* slide 4. This is the most impressive physics in the submission and it is currently one line in an abstract.

**Q23. "So you are heating my shell and my charge."**
*Wins:* "We sized it. 5.8 K is the asymptote; the flight-time participating mass is the kit plus the shell nose, about 6–8 kg → 25–35 K, because the thermal penetration depth in steel over 90 s is only 30–65 mm. And we checked the coupling you are about to ask about — the bare 2″-12 UNS thread conducts about 3–16 W/K against a ≥ 58 W/K peak requirement, so the interface is *designed*, not assumed: the well bore is used as a contacting radial path at roughly 17× the flank area, the flanks and seat are ground with the torque spec becoming a thermal requirement, and the peak is buffered by the kit's own metal while the interface is sized on the 90 s average."
*Edit:* this is the single best "we found the hard problem ourselves" passage we own. It should be visible on slide 4 in three lines, with the 3–16 W/K figure *shown*.

**Q24. "Why should I care about a thermal interface? Design your own heat path."**
*Wins:* "The conductance belongs to the platform's thread geometry, not the kit. A supplier specifies it and designs its own side of the joint. Measuring it is a rig item. And the cheapest lever is area, not surface finish — the flank path scales with engaged thread length, so a well cut to full cavity depth multiplies it several-fold at no mass or volume cost. That is why our re-baseline asks for thread engagement and torque spec as design variables rather than reading them off."
*Edit:* keep. It reframes a gap as a specification, which is what a supplier does.

**Q25. "Your kit is 1.4–1.7 kg. The fielded kit is 1.4 kg and only 0.45 kg heavier than the fuze it replaces. Your net penalty is more than twice theirs."**
*Why:* the M1156 weighs 3 lb / 1.4 kg, 1 lb / 0.45 kg more than a standard fuze — so total mass is comparable to ours (1.0–1.21×) but our net penalty is 1.55–2.2× theirs. **Both ratios must be given; quoting only the flattering one is how a mass question becomes a credibility question.**
*Wins:* "Total mass is 1.0–1.21× the fielded kit; the net penalty over the fuze it replaces is 1.55–2.2×, and it is stated as such rather than hidden: about +0.7–1.0 kg, 1.6–2.2 % of the projectile, CG shift 6–8 mm forward, about 0.8 % of length. That sits inside the platform's own 0.55–0.62 L CG envelope spread. Mass forward reduces the CP–CG separation, which should raise the stability margin — a direction we are confirming rather than assuming. The axial-flux trade and make-versus-buy are the open levers."
*Edit:* never quote the mass without the envelope comparison in the same breath.

**Q26. "What is your gyroscopic stability margin?"**
*Wins:* "Sg 1.37–3.55 across the declared envelope, design point 1.83. The conservative corner clears the customary 1.3 floor by 5 %, and that 5 % *is* the canard allowance — a derived requirement that the canards raise the pitching-moment derivative by no more than 5 % at that corner. Two useful results: the ring and canards add 5.4 % to axial inertia which raises Sg by about 11 %, partly offsetting their own destabilising effect; and because spin comes from the rifling twist, muzzle stability is charge-independent."
*Edit:* slide 4. The "that 5 % is the canard allowance" line is a design-synthesis statement, and design synthesis is what separates this deck from every other one.

### 4.6 Cost, manufacturing and programme

**Q27. "₹6.5 lakh. Where does that number come from?"**
*Invites:* a benchmark with a subtraction.
*Wins:* "It is the fielded price minus 40 % — the US M1156 at US$13,541 in FY2013 dollars, against a 2026 production award of US$863 M for the class — and it is *underwritten* by the architecture: one moving assembly, no actuators, no gearboxes, flight power self-generated, fuze and guidance sharing processor, power and housing, and no re-qualification of the shell. The bill of materials is ranked by driver, with make-versus-buy and an axial-flux option as the levers if it does not close." **Note (2026-09-19): state the volume gap in the same breath** — the fielded programme has produced over 100,000 units and we assume 5,000/year, so the assumption needs its basis given rather than left for the panel to notice. SIH also weights business potential, so the cost answer and slide 5 should both read as a business case.
*Edit:* **the weak link is the phrase "the fielded price minus 40 %".** A costing judge reads that as "we chose a number". Show the ranked driver list, even as three bars: bearings, magnet/winding, electronics.

**Q28. "What is your production yield on the bearing and air-gap assembly?"**
*Invites:* nothing. *This is J1's territory.*
*Wins:* a stated assembly concept — bearing pair preloaded on a fixture, air gap set at 0.40 mm with a 0.20 mm maximum deflection allowance at 15,000 g, and the launch load routed *around* the flight bearings through a dedicated structural path so the bearings never see the 73.5 kN setback. **Now CAD-backed (2026-09-20): the interface is modelled and verified — 124.70 mm intrusion, zero interference with the reference shell, and the seat annulus that lands the kit reproduces P6's own area to 1.3 %.** Quote the numbers when the question comes: they convert a claim into a verification.
*Edit:* the "we route the launch load around the bearings" line is a manufacturability *and* a survivability answer. Put it on slide 4 — the deck now carries the CAD verification line directly beneath the figures, and the two open CAD findings (mass; train-bore slot depth) in "what we cannot claim yet".

**Q29. "Where do the magnets come from?"** *(the question Indian defence judges are now trained to ask)*
*Invites:* "domestic supply chain" without names.
*Wins:* an explicit strategic-materials position — grade and mass of rare-earth magnet, the fact that heavy-rare-earth supply is the strategic risk, and the mitigation (a ferrite or a lower-energy-density machine as the fallback, at a stated mass or authority penalty). **[predicted — this will become a standard Indian defence-PSU question]**
*Edit:* one line on slide 5. It shows you are bidding to an Indian supply chain, not a datasheet.

**Q30. "Is your GNSS receiver ITAR-free / export-controlled?"**
*Wins:* a stated position on receiver and IMU sourcing with an anti-jam path, plus the honest note that the IMU is a tactical/industrial MEMS and the nav line closes on GNSS availability rather than on inertial grade.
*Edit:* one line. Do not name a vendor you cannot commit to; name the *class* and the constraint.

**Q31. "What is the TRL and the timeline?"**
*Invites:* nothing.
*Wins:* "TRL 2–3 today: architecture and derived budgets, no hardware. The path is simulation → bench rig → integration demonstrator, with the rig specified now and built if shortlisted. The rig is the transition from analysis to evidence."
*Edit:* **add a three-line roadmap to slide 5.** Evaluators reward a bounded plan more than an implied capability.

### 4.7 The four questions nobody prepares for

**Q32. "How much of this did AI write?"**
*Wins:* a plain, quantified answer naming what AI did (literature synthesis, drafting, arithmetic checking) and what it did not (the derivation chain, the trade decisions, the declared verifications). Never "we wrote everything".
*Edit:* rehearse. See §5.5.

**Q33. "Twelve other teams picked this statement. Why yours?"**
*Wins:* **one** thing, not a list: "We are the only entry that found the architecture's own hardest problem and answered it — 121 kJ through the fuze-well threads, with the bare-thread conductance measured and the closing route stated. Every other deck will claim 30 m. We are the one that shows what 30 m costs."
*Edit:* this is the sentence to end the pitch on.

**Q34. "What have you not solved?"**
*Wins:* the five declared open verifications, named: friction flatness at flight speed, the fuze-well thermal interface conductance, coexistence and spin modulation at speed, the ring–body power/data interface and the buffer's launch survival, and everything parametric re-baselining when YIL releases the shell drawing.
*Edit:* already in the pack. Promote to slide 4 as three bullets with mitigations.

**Q35. "What did you get wrong and change?"**
*Wins:* two real pivots from our own record — (i) the reference bench rig ran body spin 21.6× slower than flight, which *hid* the kilowatt energy load, so we re-sized the machine as a loaded generator; and (ii) we initially carried the GNSS aperture on the ring and dropped it, because the ring angle is the guidance command channel.
*Edit:* add a "two things we got wrong" line to slide 3. It is the most credible 20 words available to us.

**Q36. "How would this be sabotaged or fail in the field?"**
*Wins:* GNSS denial (handled by coasting, stated limit), bearing contamination (the friction budget is the feasibility gate, so contamination control is a design item), and the thermal interface on a poorly machined well (which is why it is a declared specification rather than an assumption).
*Edit:* the friction-budget answer is strong; say the words "the friction budget is a feasibility gate, not a preference".

**Q37. "Who owns this after the hackathon?"**
*Wins:* the PS owner does — this is a supplier kit for YIL, and the module boundaries are the handover interface. Plus the growth module is bounded and out of the baseline.
*Edit:* one line on slide 5.

**Q38. "Scale of impact — give me a number, not an adjective."**
*Wins:* "240 m CEP → 30 m is roughly an order of magnitude fewer rounds per point target: from a volume-fire solution of the order of 264 rounds to about 4, on our derived figures, for a 90 % defeat probability at a 30 m effective radius." **[ours, M8]**
*Edit:* the rounds-per-target comparison is the strongest impact visual we have. It should be the *first* thing on slide 5, not the last.

---

### 4.8 The manufacturing claims — validated, and how the room will take them

**Added 2026-09-20, after the advanced-manufacturing pass.** The question being answered here: *are the digital-cell, post-treatment, printed-electronics and modularity claims true, can they be defended, and do they help?*

**The verdict in one line.** The manufacturing story survives scrutiny **only in its bounded form**. The version that wins is — *conventional production for the volume parts, plus a bounded digital cell for the complex low-volume and electronics-bearing parts, plus a qualification route that is named and followed*. The version that loses is *"we will 3D-print the kit"*, which is the most common filler claim in a student deck and reads as exactly that to J1 and J6.

**What changed the assessment — the precedent found in this pass.** AM for munitions is not a novelty play in 2026; it is funded policy:

- **US Army ARL's SAMM programme** — *Science of Additive Manufacturing for Next Generation Munitions* — prints custom munitions and tailored alloys (J35).
- **The Army's own statement** that AM can improve *"munitions, electronic sensors and fuzes"*, plus a standing AM facility at Picatinny's Armaments Center (J36).
- **DoDI 5000.93**, *Use of Additive Manufacturing in the DoD* — there is an instruction for this (J37).
- **ASTM with the UK MoD (Project TAMPA)** — a **criticality-based certification guide** for AM parts in defence (J38). This is the qualification framework to quote; NASA-STD-6030 alone is a spaceflight reference and a sharp J3 will notice the mismatch.
- **DTIC AD1023960** — printed **conformal structural supports for circuit boards, demonstrated as viable for high-G survivability in gun-launch applications** (J39). This is the single most valuable find: it upgrades "printed structure carrying electronics through launch" from *our proposal* to *a demonstrated principle with project-specific qualification owed*.

**Claim-by-claim validation.**

| Claim as it stands | Technically possible? | Who reacts, and how | Verdict |
|---|---|---|---|
| **Digital cell: print → post-treat → assemble** as the route for complex low-volume parts | **Yes** — robot deposition+machining cells are industrial practice (J30); munitions AM is funded US Army work (J35) | **J1** asks *"which parts come off my existing line, and what do I have to buy?"* — a cell answers his question only if the boundary is stated. **J6** flags "3D printing" as generated filler | **Keep, bounded.** Name what stays conventional — windings, stator core, magnets, bearings, standard electronics — and name the cell as a bounded addition whose capex is a K5 line item |
| **Post-treatment chain** (HIP, heat treatment, critical-feature machining, finishing, vapour smoothing) | **Yes** — each step is standard practice; HIP's strength cost is published and stated (J24/J25) | **J1/J3** hear this as the difference between a manufacturing plan and a slogan | **Keep — and lead with it.** It is the claim that proves the team knows what printing *costs*, not just what it enables |
| **Qualification shape**: process control, coupons, testing, traceability | **Yes**; the defence-specific route exists (J37, J38) | **J2/J3**: *"is a printed part legal in a gun-launched fuze?"* | **Keep, and cite the defence framework** (ASTM/MoD TAMPA, DoDI 5000.93), with the boundary attached: printed parts are **non-primary structure and electronics carriers**; the primary launch path stays conventional |
| **Printed structural electronics** — components placed mid-build, conductors printed to them | **Yes — and demonstrated for gun launch** (J39) | **J2** is the risk (a printed board inside a fuze); **J5** rewards the declared residual | **Keep and strengthen with J39.** Principle demonstrated; project-specific qualification owed (risk 50) |
| **Tooling-free first articles de-risk the P6 re-baseline** | **Only for the printed subset** — the stator core, windings, magnets and bearings still carry tooling | **J3** will catch the unqualified version, because we ourselves say the primary processes are conventional | **Fix the wording everywhere**: "the *printed* parts re-iterate without tooling; the conventional parts keep their dies, which is what the two-tier split is for" |
| **Modular sensor stack with targeted redundancy** (~5–15 g, <0.5 W) | **Yes** — plausible mass and power; volume-neutral only inside the annular stack (H5) | **J3** asks *"why not spend that mass on canard authority?"*; **J1** asks what it costs | **Keep**, justified by failure effect: attitude/heading and ring angle are single-point today, and the cost is ~1 % of the mass budget |
| **Cell throughput ≈2–5 machines** | **Plausible arithmetic with stated assumptions** | **J1** asks the capital question — this is his territory, so get it right | **Keep**, name the machine class, and state that capex is priced at K5. **Do not quote a machine price** — we have no rated source for one |
| **"Fewer people" / lights-out framing** | It is a *choice*, not a claim | **PSU audience**: this is a labour question before it is a technology question, and a cell can read as a threat to the works | **Reframe**: automation for **repeatability and small-batch economics** — never as headcount reduction. The deck's word is "automated placement", not "unmanned" |
| **Printing the ring/retention carrier** | Yes for a **structural** carrier — **but not the magnetic backiron**: printed Fe-Si is research-grade and carries a loss penalty (J23) | **J3** will ask the magnetic question, and a wrong answer here is a visible domain miss | **State the split**: the carrier and retention geometry print; the **backiron stays laminated or compacted magnetic material**. One clause, and it closes the catch |

**Three questions to rehearse.**

**Q39. "Which of these parts comes off my existing line, and what do I have to buy?"**
*Invites:* a list, or worse, an admission that the whole kit moves.
*Wins:* "Almost everything. The stator core is stamped or compacted, the winding is needle-wound, the magnets are bought to grade and retained mechanically, the bearings are catalogue thin-section parts, and the electronics are standard boards. What the cell adds is bounded: the ring and retention carrier geometry, the fuze mechanism parts, the printed structures that carry the electronics, and the first articles. The cell's capital is one line in the cost case, and its first job is the parts that change — not the parts that don't."
*Edit:* this answer is why the two-tier split exists in the deck. Keep the two-tier bullet ahead of the cell bullet.

**Q40. "Is a printed part acceptable in a gun-launched fuze?"**
*Invites:* "3D printing is the future."
*Wins:* "Not by assertion — by qualification. Printed parts sit in the load path only where the load is not primary, every printed part is HIP'd, heat-treated and machined at its critical features, and the certification route is the defence one, not the spaceflight one: DoDI 5000.93's policy and the ASTM/UK-MoD criticality-based guide. The principle of printed structure carrying electronics through launch is already demonstrated — that is a DTIC result, not our idea — and what we owe is the project-specific qualification, which is risk 50 on our own list."
*Edit:* this is J2's question wearing J1's clothes. Rehearse it word-for-word.

**Q41. "Why does a 5,000-a-year kit need a factory of the future?"**
*Invites:* enthusiasm.
*Wins:* "It doesn't *need* one — it needs a production route that doesn't charge it for tooling it will outgrow. Five thousand a year is two orders below the fielded programme, our geometry changes the moment your drawing arrives, and YIL is already taking custom hardware work. A cell makes those changes file-level; it also happens to be how the electronics-carrier parts are best made. If the cell is not justified at P4, the kit still builds — on the conventional tier."
*Edit:* the last sentence is what makes the answer credible. Never let the cell sound load-bearing for the programme.

**Does it help the score?** Yes, with two conditions. It helps because it answers **J1's own killer question** — what winds it, what it costs, what is bought — in the form he wants (a process plan, not a materials statement), and because it lands on YIL's own direction toward custom and short-run hardware (J40). And it adds a **third genuine differentiator** alongside the thermal interface and the ring-as-inertial-platform: the only manufacturing answer in the field that is priced against *this* volume. The conditions: it must never displace the six proof numbers (§5.1), and every claim must keep its bound — the four bounds in `design/06-manufacturing-and-process.md` §7.5 are what make it survivable, and dropping them to sound more capable would hand J3 the room.

---

## 5. What an AI evaluator sees in our submission

Assume the organiser runs an LLM first pass, or uses assistive screening. Here is what it would return on our material, with severity and fix.

### 5.1 The structural problem: our best content is not in the artifact being scored

**[ours]** The register holds 297 KB and 191 criteria. The draft holds 43 KB. The two files the portal actually receives — the form content (3,491-character abstract, 34,769-character description) and the six-slide template — already drop most of it.

An LLM scoring the six slides sees a deck that describes a philosophy. It does not see the torque gate, the thermal interface, the nav budget, or the declared verifications, because those live in §3–§6 of a different file. **Fix: the deck must carry the six numbers that prove work was done — CEP 23.9, authority 1.11:1, friction gate 0.157 N·m, energy 121 kJ, interface 3–16 vs 58 W/K, cost ₹6.5 L.**

### 5.2 Coverage scoring is mechanical, and we can max it

If the screen degrades to coverage (likely, because the model refuses the design content **[fact]**), then each PS bullet must appear in our slide text in the PS's own vocabulary: *canard actuation assembly, GNC, proximity mode, time mode, impact mode, embedded electronics, real-time flight control, power management, high-g launch, communication and programming interface, CEP 30 m, compatibility with existing 155 mm, high reliability and safety, modular.*

**Fix: a coverage audit.** Every one of those phrases should appear at least once, spelled the same way, on the deck. Cost: twenty minutes. Value: if the screen is mechanical, this is the whole screen.

### 5.3 AI-tell audit — what makes our prose look generated

The evaluator is not detecting "AI" as such; it is detecting **low information density and unearned confidence**. Our register prose scores high on density but carries tells:

| Tell | Where it lives | Fix |
|---|---|---|
| Bracketed criterion codes `[G4]`, `[C42]`, `risk 33` | Everywhere in the draft | **Strip from anything submitted.** A screener reads them as unresolved references or editor notes, and it screams "this text was assembled from another document" |
| Internal vocabulary: DERIVED, PARAMETRIC, "the register", "P6 re-baseline", "the track" | Draft, form content | Replace with plain language or delete |
| Em-dash-heavy, clause-stacked sentences | Whole pack | Split. Aim for one clause per claim on the slides |
| "It is not X, it is Y" and tricolon constructions | Abstract, slides | Keep at most one, for emphasis |
| Hedging stacks: "broadly", "of the order of", "class" | Throughout | Give the number and the condition, or delete the claim |
| Second-person/meta commentary: "the honest version", "worth more than leaving it out", "say this on the deck" | Draft | **Never ships.** This is instruction to the writer, not content |

**The test:** read any sentence on a slide and ask whether a screener could *check* it. If not, it is either a claim to be cut or a number to be given.

### 5.4 Novelty/duplication screening

The screen may compare our deck against the other submissions and against the public web. Two exposures:

1. **The Günay thesis is public and its text is extracted into our workspace.** If any deck phrasing traces to it, a similarity flag is possible. **Fix: no verbatim sentences from `01-thesis-full-text-extracted.txt` in the submission.** Our value is the extension, not the transcription.
2. **Three of our novelty bullets match the public literature** (§6). A novelty screen that queries the web will find the patent and the papers. **Fix: restate the novelty claims in integration terms that are true and checkable.**

### 5.5 The AI-disclosure answer

**[fact]** 2026 evaluators ask this explicitly, and the documented trap answer is denial. Prepare one sentence per team member, and one on the slide if the format allows:

> "AI did our literature synthesis and our drafting. The derivation chain — the torque gate, the energy path, the stability margins, the Monte Carlo design — is ours, and every number on this slide traces to a line we computed. We have also listed what we have not verified, because that list is the part an AI will not produce for you."

That last clause is the winning move: **the declared-open-verifications list is itself the proof of human authorship.** No text generator volunteers a list of what it has not measured.

### 5.6 Hallucination-flag audit — claims that read as invented

An evaluator or an AI assesses each number for a visible basis. Current exposures:

| Claim | Why it flags | Fix |
|---|---|---|
| "≤ ₹6.5 lakh = fielded price minus 40 %" | Percentage-of-a-benchmark with no build-up | Add three ranked cost drivers or delete the derivation and keep the target |
| "≈10,000 flights, ±2.0 % at 95 %" | Sounds precise; is a *plan*, not a result | Say "planned campaign" in the same breath — the draft does; the slides must |
| "1.4–1.7 kg", "0.81–0.97 kg" | Two ranges that do not obviously nest | Show the rollup once, on slide 4 |
| "≈59 m correctable, 348 m on GNSS/INS" | Non-obvious | Fine — it is derived and refutable, which is exactly right |
| "Sg 1.37–3.55" | Wide band; reads as uncertainty | Say "across the declared charge and temperature envelope" — it is a strength when framed as an envelope |
| "≈2–5 printing machines" / cell throughput *(added 2026-09-20)* | Derived arithmetic; without its chain it reads as an invented figure | Carry the chain in the same breath: 0.3–0.5 kg printed metal per kit → 1.5–2.5 t/yr → 200–400 g/h per machine over two shifts. Assumptions stated, or the number is dropped |
| "Printed supports for electronics survive gun launch" *(added 2026-09-20)* | It is our strongest manufacturing sentence and it sounds invented | **Cite the demonstrated result** — DTIC AD1023960: printed conformal structural supports shown viable for high-G survivability in gun-launch applications. Then state the honest residual: principle demonstrated, project-specific qualification owed |
| "Tooling-free production" *(added 2026-09-20)* | Overbroad — four of our own processes carry tooling | Say **"tooling-free for the printed subset"**. The two-tier split exists precisely because this is true only of a subset |

**Rule: one number, one condition, one source, in the same sentence.** That single rule removes most hallucination warnings.

---

## 6. The novelty ledger — claim by claim, against real prior art

This is the most important section in the file. Our current pack makes five novelty claims. Three have direct prior art, and **two of those prior-art items are on our own references slide.** A domain judge who reads slide 2 and slide 6 together catches it immediately.

| Our claim | Closest prior art | Honest position | How to state it |
|---|---|---|---|
| "Actuation and power generation by a single machine… removing all control actuators and the in-flight battery" | **Günay, METU 2022** — the de-spun ring with the alternator as actuator *is* the thesis's contribution, and it is our reference #1. Also **US Patent 6,981,672**. | **Not ours.** It is a validated published concept. | "We adopt the de-spun ring with an alternator-as-actuator — validated on hardware in the literature — and we are, to our knowledge, the first to size it as a *loaded generator* in a flight-representative envelope, which reveals the kilowatt energy path nobody has published." |
| "Full two-dimensional guidance from one actuation axis… no control surface moves" | **US Patent 6,981,672** (Clancy/Bybee/Friedrich), *Fixed canard 2-D guidance of artillery projectiles* — our reference #5. Also the whole Chinese dual-spin fixed-canard corpus. | **Not ours.** This is the canonical fixed-canard 2-D geometry. | Drop as a novelty claim. Keep as a *design description* on slide 2, which is where it belongs and where it is genuinely clear. |
| "Impact-point-prediction guidance law synthesised for a control channel whose authority varies by more than an order of magnitude…" | **Zhang, Yao & Zheng 2019**, *Impact point prediction guidance based on iterative process for dual-spin projectile with fixed canards* — our reference #2. | **The law is not ours.** Our draft's sentence "the reference work for this airframe does not contain [a guidance law] — our clearest novel contribution" is **self-contradictory against our own reference list** and is the single most damaging line in the submission. | Reframe: "The IPP law exists in the literature for this airframe. What is absent from it is the *authority gate*: the reference work loses control between t = 30 s and 50 s using fixed limits. Our contribution is the state-dependent limit — `I_lim = min(2·Î_dist, I_avail(ω_rel))` — synthesised against a *measured* torque envelope, which turns authority loss from a failure mode into a designed constraint." |
| "The de-spun ring used as the inertial sensing platform" | The thesis flags in-flight ring-angle feedback as its own largest open problem; Zhang et al. used a gyro, Yin et al. geomagnetic + Hall. **[fact]** | **Genuinely ours as an architecture.** | "The reference work names in-flight ring-angle feedback as its largest unresolved problem. Our answer is architectural: put the IMU on the ring, remove 1,107–1,912 rad/s of spin from the measurement, and measure the ring itself relatively by pickoff and absolutely by magnetometer — using signals the limit laws already require, so it costs no new hardware." |
| "A three-mode electronic fuze integrated into the same nose assembly… configured over the existing inductive setter" | Fielded PGKs offer PD + proximity only; SPACIDO is 1-D range correction; the Indian Army's RFI lists the three fuze categories separately. **[fact]** | **Genuinely ours as a product configuration**, and India-relevant. | "The fielded competitor's fuze offers point-detonate and proximity. This kit carries proximity, time and impact in one unit — the three categories the Army's own electronic-fuze RFI lists separately — with the time setting re-synchronised in flight so a guided round's airburst follows its actual trajectory. One stock line where there are three." |
| *(Not currently claimed — claim it)* The **thermal interface** as a declared, sized requirement: 121 kJ through the fuze well, bare-thread conductance 3–16 W/K against ≥ 58 W/K, and the closing route | Nothing published. This falls out of running the machine at flight-representative speed rather than 21.6× slower. | **Genuinely ours, and the strongest single differentiator.** | "The reference bench rig ran body spin 21.6× below flight, which hid the energy. At flight speed the machine is a 2.92 kW / 121 kJ loaded generator, and the energy leaves through the shell. The bare 2″-12 UNS thread conducts ≈3–16 W/K against a ≥ 58 W/K peak. This is the architecture's defining cost, and it is the one number no other entry in this field will have." |
| *Added 2026-09-20* — **the digital cell**: printed structure with embedded electronics, post-treatment chain, tooling-free first articles, on-demand variants | **Industrial practice with funded defence research**: robot deposition/machining cells (J30), US Army SAMM for munitions (J35), DoDI 5000.93 (J37), ASTM/UK-MoD criticality-based certification (J38) | **Not ours as a technology, and must be credited as such.** What is ours is the *reasoning and the arithmetic*: the two-tier split priced at 5,000/yr, the tooling-free-first-article argument for the P6 re-baseline, and the modular/redundant sensor stack the capability makes affordable | "Additive manufacturing is established in our industry — the US Army funds it for munitions and there is a DoD instruction governing its use. Our contribution is the reasoning: conventional processes where volume wins, printed where complexity and low volume win, a named certification route, and a design — the modular, targeted-redundant sensor stack — that the capability is what makes affordable." |

**The reframe, in one sentence, for slide 2:** *we did not invent the de-spun ring, the fixed-canard geometry or the IPP law. We are the first to integrate them into a fuze-well-only kit, to size the machine as a flight-representative loaded generator, and to find and answer the energy problem that falls out.*

**Why this wins rather than loses:** the screening evaluator is checking for overclaiming, and the finale judge is checking for depth. Narrow, defensible novelty with two genuinely new results beats five claims that a specialist can dismantle — and the two new results we keep (the ring-as-inertial-platform architecture and the thermal interface) are exactly the kind of content no competitor will have.

---

## 7. The seven moves

Ordered by score-per-rupee-of-effort. Moves 1–3 close named PS deliverables.

**1. Ship the trajectory-correction simulation.** *PS deliverable #5, and the only artifact that evidences the CEP claim.*
Even with a declared aerodynamic set: unguided dispersion cloud vs guided cloud, Monte Carlo CEP with a confidence interval, and a time-history showing the ring-angle command and the authority gate. Label the aero source honestly and mark it as the item that re-baselines. **A run with a stated model beats a budget with a better model.** This is what C1 and C5 will have and we will not.

**2. Ship the CAA CAD.** *PS deliverable #2.*
An assembly section view, dimensioned against the ≤124.7 mm intrusion / ≤95.25 mm above-seat envelope, showing ring, bearing pair, stator, magnets, launch load path around the bearings, dump stage, and the fuze train. Clash-check at rotor phases if the earlier CAD workspace's conventions are reusable. Even without FEA, this answers J1's manufacturing question visually and satisfies the deliverable list.
**Status 2026-09-20 — partially shipped and working for us.** The in-repo CAD workspace (`design/cad/`) has built and gate-passed **Phases 0–2** (envelope, A1 kit body, ring and machine), and three verified interface facts are now on deck slide 4: **124.70 mm intrusion, zero interference with the reference shell, seat annulus matching the register's own area to 1.3 %**. The model has also produced **four findings** (`design/07-cad-evidence.md`) — two of them (the train-bore slot-depth cost and the body mass against P9) are stated on the deck as open reconciliation items rather than hidden. Remaining phases: fuze train, dump, buffer, electronics annulus, the thermal joint, then the structural case under the launch load. **The deck's slide-2 schematic stays the labelled architecture drawing; the CAD is the evidence behind it.**

**3. Ship the electronics block diagram.** *PS deliverable #3.*
Dual-core split (control core / navigation core), IMU and magnetometer on the ring with the rotating interface, GNSS with the spin-invariant aperture, barometric channel, alternator rectifier → controlled current sink → dump, supercapacitor buffer with the fireset reservoir isolated, arming interlocks, inductive setter, and the fireset. One page. It is also the artifact that proves the "embedded electronics and software" PS bullet is answered.

**4. Rewrite the deck in judge language.**
Strip criterion codes and register vocabulary. One number per claim with its condition. Six numbers carry the proof of work: **CEP 23.9 m · authority 1.11:1 · friction gate 0.157 N·m · 2.92 kW / 121 kJ · 3–16 vs ≥ 58 W/K · ₹6.5 L**. Keep the deliberate honesty, but make it three bullets with mitigations rather than a paragraph.

**5. Add the comparison table.** *(pre-empts Q4 and Q33)*
M1156 · IAI TopGun · Elbit Silver Bullet II · SPACIDO · **this kit** — over: guidance dimension, actuation, fuze modes, GNSS dependence, unit cost, and the gap each leaves. Two columns of that table are the whole differentiation argument, and one of them is "1-D range correction only" for the sleeper.

**6. Add the India layer.**
Three lines: the Army's electronic-fuze RFI categories map 1:1 onto our three modes; the source of the strategic materials in the machine and the fallback; and the indigenous-content and no-re-qualification position. **[fact — the RFI exists and matches; the magnet sourcing item is prediction but is the kind of question Indian defence evaluators now ask]**

**7. Fix the novelty framing (§6) and prepare the AI-disclosure answer (§5.5).**
Both are editing tasks. Both are the difference between a defensible submission and one caught overclaiming.

---

## 8. Edit list — what to change, in the three submission files

### 8.1 `SIH26098-template-slides.md` (the artifact that is actually scored)

| Slide | Change |
|---|---|
| 1 | Copy ID, title, theme and category character-for-character off the portal. **Resolve the Smart Vehicles / Defence-and-Security / Miscellaneous conflict first.** |
| 2 | Keep the canard force/torque diagram — it is the best asset. **Delete "no control surface moves" from the novelty framing** (keep it as description). Add the time-resynchronisation sentence. Reframe the actuation sentence to "we adopt and size" rather than "we invent". |
| 3 | Add the magnetometer-coexistence answer (1,234–2,131 Hz coherent notch, current compensation, no new hardware, shielding cannot help). Add the two-things-we-got-wrong line. |
| 4 | Add: the CEP table with RSS and the 1.1774 factor; the friction feasibility gate 0.157 N·m; the energy table (2.92 kW / 121 kJ / 3–16 vs ≥ 58 W/K / 5.8 K); the mass line with the envelope comparison; the three risks with mitigations. Add the **comparison table**. |
| 5 | Move the rounds-per-target number to the top. Add the RFI mapping line. Add the manufacturing route line. Add the three-line TRL/timeline. Add the strategic-materials line. |
| 6 | Reframe references so the prior art reads as **prior art we extend**, not as the foundation. Move the IPP and fixed-canard items under a heading like "prior art extended". Never let the deck both cite and claim the same thing. |

### 8.2 `SIH26098-form-content.md`

- **Abstract:** cut to the six proof numbers and the novelty reframe. The current abstract is 3,491 characters of argument; the objective is a stranger who understands the design and believes the team did the work.
- **Description §15 "Summary of novelty":** rewrite entirely per §6. This is the section a judge reads last and remembers.
- **Description §3.4 "Deployment mechanism":** currently describes a stow-and-deploy mechanism; **our newer decision is that the canards are permanently exposed** with in-bore safety as a static clearance question. Reconcile — the draft-from-register has the newer position, the form content has the older one. **This contradiction is visible if both are read.**
- Add: dud statement, HERO/EMR and ESD treatment, production route, RFI mapping.

### 8.3 `SIH26098-draft-from-register.md`

- **Delete every bracketed criterion ID, every "risk NN", and all internal vocabulary before any of this text reaches the portal.**
- Fix the self-contradiction in the abstract: *"the reference work for this airframe does not contain [a guidance law] — our clearest novel contribution"* is false against our own reference #2. Replace with the authority-gate framing from §6.
- Keep and promote: the thermal interface passage (§4.6 of the draft), the torque-margin passage, the mass/envelope passage, the two-pivots passage.

---

## 9. Predicted outcome, and the ten-day plan

**[predicted]** Rubric-band scoring of the predicted field, 1–5 per criterion, nine criteria, 45 maximum. This is a forecast, not a measurement.

| Entry | Novelty | Complexity | Clarity | Feasibility | Practicability | Sustainability | Impact | UX | Future | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 Vibe-coded sim | 3 | 3 | 4 | 2 | 2 | 2 | 3 | 2 | 3 | **24** |
| C2 Drone stack | 2 | 3 | 4 | 2 | 2 | 2 | 3 | 3 | 2 | **23** |
| C3 Wikipedia PGK | 1 | 2 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | **30** |
| C4 Fuze lab | 2 | 4 | 4 | 4 | 3 | 3 | 2 | 2 | 3 | **27** |
| C5 MATLAB thesis | 4 | 4 | 3 | 3 | 2 | 2 | 3 | 1 | 4 | **26** |
| C6 Excalibur dream | 5 | 4 | 3 | 1 | 1 | 2 | 5 | 3 | 5 | **29** |
| C7 Sleeper air-brake | 3 | 2 | 5 | 5 | 5 | 5 | 3 | 4 | 3 | **35** |
| **Ours — as it stands today** | 2 | 5 | 2 | 2 | 4 | 4 | 4 | 4 | 5 | **32** |
| **Ours — after moves 1–7** | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | **41** |

The table's message: **we lose today to a deck that is merely clear**, and we lose the novelty column to our own references. Two edits (clarity, novelty framing) and three artifacts (sim, CAD, block diagram) move us from third-ish to first.

**The ten days:**

| Days | Do |
|---|---|
| 1–2 | Artifact 3 (block diagram) and the coverage audit. Both are fast. Then start the simulation harness. |
| 3–6 | Simulation: unguided vs guided Monte Carlo, CEP with confidence interval, two plots, honest aero labelling. This is the long pole — start it early, ship it even if the model is coarse. |
| 6–7 | CAD: assembly section view against the fuze-well envelope, launch load path shown. |
| 7–8 | Deck rewrite: six proof numbers, comparison table, three risks, India layer, novelty reframe. |
| 9 | Adversarial pass: read the deck aloud against §4's 38 questions. Whoever cannot answer one, owns the fix. |
| 10 | Verify the portal's theme, category, deadline and character limits. Submit. Do not leave this to day 11. |

---

## 10. Sources

Public record used, with the claim each supports:

- [SIH 2026 Guidelines (official)](https://sih.gov.in/letters/2026/SIH%202026%20Guidelines.pdf) — the nine evaluation criteria verbatim; 500-idea cap per PS; 30 Sep 2026 deadline
- [SIH 2026 complete guide](https://firstvidya.com/sih-2026-guide/) — screening round decided by six slides; ~5 teams per PS; hardware draws smaller fields
- [SIH Buddy — SIH26098 analysis](https://www.sihbuddy.in/ps/SIH26098) — 65–150 teams expected; acceptance 1/5, feasibility 1/5; an AI analysis that declined to produce design content for this statement
- [SIH Fit — SIH26098](https://sih-fit.vercel.app/problem/SIH26098) — the PS's full official text, difficulty rating, idea-count snapshot (0/500) and a 20 Sep 2026 deadline field
- [Zaid Sayyed, SIH 2026 Winner's Playbook](https://zaidsayyed.in/blog/sih-2026) — slide-1 theme trap, the six-slide reading model, the feasibility-slide standard, "how much of this did AI write", and the "twelve other teams" question
- [Competitor artifact: srkself26-cmd/sih26098-guidance-sim](https://github.com/srkself26-cmd/sih26098-guidance-sim) — a real submission for this PS: 3-DOF, ZEM, sub-4 m CEP claim, deployable dashboard, no fuze
- [Yantra India Limited / Ordnance Factory Ambajhari](https://yantraindia.co.in/en/production-unit-page/eyJpdiI6IklNL1VTYlFBazN0NkNta2JuaEhFcmc9PSIsInZhbHVlIjoiajdPZkFwaUFHRHpZN3owQ3RtSkFmQT09IiwibWFjIjoiYjQ2MDljNDVjZjY1ZDcxNzljYzA1YzYwMjAyMmY0MjkzYTMyZWZiODk3YzhlN2I3MWQxNWExZDI5M2I3N2EwNSIsInRhZyI6IiJ9) — shells, cartridge cases, fuzes, rockets; the manufacturing host
- [Indian Army RFI — indigenous 155 mm electronic fuzes](https://idrw.org/indian-army-issues-rfi-for-indigenous-manufacturing-of-155mm-electronic-fuzes-under-make-in-india/) — the three fuze categories our three modes map onto
- [Indian Army 155 mm TGM programme (ADITI-4)](https://idrw.org/indian-army-pushes-indigenous-155mm-terminally-guided-munition-for-one-shot-one-kill-anti-tank-precision/) — the funded seeker programme; DRDO's 155 mm guided projectile at Aero India 2025
- [Northrop Grumman US$863 M M1156 PGK award](https://thedefensepost.com/2026/09/04/northrop-grumman-army-m1156-pgk/) — the scale of the fielded programme our cost claim is measured against
- [IAI TopGun](https://www.iai.co.il/product/topgun/) — a fielded 2-D course-correction kit advertising 20 m CEP at any range
- [Elbit Silver Bullet II](https://elbitsystems.com/sites/default/files/2026-06/silver_bullet_ii_2026_7_web.pdf) — a fielded add-on 2-D CCF for 155 mm
- [SPACIDO / CCF technology overview](https://www.scribd.com/document/61130075/Course-Correction-Fuzes) — the GPS-independent, muzzle-velocity-radar-plus-air-brake concept (the sleeper archetype)
- [Zhang, Yao & Zheng 2019, IPP guidance for dual-spin projectiles with fixed canards](https://www.sciencedirect.com/science/article/pii/S1000936119302419) — prior art for our claimed guidance law
- [Aerodynamic characterization of a canard-guided dual-spin fuze](https://arc.aiaa.org/doi/10.2514/6.2024-1105) — four fixed canards on a 155 mm dual-spin fuze, with a stated 0.8 N·m minimum design torque
- [Flight stability of fixed-canard dual-spin projectiles](https://www.sciencedirect.com/science/article/pii/S2214914725001722) — the resonance-instability literature a domain judge will know

*Internal sources: `design/00-design-criteria-register.md`, `design/02-reference-155mm-model.md`, `notes/02-PGK-SIH-design-brief.md`, `submission/SIH26098-draft-from-register.md`.*
