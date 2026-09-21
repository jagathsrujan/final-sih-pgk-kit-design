"""
The parts index — every solid in the build, named for a reader.

Two jobs, and no others:

  1. **The vocabulary.** `cadlib.add_part()` looks every object up here, so a
     part cannot enter a document unnamed: the FreeCAD tree shows
     "B1 Ring carrier" instead of "B1_Ring_Carrier", and the model is coloured
     the way the deck renders are coloured, because both read this file. One
     palette, one set of names, wherever the hardware is looked at.

  2. **The grouping.** The assembly tree is grouped by the architecture's own
     split: the body side that turns with the shell, the ring side that is
     de-spun, what sits between the two, and the reference shell that is not a
     kit part at all. `GROUP_OF` is that split, and it is the same split the
     interference grid and the mass rollup use.

It is **not**: a dimension source (pgk_params owns every dimension), a decision
record (the register owns those), or a mass source (masses are measured off the
solids and published to `out/measured.json` by each phase).

Adding a part means adding it here. A part built without an entry still builds —
it keeps its code as its name and the default grey — but it is reported as
unnamed, because silence is how a model becomes unreadable.
"""

# ---------------------------------------------------------------------------
# the split the whole workspace uses
# ---------------------------------------------------------------------------

GROUP_NAMES = {
    "body":      "1 Body side — turns with the shell",
    "ring":      "2 Ring side — de-spun, carries the fins",
    "between":   "3 Between the two bodies",
    "reference": "9 Reference — not a kit part",
}
GROUP_ORDER = ["body", "ring", "between", "reference"]

# code -> (label, group, material, colour, transparency %, what it is)
PARTS = {
    # --- body side ---------------------------------------------------------
    "A1_KitBody": (
        "A1 Kit body", "body", "steel", "#48535f", 0,
        "The spigot that screws into the fuze well, and the housing above it. "
        "Every body-side part hangs off this one."),
    "A2_Stator_Core": (
        "A2 Stator core", "body", "soft magnetic composite", "#8a949e", 0,
        "Twelve-slot stator core — the body half of the machine."),
    "A3_Windings": (
        "A3 Windings", "body", "copper", "#c27a25", 0,
        "The twelve coils in the stator slots."),
    "A4_Brg_Inner_Races": (
        "A4 Bearing inner races", "body", "steel", "#a7b0ba", 0,
        "Inner raceways of the two thin-section bearings, on the body side."),
    "A11_Retention_Collar": (
        "A11 Retention collar", "body", "steel", "#6f7b87", 0,
        "The seat that catches the ring's setback load, so the flight bearings "
        "never see launch acceleration."),
    "A5_Avionics_Stack": (
        "A5 Avionics stack", "body", "electronics, bulk", "#2f7d6b", 0,
        "Guidance and control boards, stacked as rings around the train bore."),
    "A6_Dump_Stage": (
        "A6 Dump stage", "body", "electronics, bulk", "#3f8f7b", 0,
        "Chopper dump — sheds the energy the machine generates."),
    "A7_Buffer": (
        "A7 Buffer", "body", "electronics, bulk", "#57a08c", 0,
        "Supercapacitor buffer: the fireset reservoir, hold-up, and the "
        "motoring bursts."),
    "A8_Setter_Coil": (
        "A8 Setter coil", "body", "copper", "#a4551a", 0,
        "Receives the inductive setter message on the gun line."),
    "C3_Harness": (
        "C3 Harness", "body", "electronics, bulk", "#8a6bb0", 0,
        "Interconnect between the well internals and the front end."),
    "A9_Impact_Switch": (
        "A9 Impact switch", "body", "steel", "#9c4040", 0,
        "Impact switch, on the centreline."),
    "A9_SA_Rotor": (
        "A9 S/A rotor", "body", "steel", "#b04a4a", 0,
        "Safety-and-arming rotor — the out-of-line interruption in the train."),
    "A9_Detonator": (
        "A9 Detonator", "body", "steel", "#7a2f2f", 0,
        "Detonator, on the axis at the bottom of the well."),
    "A10_Front_Hub": (
        "A10 Front hub", "body", "steel", "#5d6a78", 0,
        "Front structure: carries the radome and the aperture above the ring."),
    "D1_Radome": (
        "D1 Radome", "body", "dielectric", "#d9a441", 55,
        "Radome over the fuze aperture."),
    "D2_Gnss_Aperture": (
        "D2 GNSS aperture", "body", "electronics, bulk", "#3f6ea8", 15,
        "GNSS aperture, centred on the spin axis so spin does not modulate it."),
    "C2_Link_Body": (
        "C2 Link, body half", "body", "link potting", "#5d8bb3", 0,
        "Body half of the contactless link."),

    # --- ring side ---------------------------------------------------------
    "B1_Ring_Carrier": (
        "B1 Ring carrier", "ring", "steel", "#0b5cad", 0,
        "The de-spun ring. One billet with the four fins; carries the magnets "
        "and the outer races."),
    "B2_Rotor_Backiron": (
        "B2 Rotor backiron", "ring", "steel", "#3d5a75", 0,
        "Closes the magnetic circuit on the ring."),
    "B3_Magnets": (
        "B3 Magnets", "ring", "NdFeB", "#2b2f45", 0,
        "Fourteen magnets — seven pole pairs."),
    "B4_Brg_Outer_Races": (
        "B4 Bearing outer races", "ring", "steel", "#98a3ae", 0,
        "Outer raceways of the two bearings, on the ring."),
    "C2_Link_Ring": (
        "C2 Link, ring half", "ring", "link potting", "#8f6fb5", 0,
        "Ring half of the contactless link — power by transformer, data by "
        "light."),
    "B5_Canard_Steer": (
        "B5 Fin, steering", "ring", "steel", "#1f7ecd", 0,
        "Steering fin. Equal cant across the pair, so the two fins make net "
        "side force and their roll torques cancel."),
    "B5_Canard_Ctrl": (
        "B5 Fin, control", "ring", "steel", "#4f9ad6", 0,
        "Control fin. Opposite cant across the pair, so the two fins make net "
        "roll torque and no net force — this is the pair the machine works "
        "against, and it is why the kit generates."),
    "B5_Canard_Master": (
        "B5 Fin, master", "ring", "steel", "#1f7ecd", 0,
        "The fin before placement, at zero azimuth and unit cant sign. It is "
        "copied and rotated to make the four; it is not itself a part."),

    # --- between -----------------------------------------------------------
    "C1_Balls_Cage": (
        "C1 Balls and cage", "between", "steel", "#cdd5dd", 0,
        "Both bearing rows. The only load path between the two bodies."),

    # --- reference ---------------------------------------------------------
    "D3_Radar_Keepout": (
        "D3 Radar keep-out", "reference", "keep-out volume", "#8a949e", 88,
        "Not a part: the volume the radar needs clear of metal ahead of it. "
        "It is drawn so the constraint can be seen rather than asserted."),
    "REF_Shell_155mm": (
        "REF Reference shell", "reference", "contour model", "#b9c2cc", 78,
        "The 155 mm shell the kit is drawn against. Context only — never a "
        "kit part, and its mass is never quoted."),
}


def _key_for(code):
    """The index key an object name resolves to: exact, else longest prefix."""
    if code in PARTS:
        return code
    best = ""
    for key in PARTS:
        if code.startswith(key) and len(key) > len(best):
            best = key
    return best


def entry(code):
    """The index entry for an object name.

    Prefix matching is what lets `B5_Canard_Steer_A` and `B5_Canard_Ctrl_B`
    resolve: the four fins are one part made four times, at two cants.
    """
    return PARTS.get(_key_for(code))


def label(code):
    """The name a person reads in the FreeCAD tree."""
    key = _key_for(code)
    if not key:
        return code
    name = PARTS[key][0]
    suffix = code[len(key):].strip("_")
    if suffix:
        # A / B are the two fins of a pair; anything else is spelled out
        name = ("%s %s" % (name, suffix) if len(suffix) <= 2
                else "%s (%s)" % (name, suffix.replace("_", " ").lower()))
    return name


def group(code):
    e = entry(code)
    return e[1] if e else "body"


def material(code):
    e = entry(code)
    return e[2] if e else "steel"


def colour(code):
    """(r, g, b) in 0-1, for FreeCAD's ShapeColor."""
    e = entry(code)
    h = (e[3] if e else "#808080").lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def transparency(code):
    e = entry(code)
    return e[4] if e else 0


def note(code):
    e = entry(code)
    return e[5] if e else ""


def grouped(codes):
    """{group key: [codes]} in the order the tree should show them."""
    out = {}
    for c in codes:
        out.setdefault(group(c), []).append(c)
    return {g: sorted(out[g]) for g in GROUP_ORDER if g in out}


if __name__ == "__main__":
    missing = [c for c in PARTS if not note(c)]
    print("parts indexed: %d" % len(PARTS))
    for g in GROUP_ORDER:
        items = [c for c in PARTS if group(c) == g]
        print("  %-42s %2d parts" % (GROUP_NAMES[g], len(items)))
        for c in items:
            print("      %-24s %-28s %-22s %s"
                  % (c, label(c), material(c), note(c)[:46]))
    if missing:
        print("UNNAMED:", missing)
