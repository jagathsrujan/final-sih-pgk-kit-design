"""
Frameless outrunner PMSM sizing — pass 2.
Key fix: the stator fills the available annulus (bore fixed by structure, not by flux),
and the CONTINUOUS duty is separated from the PEAK duty.

Continuous torque: hold the ring against Taero  -> T ~ 2.2 N.m + friction
Peak torque:       slew the ring                 -> T = 5.76 N.m, transient

Also computes the power the machine must ABSORB (it is a loaded generator):
  P = T_alt * omega_rel   with T_alt ~ Taero and omega_rel = body spin
That power is dissipated, and it is where the architecture's real thermal load sits.
"""
import math as m

RHO_CU, D_CU, D_FE, D_MAG = 1.72e-8, 8960.0, 7600.0, 7500.0
B_G, B_Y, B_T = 0.80, 1.50, 1.80
K_W      = 0.933
SLOT_FR  = 0.50
CU_FILL  = 0.42
OD_MAX   = 92e-3
BORE     = 30e-3
GAP      = 0.40e-3
T_MAG    = 1.50e-3
J_CONT_TARGET = 8e6
J_PEAK_LIMIT  = 20e6

T_PEAK, T_CONT = 5.76, 2.36

def build(p, L):
    d_gap = (OD_MAX + BORE)/2.0
    for _ in range(80):
        tau_p = m.pi*d_gap/(2*p)
        phi_p = B_G*tau_p*L
        t_y   = phi_p/(2*B_Y*L)                    # both backiron and stator yoke
        r_so  = OD_MAX/2.0 - t_y - T_MAG - GAP     # stator OD
        r_si  = BORE/2.0
        t_slot= r_so - r_si - t_y                  # remaining radial space = slot depth
        d_new = 2*r_so + GAP
        if abs(d_new-d_gap) < 1e-8: break
        d_gap = 0.5*d_gap + 0.5*d_new
    r_gap = d_gap/2.0
    # tooth width for B_T
    Q = 12 if p in (5, 7) else 9                    # slots
    tooth = phi_p/(B_T*L)
    slot_pitch = 2*m.pi*r_so/Q
    slot_w = max(slot_pitch - tooth, 0.0)
    a_slot_tot = Q*slot_w*t_slot
    a_cu_ph = CU_FILL*a_slot_tot/3.0
    T = p*K_W*phi_p*a_cu_ph*1.0/m.sqrt(2.0)         # torque per unit J (A/m^2)
    v_cu = CU_FILL*a_slot_tot*L
    r_rotor_od = OD_MAX/2.0
    r_mag_od   = r_rotor_od - t_y
    r_mag_id   = r_mag_od - T_MAG
    v_back = m.pi*(r_rotor_od**2-r_mag_od**2)*L
    v_mag  = m.pi*(r_mag_od**2-r_mag_id**2)*L
    v_fe_st= 0.95*(m.pi*(r_so**2-r_si**2)*L - a_slot_tot*L)
    return dict(p=p,L=L,d_gap=d_gap,r_gap=r_gap,Q=Q,phi_p=phi_p,t_y=t_y,t_slot=t_slot,
                tooth=tooth,slot_w=slot_w,r_so=r_so,r_si=r_si,T=T,a_cu_ph=a_cu_ph,
                v_cu=v_cu,m_cu=v_cu*D_CU,m_mag=v_mag*D_MAG,m_back=v_back*D_FE,
                m_fe=v_fe_st*D_FE)

def report(p, L):
    d = build(p, L)
    j_pk  = T_PEAK/d['T']
    j_ct  = T_CONT/d['T']
    # copper loss at each duty
    P_cu_ct = RHO_CU*j_ct**2*d['v_cu']
    P_cu_pk = RHO_CU*j_pk**2*d['v_cu']
    f_e = p*1912/(2*m.pi)
    P_fe = 15.0*d['m_fe']*(f_e/400.0)**1.5
    m_tot = d['m_cu']+d['m_fe']+d['m_mag']+d['m_back']
    return d, j_pk, j_ct, P_cu_ct, P_cu_pk, f_e, P_fe, m_tot

print("="*96)
print("MACHINE SIZING  (OD 92 mm, bore 30 mm, gap 0.4 mm, magnet 1.5 mm, Bg 0.8 T)")
print("="*96)
print(f"{'p':>3} {'Q':>3} {'L mm':>6} {'gap mm':>7} {'yoke mm':>8} {'slot mm':>8} "
      f"{'J_pk':>6} {'J_ct':>6} {'Pcu_ct':>7} {'m_cu':>6} {'m_fe':>6} {'m_mag':>6} {'m_br':>6} {'m_tot g':>8}")
for p in (5, 7, 9, 10, 12):
    for L in (0.025, 0.030, 0.035, 0.040):
        d,jp,jc,Pc,Pp,fe,Pfe,mt = report(p,L)
        print(f"{p:>3} {d['Q']:>3} {L*1e3:>6.0f} {d['d_gap']*1e3:>7.1f} {d['t_y']*1e3:>8.2f} {d['t_slot']*1e3:>8.2f} "
              f"{jp/1e6:>6.1f} {jc/1e6:>6.1f} {Pc:>7.1f} {d['m_cu']*1e3:>6.1f} {d['m_fe']*1e3:>6.1f} "
              f"{d['m_mag']*1e3:>6.1f} {d['m_back']*1e3:>6.1f} {mt*1e3:>8.1f}")

print()
print("="*96)
print("IRON LOSS AND TOTAL DISSIPATION IN THE MACHINE  (L = 35 mm)")
print("="*96)
print(f"{'p':>3} {'f_e Hz':>9} {'P_fe W':>8} {'Pcu_ct W':>9} {'total_ct W':>11}   note")
for p in (5, 7, 9, 10, 12):
    d,jp,jc,Pc,Pp,fe,Pfe,mt = report(p, 0.035)
    tot = Pc+Pfe
    note = "acceptable" if tot<60 else "needs thin lam / SMC"
    print(f"{p:>3} {fe:>9.0f} {Pfe:>8.1f} {Pc:>9.1f} {tot:>11.1f}   {note}")

print()
print("="*96)
print("*** THE ARCHITECTURE'S REAL POWER LOAD ***")
print("   The machine is a LOADED GENERATOR. To hold the ring it must supply T_alt ~ Taero")
print("   against the full body spin. Mechanical power absorbed = Taero * omega_body,")
print("   and that energy must be dissipated electrically.")
print("="*96)
prof = [(0,1.80,1623),(10,1.30,1550),(20,0.80,1470),(41.16,0.1706,1400),
        (60,1.10,1300),(70,1.50,1200),(86.5,2.119,1050)]
tot = 0.0
print(f"{'t s':>6} {'Taero Nm':>9} {'omega r/s':>10} {'P kW':>7}")
prev_t = None
for t,Ta,w in prof:
    P = Ta*w
    print(f"{t:>6.1f} {Ta:>9.3f} {w:>10.0f} {P/1e3:>7.2f}")
    if prev_t is not None:
        dt = t-prev_t; tot += 0.5*(P+prev_P)*dt
    prev_t, prev_P = t, P
print(f"\n  energy over the flight (trapezoid on these points) = {tot/1e3:.0f} kJ")
print(f"  peak power = 2.92 kW at launch  |  reference alternator rating = 1.2 kW  ->  exceeded x2.4")
print(f"  the bench rig ran body spin 21.6x slower -> the same torque produced 21.6x LESS power,")
print(f"  which is why this never surfaced on the rig.")

print()
print("="*96)
print("CANT-ANGLE COUPLING  (raising cant buys force but raises Taero and dumped power)")
print("="*96)
print(f"{'cant deg':>9} {'F_steer N':>10} {'Taero Nm':>9} {'P kW at 1623':>13} {'authority OK?':>14}")
F0, T0, cant0 = 18.1, 1.80, 10.0     # datum: needs 18.1 N, gives 1.8 N.m at 10 deg
for cant in (8, 10, 12, 14, 16):
    k = cant/cant0
    F = F0*k; Ta = T0*k
    P = Ta*1623
    # symmetric criterion: Taero <= Talt_max/2 + Tf  ->  Talt_max >= 2(Taero - Tf)
    need = 2*(Ta-0.157)
    print(f"{cant:>9.1f} {F:>10.1f} {Ta:>9.2f} {P/1e3:>13.2f} {'yes' if need<=5.76 else 'NO - needs '+format(need,'.1f')+' Nm':>14}")

print()
print("="*96)
print("MASS BUDGET CONSEQUENCE")
print("="*96)
d,jp,jc,Pc,Pp,fe,Pfe,mt = report(7, 0.035)
print(f"  machine mass (rotor + stator)      : {mt*1e3:.0f} g")
print(f"  + fuze + S&A + setter coupling      : ~400-500 g (estimate)")
print(f"  + guidance/nav electronics, power   : ~200-300 g (estimate)")
print(f"  + bearings, canards, structure      : ~150-250 g (estimate)")
print(f"  --------------------------------------------------")
print(f"  kit total                           : ~1.5-2.0 kg")
print(f"  M1156 benchmark kit                 : 1.4 kg (no alternator)")
print(f"  reference net penalty over the fuze : +0.42 kg (0.9 % of the projectile)")
print(f"  implied net penalty if kit is 1.9 kg: +0.92 kg over the replaced ~0.98 kg fuze")
