#!/usr/bin/env python3
"""
Regenerate the CAD evidence documents from the single source of truth.

    TRACEABILITY.md   every dimension against the criterion it serves
    PARAMETERS.txt    the audit listing and the closure checks
    PARTS.md          every solid in the build, named, grouped and measured

Run this after any edit to pgk_params.py or part_index.py so the documents
cannot drift from the model:

    python3 design/cad/write_traceability.py

PARTS.md reads its masses from out/measured.json, which each phase writes as it
builds. A part with no measured mass is shown as unmeasured rather than given a
number it has not earned.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import part_index as PI  # noqa: E402
import pgk_params as P  # noqa: E402

MEASURED = os.path.join(HERE, "out", "measured.json")


def measured():
    try:
        with open(MEASURED) as fh:
            return json.load(fh)
    except Exception:
        return {}


def parts_md():
    data = measured()
    per_part = data.get("Parts_Kg", {})

    # several solids can share one index entry (the four fins are one part made
    # four times), so masses are aggregated onto the key, and the count is kept
    # to say so.
    by_key = {}
    for name, kg in per_part.items():
        key = PI._key_for(name)
        if not key:
            continue
        entry = by_key.setdefault(key, [0.0, 0])
        entry[0] += kg
        entry[1] += 1

    def mass_cell(key):
        if key not in by_key:
            return "—"
        total, count = by_key[key]
        each = total / count
        if count == 1:
            return "%.0f g" % (total * 1000.0)
        return "%d × %.0f g = **%.0f g**" % (count, each * 1000.0, total * 1000.0)

    out = []
    out.append("# DRISHTI-PGK — Parts\n")
    out.append("Every solid in the P4 build: what it is called, which band of the "
               "architecture it belongs to, what it is made of, what it weighs, "
               "and what it does. **Generated** by "
               "`python3 design/cad/write_traceability.py` from `part_index.py` "
               "(names, groups, materials) and `out/measured.json` (masses, "
               "measured off the solids as each phase builds).\n")
    out.append("The same three facts are carried by the model itself: every part "
               "is created through `cadlib.add_part()`, so the FreeCAD tree shows "
               "the name below, the assembly groups parts by the same band, and "
               "the colour here is the colour in the model and in the deck "
               "renders. Nothing in this file is typed twice.\n")
    out.append("**On the masses:** they are measured, not budgeted. The mass "
               "budget itself is still open — the rollup runs about ×2 over P9 "
               "as modelled (findings T4/T5/T9/T10 in "
               "`design/07-cad-evidence.md`) — so quote these as *what the model "
               "weighs*, never as *what the kit will weigh*.\n")

    for gkey in PI.GROUP_ORDER:
        codes = [c for c in PI.PARTS if PI.group(c) == gkey]
        if not codes:
            continue
        out.append("\n## %s\n" % PI.GROUP_NAMES[gkey])
        if gkey == "body":
            out.append("*Every part here turns with the shell.*\n")
        elif gkey == "ring":
            out.append("*Every part here is de-spun: it turns relative to the "
                       "body, on the bearings, and it is what the machine "
                       "acts on.*\n")
        elif gkey == "between":
            out.append("*The rolling elements — the only load path between the "
                       "two bodies.*\n")
        else:
            out.append("*Not kit parts. Drawn so the constraints can be seen.*\n")
        out.append("| Part | Code | Material | Colour | Mass | What it does |")
        out.append("|---|---|---|---|---:|---|")
        for c in sorted(codes):
            e = PI.entry(c)
            hexcode = e[3] if e else "—"
            trans = e[4] if e else 0
            swatch = hexcode + (" @ %d%% transparent" % trans if trans else "")
            out.append("| **%s** | `%s` | %s | `%s` | %s | %s |"
                       % (PI.label(c), c, PI.material(c), swatch,
                          mass_cell(c), PI.note(c)))
        subtotal = sum(by_key.get(c, [0.0])[0] for c in codes)
        if subtotal:
            out.append("| | | | | **%.0f g** | |" % (subtotal * 1000.0))

    out.append("\n---\n")
    out.append("## How it goes together\n")
    out.append("- The kit **replaces the fuze**: it screws into the MIL-STD-333B "
               "well on the 2″-12 UNS-2A thread that an in-service fuze uses. "
               "It is the same two bodies in relative rotation for the whole "
               "flight, and everything above is either body side, ring side, or "
               "between them.\n")
    out.append("- The **ring side** carries the four fins, the magnets and the "
               "outer races; the **body side** carries the coils, the inner "
               "races, the retention collar, the boards and the fuze train. The "
               "interface between the two is mechanical through the bearings "
               "(100 %% of the load, no torque) and electromagnetic through the "
               "machine (100 %% of the torque, no load).\n")
    out.append("- **Nothing moves except the ring.** The fins are fixed at one "
               "cant each; there is no actuator, no linkage and no deployment. "
               "The ring's angle is the only thing commanded.\n")
    out.append("- The **fuze train runs on the centreline** (F9): every other "
               "part is annular about it. The boards, the dump, the buffer and "
               "the harness all live in the annulus between the train bore and "
               "the well wall.\n")
    out.append("- The launch load does **not** pass through the flight bearings: "
               "the ring travels its clearance and seats on the retention "
               "collar, which is sized against the measured rotating mass.\n")
    return "\n".join(out) + "\n"


def main():
    tr = os.path.join(HERE, "TRACEABILITY.md")
    with open(tr, "w") as f:
        f.write(P.traceability_md() + "\n")
    print("wrote %s (%d bytes)" % (tr, os.path.getsize(tr)))

    pr = os.path.join(HERE, "PARAMETERS.txt")
    with open(pr, "w") as f:
        f.write(P.report() + "\n")
    print("wrote %s (%d bytes)" % (pr, os.path.getsize(pr)))

    pt = os.path.join(HERE, "PARTS.md")
    with open(pt, "w") as f:
        f.write(parts_md())
    print("wrote %s (%d bytes)" % (pt, os.path.getsize(pt)))


if __name__ == "__main__":
    main()
