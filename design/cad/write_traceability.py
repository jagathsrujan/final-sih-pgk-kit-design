#!/usr/bin/env python3
"""
Regenerate design/cad/TRACEABILITY.md and design/cad/PARAMETERS.txt from the
single source of truth. Run this after any edit to pgk_params.py so the evidence
documents cannot drift from the model.

    python3 design/cad/write_traceability.py
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pgk_params as P  # noqa: E402


def main():
    tr = os.path.join(HERE, "TRACEABILITY.md")
    with open(tr, "w") as f:
        f.write(P.traceability_md() + "\n")
    print("wrote %s (%d bytes)" % (tr, os.path.getsize(tr)))

    pr = os.path.join(HERE, "PARAMETERS.txt")
    with open(pr, "w") as f:
        f.write(P.report() + "\n")
    print("wrote %s (%d bytes)" % (pr, os.path.getsize(pr)))


if __name__ == "__main__":
    main()
