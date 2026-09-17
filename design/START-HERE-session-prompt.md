# Design Session Prompt — start a new session with this

Copy the block below and paste it as the first message of a new session in this workspace. It turns the session into a guided interview that defines the design criteria one at a time and writes every decision into `design/00-design-criteria-register.md`.

You can reuse it to resume — the prompt tells the session to pick up from the first incomplete criterion, so nothing is lost between sessions.

---

```
Work with me to define the design criteria for SIH26098 — a Precision Guidance Kit with canard actuation and a multi-mode electronic fuze for a 155 mm artillery shell — and then produce a consolidated design definition. This is an interview: you ask, I decide, you write it down.

READ FIRST, BEFORE ASKING ANYTHING
- design/00-design-criteria-register.md — the register you will fill. Read it fully, including the dependency chain, the type definitions, the status values and the risk register.
- notes/02-PGK-SIH-design-brief.md — problem statement mapping, coverage analysis and the architecture decisions already taken.
- notes/00-PGK-thesis-working-notes.md — the validated reference design for the 155 mm class. Every value marked [ref] comes from here.

Treat submission/ as reference material only. Do not edit it, and do not pull its wording into the design work unless I ask.

HOW TO WORK — FOLLOW EXACTLY

1. Work **unblocked-first**, not in strict dependency order. The domains that are not blocked, in this order: G (guidance & control) → C (canard actuation assembly) → F (fuze) → N (navigation & sensing) → W (power & thermal) → R (reliability, safety and verification). Use the [ref] platform values as declared placeholders throughout, and project each of them forward consistently. E (environment) and K (SWaP-C & cost) follow once W is closed — note that K1 and K2 inherit the P9/P12 limits and so stay blocked with P.

   Do **not** walk the dependency chain in the register literally. It runs straight into the YIL-data wall: after M5 the next criteria are M8/M9, then all of P (8 blocked on the shell drawing) and all of S (7 blocked), which would produce roughly twenty consecutive placeholder answers for no gain.

   P (platform) and S (stability) stay blocked until YIL's shell drawing arrives. Leave them open and return to them then.

   Keep the dependency logic **inside** each domain, where it still applies: within G the guidance law (G1) gates the command, window and accuracy criteria; within C the torque criteria (C9–C13) gate the bearing, stowage and retention criteria; within F the mode set (F1) gates the sensor and timing criteria.

2. Ask ONE question at a time. Never batch questions and never dump a list. Every question must contain:
   - the criterion ID and its name
   - why this criterion matters and what it constrains downstream
   - two to four concrete options, each with its consequence, in plain language
   - your recommendation and your reasoning
   Then stop and wait for my answer.

3. After I answer, immediately edit design/00-design-criteria-register.md:
   - set Value, Type, Basis / source and Status for that criterion
   - add a row to the Decision Log with the decision and the rationale in my words
   - update the row in "Progress at a glance"
   - update the risk register if my answer opens or closes a risk
   Do not defer edits to the end of the session. The file must be correct after every single turn.

4. Then ask the next question.

5. At the start of each domain, tell me in one or two lines what the domain covers, how many criteria it holds, and roughly how many turns it will take. Then proceed.

6. Maintain a todo list covering the eleven domains, and keep it updated so I can see progress.

HOW TO HANDLE EACH TYPE OF CRITERION

- Given, and I don't have the data: propose a defensible placeholder, mark the criterion OPEN-BLOCKED, add the dependency to "Requests outstanding from YIL", and move on. Never stall the session waiting for external data.
- Derived by physics: do not ask me. Derive it, show the arithmetic and state the assumption behind every input, mark it DERIVED, then ask me only to confirm or override. If any input is a placeholder, a [ref] value or an unconfirmed anchor, the result is **DERIVED — provisional** and must name that input.
- My choice: present the options with their trade-offs measured against the constraints already in the register — stability margin, friction budget, launch survival, SWaP-C, the governing criteria — and let me decide.

CHALLENGE ME
If my answer violates a constraint, say so directly and show why. Do not quietly record a bad number. Specifically, flag any answer that would:
- reduce the gyroscopic stability factor below the safe margin
- erode the friction-versus-aerodynamic-torque margin near apogee
- put the ring setback load beyond what the bearing and retention can carry
- make the CEP budget fail to close
- make the fuze capable of arming in the bore
- break platform compatibility or the SWaP-C constraints
If I insist after being warned, record the decision and log the risk explicitly.

RULES
- Only create or edit files inside design/. Never modify notes/ or submission/.
- Never invent a number without labelling it an assumption and stating what would verify it.
- Keep the Status column honest. DEFINED means I confirmed it. DERIVED means you computed it. Do not mark something DEFINED on my behalf.
- Every value that comes from the reference literature must be marked [ref] and must be flagged for confirmation against YIL's actual shell.
- If I say "you decide", make the call, mark it Chosen, and state clearly that it was your recommendation rather than my instruction.
- If I say "skip" or "later", leave the criterion OPEN, note it, and move on without argument.
- Any criterion derived on top of a placeholder must be marked *provisional* in its Value cell and must name the placeholder it depends on. A provisional value never counts as closed, however solid the arithmetic looks.

SESSIONS ARE RESUMABLE
If this is a resumed session, read the Status column, find the first incomplete criterion in the **unblocked-first** order, tell me where we are in two lines, and continue from there. Do not re-ask anything already DEFINED. A DERIVED — provisional value may be revisited, but only when the data that unblocks it arrives — never by re-asking the same question.

WHEN THE REGISTER IS COMPLETE
Write design/01-design-definition.md — a consolidated, self-contained design definition organised as a coherent document: system architecture, sizing and the derivation chain, budgets (torque, power, error), interfaces, verification approach, and cost. Every number must trace to a criterion ID. End with the list of criteria still blocked on YIL data and the residual risks.

Start now. Read the three files, tell me in a few lines what you found and what the plan is, then ask me the first question — criterion M1.
```
