#!/usr/bin/env python3
"""DRISHTI-PGK architecture atlas - the single source of truth for every sheet.

Why this file exists rather than a hand-saved .excalidraw
---------------------------------------------------------
The Excalidraw MCP in this session runs headless: elements persist, but
`export_to_image`, `export_scene` and `get_canvas_screenshot` all require a
browser frontend, so the MCP cannot hand us an SVG.  The atlas has to reach the
submission deck as crisp vector art, so this module is the authority and two
consumers are generated from it:

    render_svg.py    -> token-mapped SVG, inlined into submission/deck/deck.html
    emit_payloads.py -> the same elements as MCP batch payloads, so the canvas
                        can be populated (or restored) in Excalidraw at any time

That is the same arrangement as `design/cad/`: one source of truth, generated
artifacts, no number typed twice.

Colour: the sheets carry NO new design tokens.  Every colour is one of the
eleven `--f-*` custom properties the deck already defines, referenced as
`var(--f-x, fallback)` exactly the way `submission/deck/figures/figlib.py` does
it.  So the deck keeps restyling the atlas with everything else, and the
fallbacks below are what the standalone SVG and the PNG check render with.

Type: sizes are in the sheet's own units.  Sheet 1 is drawn to be scaled to the
slide (see PRINT_TARGET), so its floor is 12, not the MCP guide's 14 - the guide
sizes for a diagram read at 1:1 on screen, and this one is not.

Geometry note: the timeline band places elements by *timestamp*, not on the
guide's 20 px grid, because x is carrying meaning there.  Everything else is on
a 6 px rhythm inside the bands.
"""

# --------------------------------------------------------------- tokens ----
# name -> (fallback, role).  Names are the deck's existing custom properties.
TOKEN = {
    "ink":   "#10151b",
    "ink2":  "#46525f",
    "ink3":  "#7b8794",
    "rule":  "#d9dee4",
    "band":  "#f2f5f8",
    "paper": "#ffffff",
    "accent": "#0b5cad",
    "tint":  "rgba(11,92,173,.13)",   # accent fill
    "flag":  "#a4551a",
    "flagt": "rgba(164,85,26,.13)",   # open / not-yet-ruled fill
}

# role -> token name, so the sheet vocabulary is intent, not hex
ROLE = {
    "zone":        "band",    # swimlane background
    "zone_edge":   "rule",
    "node_ours":   "tint",    # decided or derived by us
    "edge_ours":   "accent",
    "node_ref":    "paper",   # carried from the reference work
    "edge_ref":    "ink3",
    "node_open":   "flagt",   # open, not yet ruled
    "edge_open":   "flag",
    "t_hi":        "ink",
    "t_mid":       "ink2",
    "t_lo":        "ink3",
    "t_accent":    "accent",
    "t_flag":      "flag",
}


def _svg_colour(role):
    """Return the var(--f-*) reference for a role, with its fallback."""
    tok = ROLE[role]
    return "var(--f-%s, %s)" % (tok, TOKEN[tok])


# --------------------------------------------------------------- helpers ---
def zone(eid, x, y, w, h):
    """A swimlane background."""
    return {"id": eid, "type": "rectangle", "x": x, "y": y, "width": w,
            "height": h, "fill": _svg_colour("zone"),
            "stroke": _svg_colour("zone_edge"), "sw": 1, "roughness": 0}


def node(eid, x, y, w, h, kind="ours"):
    """A node box. kind: ours | ref | open."""
    return {"id": eid, "type": "rectangle", "x": x, "y": y, "width": w,
            "height": h, "fill": _svg_colour("node_" + kind),
            "stroke": _svg_colour("edge_" + kind), "sw": 1.4,
            "dash": None if kind != "ref" else "dashed", "roughness": 0}


def bar(eid, x, y, w, h, kind="ours", dash=None):
    """A solid-filled rule/axis/tick - fill and stroke the same colour."""
    return {"id": eid, "type": "rectangle", "x": x, "y": y, "width": w,
            "height": h, "fill": _svg_colour("edge_" + kind),
            "stroke": _svg_colour("edge_" + kind), "sw": 1, "dash": dash,
            "roughness": 0}


def txt(eid, x, y, w, h, s, size=12, role="t_mid", anchor="start"):
    return {"id": eid, "type": "text", "x": x, "y": y, "width": w, "height": h,
            "text": s, "fontSize": size, "fill": _svg_colour(role),
            "anchor": anchor}


def edge(eid, points, kind="ours", dash=None):
    """A connector. `points` is an absolute list of (x, y) vertices.

    Explicit geometry rather than Excalidraw's auto-routing: the renderer has no
    layout engine, and on a flow sheet the route IS the drawing - an arrow that
    overshoots into a neighbour is a defect, not a rendering choice."""
    return {"id": eid, "type": "arrow", "points": [(float(px), float(py))
                                                   for px, py in points],
            "stroke": _svg_colour("edge_" + kind), "sw": 1.4, "dash": dash}


def cell(eid, x, y, size, state):
    """One activation cell. state: on | hold | off | gate | safe | armed."""
    look = {
        "on":    ("edge_ours", True),
        "hold":  ("edge_ours", "half"),
        "off":   ("edge_ref", False),
        "gate":  ("edge_open", False),
        "safe":  ("edge_open", False),
        "armed": ("edge_open", True),
    }[state]
    role, filled = look
    return {"id": eid, "type": "cell", "x": x, "y": y, "width": size,
            "height": size, "state": state, "fill": _svg_colour(role),
            "filled": filled, "roughness": 0}


def seq(prefix, n, start_x, width, gap, y, h):
    """n boxes across, returning their x positions."""
    return [start_x + i * (width + gap) for i in range(n)]


# ------------------------------------------------------------ sheet 1 -----
# The print sheet: 1560 x 660, drawn to be scaled into the deck.
# Printed size check: displayed at 1172 CSS px wide => scale 0.751.
#   12 px -> 6.8 pt   14 px -> 7.9 pt   20 px -> 11.3 pt
# Both floors clear the deck's existing figure text (~6.3 pt), so nothing on
# this sheet is smaller than the deck already asks a reader to read.
PRINT_TARGET = {"sheet": "sheet1", "canvas": (1560, 660),
                "display_width_css_px": 1172}

# timeline: x = 150 + t/90 * 1278, so the axis spans 90 s after muzzle exit
AX_X0, AX_X1 = 150, 1428
T_AT = {0: 150, 15: 363, 35: 647, 41.16: 735, 55: 931, 86.5: 1378}

BANDS = [
    # id, label, sublabel, y, h
    ("b1", "FLIGHT",   "timeline (s)", 68, 80),
    ("b2", "SENSE",    "on board",    154, 66),
    ("b3", "NAV",      "state",       226, 66),
    ("b4", "GUIDE",    "the law",     298, 66),
    ("b5", "CONTROL",  "the loop",    370, 66),
    ("b6", "RING",     "and machine", 442, 74),
    ("b7", "POWER",    "and heat",    522, 66),
    ("b8", "FUZE",     "and safety",  594, 66),
]

CX = 116            # content left edge
CW = 1412           # content width; leaves 20 px between the last node and
                    # the swimlane's right border
GAP = 16

# per-band node width, chosen so each row fills CW exactly
def _w(n):
    return (CW - GAP * (n - 1)) / n


SHEET1_NODES = {
    # band 2 - SENSE (7)
    "b2": [
        ("IMU rides the ring", "spin off mechanically", "ours"),
        ("GNSS on spin axis", "symmetric, no mod", "ours"),
        ("Magnetometer ≤50 Hz", "earth ref for \u03b8", "ours"),
        ("Ring angle pickoff", "0.8° body, 1.0° abs", "ours"),
        ("Relative speed", "body-side, \u03c9_rel", "ours"),
        ("Coil current", "in-flight cal input", "ours"),
        ("24 GHz proximity", "burst 2–15 m", "ours"),
    ],
    # band 3 - NAV (6)
    "b3": [
        ("One hardware time base", "GNSS = epoch label only", "ours"),
        ("Stamp at conversion", "≤100 µs, mission set", "ours"),
        ("Nav filter", "GNSS 3.0 + IMU 2.0", "ours"),
        ("RSS 3.7 m at impact", "against 5 m allocation", "ours"),
        ("In-flight mag cal", "rejects 1234–2131 Hz", "ours"),
        ("IMU on the de-spun ring", "±2 000 °/s, ≥100 Hz", "ours"),
    ],
    # band 4 - GUIDE (7)
    "b4": [
        ("Propagate to impact", "state \u2192 impact point", "ours"),
        ("Compare to target", "uploaded pre-flight", "ours"),
        ("Command \u03b8_gk only", "magnitude is fixed", "ours"),
        # the gate mechanism is ours (G3, DEFINED) but the band edges are
        # derived from the reference force profile, so the numbers are ref
        ("Authority gate", "15 s open, 35 s shut", "ref"),
        ("Dwell-fraction phasor", "d = a_cmd / a_auth(t)", "ours"),
        ("Parks at ±90°", "cycle mean = command", "ours"),
        ("≈6 Hz, 300 props", "every flight", "ours"),
    ],
    # band 5 - CONTROL (7)
    "b5": [
        ("Outer P, 6.2 Hz", "settling 0.103 s", "ours"),
        ("Inner PI, 33.6 Hz", "0.29 + 7.82/s", "ours"),
        ("Disturbance observer", "Q = 1/(0.5s + 1)", "ours"),
        ("Limit is a minimum", "2·Î_dist, I_avail(\u03c9)", "ours"),
        ("V_lim 26 rad/s per A", "both state-dependent", "ours"),
        ("Clamping anti-windup", "live limit, 1 ms", "ours"),
        ("Guard band 18°", "no runaway, no wrap", "ours"),
    ],
    # band 6 - RING (6)
    "b6": [
        ("12 slots / 14 poles", "Ø91.9 mm · 0.40 mm gap", "ours"),
        ("Talt 5.76 N·m peak", "0.362 N·m/A · 15.9 A", "ours"),
        ("Taero 0.171 → 2.12 N·m", "min at apogee, max late", "ref"),
        ("Tf ≤ 0.10 N·m, flat", "gate 0.1567 N·m", "ours"),
        ("4 fixed fins, 10° cant", "F_steer ≥ 18.1 N", "ours"),
        ("276 kN setback", "seats past the bearings", "ours"),
    ],
    # band 7 - POWER (5)
    "b7": [
        ("2.92 kW peak", "121 kJ per flight, not storable", "ours"),
        ("Demand ≈12 W", "≈20:1 at the apogee floor", "ours"),
        ("Bus 180 V nominal", "below flight-min EMF 231 V", "ours"),
        ("Dump + 150–200 J buffer", "derates authority, then trips", "ours"),
        ("≥58 W/K interface", "into the shell body \u2192 5.8 K", "ours"),
    ],
    # band 8 - FUZE (7)
    "b8": [
        ("Three modes", "prox · time · impact", "ours"),
        ("Out-of-line rotor", "setback + spin + cmd", "ours"),
        ("No in-bore function", "by construction", "ours"),
        ("Time re-sync in flight", "bounded, one-way", "ours"),
        ("Predicted-miss failsafe", ">150 m \u2192 latch, dud", "ours"),
        ("BIT: hold / derate", "third tier: fuze-alone", "ours"),
        ("Fuze keeps its own MCU", "one bounded crossing", "ours"),
    ],
}


def sheet1():
    """The print sheet."""
    els = []
    W, H = PRINT_TARGET["canvas"]

    # ---- header ----------------------------------------------------------
    els.append(txt("s1-title", 22, 4, 700, 26,
                   "DRISHTI-PGK — system architecture over the flight",
                   20, "t_hi"))
    # Subtitle is deliberately descriptive, not a novelty claim: the register
    # records that the de-spun-ring / fixed-canard / no-actuator list is the
    # fielded kit's own published specification, so presenting it as ours is
    # the correction `05-source-register.md` §3.4 raises first.  Stating the
    # architecture is fine; claiming it as new is not.
    els.append(txt("s1-sub", 22, 30, 880, 18,
                   "155 mm · de-spun ring and fixed canards · four fins, no "
                   "actuator · the machine is both actuator and generator",
                   13, "t_lo"))
    els.append(txt("s1-read", 22, 47, 960, 16,
                   "Read the bands downwards as one chain: the flight, then what "
                   "we sense, decide, drive and shed — and what the fuze will not do.",
                   12, "t_lo"))

    # ---- legend ----------------------------------------------------------
    for i, (role_kind, label) in enumerate((
            ("ours", "decided or derived — ours"),
            ("ref",  "carried from the reference work"),
            ("open", "open — not yet ruled"))):
        y = 8 + i * 18
        els.append(node("lg%d" % (i + 1), 1004, y, 20, 12, role_kind))
        if role_kind == "ref":
            els[-1]["dash"] = "dashed"
        if role_kind == "open":
            els[-1]["dash"] = None
        els.append(txt("lgl%d" % (i + 1), 1032, y - 4, 300, 16, label,
                       12, "t_mid"))

    # ---- swimlanes -------------------------------------------------------
    for bid, label, sub, y, h in BANDS:
        els.append(zone(bid, 12, y, 1536, h))
        els.append(txt(bid + "lab", 24, y + 18, 88, 18, label, 14, "t_mid"))
        els.append(txt(bid + "sub", 24, y + 36, 88, 16, sub, 12, "t_lo"))

    # ---- band 1: the timeline -------------------------------------------
    # The launch state and the rate budget belong with the time axis, because
    # every one of them is a function of where in the flight you are.
    els.append(txt("v0", 150, 70, 900, 16,
                   "muzzle 546–943 m/s · body spin 1 108–1 913 rad/s "
                   "(176–304 Hz) · ring rate ±31.42 rad/s · authority Δv 19.0 m/s",
                   12, "t_lo"))

    phases = (
        ("pre", 0, 15, "pre-nav   0–15 s", "ours"),
        ("gA", 15, 35, "guided   15–35 s", "ours"),
        ("inh", 35, 55, "inhibited   35–55 s", "open"),
        ("gB", 55, 86.5, "guided   55–86.5 s", "ours"),
    )
    for pid, t0, t1, label, kind in phases:
        x0, x1 = T_AT_AT(t0), T_AT_AT(t1)
        els.append(node("ph-" + pid, x0, 88, x1 - x0, 16, kind))
        els[-1]["dash"] = "dashed" if kind == "open" else None
        els.append(txt("phl-" + pid, x0 + 6, 87, x1 - x0 - 12, 16, label,
                       12, "t_flag" if kind == "open" else "t_accent"))
        els.append(bar("tk-" + pid, x0, 107, 2, 10, kind))

    els.append(bar("ax", AX_X0, 112, AX_X1 - AX_X0, 2, "ours"))
    els.append(bar("tk-end", AX_X1, 107, 2, 10, "ours"))

    ticks = (
        (150, "t = 0  muzzle exit", "t_mid"),
        (363, "15 s  nav open", "t_mid"),
        (647, "35 s  gated", "t_flag"),
        (759, "41.2 s  apogee", "t_mid"),
        (931, "55 s  re-open", "t_mid"),
        (1390, "86.5 s  impact", "t_mid"),
    )
    for i, (x, label, role) in enumerate(ticks):
        els.append(txt("tl%d" % i, x, 118, 200, 16, label, 12, role))

    # ---- bands 2-8: the node rows ---------------------------------------
    for bid, _label, _sub, y, h in BANDS[1:]:
        items = SHEET1_NODES[bid]
        n = len(items)
        w = _w(n)
        ny = y + (9 if h == 66 else 13)
        nh = h - 18
        for i, (title, detail, kind) in enumerate(items):
            x = CX + i * (w + GAP)
            els.append(node("%s-n%d" % (bid, i), x, ny, w, nh, kind))
            els.append(txt("%s-t%d" % (bid, i), x + 8, ny + 5, w - 16, 18,
                           title, 14,
                           "t_accent" if kind == "ours" else "t_mid"))
            els.append(txt("%s-d%d" % (bid, i), x + 8, ny + 24, w - 16, 16,
                           detail, 12,
                           "t_flag" if kind == "open" else "t_lo"))

    return {"id": "sheet1", "title": "System architecture over the flight",
            "canvas": PRINT_TARGET["canvas"], "elements": els}


def T_AT_AT(t):
    """Linear map from flight time to axis x, using the same span as the axis."""
    return round(AX_X0 + (t / 90.0) * (AX_X1 - AX_X0))


# =========================================================================
# Review sheets 2-5.
#
# These are NOT the deck figure: they are the working atlas - read on screen, in
# the repo, at the rig and at the finale.  So they carry what the deck's tone
# rules exclude: criterion IDs on every row, and the open items drawn as open.
# Density is higher because they are never scaled down to a 1172 px slide.
# =========================================================================
RBAND_H = 74          # node 54 + breathing room
RBAND_GAP = 10
RHEAD = 62
RCX = 176             # review sheets need a wider gutter: their band labels
RCW = 1352            # carry a criterion-group name plus a description.
RLAB_W = 140


def _rw(n):
    return (RCW - GAP * (n - 1)) / n


def review_sheet(sid, title, sub, bands):
    """Bands: [(label, sublabel, [(title, detail, kind), ...]), ...]."""
    els = [txt(sid + "-title", 22, 6, 1200, 26, title, 20, "t_hi"),
           txt(sid + "-sub", 22, 32, 1400, 18, sub, 13, "t_lo")]
    n = len(bands)
    height = RHEAD + n * (RBAND_H + RBAND_GAP) + 6

    for bi, (label, sublabel, items) in enumerate(bands):
        y = RHEAD + bi * (RBAND_H + RBAND_GAP)
        els.append(zone("%s-b%d" % (sid, bi + 1), 12, y, 1536, RBAND_H))
        els.append(txt("%s-b%dl" % (sid, bi + 1), 24, y + 14, RLAB_W, 18,
                       label, 14, "t_mid"))
        els.append(txt("%s-b%ds" % (sid, bi + 1), 24, y + 32, RLAB_W, 16,
                       sublabel, 12, "t_lo"))
        cnt = len(items)
        w = _rw(cnt)
        ny = y + 10
        nh = RBAND_H - 20
        for i, (t, d, kind) in enumerate(items):
            x = RCX + i * (w + GAP)
            els.append(node("%s-b%dn%d" % (sid, bi + 1, i), x, ny, w, nh, kind))
            els.append(txt("%s-b%dt%d" % (sid, bi + 1, i), x + 8, ny + 6,
                           w - 16, 18, t, 14,
                           "t_accent" if kind == "ours" else "t_mid"))
            els.append(txt("%s-b%dd%d" % (sid, bi + 1, i), x + 8, ny + 27,
                           w - 16, 17, d, 13,
                           "t_flag" if kind == "open" else "t_lo"))
    return {"id": sid, "title": title, "canvas": (1560, height),
            "elements": els}


def sheet2_mechanical():
    return review_sheet(
        "sheet2",
        "Mechanical architecture — the three bodies",
        "Every solid in the P4 build, with the mass measured off it. "
        "Masses are what the model weighs, never yet what the kit will weigh "
        "(T4/T5/T9/T10 are unruled).",
        [
            ("BODY SIDE", "turns with the shell", [
                ("A1 Kit body", "696 g · the spigot in the well", "ours"),
                ("A2 Stator core", "296 g · 12 slots, SMC", "ours"),
                ("A3 Windings", "365 g · copper, 12 coils", "ours"),
                ("A10 Front hub", "433 g · radome + aperture", "ours"),
                ("A11 Retention collar", "138 g · takes the setback", "ours"),
            ]),
            ("BODY SIDE", "electronics and fuze", [
                ("A4 Inner races", "68 g · body half", "ours"),
                ("A5 Avionics stack", "8 g · rings round the bore", "ours"),
                ("A6 Dump stage", "20 g · chopper shunt", "ours"),
                ("A7 Buffer", "54 g · 150–200 J", "ours"),
                ("A8 Setter coil", "47 g · inductive set", "ours"),
                ("A9 Fuze train", "60 g · det, switch, rotor", "ours"),
                ("F9 · the reservation", "Ø30 clear on the axis", "ours"),
            ]),
            ("BETWEEN", "the rolling elements", [
                ("C1 Balls and cage", "13 g · the only load path", "ours"),
                ("Mechanical interface", "100% of the load, no torque", "ours"),
                ("Electromagnetic", "100% of the torque, no load", "ours"),
                ("Launch load path", "setback misses the bearings", "ours"),
                ("Air gap 0.400 mm", "0.20 mm max deflection", "ours"),
            ]),
            ("RING SIDE", "de-spun, carries fins", [
                ("B1 Ring carrier", "1520 g · one billet", "ours"),
                ("B2 Rotor backiron", "283 g · closes the circuit", "ours"),
                ("B3 Magnets", "74 g · 14 magnets, 7 pairs", "ours"),
                ("B4 Outer races", "90 g · ring half", "ours"),
                ("B5 Steering fins", "296 g · equal cant", "ours"),
                ("B5 Control fins", "296 g · opposite cant", "ours"),
                ("C2 Link, ring half", "36 g · transformer + light", "ours"),
            ]),
            ("MASS", "measured, not budgeted", [
                ("Kit total, steel", "4.839 kg as modelled", "open"),
                ("Kit total, aluminium", "2.713 kg as modelled", "open"),
                ("Machine alone", "1.018 kg · +5% over C40", "open"),
                ("Rotating assembly", "1.876 kg · C26's load", "ours"),
                ("Against P9 ≤ 1.4 kg", "+246% steel, +94% alu", "open"),
            ]),
        ])


def sheet3_power():
    return review_sheet(
        "sheet3",
        "Power, energy and heat — the architecture's defining cost",
        "121 kJ per flight that cannot be stored, cannot be held in the kit, "
        "and leaves through the face the kit seats on. This is the price of the "
        "de-spun architecture, stated rather than hidden.",
        [
            ("GENERATED", "Taero × body spin", [
                ("2.92 kW peak", "at the launch condition", "ours"),
                ("121 kJ per flight", "cannot be stored", "ours"),
                ("Loaded generator", "×2.4 the reference rating", "ours"),
                ("Rectifier to bus", "180 V nominal", "ours"),
                ("E_min 231 V", "at the 1 108 rad/s floor", "ours"),
            ]),
            ("CONVERTER", "the W8 condition", [
                ("Four-quadrant stage", "never crosses buck↔boost", "ours"),
                ("W8 route A", "winding kept, bus lowered", "ours"),
                ("E = V_bus at launch", "no current headroom at peak", "open"),
                ("R ∝ Kt² at fixed slots", "the bus is a free choice", "ours"),
            ]),
            ("CONSUMED", "the demand", [
                ("≈12 W peak", "≈10 W average", "ours"),
                ("≈0.9 kJ per flight", "avionics is ≈0.8% of it", "ours"),
                ("≈20:1 at apogee", "the demand never binds", "ours"),
                ("Supercap buffer", "150–200 J · 55 mm long", "ours"),
                ("≥2 s hold-up", "fireset + actuator bursts", "ours"),
            ]),
            ("DISPOSED", "where the 121 kJ goes", [
                ("Chopper dump", "first action derates G15", "ours"),
                ("Then it trips", "authority traded, then shed", "ours"),
                ("≥58 W/K peak", "P6 thermal interface", "ours"),
                ("≥20–27 W/K average", "sized on the flight average", "ours"),
                ("Shell body +5.8 K", "asymptote, reached in minutes", "ours"),
            ]),
            ("NOT FREE", "what it costs", [
                ("Friction heat 140–190 W", "12–17 kJ in the bearings", "ours"),
                ("≈26% rejectable", "the rest must enter the shell", "ours"),
                ("Cant 10° → 16°", "+60% force and +60% heat", "ours"),
            ]),
        ])


def sheet4_control():
    return review_sheet(
        "sheet4",
        "Guidance, control and the error budget",
        "The reference work contains no guidance law at all — it is an "
        "actuation study. The law is ours; the cascade, the observer and the "
        "state-dependent limits are retained from it, and the criterion that "
        "put each block here is named.",
        [
            ("THE LAW", "impact-point prediction", [
                ("Propagate to impact", "G1 · every cycle", "ours"),
                ("Command only θ_gk", "G2 · magnitude is not a command", "ours"),
                ("Authority gate", "G3 · opens ≈15 s, shut 35–55", "ref"),
                ("Dwell-fraction phasor", "G2 · d = a_cmd / a_auth(t)", "ours"),
                ("Parks at ±90°", "G2 · cycle mean is the command", "ours"),
                ("≈6 Hz, 300 props", "G2 · ≤10 Hz is a ceiling", "ours"),
            ]),
            ("THE LOOP", "the retained cascade", [
                ("Outer P, 6.2 Hz", "G8 · requirement was 4 Hz", "ours"),
                ("Inner PI, 33.6 Hz", "G9 · 0.29 + 7.82/s", "ours"),
                ("Settling 0.103 s", "G10 · bounds the guidance rate", "ours"),
                ("Loop rate 1 kHz", "G13 · 30× the inner bandwidth", "ours"),
                ("M4F runs the loop", "H1 · HW-triggered sampling", "ours"),
                ("M7 runs law and nav", "H1 · double precision", "ours"),
            ]),
            ("DISTURBANCE", "and the limits", [
                ("Observer Q = 1/(0.5s+1)", "G14 · corner ≈0.32 Hz", "ours"),
                ("Limit is a minimum", "G15 · DOB floor + capability", "ours"),
                ("Clamping anti-windup", "G12 · live limit every 1 ms", "ours"),
                ("Guard band δ ≈ 18°", "G11 · no runaway, no wrap", "ours"),
                ("Cogging vs 0.171 N·m", "C37 · budget not yet set", "open"),
            ]),
            ("TIMING", "the H4 compute budget", [
                ("Loop ≤100 µs budget", "≈5–15 µs used, ~10× margin", "ours"),
                ("Propagation ≤100 ms", "≈5–20 ms in a 0.17 s interval", "ours"),
                ("The log is the limit", "8–9 MB at IMU rate vs 2 MB", "ours"),
                ("≈300 propagations", "per flight, each to impact", "ours"),
            ]),
            ("ERROR BUDGET", "to the CEP claim", [
                ("Navigation 5 m", "G4 · now derived at 3.7 m", "ours"),
                ("Guidance 17 m", "IPP 13 + ring 9 + lag 6", "ours"),
                ("Meteo 5 m", "residual over the flight", "ours"),
                ("Aero model 8 m", "coefficient uncertainty", "ours"),
                ("Fuze 3 m", "detonation dispersion", "ours"),
                ("RSS 20.3 → CEP 23.9 m", "≈20% margin under 30 m", "ours"),
            ]),
        ])


def sheet5_timeline():
    return review_sheet(
        "sheet5",
        "Flight timeline and the action → reaction set",
        "What happens when, what acts on the ring while it happens, and what "
        "the design does in response. The bottom lane is what we have not yet "
        "demonstrated — it is drawn rather than omitted.",
        [
            ("PHASES", "as the design sees it", [
                ("In bore", "no in-bore function", "ours"),
                ("Muzzle exit t = 0", "546–943 m/s · 545 kPa", "ours"),
                ("Pre-nav 0–15 s", "max(arming, converg.)", "ours"),
                ("Guided 15–35 s", "authority available", "ours"),
                ("Inhibited 35–55 s", "computed, not planned", "ref"),
                ("Guided 55–86.5 s", "the long segment", "ref"),
                ("Apogee 41.2 s", "Taero floor 0.171 N·m", "ref"),
                ("Impact 86.5 s", "Taero 2.12 N·m", "ref"),
            ]),
            ("LOADS", "what acts on the ring", [
                ("276 kN setback", "seats past the bearings", "ours"),
                ("Taero 1.80 → 0.171 N·m", "launch down to apogee", "ref"),
                ("Taero 0.171 → 2.12 N·m", "apogee on to impact", "ref"),
                ("Tf ≤ 0.10 N·m", "flat over every speed", "ours"),
                ("F_steer ≥ 18.1 N", "a minimum, not an average", "ours"),
            ]),
            ("RESPONSE", "action → reaction", [
                ("Command open", "realised by the phasor", "ours"),
                ("Authority short", "derate to I_avail(ω)", "ours"),
                ("Thermal high", "derate G15, then trip", "ours"),
                ("Mag disturbed", "notch + in-flight cal", "ours"),
                ("GNSS lost", "INS coast, bounded", "open"),
                ("BIT flags a fault", "hold / derate / fuze", "ours"),
                ("Predicted-miss veto", ">150 m → latch, dud", "ours"),
                ("No setback", "safe, no abort logic", "ours"),
            ]),
            ("DECLARED OPEN", "not yet demonstrated", [
                ("Friction at flight speed", "C13 · rig parameter only", "open"),
                ("Thermal joint at speed", "P6 · ≥58 W/K by test", "open"),
                ("Coexistence at speed", "F15 · rig run required", "open"),
                ("Ring-body link", "H7 · 4.0 mm working gap", "open"),
                ("Buffer under launch", "W4 · setback pulse", "open"),
            ]),
        ])


SCENES = {"sheet1": sheet1, "sheet2": sheet2_mechanical,
          "sheet3": sheet3_power, "sheet4": sheet4_control,
          "sheet5": sheet5_timeline}


# =========================================================================
# flow - the single-page flow diagram: connections and activation states.
#
# Slide 3 used to carry `sheet1` (a swimlane grid).  A grid shows what exists
# but not what is wired to what, so this sheet replaces it as the deck figure:
# nodes are connected left to right by the real interfaces, and the table below
# says which block is acting in each phase of the flight.
#
# Routing rule, and the reason this file spells out every vertex: connectors
# run in the *gaps*.  Rows are 56 tall with 16 px corridors between them, and
# row 2-4 node columns are 372 wide on a 388 pitch, leaving a 16 px vertical
# corridor between columns.  Nothing crosses a box, so no connector is
# ambiguous.  `check_routes()` below fails the build if one ever does.
# =========================================================================
FLOW_W, FLOW_H = 1560, 710

# graph rows: (y, height).  Four rows of 56 with 16 px corridors between them.
# The height is set by the slide, not by taste: at the deck body's 1172 px this
# sheet is 533 px tall, and slide 3 has 561 px for the figure *and* its caption.
FY = (66, 138, 210, 282)
FH = 56
# row 1: 5 nodes; rows 2-4: 4 nodes
FX5 = [12, 322, 632, 942, 1252]
FX4 = [12, 400, 788, 1176]
FW5, FW4 = 294, 372

MID = lambda y: y + FH // 2          # vertical centre of a row

FLOW_NODES = [
    # (row, col, title, detail, kind)
    (0, 0, "Sensing", "IMU on the ring · GNSS on the axis ·\nmagnetometer · ring pickup", "ours"),
    (0, 1, "NAV filter", "GNSS 3.0 + IMU 2.0 · RSS 3.7 m", "ours"),
    (0, 2, "IPP law", "propagate to impact · ≈6 Hz", "ours"),
    (0, 3, "Authority gate", "15 s open · 35–55 s shut", "ref"),
    (0, 4, "Phasor → θ_gk", "d = a_cmd/a_auth · parks ±90°", "ours"),
    (1, 0, "Cascade: P then PI", "6.2 Hz / 33.6 Hz · 1 kHz loop", "ours"),
    (1, 1, "Machine 12 / 14", "Talt 5.76 N·m · 0.40 mm gap", "ours"),
    (1, 2, "Ring, de-spun", "Tf ≤ 0.10 N·m · Taero → 2.12 N·m", "ours"),
    (1, 3, "4 fins, 10° cant", "F_steer ≥ 18.1 N", "ours"),
    (2, 0, "DOB + limits", "min(2·Î_dist, I_avail(ω))", "ours"),
    (2, 1, "Rectifier → bus", "180 V nominal · E_min 231 V", "ours"),
    (2, 2, "Dump + buffer", "2.92 kW · 121 kJ · 150–200 J", "ours"),
    (2, 3, "Thermal joint", "≥58 W/K into the shell → 5.8 K", "ours"),
    (3, 0, "Setter → package", "275 ms window · read-back", "ours"),
    (3, 1, "S/A rotor", "setback + spin + arm command", "ours"),
    (3, 2, "Fireset", "prox 2–15 m · time · impact", "ours"),
    (3, 3, "Predicted-miss veto", ">150 m → latch, withhold arm", "ours"),
]


def flow_boxes():
    """The obstacle boxes a connector must not cross: the graph nodes."""
    out = []
    for r, c, _t, _d, _k in FLOW_NODES:
        x = (FX5 if r == 0 else FX4)[c]
        w = FW5 if r == 0 else FW4
        out.append(("f-n%d%d" % (r, c), x, FY[r], x + w, FY[r] + FH))
    return out


def flow_edges():
    """Every connector, as explicit vertices.  See the routing rule above."""
    out = []

    def add(pts, kind="ours", dash=None):
        out.append((pts, kind, dash))

    r1, r2, r3, r4 = FY
    m1, m2, m3, m4 = (MID(r) for r in FY)

    # row 1, left to right: nodes are adjacent, so plain horizontals
    for x0 in (306, 616, 926, 1236):
        add([(x0, m1), (x0 + 16, m1)])

    # wrap: row 1 col 5 -> row 2 col 1, through the corridor above row 2
    cy = r2 - 8
    add([(1399, r1 + FH), (1399, cy), (198, cy), (198, r2)])

    # row 2, left to right
    for x0 in (384, 772, 1160):
        add([(x0, m2), (x0 + 16, m2)])

    # the observer constrains the cascade: straight up, same column
    add([(198, r3), (198, r2 + FH)])

    # the machine is the generator for the power chain: straight down
    add([(586, r2 + FH), (586, r3)])

    # power chain, left to right
    for x0 in (772, 1160):
        add([(x0, m3), (x0 + 16, m3)])

    # fuze chain, left to right
    for x0 in (384, 772):
        add([(x0, m4), (x0 + 16, m4)])

    # arm command: down the vertical corridor at x = 1168, then right into the
    # veto.  x = 1168 sits in the 16 px gap between the 372-wide columns.
    add([(1168, r1 + FH), (1168, m4), (1176, m4)], kind="open", dash="dashed")

    # the veto acts on the arm command: over the top of row 4, into the rotor
    vy = r4 - 10
    add([(1362, r4), (1362, vy), (586, vy), (586, r4)],
        kind="open", dash="dashed")
    return out


def check_routes():
    """Fail if any connector segment passes through a node box.

    A connector that disappears behind a box is the one defect a reader cannot
    see past - they cannot tell whether it goes under, over or nowhere.  Every
    vertex pair is tested against every box, with a 2 px guard so a route that
    merely grazes an edge is reported too."""
    boxes = flow_boxes()
    bad = []
    for pts, _kind, _dash in flow_edges():
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            lo_x, hi_x = min(x0, x1) + 2, max(x0, x1) - 2
            lo_y, hi_y = min(y0, y1) + 2, max(y0, y1) - 2
            if lo_x > hi_x:
                lo_x = hi_x = (x0 + x1) / 2.0
            if lo_y > hi_y:
                lo_y = hi_y = (y0 + y1) / 2.0
            for name, bx0, by0, bx1, by1 in boxes:
                if lo_x < bx1 and bx0 < hi_x and lo_y < by1 and by0 < hi_y:
                    bad.append((name, (x0, y0, x1, y1)))
    return bad


# (label, kind) per phase column, and per-row activation
FLOW_PHASES = ["IN-BORE", "LAUNCH", "PRE-NAV", "GUID-A", "INHIB", "GUID-B", "IMPACT"]

FLOW_ROWS_A = [
    ("IMU on the ring",              ["off", "off", "on",  "on",  "on",  "on",  "on"]),
    ("GNSS on the spin axis",        ["off", "off", "on",  "on",  "on",  "on",  "on"]),
    ("Magnetometer",                 ["off", "off", "on",  "on",  "on",  "on",  "on"]),
    ("Ring angle pickup",            ["off", "off", "on",  "on",  "on",  "on",  "on"]),
    ("NAV filter and time base",     ["off", "off", "on",  "on",  "on",  "on",  "on"]),
    ("IPP guidance law",             ["off", "off", "off", "on",  "gate", "on", "on"]),
    ("Authority gate",               ["off", "off", "off", "on",  "gate", "on", "on"]),
    ("Phasor → θ_gk",                ["off", "off", "off", "on",  "hold", "on", "on"]),
]
FLOW_ROWS_B = [
    ("Cascade: P then PI",           ["off", "off", "hold", "on", "on", "on", "on"]),
    ("Observer and limits",          ["off", "off", "on",  "on",  "on",  "on",  "on"]),
    ("Machine (alternator)",         ["off", "on",  "on",  "on",  "on",  "on",  "on"]),
    ("Ring and four fins",           ["off", "hold", "on", "on",  "on",  "on",  "on"]),
    ("Bus and dump",                 ["off", "on",  "on",  "on",  "on",  "on",  "on"]),
    ("Supercap buffer",              ["off", "on",  "on",  "on",  "on",  "on",  "on"]),
    ("Thermal joint",                ["off", "on",  "on",  "on",  "on",  "on",  "on"]),
    ("Fuze S/A and fireset",         ["safe", "safe", "safe", "safe", "safe", "safe", "armed"]),
]

# matrix geometry
MB_X = (12, 786)          # the two blocks
MB_W = 770
M_LAB_X = 10              # label offset inside a block
M_LAB_W = 290
M_COL_X = 310             # first phase column offset inside a block
M_ROW0 = 380
M_PITCH = 41
M_CELL = 20


def flow():
    """The single-page flow diagram: connections above, activation below."""
    els = []

    # ---- header ----------------------------------------------------------
    els.append(txt("f-title", 22, 4, 900, 26,
                   "DRISHTI-PGK — what is connected to what, and what is live when",
                   20, "t_hi"))
    els.append(txt("f-sub", 22, 30, 1000, 18,
                   "Left to right is signal flow; the arrows are the real "
                   "interfaces. The table below says which block is acting in "
                   "each phase of the flight.", 12, "t_lo"))

    # legend: the five cell states and the two connector kinds
    lg = [("cell", "on", "acting"),
          ("cell", "hold", "holding"),
          ("cell", "off", "off"),
          ("cell", "gate", "inhibited"),
          ("cell", "armed", "armed"),
          ("dash", None, "one-way, gated"),
          ("solid", None, "signal or power")]
    lx = 22
    for i, (what, state, label) in enumerate(lg):
        if what == "cell":
            els.append(cell("f-lg%d" % i, lx, 50, 13, state))
        else:
            dash = "dashed" if what == "dash" else None
            els.append(edge("f-lg%d" % i, [(lx, 56), (lx + 18, 56)], "ours"
                            if what == "solid" else "open", dash))
        els.append(txt("f-lgt%d" % i, lx + 24, 46, 200, 14, label, 11, "t_lo"))
        lx += 218

    # ---- the flow graph --------------------------------------------------
    labels = {}
    for r, c, title, detail, kind in FLOW_NODES:
        x = (FX5 if r == 0 else FX4)[c]
        w = FW5 if r == 0 else FW4
        y = FY[r]
        eid = "f-n%d%d" % (r, c)
        labels[eid] = (x, y, w)
        els.append(node(eid, x, y, w, FH, kind))
        els[-1]["dash"] = "dashed" if kind == "ref" else None
        els.append(txt(eid + "t", x + 10, y + 7, w - 20, 18, title, 14,
                       "t_accent" if kind == "ours" else "t_mid"))
        for j, line in enumerate(detail.split("\n")):
            els.append(txt("%sd%d" % (eid, j), x + 10, y + 28 + j * 14,
                           w - 20, 16, line, 12, "t_lo"))

    for i, (pts, kind, dash) in enumerate(flow_edges()):
        els.append(edge("f-e%d" % i, pts, kind, dash))

    # ---- the activation matrix ------------------------------------------
    for b, (bx, rows, title) in enumerate((
            (MB_X[0], FLOW_ROWS_A,
             "GUIDANCE CHAIN — phases: in-bore · 0 s · 0–15 s · 15–35 s · "
             "35–55 s · 55–86.5 s · impact"),
            (MB_X[1], FLOW_ROWS_B,
             "SUPPORTING CHAINS — power, thermal and fuze"))):
        els.append(txt("f-m%ds" % b, bx + 4, 344, 760, 16, title, 12, "t_mid"))
        cw = (MB_W - M_COL_X - 10) / 7.0
        # hairline rules between the phase columns.  The cells are 20 px in a
        # 64 px column, so without them the eye cannot track one phase down the
        # table - the row labels and the cells are too far apart to pair up.
        last = M_ROW0 + (len(rows) - 1) * M_PITCH + 32
        for c in range(1, 7):
            els.append({"id": "f-m%dx%d" % (b, c), "type": "rectangle",
                        "x": bx + M_COL_X + c * cw, "y": 350, "width": 1,
                        "height": last - 350,
                        "fill": _svg_colour("zone_edge"),
                        "stroke": _svg_colour("zone_edge"),
                        "sw": 1, "dash": None, "roughness": 0})
        for c, ph in enumerate(FLOW_PHASES):
            cx = bx + M_COL_X + c * cw + cw / 2.0
            els.append(txt("f-m%dp%d" % (b, c), cx - 32, 360, 64, 14, ph, 11,
                           "t_lo", anchor="middle"))
        for r, (label, states) in enumerate(rows):
            ry = M_ROW0 + r * M_PITCH
            els.append(txt("f-m%dl%d" % (b, r), bx + M_LAB_X, ry + 7,
                           M_LAB_W, 16, label, 12, "t_mid"))
            for c, st in enumerate(states):
                cw = (MB_W - M_COL_X - 10) / 7.0
                cx = bx + M_COL_X + c * cw + cw / 2.0
                els.append(cell("f-m%dr%dc%d" % (b, r, c), cx - M_CELL / 2.0,
                                ry + 6, M_CELL, st))

    return {"id": "flow", "title":
            "System architecture — connections and activation by flight phase",
            "canvas": (FLOW_W, FLOW_H), "elements": els}


SCENES["flow"] = flow


if __name__ == "__main__":
    import json
    import os
    out = {}
    for name, fn in SCENES.items():
        s = fn()
        out[name] = s
        print("%-8s %4d elements  canvas %s" %
              (name, len(s["elements"]), s["canvas"]))
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "scenes.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", dest)
