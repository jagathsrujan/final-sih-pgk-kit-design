# design/atlas — the architecture atlas

The kit drawn as one system: five sheets, generated from one source of truth,
with every number traceable to a criterion. **Sheet 1 is the deck figure** for
slide 3 and prints in the submission PDF; sheets 2–5 are the working atlas.

**The ledger — what every number is and which criterion owns it — is
`design/08-atlas.md`.** Read that before quoting anything off a sheet.

## The sheets

| Sheet | What it shows | In the deck? |
|---|---|---|
| `flow` | **Connections and activation** — nodes wired by the real interfaces, plus a 16-row × 7-phase activation table | **Yes — slide 3** |
| `sheet1` | System architecture over the flight — 8 swimlanes on one time axis | No (superseded on the slide by `flow`) |
| `sheet2` | Mechanical architecture — the three bodies, every measured mass | No |
| `sheet3` | Power, energy and heat — the 121 kJ path to the shell | No |
| `sheet4` | Guidance, control and the error budget to the CEP claim | No |
| `sheet5` | Flight timeline and the action → reaction set | No |

The deck is capped at six slides by the SIH format and was already at six, so
there is no seventh page. Sheets 1–5 live here, at the rig and at the finale.

## Files

| File | Role |
|---|---|
| `atlas_scene.py` | **Source of truth.** Every sheet as data. No number is typed twice. |
| `render_svg.py` | Renders a sheet to token-mapped SVG, plus a PNG for review. Gates the layout. |
| `out/sheetN.svg` | The artwork. Vector, so it stays sharp in the PDF. |
| `out/sheetN.png` | Review renders, made with headless Chrome. |
| `embed_atlas.py` | Inlines a sheet into `submission/deck/deck.html` between marker pairs. |
| `emit_payloads.py` | Emits a sheet as Excalidraw MCP payloads, to populate the canvas. |
| `scenes.json` | Written by `atlas_scene.py`; the data in a form other tools can read. |

## The pipeline

```bash
python3 atlas_scene.py                              # counts + scenes.json
python3 render_svg.py --all --png --strict           # render, fail on any defect
python3 embed_atlas.py --inline ../../submission/deck/deck.html
python3 emit_payloads.py sheet1 --out /tmp/s1.json  # optional: fill the canvas
```

Then verify the PDF:

```bash
google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf=/tmp/deck.pdf "file://$PWD/../../submission/deck/deck.html"
pdfinfo /tmp/deck.pdf | grep -E "Pages|Page size"    # 6 pages, 960x540 pts
pdftoppm -png -r 110 -f 3 -l 3 /tmp/deck.pdf /tmp/slide   # look at slide 3
```

## Three rules this directory holds to

1. **The atlas evidences; it never decides.** No value in the register moves
   because a sheet shows it. Where a sheet and the register disagree, the
   register wins and the sheet is wrong.

2. **`atlas_scene.py` is the source of truth, not the Excalidraw canvas.** The
   Excalidraw MCP here is headless — it cannot export. If you hand-edit on the
   canvas, port the change back here or the next render will overwrite it.

3. **Zero new design tokens.** Every colour is one of the deck's existing
   `--f-*` properties, referenced as `var(--f-x, fallback)`. The deck restyles
   the atlas with everything else, and the sheet matches the CAD renders.

## Three checks gate every render

All three fail loudly under `--strict`:

- **`check_fit`** — is any label wider than its box? Measured with **Liberation
  Sans**, the font Chrome resolves this stack's Arial entry to, so it measures
  the glyphs that will actually print.
- **`check_overlap`** — do two labels' rendered extents collide? `check_fit`
  cannot see this: two labels in adjacent boxes can each fit inside their own box
  and still run into each other. That is exactly how a timeline's tick row fails.
- **`check_routes`** — does any connector pass through a node box? Only `flow`
  has this failure mode, and it is the one a reader cannot see past: a line that
  vanishes behind a box leaves no way to tell whether it goes under, over or
  nowhere.

`check_fit` and `check_overlap` were verified to fire on synthetic defects before
being trusted. The renderer also parses its own SVG as XML before writing it — an
inlined SVG is XML, and one bad attribute breaks the whole slide.

## Connectors are explicit geometry, on purpose

Excalidraw auto-routes arrows between bound shapes. This renderer has no layout
engine, so `flow_edges()` spells out every vertex. That is a feature on a flow
sheet: the route *is* the drawing, and an arrow that overshoots into a neighbour
is a defect rather than a rendering choice. Connectors run in the gaps — 16 px
corridors between rows, 16 px vertical corridors between the 372-wide columns.

Note that `emit_payloads.py --out` (the reduced `batch_create_elements` schema)
**cannot carry connectors**, because that schema has no `points` field. Use
`--scene` with `import_scene`, which takes the full element schema.

## A note on the type sizes

Sheet 1 uses a **12 px floor**, below the Excalidraw guide's 14 px. That is
deliberate and recorded: the guide sizes for a diagram read 1:1 on screen, and
sheet 1 is a *scaled print artifact* — shown at 1172 px across, it scales by
0.751, so 12 px prints at 6.8 pt and 14 px at 7.9 pt. The deck's own figures
already print at about 6.3 pt, so nothing on the sheet is smaller than the deck
already asks a reader to read.

Sheet 1 also breaks the guide's 20 px grid in band 1 only, because the timeline
places elements by *timestamp*: x carries meaning there.
