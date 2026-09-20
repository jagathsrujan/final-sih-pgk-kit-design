<!-- GENERATED from design/cad/pgk_params.py — do not edit by hand. -->
<!-- Regenerate:  python3 design/cad/write_traceability.py          -->


# CAD traceability — every dimension against its criterion

Status vocabulary is the register's own. **PROVISIONAL** means the CAD adopted a value for an OPEN criterion: it is a working value, it names the criterion that must close it, and it is never counted as closed. The CAD evidences criteria; it never marks one DEFINED.

| status | count |
|---|---:|
| DEFINED | 18 |
| DERIVED | 92 |
| PARAMETRIC | 16 |
| PROVISIONAL | 45 |


## REFERENCE

| alias | value | unit | criterion | status | basis |
|---|---:|---|---|---|---|
| `ShellBodyDia` | 154.89 | mm | P2 | PARAMETRIC | M795/M549A1 public body diameter |
| `ShellMass` | 45 | kg | P2 | PARAMETRIC | design point, 43-47 kg envelope |
| `ShellIxx` | 0.155 | kg*m^2 | P4 | PARAMETRIC | design point, kx-calibrated |
| `ShellIyy` | 1.75 | kg*m^2 | P5 | PARAMETRIC | design point, ky-calibrated; NOT the [ref] 1.216 |
| `ShellCGFromNose` | 500 | mm | P3 | PARAMETRIC | 0.585 L from nose at the design point |
| `ShellTotalLen` | 855 | mm | P2 | PARAMETRIC | 855 mm fused, design point of 840-874 band |
| `OgiveLen` | 449.4 | mm | P8 | PARAMETRIC | nose 2.4129 cal of 4.5097 cal -> 0.535 of the fused length |
| `OgiveTruncDia` | 50.8 | mm | P6 | PARAMETRIC | ogive truncated at the standard fuze diameter |
| `SeatFromTip` | 79.3 | mm | P8 | DERIVED | solved from the tangent-ogive; reproduces P8's 11 stations to 0.05 mm |
| `WellDepthAvail` | 124.7 | mm | P7 | PARAMETRIC | M1156 PGK's own intrusion depth on both reference platforms |
| `WellThreadMajDia` | 50.8 | mm | P6 | PARAMETRIC | 2 in - 12 UNS-2A |
| `WellThreadTPI` | 12 | 1/in | P6 | DEFINED | 2 in - 12 UNS, MIL-STD-333B |
| `WellEngageTurns` | 9 |  | P6 | PROVISIONAL | P6's own flank-area estimate uses ~9 turns; confirm against YIL |
| `WellFlankBand` | 0.8 | mm | P6 | PROVISIONAL | P6's effective contact band on the thread flank |
| `WellBoreDia` | 44 | mm | P6 | PROVISIONAL | the well bore below the thread. 44.0 is the SELF-CONSISTENT reading: P6's seat annulus of 0.5e-3 m^2 over a ring 44-50.8 reproduces exactly at this diameter (and a kit shoulder bearing on that seat is what makes the annulus real). P6's other figure, an 18.8e-3 m^2 contact area, implies a 48 mm bore -- 9 %% larger, and it is the figure P6's >=58 W/K closing route is sized on. Both areas are computed outputs here so the register can adopt whichever YIL's drawing confirms. |
| `SpigotClearance` | 0.1 | mm | P6 | PROVISIONAL | RADIAL assembly clearance on the spigot. It is a MODELLING necessity -- a nominal-against-nominal fit is a full-volume boolean clash -- and a design one: P6 rules that a clearance gap conducts nothing (a 0.1 mm air film over that area is only ~5 W/K), so this gap is not the thermal path. P6's route is a COMPLIANT CONTACTING element in it, modelled in Phase 6. |
| `ThreadClearance` | 0.1 | mm | P6 | PROVISIONAL | radial allowance so the 2A external thread clears the 2B internal |
| `KitIntrusionMax` | 124.7 | mm | P12 | PARAMETRIC | fielded benchmark intrusion |
| `KitVisibleMax` | 95.25 | mm | P12 | PARAMETRIC | fielded benchmark visible length above the seat |
| `KitMassMax` | 1.4 | kg | P9 | PARAMETRIC | fielded benchmark kit mass |

## CAA

| alias | value | unit | criterion | status | basis |
|---|---:|---|---|---|---|
| `CanardCount` | 4 |  | C1 | DEFINED | two pairs: steering 0/180 deg, control 90/-90 deg |
| `AzSteering1` | 0 | deg | C1 | DEFINED | steering pair, canard 1 |
| `AzSteering2` | 180 | deg | C1 | DEFINED | steering pair, canard 2 |
| `AzControl1` | 90 | deg | C1 | DEFINED | control pair, canard 1 |
| `AzControl2` | 270 | deg | C1 | DEFINED | control pair, canard 2 |
| `RingOD` | 98 | mm | C7 | PROVISIONAL | ring OD at the canard root station; register's own C31 arithmetic (151-98)/2 = 26.5 exposed span confirms the pairing |
| `CanardTipDiaMax` | 151 | mm | C31 | DEFINED | 155.0 bore - 2 mm/side engineering clearance |
| `CanardChordRoot` | 80 | mm | C4 | PROVISIONAL | C31(d): the q-floor sizing case, ~8 cm chord at 21.2 cm^2 per canard |
| `CanardArea` | 2120 | mm^2 | C4 | PROVISIONAL | C31(d): 21.2 cm^2 per canard |
| `CanardThick` | 4 | mm | C6 | PROVISIONAL | section thickness at the root; C6 (section) is OPEN |
| `CantSteer` | 10 | deg | C2 | PROVISIONAL | C43's datum cant; C8 needs >= 10 deg, exactly 10.00 at the datum |
| `CantCtrl` | 10 | deg | C3 | PROVISIONAL | control pair, opposite senses, sized by C3 |
| `CanardRootThick` | 12 | mm | C5 | PROVISIONAL | root thickness where the fin blends into the ring skin |

## MACHINE

| alias | value | unit | criterion | status | basis |
|---|---:|---|---|---|---|
| `PolePairs` | 7 |  | C16 | DEFINED | p = 7 |
| `Poles` | 14 |  | C16 | DEFINED | 14 poles |
| `Slots` | 12 |  | C36 | DEFINED | 12 slots, concentrated double-layer |
| `WindingFactor` | 0.933 |  | C36 | DEFINED | kw for the 12/14 combination |
| `GapDiaMid` | 79.1 | mm | C34 | DERIVED | air-gap diameter at mid-gap |
| `AirGap` | 0.4 | mm | C35 | DERIVED | -> 0.20 mm maximum relative deflection under launch load |
| `MagnetThick` | 1.5 | mm | C38 | DERIVED | NdFeB radial thickness, SH/UH grade |
| `BackironThick` | 4.7 | mm | C40 | DERIVED | rotor backiron at 1.5 T |
| `StatorYokeThick` | 4.7 | mm | C40 | DERIVED | stator yoke at 1.5 T |
| `SlotDepthSizing` | 19.6 | mm | C40 | DERIVED | the sizing's slot depth, = gap inner radius - yoke inner radius. It assumes the stator's own bore IS the train bore, i.e. that the 30 mm train reservation costs no structural material. T3: it does. |
| `SpineWall` | 1.5 | mm | F9 | PROVISIONAL | T3: the structural spine tube that carries the machine between its two races. The stator core cannot double as the train-bore wall, because F9 reserves a clear 30 mm through the machine section -- so something has to be there and it is not the core. 1.5 mm of steel is the thin end of what carries the machine's bending; set with C32/C35. |
| `StatorBoreDia` | 30 | mm | F9 | DEFINED | the TRAIN-BORE reservation, not the stator core's own bore |
| `MachineODMax` | 92 | mm | C34 | DEFINED | hard ceiling, set by the annulus |
| `StackLen` | 28 | mm | C40 | PROVISIONAL | nominal of the 25-30 mm sizing band (L=25 -> 0.81 kg, L=30 -> 0.97 kg) |
| `Kt` | 0.362 | N*m/A | C14 | DEFINED | per ampere rms line current |
| `Kv` | 0.209 | V/(rad/s) | C15 | DEFINED | rms line-to-line |
| `BusVoltage` | 180 | V | C41 | DEFINED | 180 V nominal, below flight-minimum EMF |
| `PeakCurrentRms` | 15.9 | A | C18 | DERIVED | at 5.76 N*m peak torque |
| `HoldCurrentRms` | 6.5 | A | C18 | DERIVED | holding duty |
| `MachineMassLo` | 0.81 | kg | C40 | DERIVED | at L = 25 mm |
| `MachineMassHi` | 0.97 | kg | C40 | DERIVED | at L = 30 mm |

## BEARING

| alias | value | unit | criterion | status | basis |
|---|---:|---|---|---|---|
| `BrgBoreDia` | 46 | mm | C22 | PROVISIONAL | inner race bore seat; between the 30-50 mm band C26 names |
| `BrgInnerRaceOD` | 53 | mm | C22 | PROVISIONAL | inner race outer face |
| `BrgOuterRaceID` | 62 | mm | C22 | PROVISIONAL | outer race inner face |
| `BrgOuterRaceOD` | 69 | mm | C22 | PROVISIONAL | outer race outer face, presses into the ring |
| `BrgBallDia` | 4 | mm | C22 | PROVISIONAL | ball diameter |
| `BrgBallsPerRow` | 24 |  | C22 | PROVISIONAL | balls per row |
| `BrgRow1Z` | 14 | mm | C35 | PROVISIONAL | aft row station |
| `BrgRow2Z` | 72 | mm | C35 | PROVISIONAL | fore row station; the pair's separation sets the moment stiffness |
| `BrgRowWidth` | 8 | mm | C22 | PROVISIONAL | loaded race width per row |
| `BrgPreload` | 0 | N | C23 | PROVISIONAL | PLACEHOLDER — the one knob owning the C35 (>=122 N/um) vs C13 (Tf <= 0.10 N*m) tension; value set with C22 |
| `BrgStiffnessReq` | 122 | N/um | C35 | DERIVED | 24.5 kN radial / 0.20 mm allowable deflection, on the pair |
| `FrictionBudget` | 0.1 | N*m | C13 | DERIVED | flat across the speed envelope; load-dominated, not viscous |
| `PressFitClearance` | 0.02 | mm | CAD | PROVISIONAL | press-fit interfaces are MODELLED with a nominal clearance so the interference check reports real clashes only. Press fits, thread engagement and bond lines are the allowed interfaces. |

## RETENTION

| alias | value | unit | criterion | status | basis |
|---|---:|---|---|---|---|
| `RetTravel` | 0.1 | mm | C32 | PROVISIONAL | axial travel of the ring before the thrust collar takes the load. It must stay well inside the bearing's internal clearance and it does NOT affect the radial air gap. |
| `RetCollarThick` | 4 | mm | C32 | PROVISIONAL | thrust collar thickness; 212 kN across this face at ~230 MPa |
| `RetFaceBite` | 75 | mm^2/kN | C32 | DERIVED | FACE AREA PER kN of setback the collar must accept at a stated allowable bearing stress — recomputed against the measured load below |
| `RetBearingStress` | 300 | MPa | C32 | PROVISIONAL | allowable compressive stress on a hardened, ground thrust face |
| `RingThrustBoreDia` | 91.9 | mm | C32 | PROVISIONAL | the ring's bore over the aft band. NOT opened beyond the bearing bore: the collar's thrust face has to sit UNDER the ring's aft face, so the two must share a radius band, and a narrow band at the skin radius costs 245 MPa of contact stress where a wide one costs 56 MPa. The 0.03 kg the opening would have saved is not worth that. |
| `RetFaceID` | 26.5 | mm | C32 | DERIVED | inner edge of the thrust contact band. Set as low as the ring's aft recess allows, because contact stress falls directly with area: at 34.5 the margin is x1.3, at 26.5 it is x1.8. |
| `RingAftBoreDia` | 53 | mm | C32 | PROVISIONAL | the ring's bore over the aft recess band, below the bearing. Opened from the bearing bore to widen the C32 thrust face — the one place the ring can afford a few grams because it buys contact area directly. |
| `RetFaceOD` | 48.8 | mm | C32 | PROVISIONAL | outer edge of the thrust contact band, just inside the ring's skin |
| `CollarID` | 25.92 | mm | C32 | PROVISIONAL | the collar is a disc from the body's shoulder (r 25.9 + press fit) out to RetFaceOD, so the load reaches the body through a continuous section rather than a ring on stilts |

## LOADS

| alias | value | unit | criterion | status | basis |
|---|---:|---|---|---|---|
| `gAxial` | 15000 | g | E1 | PARAMETRIC | setback, [ref] |
| `gRadial` | 5000 | g | E2 | PARAMETRIC | radial launch load, [ref] |
| `SetbackRing` | 73.5 | kN | C26 | DERIVED | 0.5 kg ring x 15 000 g; scales 14.7 kN per 0.1 kg — recomputed from the CAD's own ring mass |
| `SetbackRadial` | 24.5 | kN | C26 | DERIVED | 0.5 kg ring x 5 000 g |
| `CanardSteady` | 18.1 | N | C8 | DERIVED | F_steer >= 18.1 N minimum over the guided window |
| `CanardTransient` | 85 | N | C28 | PROVISIONAL | [ref] launch transient |
| `AirGapDeflMax` | 0.2 | mm | C35 | DERIVED | gap 0.40 mm -> half the gap is the allowable relative deflection |
| `AxialPathStiff` | 367 | N/um | C35 | DERIVED | 73.5 kN / 0.20 mm — a structural-case spec, NOT a bearing spec |

## BODY

| alias | value | unit | criterion | status | basis |
|---|---:|---|---|---|---|
| `SpiderHoles` | 8 |  | CAD | PROVISIONAL | lightening holes per spider. T4: modelled solid, the body alone is 2.57 kg in steel against P9's 1.4 kg for the WHOLE kit, so every web that is not a load path gets a hole. |
| `SpiderHoleDia` | 10 | mm | CAD | PROVISIONAL | lightening hole diameter |
| `SpiderHolePCD` | 41 | mm | CAD | PROVISIONAL | hole pitch circle, midway between the train bore and the spider OD |
| `WebThickness` | 2 | mm | CAD | PROVISIONAL | stator end-plate thickness; a mounting face, not a structural member |

## FRONT_END

| alias | value | unit | criterion | status | basis |
|---|---:|---|---|---|---|
| `RadarFreq` | 24 | GHz | F2 | DEFINED | ISM, RF Doppler proximity |
| `GnssApertureDia` | 48 | mm | N3 | PROVISIONAL | rotationally symmetric aperture on the spin axis, elements combined |
| `NoseWallThick` | 2 | mm | CAD | PROVISIONAL | radome / fairing wall |
| `NoseCapLen` | 18 | mm | CAD | PROVISIONAL | length of the nose cap forward of the canard bay — the CAD computes the SHORTFALL against KitVisibleMax and reports it |

## STATIONS

| alias | value | unit | criterion | status | basis |
|---|---:|---|---|---|---|
| `ZSeat` | 0 | mm | CAD | DEFINED | datum origin |
| `ZThreadRoot` | -19.05 | mm | P6 | DERIVED | WellEngageTurns x pitch, into the well |
| `ZWellBottom` | -124.7 | mm | P7 | PARAMETRIC | intrusion limit |
| `ShoulderLen` | 6 | mm | CAD | PROVISIONAL | steep collar from the well thread out to the working diameter; it is also the seat's bearing face |
| `MachineInRingAft` | 20 | mm | CAD | PROVISIONAL | machine stack starts this far forward of the ring's aft face |
| `BrgRow1Inset` | 10 | mm | CAD | PROVISIONAL | aft bearing row, in from the ring aft face |
| `BrgRow2Inset` | 10 | mm | CAD | PROVISIONAL | fore bearing row, in from the ring fore face |
| `HubAftInset` | 10 | mm | CAD | PROVISIONAL | front hub starts this far forward of the ring aft face |

## Derived quantities

Recomputed on every load from the table above — change an input and these move with it.

| alias | value |
|---|---:|
| `AxialPathStiffMeasured` | 1116.9494 |
| `AxialPathStiffRatio` | 3.0435 |
| `BrgRowSeparation` | 60 |
| `CanardAspectRatio` | 0.3312 |
| `CanardChordFitMax` | 69.25 |
| `CanardFinForce` | 52.1169 |
| `CanardMeanChord` | 80 |
| `CanardSpanExposed` | 26.5 |
| `CanardTipR` | 75.5 |
| `CantCosSteer` | 0.9848 |
| `CantForceRatio10to16` | 1.5873 |
| `CantSinCtrl` | 0.1736 |
| `ChordOverrun` | 10.75 |
| `FSteerFromCos` | 102.6502 |
| `FSteerFromSin` | 18.1 |
| `KitVisibleOvershoot` | 10.75 |
| `KitVisibleReq` | 106 |
| `MachineODCheck` | 91.9 |
| `MachineODMargin` | 0.1 |
| `MachineSitsInRing` | true |
| `MachineToRingAftGap` | 20 |
| `MachineToRingForeGap` | 32 |
| `NoseLenAvail` | 9.25 |
| `NoseLenReq` | 20 |
| `NoseShortfall` | 10.75 |
| `OgiveRho` | 1342.6179 |
| `RBackironOut` | 45.95 |
| `RGapIn` | 39.35 |
| `RGapMid` | 39.55 |
| `RGapOut` | 39.75 |
| `RMagnetOut` | 41.25 |
| `RSpineOut` | 16.5 |
| `RTrainBore` | 15 |
| `RYokeIn` | 16.5 |
| `RYokeOut` | 21.2 |
| `RetFaceArea` | 1318.8327 |
| `RetFaceStress` | 169.3845 |
| `RetOverlapCheck` | true |
| `RetStressMargin` | 1.7711 |
| `RingLen` | 80 |
| `RingMassAssumed_C26` | 0.5 |
| `RingMassMeasured` | 1.5197 |
| `RingMassScaling` | 3.0393 |
| `RingR` | 49 |
| `RingRotatingMeasured` | 1.8764 |
| `RingWallThick` | 3.05 |
| `SetbackMeasured` | 223.3899 |
| `SetbackRotating` | 275.832 |
| `SlotAreaRatio` | 0.926 |
| `SlotDepth` | 18.15 |
| `SlotDepthLost` | 1.45 |
| `TorqueScaleFromT3` | 0.926 |
| `WellBoreArea` | 17237.2906 |
| `WellBoreAreaP6` | 18800 |
| `WellEngageLen` | 19.05 |
| `WellFlankArea` | 1117.9713 |
| `WellFlankAreaP6` | 1120 |
| `WellPitch` | 2.1167 |
| `WellPitchDia` | 49.4252 |
| `WellSeatArea` | 506.2991 |
| `WellSeatAreaP6` | 500 |
| `WellSeatIDImpliedByP6` | 44.091 |
| `ZBrgRow1` | 16 |
| `ZBrgRow2` | 76 |
| `ZFrontHubAft` | 16 |
| `ZFrontHubFore` | 106 |
| `ZMachineAft` | 26 |
| `ZMachineFore` | 54 |
| `ZRingAft` | 6 |
| `ZRingFore` | 86 |
| `ZShoulderFore` | 6 |

## The provisional set — what closes each one

| alias | criterion | what closes it |
|---|---|---|
| `BrgBallDia` | C22 | see basis — criterion is OPEN in the register |
| `BrgBallsPerRow` | C22 | see basis — criterion is OPEN in the register |
| `BrgBoreDia` | C22 | see basis — criterion is OPEN in the register |
| `BrgInnerRaceOD` | C22 | see basis — criterion is OPEN in the register |
| `BrgOuterRaceID` | C22 | see basis — criterion is OPEN in the register |
| `BrgOuterRaceOD` | C22 | see basis — criterion is OPEN in the register |
| `BrgPreload` | C23 | see basis — criterion is OPEN in the register |
| `BrgRow1Inset` | CAD | see basis — criterion is OPEN in the register |
| `BrgRow1Z` | C35 | see basis — criterion is OPEN in the register |
| `BrgRow2Inset` | CAD | see basis — criterion is OPEN in the register |
| `BrgRow2Z` | C35 | see basis — criterion is OPEN in the register |
| `BrgRowWidth` | C22 | see basis — criterion is OPEN in the register |
| `CanardArea` | C4 | see basis — criterion is OPEN in the register |
| `CanardChordRoot` | C4 | see basis — criterion is OPEN in the register |
| `CanardRootThick` | C5 | see basis — criterion is OPEN in the register |
| `CanardThick` | C6 | see basis — criterion is OPEN in the register |
| `CanardTransient` | C28 | see basis — criterion is OPEN in the register |
| `CantCtrl` | C3 | see basis — criterion is OPEN in the register |
| `CantSteer` | C2 | see basis — criterion is OPEN in the register |
| `CollarID` | C32 | see basis — criterion is OPEN in the register |
| `GnssApertureDia` | N3 | see basis — criterion is OPEN in the register |
| `HubAftInset` | CAD | see basis — criterion is OPEN in the register |
| `MachineInRingAft` | CAD | see basis — criterion is OPEN in the register |
| `NoseCapLen` | CAD | see basis — criterion is OPEN in the register |
| `NoseWallThick` | CAD | see basis — criterion is OPEN in the register |
| `PressFitClearance` | CAD | see basis — criterion is OPEN in the register |
| `RetBearingStress` | C32 | see basis — criterion is OPEN in the register |
| `RetCollarThick` | C32 | see basis — criterion is OPEN in the register |
| `RetFaceOD` | C32 | see basis — criterion is OPEN in the register |
| `RetTravel` | C32 | see basis — criterion is OPEN in the register |
| `RingAftBoreDia` | C32 | see basis — criterion is OPEN in the register |
| `RingOD` | C7 | see basis — criterion is OPEN in the register |
| `RingThrustBoreDia` | C32 | see basis — criterion is OPEN in the register |
| `ShoulderLen` | CAD | see basis — criterion is OPEN in the register |
| `SpiderHoleDia` | CAD | see basis — criterion is OPEN in the register |
| `SpiderHolePCD` | CAD | see basis — criterion is OPEN in the register |
| `SpiderHoles` | CAD | see basis — criterion is OPEN in the register |
| `SpigotClearance` | P6 | see basis — criterion is OPEN in the register |
| `SpineWall` | F9 | see basis — criterion is OPEN in the register |
| `StackLen` | C40 | see basis — criterion is OPEN in the register |
| `ThreadClearance` | P6 | see basis — criterion is OPEN in the register |
| `WebThickness` | CAD | see basis — criterion is OPEN in the register |
| `WellBoreDia` | P6 | see basis — criterion is OPEN in the register |
| `WellEngageTurns` | P6 | see basis — criterion is OPEN in the register |
| `WellFlankBand` | P6 | see basis — criterion is OPEN in the register |

