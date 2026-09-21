# DRISHTI-PGK — CAD images for the deck

Rendered from the P4 CAD (Phases 0–7) on 2026-09-21. Every shape is the solid
that `design/cad/` built and gate-checked — nothing is redrawn, retouched or
posed. 16:9, ~2400 x 1350, white background, ready to drop into a slide.

Regenerate: `macros/95_render_deck_images.py` from the FreeCAD session, then
`python3 design/cad/deck_render_trim.py` to trim and republish here.

**Three of these are already in the deck**, embedded as data URIs by
`figures/embed_cad.py` (`--inline ../deck.html`):

| Slot | Image | Slide |
|---|---|---|
| `s3-hardware` | `11-section-machine.png` | 3 — Technical approach |
| `s4-fit` | `05-shell-kit-section.png` | 4 — Feasibility |
| `s5-gunline` | `04-shell-kit-iso.png` | 5 — Impact and benefits |

The rest are unused and available. They are **not** in the deck for want of
room rather than for want of quality: slides 1, 2 and 6 have no slack, and
slide 2's annotated schematic occupies its whole right column.

## Colour key

**Not repeated here.** The colour, the readable name and the group of every part
live in `design/cad/part_index.py`, and `design/cad/PARTS.md` prints them as a
generated table, so the key cannot drift from the model it describes. Three
things worth knowing when reading these images:

- The **steering fins** (`#1f7ecd`) and the **control fins** (`#4f9ad6`) are one
  part at two cants: the steering pair makes net side force, the control pair
  makes net roll torque and no net force.
- The **reference shell** (`#b9c2cc`, 78 % transparent) is never a kit part, and
  nothing forward of the fuze well is modelled as changed.
- The cutaway images **do not cut the fins or the internals**: the housings are
  cut so the fit can be read, everything inside stays whole.

## The set

**Assembly**
- `01-assembly-iso` — the kit as fielded, nose up
- `02-assembly-profile` — side elevation: exposed length, canard chord, thread seat
- `03-assembly-nose-on` — looking down the axis: four fins, span against the bore
- `04-shell-kit-iso` — installed on the reference shell (ghosted)
- `05-shell-kit-section` — same, shell and body cut away: the well, the thread, the seat

**Staged — parts taken off, so the fit reads off the picture**
- `06-nose-removed` — front end off: fins, ring, setter coil, link
- `07-ring-removed` — ring and fins off: stator, windings, inner races, electronics
- `08-ring-group-alone` — the rotating group by itself (the 1.876 kg of C26)
- `09-body-removed` — shell off, seen from the well end
- `10-section-through-axis` — full half-section: machine, bearing, train bore, buffer
- `11-section-machine` — half-section on the machine: windings, magnets, air gap, bearings
- `12-exploded-stack` — the assembly order along the axis

**Parts**
- `13-part-body`, `13b-part-body-section` — A1 kit body, whole and half-section
- `14-part-ring-canards` — ring carrier with its four integral fins
- `15-part-canard` — one steering fin, showing the cant
- `16-part-stator-windings`, `17-part-rotor-magnets` — the two machine halves
- `18-part-bearing-path` — races, balls, cage, retention collar
- `19-part-electronics-stack` — avionics, dump, buffer, setter coil, harness, link
- `20-part-front-end` — hub, radome, GNSS aperture
- `21-part-fuze-train` — the on-axis train parts

**Numbers these images carry are interface verifications only** — 124.70 mm
intrusion, zero interference with the reference shell, the 0.400 mm air gap, the
canard cant. Mass, energy and the junction step are still open in
`design/07-cad-evidence.md` (findings T1–T10) and must not be quoted yet.
