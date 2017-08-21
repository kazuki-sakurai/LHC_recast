#!/usr/bin/env python

import sys, os
import numpy as np
from scipy import interpolate

def get_xsfb(infile, m_in, unit):

    if unit == 'pb': fac = 1000.
    if unit == 'fb': fac = 1.

    dirname = os.path.dirname(__file__)    
    infile_path = os.path.join(dirname, infile)
    data = np.loadtxt(infile_path)
    try:
        mass_ar, xspb_ar = np.transpose(data)
    except:
        mass_ar, xspb_ar, dummy = np.transpose(data)        
    xspb_data = interpolate.interp1d(mass_ar, xspb_ar)

    xspb = xspb_data(m_in)
    xsfb = xspb * fac
    return xsfb

try:
    mode = sys.argv[1]    
    m_in = float(sys.argv[2])
    rs   = int(sys.argv[3])
    br   = float(sys.argv[4])    
except:
    print '[mode] [mass] [energy] [BR]'

if mode in ['QqN1']: mode = 'QQ4F'
if mode in ['GqqN1', 'GttN1', 'GbbN1', 'GqqN2lLlN1', 'GqqC1wN1', 'GqqC1wN2zN1']: mode = 'GG'
if mode in ['C1lLlN1_C1lLlN1', 'C1lL3lN1_C1lL3lN1']: mode = 'C1C1wino'
if mode in ['C1lLlN1_N2lLlN1', 'C1lL3lN1_N2lL3lN1', 'C1whadN1_N2zlepN1', 'C1wlepN1_N2zlepN1']: mode = 'C1N2wino'
if mode in ['B1tC1wN1', 'B1bN1', 'T1bC1wN1']: mode = 'Q3Q3'

GG_file = 'GGxsec{rs}.dat'.format(rs=rs)
QQ5F_file = 'QQxsec{rs}_5F.dat'.format(rs=rs)
Q3Q3_file = 'Q3Q3xsec{rs}.dat'.format(rs=rs)
C1C1_file = 'C1C1wino{rs}.dat'.format(rs=rs)
C1N2_file = 'C1N2wino{rs}.dat'.format(rs=rs)

if mode == 'GG': 
    print get_xsfb(GG_file, m_in, 'pb') * br
    exit()

if mode == 'QQ5F': 
    print get_xsfb(QQ5F_file, m_in, 'pb') * br
    exit()

if mode == 'Q3Q3': 
    print get_xsfb(Q3Q3_file, m_in, 'pb') * br
    exit()

if mode == 'QQ4F': 
    QQ5F = get_xsfb(QQ5F_file, m_in, 'pb')
    BLBL = BRBR = get_xsfb(Q3Q3_file, m_in, 'pb')
    QQ4F = QQ5F - BLBL - BRBR
    print QQ4F * br
    exit()

if mode == 'C1C1wino': 
    print get_xsfb(C1C1_file, m_in, 'fb') * br
    exit()

if mode == 'C1N2wino': 
    print get_xsfb(C1N2_file, m_in, 'fb') * br
    exit()
