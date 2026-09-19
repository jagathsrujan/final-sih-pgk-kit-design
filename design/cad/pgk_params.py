"""
DRISHTI-PGK — CAD parameter source of truth (SSOT).

Every dimension used anywhere in the CAD comes from this file. No sketch,
macro or assembly placement may contain a literal number: everything is read
from here, either directly or as an expression on the `Params` spreadsheet
that `to_sheet()` writes.

Provenance discipline (copied from design/00-design-criteria-register.md):

    DEFINED     confirmed by the team
    DERIVED     computed from other defined criteria
    PARAMETRIC  sized over the declared envelope from public data
    PROVISIONAL a value adopted by the CAD for an OPEN criterion; names the
                criterion that must close it. Never counted as closed.

Rule carried from the register: the CAD may EVIDENCE a criterion; it may never
mark one DEFINED on the team's behalf. Anything resting on a PROVISIONAL input
stays provisional in the evidence pack.

Units: millimetres, degrees, kilograms, newtons, newtons-metre, hertz.
Axes:  +Z = spin axis, forward toward the nose.
       datum Z = 0 at the fuze seat face; well intrusion is at negative Z.
       +X = azimuth 0 deg (steering canard 1); roll about +Z, right-hand rule.
"""

from dataclasses import dataclass
import math

# ---------------------------------------------------------------------------
# Record type
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Param:
    alias: str
    value: float
    unit: str
    crit: str        # criterion ID(s) in the register, or 'CAD'
    status: str      # DEFINED | DERIVED | PARAMETRIC | PROVISIONAL
    basis: str       # one line: where the number comes from


def _p(alias, value, unit, crit, status, basis):
    return Param(alias, value, unit, crit, status, basis)


# ---------------------------------------------------------------------------
# 1. Reference 155 mm platform            (design/02-reference-155mm-model.md)
# ---------------------------------------------------------------------------

REFERENCE = [
    _p("ShellBodyDia",      154.89, "mm", "P2", "PARAMETRIC",
       "M795/M549A1 public body diameter"),
    _p("ShellMass",          45.0,  "kg", "P2", "PARAMETRIC",
       "design point, 43-47 kg envelope"),
    _p("ShellIxx",           0.155, "kg*m^2", "P4", "PARAMETRIC",
       "design point, kx-calibrated"),
    _p("ShellIyy",           1.75,  "kg*m^2", "P5", "PARAMETRIC",
       "design point, ky-calibrated; NOT the [ref] 1.216"),
    _p("ShellCGFromNose",  500.0,  "mm", "P3", "PARAMETRIC",
       "0.585 L from nose at the design point"),
    _p("ShellTotalLen",    855.0,  "mm", "P2", "PARAMETRIC",
       "855 mm fused, design point of 840-874 band"),

    # Tangent-ogive nose, verified against the P8 table before use.
    _p("OgiveLen",         449.4,  "mm", "P8", "PARAMETRIC",
       "nose 2.4129 cal of 4.5097 cal -> 0.535 of the fused length"),
    _p("OgiveTruncDia",     50.8,  "mm", "P6", "PARAMETRIC",
       "ogive truncated at the standard fuze diameter"),
    _p("SeatFromTip",       79.3,  "mm", "P8", "DERIVED",
       "solved from the tangent-ogive; reproduces P8's 11 stations to 0.05 mm"),

    # Fuze-well interface, MIL-STD-333B
    _p("WellDepthAvail",   124.7,  "mm", "P7", "PARAMETRIC",
       "M1156 PGK's own intrusion depth on both reference platforms"),
    _p("WellThreadMajDia",  50.8,  "mm", "P6", "PARAMETRIC",
       "2 in - 12 UNS-2A"),
    _p("WellThreadTPI",     12.0,  "1/in", "P6", "DEFINED",
       "2 in - 12 UNS, MIL-STD-333B"),
    _p("WellEngageTurns",    9.0,  "", "P6", "PROVISIONAL",
       "P6's own flank-area estimate uses ~9 turns; confirm against YIL"),
    _p("WellFlankBand",      0.8,  "mm", "P6", "PROVISIONAL",
       "P6's effective contact band on the thread flank"),
    _p("WellBoreDia",       44.0,  "mm", "P6", "PROVISIONAL",
       "the well bore below the thread. 44.0 is the SELF-CONSISTENT reading: "
       "P6's seat annulus of 0.5e-3 m^2 over a ring 44-50.8 reproduces exactly "
       "at this diameter (and a kit shoulder bearing on that seat is what makes "
       "the annulus real). P6's other figure, an 18.8e-3 m^2 contact area, "
       "implies a 48 mm bore -- 9 %% larger, and it is the figure P6's >=58 W/K "
       "closing route is sized on. Both areas are computed outputs here so the "
       "register can adopt whichever YIL's drawing confirms."),
    _p("SpigotClearance",   0.10,  "mm", "P6", "PROVISIONAL",
       "RADIAL assembly clearance on the spigot. It is a MODELLING necessity -- "
       "a nominal-against-nominal fit is a full-volume boolean clash -- and a "
       "design one: P6 rules that a clearance gap conducts nothing (a 0.1 mm air "
       "film over that area is only ~5 W/K), so this gap is not the thermal path. "
       "P6's route is a COMPLIANT CONTACTING element in it, modelled in Phase 6."),
    _p("ThreadClearance",   0.10,  "mm", "P6", "PROVISIONAL",
       "radial allowance so the 2A external thread clears the 2B internal"),

    # Kit envelope limits
    _p("KitIntrusionMax",  124.7,  "mm", "P12", "PARAMETRIC",
       "fielded benchmark intrusion"),
    _p("KitVisibleMax",     95.25, "mm", "P12", "PARAMETRIC",
       "fielded benchmark visible length above the seat"),
    _p("KitMassMax",         1.4,  "kg", "P9", "PARAMETRIC",
       "fielded benchmark kit mass"),
]

# ---------------------------------------------------------------------------
# 2. Canard actuation assembly
# ---------------------------------------------------------------------------

CAA = [
    # Arrangement — C1 DEFINED
    _p("CanardCount",        4.0,  "", "C1", "DEFINED",
       "two pairs: steering 0/180 deg, control 90/-90 deg"),
    _p("AzSteering1",        0.0,  "deg", "C1", "DEFINED", "steering pair, canard 1"),
    _p("AzSteering2",      180.0,  "deg", "C1", "DEFINED", "steering pair, canard 2"),
    _p("AzControl1",        90.0,  "deg", "C1", "DEFINED", "control pair, canard 1"),
    _p("AzControl2",       270.0,  "deg", "C1", "DEFINED", "control pair, canard 2"),

    # Sizing — C31 DEFINED gives the cap; the rest is PROVISIONAL on C4/C5/C7
    _p("RingOD",            98.0,  "mm", "C7", "PROVISIONAL",
       "ring OD at the canard root station; register's own C31 arithmetic "
       "(151-98)/2 = 26.5 exposed span confirms the pairing"),
    _p("CanardTipDiaMax",  151.0,  "mm", "C31", "DEFINED",
       "155.0 bore - 2 mm/side engineering clearance"),
    _p("CanardChordRoot",   80.0,  "mm", "C4", "PROVISIONAL",
       "C31(d): the q-floor sizing case, ~8 cm chord at 21.2 cm^2 per canard"),
    _p("CanardArea",      2120.0,  "mm^2", "C4", "PROVISIONAL",
       "C31(d): 21.2 cm^2 per canard"),
    _p("CanardThick",        4.0,  "mm", "C6", "PROVISIONAL",
       "section thickness at the root; C6 (section) is OPEN"),
    _p("CantSteer",         10.0,  "deg", "C2", "PROVISIONAL",
       "C43's datum cant; C8 needs >= 10 deg, exactly 10.00 at the datum"),
    _p("CantCtrl",          10.0,  "deg", "C3", "PROVISIONAL",
       "control pair, opposite senses, sized by C3"),
    _p("CanardRootThick",   12.0,  "mm", "C5", "PROVISIONAL",
       "root thickness where the fin blends into the ring skin"),
]

# ---------------------------------------------------------------------------
# 3. Machine — frameless outrunner PMSM     (design/03-caa-machine-sizing.md)
#    The radial build below closes to Ø91.9 against the Ø92 ceiling.
# ---------------------------------------------------------------------------

MACHINE = [
    _p("PolePairs",          7.0,  "", "C16", "DEFINED", "p = 7"),
    _p("Poles",             14.0,  "", "C16", "DEFINED", "14 poles"),
    _p("Slots",             12.0,  "", "C36", "DEFINED", "12 slots, concentrated double-layer"),
    _p("WindingFactor",      0.933, "", "C36", "DEFINED", "kw for the 12/14 combination"),
    _p("GapDiaMid",         79.1,  "mm", "C34", "DERIVED", "air-gap diameter at mid-gap"),
    _p("AirGap",             0.40, "mm", "C35", "DERIVED",
       "-> 0.20 mm maximum relative deflection under launch load"),
    _p("MagnetThick",        1.5,  "mm", "C38", "DERIVED", "NdFeB radial thickness, SH/UH grade"),
    _p("BackironThick",      4.7,  "mm", "C40", "DERIVED", "rotor backiron at 1.5 T"),
    _p("StatorYokeThick",    4.7,  "mm", "C40", "DERIVED", "stator yoke at 1.5 T"),
    _p("SlotDepthSizing",   19.6,  "mm", "C40", "DERIVED",
       "the sizing's slot depth, = gap inner radius - yoke inner radius. It "
       "assumes the stator's own bore IS the train bore, i.e. that the 30 mm "
       "train reservation costs no structural material. T3: it does."),
    _p("SpineWall",          1.5,  "mm", "F9",  "PROVISIONAL",
       "T3: the structural spine tube that carries the machine between its two "
       "races. The stator core cannot double as the train-bore wall, because F9 "
       "reserves a clear 30 mm through the machine section -- so something has "
       "to be there and it is not the core. 1.5 mm of steel is the thin end of "
       "what carries the machine's bending; set with C32/C35."),
    _p("StatorBoreDia",     30.0,  "mm", "F9",  "DEFINED",
       "the TRAIN-BORE reservation, not the stator core's own bore"),
    _p("MachineODMax",      92.0,  "mm", "C34", "DEFINED", "hard ceiling, set by the annulus"),
    _p("StackLen",          28.0,  "mm", "C40", "PROVISIONAL",
       "nominal of the 25-30 mm sizing band (L=25 -> 0.81 kg, L=30 -> 0.97 kg)"),
    _p("Kt",                 0.362, "N*m/A", "C14", "DEFINED", "per ampere rms line current"),
    _p("Kv",                 0.209, "V/(rad/s)", "C15", "DEFINED", "rms line-to-line"),
    _p("BusVoltage",       180.0,  "V", "C41", "DEFINED", "180 V nominal, below flight-minimum EMF"),
    _p("PeakCurrentRms",    15.9,  "A", "C18", "DERIVED", "at 5.76 N*m peak torque"),
    _p("HoldCurrentRms",     6.5,  "A", "C18", "DERIVED", "holding duty"),
    _p("MachineMassLo",      0.81, "kg", "C40", "DERIVED", "at L = 25 mm"),
    _p("MachineMassHi",      0.97, "kg", "C40", "DERIVED", "at L = 30 mm"),
]

# ---------------------------------------------------------------------------
# 4. Bearing pair                           (C13, C22, C23, C25, C35)
#    All PROVISIONAL: C22 (type) and C23 (preload) are OPEN, and C23 owns the
#    C35 <-> C13 tension. Geometry is chosen so the preload trade can be swept
#    by changing ONE parameter without rebuilding a part.
# ---------------------------------------------------------------------------

BEARING = [
    _p("BrgBoreDia",        46.0,  "mm", "C22", "PROVISIONAL",
       "inner race bore seat; between the 30-50 mm band C26 names"),
    _p("BrgInnerRaceOD",    53.0,  "mm", "C22", "PROVISIONAL", "inner race outer face"),
    _p("BrgOuterRaceID",    62.0,  "mm", "C22", "PROVISIONAL", "outer race inner face"),
    _p("BrgOuterRaceOD",    69.0,  "mm", "C22", "PROVISIONAL", "outer race outer face, presses into the ring"),
    _p("BrgBallDia",         4.0,  "mm", "C22", "PROVISIONAL", "ball diameter"),
    _p("BrgBallsPerRow",    24.0,  "", "C22", "PROVISIONAL", "balls per row"),
    _p("BrgRow1Z",          14.0,  "mm", "C35", "PROVISIONAL", "aft row station"),
    _p("BrgRow2Z",          72.0,  "mm", "C35", "PROVISIONAL",
       "fore row station; the pair's separation sets the moment stiffness"),
    _p("BrgRowWidth",        8.0,  "mm", "C22", "PROVISIONAL", "loaded race width per row"),
    _p("BrgPreload",         0.0,  "N",  "C23", "PROVISIONAL",
       "PLACEHOLDER — the one knob owning the C35 (>=122 N/um) vs C13 "
       "(Tf <= 0.10 N*m) tension; value set with C22"),
    _p("BrgStiffnessReq",  122.0,  "N/um", "C35", "DERIVED",
       "24.5 kN radial / 0.20 mm allowable deflection, on the pair"),
    _p("FrictionBudget",     0.10, "N*m", "C13", "DERIVED",
       "flat across the speed envelope; load-dominated, not viscous"),
]

# ---------------------------------------------------------------------------
# 5. Loads and the launch path              (C26, C32, C35, E1, E2)
# ---------------------------------------------------------------------------

LOADS = [
    _p("gAxial",         15000.0,  "g",  "E1", "PARAMETRIC", "setback, [ref]"),
    _p("gRadial",         5000.0,  "g",  "E2", "PARAMETRIC", "radial launch load, [ref]"),
    _p("SetbackRing",     73.5,    "kN", "C26", "DERIVED",
       "0.5 kg ring x 15 000 g; scales 14.7 kN per 0.1 kg — recomputed "
       "from the CAD's own ring mass"),
    _p("SetbackRadial",   24.5,    "kN", "C26", "DERIVED", "0.5 kg ring x 5 000 g"),
    _p("CanardSteady",    18.1,    "N",  "C8",  "DERIVED",
       "F_steer >= 18.1 N minimum over the guided window"),
    _p("CanardTransient", 85.0,    "N",  "C28", "PROVISIONAL", "[ref] launch transient"),
    _p("AirGapDeflMax",    0.20,   "mm", "C35", "DERIVED",
       "gap 0.40 mm -> half the gap is the allowable relative deflection"),
    _p("AxialPathStiff",  367.0,   "N/um", "C35", "DERIVED",
       "73.5 kN / 0.20 mm — a structural-case spec, NOT a bearing spec"),
]

# ---------------------------------------------------------------------------
# 5b. Kit body detail                      (T4 -- mass is the live problem)
# ---------------------------------------------------------------------------

BODY = [
    _p("SpiderHoles",        8.0,  "", "CAD", "PROVISIONAL",
       "lightening holes per spider. T4: modelled solid, the body alone is "
       "2.57 kg in steel against P9's 1.4 kg for the WHOLE kit, so every web "
       "that is not a load path gets a hole."),
    _p("SpiderHoleDia",     10.0,  "mm", "CAD", "PROVISIONAL", "lightening hole diameter"),
    _p("SpiderHolePCD",     41.0,  "mm", "CAD", "PROVISIONAL",
       "hole pitch circle, midway between the train bore and the spider OD"),
    _p("WebThickness",       2.0,  "mm", "CAD", "PROVISIONAL",
       "stator end-plate thickness; a mounting face, not a structural member"),
]

# ---------------------------------------------------------------------------
# 6. Front end                              (F2, N3, P8, risk 27)
# ---------------------------------------------------------------------------

FRONT_END = [
    _p("RadarFreq",         24.0,  "GHz", "F2", "DEFINED", "ISM, RF Doppler proximity"),
    _p("GnssApertureDia",   48.0,  "mm", "N3", "PROVISIONAL",
       "rotationally symmetric aperture on the spin axis, elements combined"),
    _p("NoseWallThick",      2.0,  "mm", "CAD", "PROVISIONAL", "radome / fairing wall"),
    _p("NoseCapLen",        18.0,  "mm", "CAD", "PROVISIONAL",
       "length of the nose cap forward of the canard bay — the CAD computes "
       "the SHORTFALL against KitVisibleMax and reports it"),
]

# ---------------------------------------------------------------------------
# 7. Station stack — Z from the seat face, +Z forward toward the nose
#
# The stack is built BOTTOM-UP: only the anchors are declared, everything else
# is placed relative to the part it bolts to. That way the axial audit in
# derived() moves honestly when any one of them changes, instead of being a
# set of numbers that happen to agree.
#
# READ THIS BEFORE QUOTING ANY STATION. The exposed section's outer contour is
# one point on which the source documents genuinely disagree. P8's table is
# headed "station AFT of the fuze seat" and its six stations reproduce the
# tangent ogive exactly read that way (verified, 0.05 mm) -- but P8's own note
# then speaks of "the forward end of the kit's visible length" being Ø97.9, and
# C31's exposed-span arithmetic (151 - 98) / 2 = 26.5 mm only closes if the
# kit's body is Ø98 at the canard root. The reading adopted here is the one
# that makes the register's own numbers cohere and matches the fielded
# analogue's appearance: the kit flares from the Ø50.8 well thread to its
# working diameter just above the shell's nose shoulder, runs that diameter
# through the canard bay, then closes into the nose. Whether the kit must ALSO
# stay inside the mirrored ogive table is an open question carried to the
# evidence pack -- the CAD reports the departure rather than hiding it.
# ---------------------------------------------------------------------------

STATIONS = [
    _p("ZSeat",              0.0,  "mm", "CAD",   "DEFINED", "datum origin"),
    _p("ZThreadRoot",      -19.05, "mm", "P6",    "DERIVED", "WellEngageTurns x pitch, into the well"),
    _p("ZWellBottom",     -124.7,  "mm", "P7",    "PARAMETRIC", "intrusion limit"),

    _p("ShoulderLen",        6.0,  "mm", "CAD",   "PROVISIONAL",
       "steep collar from the well thread out to the working diameter; "
       "it is also the seat's bearing face"),
    _p("MachineInRingAft",  20.0,  "mm", "CAD",   "PROVISIONAL",
       "machine stack starts this far forward of the ring's aft face"),
    _p("BrgRow1Inset",      10.0,  "mm", "CAD",   "PROVISIONAL", "aft bearing row, in from the ring aft face"),
    _p("BrgRow2Inset",      10.0,  "mm", "CAD",   "PROVISIONAL", "fore bearing row, in from the ring fore face"),
    _p("HubAftInset",       10.0,  "mm", "CAD",   "PROVISIONAL", "front hub starts this far forward of the ring aft face"),
]

# ---------------------------------------------------------------------------
# 8. Derived values — recomputed, never retyped
# ---------------------------------------------------------------------------


def derived():
    d = {}

    # --- ogive -------------------------------------------------------------
    R = p("ShellBodyDia") / 2.0
    Ln = p("OgiveLen")
    d["OgiveRho"] = (R * R + Ln * Ln) / (2.0 * R)

    # --- well thread -------------------------------------------------------
    pitch = 25.4 / p("WellThreadTPI")
    d["WellPitch"] = pitch
    d["WellEngageLen"] = p("WellEngageTurns") * pitch
    # UN 2A: pitch diameter = major - 0.649519 * pitch
    d["WellPitchDia"] = p("WellThreadMajDia") - 0.649519 * pitch
    # P6's flank-area estimate, recomputed from our own geometry
    d["WellFlankArea"] = (p("WellEngageTurns") * math.pi
                          * d["WellPitchDia"] * p("WellFlankBand"))
    d["WellFlankAreaP6"] = 1.12e-3 * 1e6  # mm^2, the register's own figure

    # The two areas P6's thermal argument rests on, as computed outputs.
    # Seat annulus = the shoulder the kit bears on, between the well bore and
    # the thread crest. Well bore = the cylindrical contact path below it.
    d["WellSeatArea"] = (math.pi / 4.0
                         * (p("WellThreadMajDia") ** 2 - p("WellBoreDia") ** 2))
    d["WellSeatAreaP6"] = 0.5e-3 * 1e6               # mm^2, the register's figure
    d["WellSeatIDImpliedByP6"] = math.sqrt(
        p("WellThreadMajDia") ** 2 - 4.0 * d["WellSeatAreaP6"] / math.pi)
    d["WellBoreArea"] = math.pi * p("WellBoreDia") * p("KitIntrusionMax")
    d["WellBoreAreaP6"] = 18.8e-3 * 1e6              # mm^2, the register's figure

    # --- canards -----------------------------------------------------------
    d["CanardSpanExposed"] = (p("CanardTipDiaMax") - p("RingOD")) / 2.0
    d["CanardTipR"] = p("CanardTipDiaMax") / 2.0
    d["RingR"] = p("RingOD") / 2.0
    d["CanardAspectRatio"] = d["CanardSpanExposed"] / p("CanardChordRoot")
    d["CanardMeanChord"] = p("CanardArea") / d["CanardSpanExposed"]
    # cant splits normal force: steering component = cos(cant)
    d["CantCosSteer"] = math.cos(math.radians(p("CantSteer")))
    d["CantSinCtrl"] = math.sin(math.radians(p("CantCtrl")))

    # --- machine radial build, outward from the axis ------------------------
    # T3 shapes this: F9 reserves a clear 30 mm bore through the machine
    # section, so the stator core cannot also be the train-bore wall. A spine
    # tube of SpineWall sits on the reservation and the core is built outside
    # it, which costs slot depth -- and torque -- against the sizing.
    r_train = p("StatorBoreDia") / 2.0
    r_spine_out = r_train + p("SpineWall")
    r_gap_mid = p("GapDiaMid") / 2.0
    r_gap_in = r_gap_mid - p("AirGap") / 2.0
    r_gap_out = r_gap_mid + p("AirGap") / 2.0
    r_yoke_in = r_spine_out
    r_yoke_out = r_yoke_in + p("StatorYokeThick")
    slot_depth = r_gap_in - r_yoke_out
    r_mag_out = r_gap_out + p("MagnetThick")
    r_back_out = r_mag_out + p("BackironThick")

    d["RTrainBore"] = r_train
    d["RSpineOut"] = r_spine_out
    d["RGapMid"] = r_gap_mid
    d["RGapIn"] = r_gap_in
    d["RGapOut"] = r_gap_out
    d["RYokeIn"] = r_yoke_in
    d["RYokeOut"] = r_yoke_out
    d["SlotDepth"] = slot_depth
    d["SlotDepthLost"] = p("SlotDepthSizing") - slot_depth
    d["SlotAreaRatio"] = slot_depth / p("SlotDepthSizing")
    d["RMagnetOut"] = r_mag_out
    d["RBackironOut"] = r_back_out
    d["MachineODCheck"] = 2.0 * r_back_out
    d["MachineODMargin"] = p("MachineODMax") - d["MachineODCheck"]
    # radial space left for the ring skin outside the rotor backiron
    d["RingWallThick"] = d["RingR"] - r_back_out
    # torque scales with slot area, so T3's cost lands directly on C19/C42
    d["TorqueScaleFromT3"] = d["SlotAreaRatio"]

    # --- axial envelope audit ---------------------------------------------
    # Bottom-up: every station is placed relative to the part it bolts to.
    d["ZShoulderFore"] = p("ZSeat") + p("ShoulderLen")
    d["ZRingAft"] = d["ZShoulderFore"]
    d["ZRingFore"] = d["ZRingAft"] + p("CanardChordRoot")
    d["ZMachineAft"] = d["ZRingAft"] + p("MachineInRingAft")
    d["ZMachineFore"] = d["ZMachineAft"] + p("StackLen")
    d["ZBrgRow1"] = d["ZRingAft"] + p("BrgRow1Inset")
    d["ZBrgRow2"] = d["ZRingFore"] - p("BrgRow2Inset")
    d["ZFrontHubAft"] = d["ZRingAft"] + p("HubAftInset")
    d["ZFrontHubFore"] = d["ZRingFore"] + p("NoseWallThick") + p("NoseCapLen")

    d["RingLen"] = d["ZRingFore"] - d["ZRingAft"]
    d["BrgRowSeparation"] = d["ZBrgRow2"] - d["ZBrgRow1"]
    d["MachineSitsInRing"] = (
        d["ZMachineAft"] >= d["ZRingAft"] and d["ZMachineFore"] <= d["ZRingFore"])
    d["MachineToRingAftGap"] = d["ZMachineAft"] - d["ZRingAft"]
    d["MachineToRingForeGap"] = d["ZRingFore"] - d["ZMachineFore"]

    # The axial tension: P12 caps the visible length, C31 caps the canard span,
    # and the span cap is paid for with chord (C31(d)) -- so the cap on length
    # and the cap on span meet in the canard planform.
    d["NoseLenAvail"] = p("KitVisibleMax") - d["ZRingFore"]
    d["NoseLenReq"] = p("NoseWallThick") + p("NoseCapLen")
    d["NoseShortfall"] = d["NoseLenReq"] - d["NoseLenAvail"]
    d["KitVisibleReq"] = d["ZFrontHubFore"]
    d["KitVisibleOvershoot"] = d["KitVisibleReq"] - p("KitVisibleMax")

    # What the canard chord would have to be to fit inside P12's own benchmark
    d["CanardChordFitMax"] = (p("KitVisibleMax") - d["ZRingAft"]) - d["NoseLenReq"]
    d["ChordOverrun"] = p("CanardChordRoot") - d["CanardChordFitMax"]
    # ...and the q floor that a shorter chord would impose is C31(d)'s trade,
    # which the register already shows cannot buy the force back with area.

    return d


_TABLE = {}


def _load():
    _TABLE.clear()
    for group in (REFERENCE, CAA, MACHINE, BEARING, LOADS, BODY, FRONT_END, STATIONS):
        for prm in group:
            if prm.alias in _TABLE:
                raise ValueError("duplicate alias: %s" % prm.alias)
            _TABLE[prm.alias] = prm


_load()


def _promote():
    """Fold every derived() quantity into the table as a DERIVED record.

    derived() must only read base aliases through p(); derived-to-derived
    references inside it use its own local dict, so this cannot recurse.
    """
    for k, v in derived().items():
        if k not in _TABLE:
            _TABLE[k] = _p(k, v, "", "CAD", "DERIVED", "computed in derived()")


def p(alias):
    """Value of a parameter or derived quantity, by alias."""
    if alias not in _TABLE:
        _promote()
    return _TABLE[alias].value


def rec(alias):
    """Full record for a parameter, by alias."""
    if alias not in _TABLE:
        _promote()
    return _TABLE[alias]


def all_params():
    """Every parameter and derived quantity, sorted by alias."""
    _promote()
    return [_TABLE[k] for k in sorted(_TABLE)]


def groups():
    return [
        ("REFERENCE", REFERENCE),
        ("CAA", CAA),
        ("MACHINE", MACHINE),
        ("BEARING", BEARING),
        ("LOADS", LOADS),
        ("BODY", BODY),
        ("FRONT_END", FRONT_END),
        ("STATIONS", STATIONS),
    ]


# ---------------------------------------------------------------------------
# 9. FreeCAD binding — writes the Params spreadsheet
# ---------------------------------------------------------------------------


def to_sheet(doc, name="Params"):
    """Create or refresh the `Params` spreadsheet in `doc`.

    Columns: alias | value | unit | criterion | status | basis
    FreeCAD aliases are set so sketches can reference `Params.RingOD` etc.
    """
    if name in doc.Objects:
        sheet = doc.getObject(name)
        doc.removeObject(name)
    sheet = doc.addObject("Spreadsheet::Sheet", name)
    sheet.Label = "Params"

    hdr = ["alias", "value", "unit", "criterion", "status", "basis"]
    for c, text in enumerate(hdr):
        sheet.set("%s1" % chr(ord("A") + c), text)

    row = 2
    for prm in all_params():
        sheet.set("A%d" % row, prm.alias)
        sheet.set("B%d" % row, str(prm.value))
        sheet.set("C%d" % row, prm.unit)
        sheet.set("D%d" % row, prm.crit)
        sheet.set("E%d" % row, prm.status)
        sheet.set("F%d" % row, prm.basis)
        sheet.setAlias("B%d" % row, prm.alias)
        row += 1

    sheet.setColumnWidth("A", 130)
    sheet.setColumnWidth("B", 70)
    sheet.setColumnWidth("C", 60)
    sheet.setColumnWidth("D", 60)
    sheet.setColumnWidth("E", 70)
    sheet.setColumnWidth("F", 420)
    doc.recompute()
    return sheet


# ---------------------------------------------------------------------------
# 10. Self-report — run as a script to audit the numbers
# ---------------------------------------------------------------------------


def report():
    lines = []
    lines.append("DRISHTI-PGK — CAD parameter audit")
    lines.append("=" * 78)
    for gname, group in groups():
        lines.append("")
        lines.append("[%s]" % gname)
        for prm in group:
            lines.append("  %-20s %12.4f %-10s %-6s %-12s"
                         % (prm.alias, prm.value, prm.unit, prm.crit, prm.status))
    lines.append("")
    lines.append("[DERIVED]")
    d = derived()
    for k in sorted(d):
        lines.append("  %-22s %14.5f" % (k, d[k]))

    lines.append("")
    lines.append("-" * 78)
    lines.append("CLOSURE CHECKS")
    lines.append("  machine OD          = %.2f mm  vs limit %.1f mm  -> margin %.2f mm"
                 % (d["MachineODCheck"], p("MachineODMax"), d["MachineODMargin"]))
    lines.append("  spine tube          = Ø%.1f .. Ø%.1f  (wall %.2f)"
                 % (2 * d["RTrainBore"], 2 * d["RSpineOut"], p("SpineWall")))
    lines.append("  yoke                = r %.2f .. %.2f  (%.2f mm)"
                 % (d["RYokeIn"], d["RYokeOut"], p("StatorYokeThick")))
    lines.append("  slot depth          = %.2f mm  vs sizing %.2f mm  -> lost %.2f mm (%.1f %%)"
                 % (d["SlotDepth"], p("SlotDepthSizing"), d["SlotDepthLost"],
                    100.0 * (1.0 - d["SlotAreaRatio"])))
    lines.append("    T3: torque scales with slot area, so C19's 5.76 N·m and C42's")
    lines.append("        2.92 kW both carry a x%.3f factor from the train bore." % d["TorqueScaleFromT3"])
    lines.append("  ring wall over rotor= %.2f mm" % d["RingWallThick"])
    lines.append("  exposed canard span = %.2f mm  (register says 26.5)" % d["CanardSpanExposed"])
    lines.append("  canard chord/span   = %.2f  (AR)" % d["CanardAspectRatio"])
    lines.append("  thread pitch        = %.4f mm  (12 TPI)" % d["WellPitch"])
    lines.append("  thread flank area   = %.4f e-3 m^2  vs P6's 1.12 e-3 m^2"
                 % (d["WellFlankArea"] / 1000.0))
    lines.append("")
    lines.append("  AXIAL AUDIT  (register P12 allows %.2f mm visible)" % p("KitVisibleMax"))
    lines.append("    shoulder          : Z %+.1f .. %+.1f  (%.1f mm, dia %.1f -> %.1f)"
                 % (p("ZSeat"), p("ZShoulderFore"), p("ShoulderLen"),
                    p("WellThreadMajDia"), p("RingOD")))
    lines.append("    ring / canard bay : Z %+.1f .. %+.1f  (%.1f mm, chord %.0f)"
                 % (p("ZRingAft"), p("ZRingFore"), d["RingLen"], p("CanardChordRoot")))
    lines.append("    machine stack     : Z %+.1f .. %+.1f  (%.1f mm)  inside ring: %s"
                 % (p("ZMachineAft"), p("ZMachineFore"), p("StackLen"),
                    d["MachineSitsInRing"]))
    lines.append("    bearing rows      : Z %+.1f  and  Z %+.1f  (separation %.1f mm)"
                 % (p("ZBrgRow1"), p("ZBrgRow2"), d["BrgRowSeparation"]))
    lines.append("    front hub fore    : Z %+.1f" % p("ZFrontHubFore"))
    lines.append("    nose length avail : %.2f mm" % d["NoseLenAvail"])
    lines.append("    nose length req'd : %.2f mm" % d["NoseLenReq"])
    lines.append("    >>> SHORTFALL     : %.2f mm" % d["NoseShortfall"])
    lines.append("    required visible  : %.2f mm  (overshoot %.2f mm)"
                 % (d["KitVisibleReq"], d["KitVisibleOvershoot"]))
    lines.append("    chord that WOULD fit P12 : %.2f mm  (we need %.0f, overrun %.2f)"
                 % (d["CanardChordFitMax"], p("CanardChordRoot"), d["ChordOverrun"]))
    return "\n".join(lines)


if __name__ == "__main__":
    print(report())


# ---------------------------------------------------------------------------
# 11. Traceability report — generated, never hand-kept
# ---------------------------------------------------------------------------

GENERATOR_NOTE = (
    "<!-- GENERATED from design/cad/pgk_params.py — do not edit by hand. -->\n"
    "<!-- Regenerate:  python3 design/cad/write_traceability.py          -->\n"
)


def traceability_md():
    out = [GENERATOR_NOTE, ""]
    out.append("# CAD traceability — every dimension against its criterion")
    out.append("")
    out.append("Status vocabulary is the register's own. **PROVISIONAL** means the "
               "CAD adopted a value for an OPEN criterion: it is a working value, "
               "it names the criterion that must close it, and it is never counted "
               "as closed. The CAD evidences criteria; it never marks one DEFINED.")
    out.append("")

    counts = {}
    for prm in all_params():
        counts[prm.status] = counts.get(prm.status, 0) + 1
    out.append("| status | count |")
    out.append("|---|---:|")
    for k in sorted(counts):
        out.append("| %s | %d |" % (k, counts[k]))
    out.append("")

    for gname, group in groups():
        out.append("")
        out.append("## %s" % gname)
        out.append("")
        out.append("| alias | value | unit | criterion | status | basis |")
        out.append("|---|---:|---|---|---|---|")
        for prm in group:
            out.append("| `%s` | %s | %s | %s | %s | %s |"
                       % (prm.alias, _fmt(prm.value), prm.unit, prm.crit,
                          prm.status, prm.basis))

    out.append("")
    out.append("## Derived quantities")
    out.append("")
    out.append("Recomputed on every load from the table above — change an input "
               "and these move with it.")
    out.append("")
    out.append("| alias | value |")
    out.append("|---|---:|")
    d = derived()
    for k in sorted(d):
        out.append("| `%s` | %s |" % (k, _fmt(d[k])))
    out.append("")

    out.append("## The provisional set — what closes each one")
    out.append("")
    out.append("| alias | criterion | what closes it |")
    out.append("|---|---|---|")
    for prm in all_params():
        if prm.status == "PROVISIONAL":
            out.append("| `%s` | %s | see basis — criterion is OPEN in the register |"
                       % (prm.alias, prm.crit))
    out.append("")
    return "\n".join(out)


def _fmt(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    try:
        return ("%.4f" % v).rstrip("0").rstrip(".")
    except (TypeError, ValueError):
        return str(v)
