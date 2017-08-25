#!/usr/bin/env python

import sys, os

rootS = sys.argv[1]
nev = sys.argv[2]

if rootS == '8': energy = 4000.0
if rootS == '13': energy = 6500.0
if rootS == '14': energy = 7000.0

print '''#*********************************************************************
#                       MadGraph5_aMC@NLO                            *
#                                                                    *
#                     run_card.dat MadEvent                          *
#                                                                    *
#  This file is used to set the parameters of the run.               *
#                                                                    *
#  Some notation/conventions:                                        *
#                                                                    *
#   Lines starting with a '# ' are info or comments                  *
#                                                                    *
#   mind the format:   value    = variable     ! comment             *
#*********************************************************************
#
#*******************                                                 
# Running parameters
#*******************                                                 
#                                                                    
#*********************************************************************
# Tag name for the run (one word)                                    *
#*********************************************************************
  tag_1     = run_tag ! name of the run 
#*********************************************************************
# Number of events and rnd seed                                      *
# Warning: Do not generate more than 1M events in a single run       *
# If you want to run Pythia, avoid more than 50k events in a run.    *
#*********************************************************************
  {nev} = nevents ! Number of unweighted events requested 
  0   = iseed   ! rnd seed (0=assigned automatically=default))
#*********************************************************************
# Collider type and energy                                           *
# lpp: 0=No PDF, 1=proton, -1=antiproton, 2=photon from proton,      *
#                                         3=photon from electron     *
#*********************************************************************
     1        = lpp1    ! beam 1 type 
     1        = lpp2    ! beam 2 type
     {energy}     = ebeam1  ! beam 1 total energy in GeV
     {energy}     = ebeam2  ! beam 2 total energy in GeV
#*********************************************************************
# Beam polarization from -100 (left-handed) to 100 (right-handed)    *
#*********************************************************************
     0.0     = polbeam1 ! beam polarization for beam 1
     0.0     = polbeam2 ! beam polarization for beam 2
#*********************************************************************
# PDF CHOICE: this automatically fixes also alpha_s and its evol.    *
#*********************************************************************
     nn23lo1    = pdlabel     ! PDF set                                     
     230000    = lhaid     ! if pdlabel=lhapdf, this is the lhapdf number
#*********************************************************************
# Renormalization and factorization scales                           *
#*********************************************************************
 False = fixed_ren_scale  ! if .true. use fixed ren scale
 False        = fixed_fac_scale  ! if .true. use fixed fac scale
 91.188  = scale            ! fixed ren scale
 91.188  = dsqrt_q2fact1    ! fixed fact scale for pdf1
 91.188  = dsqrt_q2fact2    ! fixed fact scale for pdf2
 -1 = dynamical_scale_choice ! Choose one of the preselected dynamical choices
 1.0  = scalefact        ! scale factor for event-by-event scales
#*********************************************************************
# Type and output format
#*********************************************************************
  False     = gridpack  !True = setting up the grid pack
  -1.0 = time_of_flight ! threshold (in mm) below which the invariant livetime is not written (-1 means not written)
  3.0 = lhe_version       ! Change the way clustering information pass to shower.        
  True = clusinfo         ! include clustering tag in output
  average =  event_norm       ! average/sum. Normalization of the weight in the LHEF

#*********************************************************************
# Matching parameter (MLM only)
#*********************************************************************
 0 = ickkw            ! 0 no matching, 1 MLM
 1.0 = alpsfact         ! scale factor for QCD emission vx
 False = chcluster        ! cluster only according to channel diag
 4 = asrwgtflavor     ! highest quark flavor for a_s reweight
 False  = auto_ptj_mjj  ! Automatic setting of ptj and mjj if xqcut >0
                                   ! (turn off for VBF and single top processes) 
 0.0   = xqcut   ! minimum kt jet measure between partons
#*********************************************************************
#
#*********************************************************************
# handling of the helicities:
#  0: sum over all helicities
#  1: importance sampling over helicities
#*********************************************************************
   0  = nhel          ! using helicities importance sampling or not.'''.format(energy=energy, nev=nev)
print '''#*********************************************************************
# Generation bias, check the wiki page below for more information:   *
#  'cp3.irmp.ucl.ac.be/projects/madgraph/wiki/LOEventGenerationBias' *
#*********************************************************************
 None = bias_module  ! Bias type of bias, [None, ptj_bias, -custom_folder-]
 {} = bias_parameters ! Specifies the parameters of the module.
#
#*******************************                                                 
# Parton level cuts definition *
#*******************************                                     
#                                                                    
#
#*********************************************************************
# BW cutoff (M+/-bwcutoff*Gamma) ! Define on/off-shell for "$" and decay  
#*********************************************************************
  15.0  = bwcutoff      ! (M+/-bwcutoff*Gamma)
#*********************************************************************
# Apply pt/E/eta/dr/mij/kt_durham cuts on decay products or not
# (note that etmiss/ptll/ptheavy/ht/sorted cuts always apply)
#*********************************************************************
   False  = cut_decays    ! Cut decay products 
#*********************************************************************
# Standard Cuts                                                      *
#*********************************************************************
# Minimum and maximum pt's (for max, -1 means no cut)                *
#*********************************************************************
 0.0  = ptj       ! minimum pt for the jets 
 0.0  = ptb       ! minimum pt for the b 
 0.0  = pta       ! minimum pt for the photons 
 0.0  = ptl       ! minimum pt for the charged leptons 
 0.0  = misset    ! minimum missing Et (sum of neutrino's momenta)
 0.0  = ptheavy   ! minimum pt for one heavy final state
 -1.0  = ptjmax    ! maximum pt for the jets
 -1.0  = ptbmax    ! maximum pt for the b
 -1.0  = ptamax    ! maximum pt for the photons
 -1.0  = ptlmax    ! maximum pt for the charged leptons
 -1.0  = missetmax ! maximum missing Et (sum of neutrino's momenta)
#*********************************************************************
# Minimum and maximum E's (in the center of mass frame)              *
#*********************************************************************
  0.0  = ej     ! minimum E for the jets 
  0.0  = eb     ! minimum E for the b 
  0.0  = ea     ! minimum E for the photons 
  0.0  = el     ! minimum E for the charged leptons 
  -1.0   = ejmax ! maximum E for the jets
 -1.0   = ebmax ! maximum E for the b
 -1.0   = eamax ! maximum E for the photons
 -1.0   = elmax ! maximum E for the charged leptons
#*********************************************************************
# Maximum and minimum absolute rapidity (for max, -1 means no cut)   *
#*********************************************************************
  -1.0 = etaj    ! max rap for the jets 
  -1.0  = etab    ! max rap for the b
 -1.0  = etaa    ! max rap for the photons 
 -1.0  = etal    ! max rap for the charged leptons 
 0.0  = etajmin ! min rap for the jets
 0.0  = etabmin ! min rap for the b
 0.0  = etaamin ! min rap for the photons
 0.0  = etalmin ! main rap for the charged leptons
#*********************************************************************
# Minimum and maximum DeltaR distance                                *
#*********************************************************************
 0.0 = drjj    ! min distance between jets 
 0.0   = drbb    ! min distance between b's 
 0.0 = drll    ! min distance between leptons 
 0.0 = draa    ! min distance between gammas 
 0.0   = drbj    ! min distance between b and jet 
 0.0 = draj    ! min distance between gamma and jet 
 0.0 = drjl    ! min distance between jet and lepton 
 0.0   = drab    ! min distance between gamma and b 
 0.0   = drbl    ! min distance between b and lepton 
 0.0 = dral    ! min distance between gamma and lepton 
 -1.0  = drjjmax ! max distance between jets
 -1.0  = drbbmax ! max distance between b's
 -1.0  = drllmax ! max distance between leptons
 -1.0  = draamax ! max distance between gammas
 -1.0  = drbjmax ! max distance between b and jet
 -1.0  = drajmax ! max distance between gamma and jet
 -1.0  = drjlmax ! max distance between jet and lepton
 -1.0  = drabmax ! max distance between gamma and b
 -1.0  = drblmax ! max distance between b and lepton
 -1.0  = dralmax ! maxdistance between gamma and lepton
#*********************************************************************
# Minimum and maximum invariant mass for pairs                       *
# WARNING: for four lepton final state mmll cut require to have      *
#          different lepton masses for each flavor!                  *           
#*********************************************************************
 0.0   = mmjj    ! min invariant mass of a jet pair 
 0.0   = mmbb    ! min invariant mass of a b pair 
 0.0   = mmaa    ! min invariant mass of gamma gamma pair
 0.0   = mmll    ! min invariant mass of l+l- (same flavour) lepton pair
 -1.0  = mmjjmax ! max invariant mass of a jet pair
 -1.0  = mmbbmax ! max invariant mass of a b pair
 -1.0  = mmaamax ! max invariant mass of gamma gamma pair
 -1.0  = mmllmax ! max invariant mass of l+l- (same flavour) lepton pair
#*********************************************************************
# Minimum and maximum invariant mass for all letpons                 *
#*********************************************************************
 0.0   = mmnl    ! min invariant mass for all letpons (l+- and vl) 
 -1.0  = mmnlmax ! max invariant mass for all letpons (l+- and vl) 
#*********************************************************************
# Minimum and maximum pt for 4-momenta sum of leptons                *
#*********************************************************************
 0.0   = ptllmin  ! Minimum pt for 4-momenta sum of leptons(l and vl)
 -1.0  = ptllmax  ! Maximum pt for 4-momenta sum of leptons(l and vl)
#*********************************************************************
# Inclusive cuts                                                     *
#*********************************************************************
 0.0  = xptj ! minimum pt for at least one jet  
 0.0  = xptb ! minimum pt for at least one b 
 0.0  = xpta ! minimum pt for at least one photon 
 0.0  = xptl ! minimum pt for at least one charged lepton 
#*********************************************************************
# Control the pt's of the jets sorted by pt                          *
#*********************************************************************
 0.0   = ptj1min ! minimum pt for the leading jet in pt
 0.0   = ptj2min ! minimum pt for the second jet in pt
 0.0   = ptj3min ! minimum pt for the third jet in pt
 0.0   = ptj4min ! minimum pt for the fourth jet in pt
 -1.0  = ptj1max ! maximum pt for the leading jet in pt 
 -1.0  = ptj2max ! maximum pt for the second jet in pt
 -1.0  = ptj3max ! maximum pt for the third jet in pt
 -1.0  = ptj4max ! maximum pt for the fourth jet in pt
 0   = cutuse  ! reject event if fails any (0) / all (1) jet pt cuts
#*********************************************************************
# Control the pt's of leptons sorted by pt                           *
#*********************************************************************
 0.0   = ptl1min ! minimum pt for the leading lepton in pt
 0.0   = ptl2min ! minimum pt for the second lepton in pt
 0.0   = ptl3min ! minimum pt for the third lepton in pt
 0.0   = ptl4min ! minimum pt for the fourth lepton in pt
 -1.0  = ptl1max ! maximum pt for the leading lepton in pt 
 -1.0  = ptl2max ! maximum pt for the second lepton in pt
 -1.0  = ptl3max ! maximum pt for the third lepton in pt
 -1.0  = ptl4max ! maximum pt for the fourth lepton in pt
#*********************************************************************
# Control the Ht(k)=Sum of k leading jets                            *
#*********************************************************************
 0.0   = htjmin ! minimum jet HT=Sum(jet pt)
 -1.0  = htjmax ! maximum jet HT=Sum(jet pt)
 0.0   = ihtmin  !inclusive Ht for all partons (including b)
 -1.0  = ihtmax  !inclusive Ht for all partons (including b)
 0.0   = ht2min ! minimum Ht for the two leading jets
 0.0   = ht3min ! minimum Ht for the three leading jets
 0.0   = ht4min ! minimum Ht for the four leading jets
 -1.0  = ht2max ! maximum Ht for the two leading jets
 -1.0  = ht3max ! maximum Ht for the three leading jets
 -1.0  = ht4max ! maximum Ht for the four leading jets
#***********************************************************************
# Photon-isolation cuts, according to hep-ph/9801442                   *
# When ptgmin=0, all the other parameters are ignored                  *
# When ptgmin>0, pta and draj are not going to be used                 *
#***********************************************************************
 0.0 = ptgmin ! Min photon transverse momentum
 0.4 = R0gamma ! Radius of isolation code
 1.0 = xn ! n parameter of eq.(3.4) in hep-ph/9801442
 1.0 = epsgamma ! epsilon_gamma parameter of eq.(3.4) in hep-ph/9801442
 True = isoEM ! isolate photons from EM energy (photons and leptons)
#*********************************************************************
# WBF cuts                                                           *
#*********************************************************************
 0.0   = xetamin ! minimum rapidity for two jets in the WBF case  
 0.0   = deltaeta ! minimum rapidity for two jets in the WBF case 
#***********************************************************************
# Turn on either the ktdurham or ptlund cut to activate                *
# CKKW(L) merging with Pythia8 [arXiv:1410.3012, arXiv:1109.4829]      *
#***********************************************************************
 -1.0  =  ktdurham        
 0.4   =  dparameter
 -1.0  =  ptlund
 1, 2, 3, 4, 5, 6, 21, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000021, 2000001, 2000002, 2000003, 2000004, 2000005, 2000006  =  pdgs_for_merging_cut ! PDGs for two cuts above   
#*********************************************************************
# maximal pdg code for quark to be considered as a light jet         *
# (otherwise b cuts are applied)                                     *
#*********************************************************************
 4 = maxjetflavor    ! Maximum jet pdg code
#*********************************************************************
#
#*********************************************************************
# Store info for systematics studies                                 *
# WARNING: Do not use for interference type of computation           *
#*********************************************************************
   False  = use_syst      ! Enable systematics studies
#
#**************************************
# Parameter of the systematics study
#  will be used by SysCalc (if installed)
#**************************************                                  
#
# 0.5 1 2 = sys_scalefact  # factorization/renormalization scale factor
# None = sys_alpsfact  # \alpha_s emission scale factors
# auto = sys_matchscale # variation of merging scale
# PDF sets and number of members (0 or none for all members).
NNPDF23_lo_as_0130_qed = sys_pdf # list of pdf sets
# MSTW2008nlo68cl.LHgrid 1  = sys_pdf
#'''