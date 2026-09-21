# DRISHTI-PGK — Parts

Every solid in the P4 build: what it is called, which band of the architecture it belongs to, what it is made of, what it weighs, and what it does. **Generated** by `python3 design/cad/write_traceability.py` from `part_index.py` (names, groups, materials) and `out/measured.json` (masses, measured off the solids as each phase builds).

The same three facts are carried by the model itself: every part is created through `cadlib.add_part()`, so the FreeCAD tree shows the name below, the assembly groups parts by the same band, and the colour here is the colour in the model and in the deck renders. Nothing in this file is typed twice.

**On the masses:** they are measured, not budgeted. The mass budget itself is still open — the rollup runs about ×2 over P9 as modelled (findings T4/T5/T9/T10 in `design/07-cad-evidence.md`) — so quote these as *what the model weighs*, never as *what the kit will weigh*.


## 1 Body side — turns with the shell

*Every part here turns with the shell.*

| Part | Code | Material | Colour | Mass | What it does |
|---|---|---|---|---:|---|
| **A10 Front hub** | `A10_Front_Hub` | steel | `#5d6a78` | 433 g | Front structure: carries the radome and the aperture above the ring. |
| **A11 Retention collar** | `A11_Retention_Collar` | steel | `#6f7b87` | 138 g | The seat that catches the ring's setback load, so the flight bearings never see launch acceleration. |
| **A1 Kit body** | `A1_KitBody` | steel | `#48535f` | 696 g | The spigot that screws into the fuze well, and the housing above it. Every body-side part hangs off this one. |
| **A2 Stator core** | `A2_Stator_Core` | soft magnetic composite | `#8a949e` | 296 g | Twelve-slot stator core — the body half of the machine. |
| **A3 Windings** | `A3_Windings` | copper | `#c27a25` | 365 g | The twelve coils in the stator slots. |
| **A4 Bearing inner races** | `A4_Brg_Inner_Races` | steel | `#a7b0ba` | 68 g | Inner raceways of the two thin-section bearings, on the body side. |
| **A5 Avionics stack** | `A5_Avionics_Stack` | electronics, bulk | `#2f7d6b` | 8 g | Guidance and control boards, stacked as rings around the train bore. |
| **A6 Dump stage** | `A6_Dump_Stage` | electronics, bulk | `#3f8f7b` | 20 g | Chopper dump — sheds the energy the machine generates. |
| **A7 Buffer** | `A7_Buffer` | electronics, bulk | `#57a08c` | 54 g | Supercapacitor buffer: the fireset reservoir, hold-up, and the motoring bursts. |
| **A8 Setter coil** | `A8_Setter_Coil` | copper | `#a4551a` | 47 g | Receives the inductive setter message on the gun line. |
| **A9 Detonator** | `A9_Detonator` | steel | `#7a2f2f` | 16 g | Detonator, on the axis at the bottom of the well. |
| **A9 Impact switch** | `A9_Impact_Switch` | steel | `#9c4040` | 15 g | Impact switch, on the centreline. |
| **A9 S/A rotor** | `A9_SA_Rotor` | steel | `#b04a4a` | 29 g | Safety-and-arming rotor — the out-of-line interruption in the train. |
| **C2 Link, body half** | `C2_Link_Body` | link potting | `#5d8bb3` | 33 g | Body half of the contactless link. |
| **C3 Harness** | `C3_Harness` | electronics, bulk | `#8a6bb0` | 2 g | Interconnect between the well internals and the front end. |
| **D1 Radome** | `D1_Radome` | dielectric | `#d9a441 @ 55% transparent` | 12 g | Radome over the fuze aperture. |
| **D2 GNSS aperture** | `D2_Gnss_Aperture` | electronics, bulk | `#3f6ea8 @ 15% transparent` | 1 g | GNSS aperture, centred on the spin axis so spin does not modulate it. |
| | | | | **2231 g** | |

## 2 Ring side — de-spun, carries the fins

*Every part here is de-spun: it turns relative to the body, on the bearings, and it is what the machine acts on.*

| Part | Code | Material | Colour | Mass | What it does |
|---|---|---|---|---:|---|
| **B1 Ring carrier** | `B1_Ring_Carrier` | steel | `#0b5cad` | 1520 g | The de-spun ring. One billet with the four fins; carries the magnets and the outer races. |
| **B2 Rotor backiron** | `B2_Rotor_Backiron` | steel | `#3d5a75` | 283 g | Closes the magnetic circuit on the ring. |
| **B3 Magnets** | `B3_Magnets` | NdFeB | `#2b2f45` | 74 g | Fourteen magnets — seven pole pairs. |
| **B4 Bearing outer races** | `B4_Brg_Outer_Races` | steel | `#98a3ae` | 90 g | Outer raceways of the two bearings, on the ring. |
| **B5 Fin, control** | `B5_Canard_Ctrl` | steel | `#4f9ad6` | 2 × 148 g = **296 g** | Control fin. Opposite cant across the pair, so the two fins make net roll torque and no net force — this is the pair the machine works against, and it is why the kit generates. |
| **B5 Fin, master** | `B5_Canard_Master` | steel | `#1f7ecd` | — | The fin before placement, at zero azimuth and unit cant sign. It is copied and rotated to make the four; it is not itself a part. |
| **B5 Fin, steering** | `B5_Canard_Steer` | steel | `#1f7ecd` | 2 × 148 g = **296 g** | Steering fin. Equal cant across the pair, so the two fins make net side force and their roll torques cancel. |
| **C2 Link, ring half** | `C2_Link_Ring` | link potting | `#8f6fb5` | 36 g | Ring half of the contactless link — power by transformer, data by light. |
| | | | | **2595 g** | |

## 3 Between the two bodies

*The rolling elements — the only load path between the two bodies.*

| Part | Code | Material | Colour | Mass | What it does |
|---|---|---|---|---:|---|
| **C1 Balls and cage** | `C1_Balls_Cage` | steel | `#cdd5dd` | 13 g | Both bearing rows. The only load path between the two bodies. |
| | | | | **13 g** | |

## 9 Reference — not a kit part

*Not kit parts. Drawn so the constraints can be seen.*

| Part | Code | Material | Colour | Mass | What it does |
|---|---|---|---|---:|---|
| **D3 Radar keep-out** | `D3_Radar_Keepout` | keep-out volume | `#8a949e @ 88% transparent` | — | Not a part: the volume the radar needs clear of metal ahead of it. It is drawn so the constraint can be seen rather than asserted. |
| **REF Reference shell** | `REF_Shell_155mm` | contour model | `#b9c2cc @ 78% transparent` | — | The 155 mm shell the kit is drawn against. Context only — never a kit part, and its mass is never quoted. |

---

## How it goes together

- The kit **replaces the fuze**: it screws into the MIL-STD-333B well on the 2″-12 UNS-2A thread that an in-service fuze uses. It is the same two bodies in relative rotation for the whole flight, and everything above is either body side, ring side, or between them.

- The **ring side** carries the four fins, the magnets and the outer races; the **body side** carries the coils, the inner races, the retention collar, the boards and the fuze train. The interface between the two is mechanical through the bearings (100 %% of the load, no torque) and electromagnetic through the machine (100 %% of the torque, no load).

- **Nothing moves except the ring.** The fins are fixed at one cant each; there is no actuator, no linkage and no deployment. The ring's angle is the only thing commanded.

- The **fuze train runs on the centreline** (F9): every other part is annular about it. The boards, the dump, the buffer and the harness all live in the annulus between the train bore and the well wall.

- The launch load does **not** pass through the flight bearings: the ring travels its clearance and seats on the retention collar, which is sized against the measured rotating mass.
