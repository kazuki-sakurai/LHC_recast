#!/usr/bin/env python

import sys

try:
    slha_file = sys.argv[1]
    mode = sys.argv[2]
    energy = sys.argv[3]
    nev = int(sys.argv[4])
except:
    print '[slha] [mode] [energy] [nev]'
    exit()

if mode in ['QqN1']:  mode = 'squark_only'
if mode in ['GqqN1', 'GttN1', 'GqqN2lLlN1']: mode = 'gluino_only'
if mode in ['C1lLlN1_C1lLlN1', 'C1lL3lN1_C1lL3lN1']: mode = 'C1C1'
if mode in ['C1lLlN1_N2lLlN1', 'C1lL3lN1_N2lL3lN1']: mode = 'C1N2'


if mode == 'all': process = 'SUSY:all = on'
if mode == 'squark_only': 
    process = '''SUSY:gg2squarkantisquark = on
SUSY:qqbar2squarkantisquark = on'''
if mode == 'gluino_only': 
    process = '''SUSY:gg2gluinogluino  = on
SUSY:qqbar2gluinogluino  = on'''
if mode == 'C1C1': process = 'SUSY:qqbar2chi+chi-  = on'
if mode == 'C1N2': process = 'SUSY:qqbar2chi+-chi0 = on'

if mode not in ['all', 'squark_only', 'gluino_only', 'C1C1', 'C1N2']:
    print '[mode] has to be chosen from [all, squark_only, gluino_only, C1C1, C1N2]'
    exit()

print '''
! main24.cmnd
! This file contains commands to be read in for a Pythia8 run.
! Lines not beginning with a letter or digit are comments.

! 1) Settings used in the main program.
Main:numberOfEvents = {nev}        ! number of events to generate
Main:timesAllowErrors = 3          ! how many aborts before run stops

! 2) Settings related to output in init(), next() and stat().
Init:showChangedSettings = on      ! list changed settings
Init:showChangedParticleData = off ! list changed particle data
Next:numberCount = 500             ! print message every n events
Next:numberShowInfo = 2            ! print event information n times
Next:numberShowProcess = 2         ! print process record n times
Next:numberShowEvent = 2           ! print event record n times

! 3) Beam parameter settings. Values below agree with default ones.
Beams:idA = 2212                   ! first beam, p = 2212, pbar = -2212
Beams:idB = 2212                   ! second beam, p = 2212, pbar = -2212
Beams:eCM = {energy}000.                 ! CM energy of collision

! 4) Read SLHA spectrum (a few examples are provided by default)
SLHA:file = {slha_file}       ! Sample SLHA2 spectrum

! 5) Process selection
{process}
#SUSY:all = on                      ! Switches on ALL (~400) SUSY processes
#SUSY:gg2gluinogluino  = on
#SUSY:qqbar2gluinogluino  = on
#SUSY:qg2squarkgluino = on
#SUSY:gg2squarkantisquark = on
#SUSY:qqbar2squarkantisquark = on
#SUSY:qq2squarksquark = on
#SUSY:qqbar2chi0chi0  = on
#SUSY:qqbar2chi+-chi0 = on
#SUSY:qqbar2chi+chi-  = on
#SUSY:qg2chi0squark = on
#SUSY:qg2chi+-squark  = on
! Optionally select only specific sparticle codes in the final state
#SUSY:idA        = 2000001           ! 0: all
#SUSY:idB        = 2000001           ! 0: all

! 6) Settings for the event generation process in the Pythia8 library.
PartonLevel:MPI = off              ! no multiparton interactions
PartonLevel:ISR = on              ! no initial-state radiation
PartonLevel:FSR = off              ! no final-state radiation
HadronLevel:Hadronize = on        ! no hadronization
'''.format(slha_file=slha_file, process=process, energy=energy, nev=nev)

