#!/usr/bin/env python

import sys, os

mC1 = mN2 = sys.argv[1]
mL  = sys.argv[2]
mN1 = sys.argv[3]

decouple = 10000.
mQ = mG = decouple
mA = mB1 = mB2 = mT1 = mT2 = mN3 = mN4 = mC2 = mlepR = decouple

print '''#
#
BLOCK DCINFO  # Decay Program information
     1   SDECAY/HDECAY # decay calculator
     2   1.3b  /3.4    # version number
#
BLOCK SPINFO  # Spectrum calculator information
     1   SuSpect     # RGE +Spectrum calculator            
     2   2.41        # version number                      
#
BLOCK MODSEL  # Model selection
     1     1   # #SUGRA                                            
#
BLOCK SMINPUTS  # Standard Model inputs
         1     1.27934000E+02   # alpha_em^-1(M_Z)^MSbar
         2     1.16639000E-05   # G_F [GeV^-2]
         3     1.17200000E-01   # alpha_S(M_Z)^MSbar
         4     9.11870000E+01   # M_Z pole mass
         5     4.25000000E+00   # mb(mb)^MSbar
         6     1.72500000E+02   # mt pole mass
         7     1.77710000E+00   # mtau pole mass
#
BLOCK MINPAR  # Input parameters - minimal models
         1     5.00000000E+02   # m0                  
         2     5.00000000E+03   # m_1                 
         3     1.00000000E+01   # tanbeta(mZ)         
         4     1.00000000E+00   # sign(mu)            
         5     0.00000000E+00   # A0                  
#
BLOCK EXTPAR  # Input parameters - non-minimal models
         0     7.28047708E+03   # EWSB                
#
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
        24     8.05067070E+01   # W+
        25     1.25776468E+02   # h
        35     {mA}   # H
        36     {mA}   # A
        37     {mA}   # H+
         5     {mA}   # b-quark pole mass calculated from mb(mb)_Msbar
   1000001     {mQ}   # ~d_L
   2000001     {mQ}   # ~d_R
   1000002     {mQ}   # ~u_L
   2000002     {mQ}   # ~u_R
   1000003     {mQ}   # ~s_L
   2000003     {mQ}   # ~s_R
   1000004     {mQ}   # ~c_L
   2000004     {mQ}   # ~c_R
   1000005     {mB1}   # ~b_1
   2000005     {mB2}   # ~b_2
   1000006     {mT1}   # ~t_1
   2000006     {mT2}   # ~t_2
   1000011     {mL}   # ~e_L
   2000011     {mlepR}   # ~e_R
   1000012     {mL}   # ~nu_eL
   1000013     {mL}   # ~mu_L
   2000013     {mlepR}   # ~mu_R
   1000014     {mL}   # ~nu_muL
   1000015     {mL}   # ~tau_1
   2000015     {mlepR}   # ~tau_2
   1000016     {mL}   # ~nu_tauL
   1000021     {mG}   # ~g
   1000022     {mN1}   # ~chi_10
   1000023     {mN2}   # ~chi_20
   1000025    -{mN3}   # ~chi_30
   1000035     {mN4}   # ~chi_40
   1000024     {mC1}   # ~chi_1+
   1000037     {mC2}   # ~chi_2+
#
BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     9.99888558E-01   # N_11
  1  2    -3.58719241E-04   # N_12
  1  3     1.30051173E-02   # N_13
  1  4    -7.32188922E-03   # N_14
  2  1     1.86828359E-03   # N_21
  2  2     9.94599551E-01   # N_22
  2  3    -7.71134853E-02   # N_23
  2  4     6.94388446E-02   # N_24
  3  1     4.01633535E-03   # N_31
  3  2    -5.45852312E-03   # N_32
  3  3    -7.07055573E-01   # N_33
  3  4    -7.07125512E-01   # N_34
  4  1     1.42565904E-02   # N_41
  4  2    -1.03642700E-01   # N_42
  4  3    -7.02820599E-01   # N_43
  4  4     7.03632110E-01   # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1    -9.94028426E-01   # U_11
  1  2     1.09121443E-01   # U_12
  2  1     1.09121443E-01   # U_21
  2  2     9.94028426E-01   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1    -9.95160413E-01   # V_11
  1  2     9.82636856E-02   # V_12
  2  1     9.82636856E-02   # V_21
  2  2     9.95160413E-01   # V_22
#
BLOCK STOPMIX  # Stop Mixing Matrix
  1  1     6.10404586E-02   # cos(theta_t)
  1  2     9.98135293E-01   # sin(theta_t)
  2  1    -9.98135293E-01   # -sin(theta_t)
  2  2     6.10404586E-02   # cos(theta_t)
#
BLOCK SBOTMIX  # Sbottom Mixing Matrix
  1  1     9.94848083E-01   # cos(theta_b)
  1  2     1.01376978E-01   # sin(theta_b)
  2  1    -1.01376978E-01   # -sin(theta_b)
  2  2     9.94848083E-01   # cos(theta_b)
#
BLOCK STAUMIX  # Stau Mixing Matrix
  1  1     1.24331161E-02   # cos(theta_tau)
  1  2     9.99922706E-01   # sin(theta_tau)
  2  1    -9.99922706E-01   # -sin(theta_tau)
  2  2     1.24331161E-02   # cos(theta_tau)
#
BLOCK ALPHA  # Higgs mixing
          -1.05523503E-01   # Mixing angle in the neutral Higgs boson sector
#
BLOCK HMIX Q=  7.28047708E+03  # DRbar Higgs Parameters
         1     4.69053396E+03   # mu(Q)               
         2     9.44789163E+00   # tanbeta(Q)          
         3     2.43906078E+02   # vev(Q)              
         4     3.33677648E+07   # MA^2(Q)             
#
BLOCK GAUGE Q=  7.28047708E+03  # The gauge couplings
     1     3.67061657E-01   # gprime(Q) DRbar
     2     6.30911545E-01   # g(Q) DRbar
     3     9.63087063E-01   # g3(Q) DRbar
#
BLOCK AU Q=  7.28047708E+03  # The trilinear couplings
  1  1    -9.03120428E+03   # A_u(Q) DRbar
  2  2    -9.03120428E+03   # A_c(Q) DRbar
  3  3    -7.24008031E+03   # A_t(Q) DRbar
#
BLOCK AD Q=  7.28047708E+03  # The trilinear couplings
  1  1    -1.07441942E+04   # A_d(Q) DRbar
  2  2    -1.07441942E+04   # A_s(Q) DRbar
  3  3    -1.01154712E+04   # A_b(Q) DRbar
#
BLOCK AE Q=  7.28047708E+03  # The trilinear couplings
  1  1    -2.66585482E+03   # A_e(Q) DRbar
  2  2    -2.66585482E+03   # A_mu(Q) DRbar
  3  3    -2.65331805E+03   # A_tau(Q) DRbar
#
BLOCK Yu Q=  7.28047708E+03  # The Yukawa couplings
  1  1     0.00000000E+00   # y_u(Q) DRbar
  2  2     0.00000000E+00   # y_c(Q) DRbar
  3  3     7.92398223E-01   # y_t(Q) DRbar
#
BLOCK Yd Q=  7.28047708E+03  # The Yukawa couplings
  1  1     0.00000000E+00   # y_d(Q) DRbar
  2  2     0.00000000E+00   # y_s(Q) DRbar
  3  3     1.23634076E-01   # y_b(Q) DRbar
#
BLOCK Ye Q=  7.28047708E+03  # The Yukawa couplings
  1  1     0.00000000E+00   # y_e(Q) DRbar
  2  2     0.00000000E+00   # y_mu(Q) DRbar
  3  3     9.76024869E-02   # y_tau(Q) DRbar
#
BLOCK MSOFT Q=  7.28047708E+03  # The soft SUSY breaking masses at the scale Q
         1     2.32031165E+03   # M_1                 
         2     4.06028931E+03   # M_2                 
         3     9.59599890E+03   # M_3                 
        21     9.19129817E+06   # M^2_Hd              
        22    -2.08944799E+07   # M^2_Hu              
        31     3.18275914E+03   # M_eL                
        32     3.18275914E+03   # M_muL               
        33     3.17553299E+03   # M_tauL              
        34     1.86712148E+03   # M_eR                
        35     1.86712148E+03   # M_muR               
        36     1.84177235E+03   # M_tauR              
        41     8.45237387E+03   # M_q1L               
        42     8.45237387E+03   # M_q2L               
        43     7.86386925E+03   # M_q3L               
        44     8.03151501E+03   # M_uR                
        45     8.03151501E+03   # M_cR                
        46     6.73955076E+03   # M_tR                
        47     7.97436780E+03   # M_dR                
        48     7.97436780E+03   # M_sR                
        49     7.93910496E+03   # M_bR                
#
#
#
#         PDG            Width
DECAY   1000022          0.0                     # neutralino1 decays
#
DECAY   1000024     1.72043260E+00   # C1 decays
#          BR         NDA      ID1       ID2
     1.666666E-01     2    -1000011          12     # BR(~chi_1+ -> ~e+  ne)
     1.666666E-01     2     1000012         -11     # BR(~chi_1+ -> ~ne  e+)     
     1.666666E-01     2    -1000013          14     # BR(~chi_1+ -> ~mu+  nmu)
     1.666666E-01     2     1000014         -13     # BR(~chi_1+ -> ~nmu  mu+)     
     1.666666E-01     2    -1000015          16     # BR(~chi_1+ -> ~tau+  ntau)
     1.666666E-01     2     1000016         -15     # BR(~chi_1+ -> ~ntau  tau+)     
#
DECAY   1000023     1.72043260E+00   # N2 decays
#          BR         NDA      ID1       ID2
     8.333333E-02     2     1000011         -11     # BR(~chi_20 -> ~e-  e+)
     8.333333E-02     2    -1000011          11     # BR(~chi_20 -> ~e+  e-)
     8.333333E-02     2     1000012         -12     # BR(~chi_20 -> ~ne*  ne)
     8.333333E-02     2    -1000012          12     # BR(~chi_20 -> ~ne  ne*)
     8.333333E-02     2     1000013         -13     # BR(~chi_20 -> ~mu-  mu+)
     8.333333E-02     2    -1000013          13     # BR(~chi_20 -> ~mu+  mu-)
     8.333333E-02     2     1000014         -14     # BR(~chi_20 -> ~nmu*  nmu)
     8.333333E-02     2    -1000014          14     # BR(~chi_20 -> ~nmu  nmu*)
     8.333333E-02     2     1000015         -15     # BR(~chi_20 -> ~tau-  tau+)
     8.333333E-02     2    -1000015          15     # BR(~chi_20 -> ~tau+  tau-)
     8.333333E-02     2     1000016         -16     # BR(~chi_20 -> ~ntau*  ntau)
     8.333333E-02     2    -1000016          16     # BR(~chi_20 -> ~ntau  ntau*)
#
DECAY   1000011     1.72043260E+00   # e~ decays
#          BR         NDA      ID1       ID2
       1.0000E+00     2     1000022          11     # BR(~e- -> ~chi_10  e-)
DECAY   1000012     1.72043260E+00   # ne~ decays
#          BR         NDA      ID1       ID2
       1.0000E+00     2     1000022          12     # BR(~ne -> ~chi_10  ne)
DECAY   1000013     1.72043260E+00   # mu~ decays
#          BR         NDA      ID1       ID2
       1.0000E+00     2     1000022          13     # BR(~mu- -> ~chi_10  mu-)
DECAY   1000014     1.72043260E+00   # nmu~ decays
#          BR         NDA      ID1       ID2
       1.0000E+00     2     1000022          14     # BR(~nmu -> ~chi_10  nmu)
DECAY   1000015     1.72043260E+00   # tau~ decays
#          BR         NDA      ID1       ID2
       1.0000E+00     2     1000022          15     # BR(~tau- -> ~chi_10  tau-)
DECAY   1000016     1.72043260E+00   # ntau~ decays
#          BR         NDA      ID1       ID2
       1.0000E+00     2     1000022          16     # BR(~ntau -> ~chi_10  ntau)
'''.format(mN1=mN1, mQ=mQ, mG=mG, mA=mA, mB1=mB1, mB2=mB2, mT1=mT1, mT2=mT2, mL=mL, mN2=mN2, mN3=mN3, mN4=mN4, mC1=mC1, mC2=mC2, mlepR=mlepR)


