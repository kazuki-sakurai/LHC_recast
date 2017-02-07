#!/usr/bin/env python

import sys, os
import numpy as np
from scipy import interpolate

def get_xsfb(infile, m_in):

    dirname = os.path.dirname(__file__)    
    infile_path = os.path.join(dirname, infile)
    data = np.loadtxt(infile_path)
    mass_ar, xspb_ar = np.transpose(data)
    xspb_data = interpolate.interp1d(mass_ar, xspb_ar)

    xspb = xspb_data(m_in)
    xsfb = xspb * 1000.
    return xsfb

try:
    mode = sys.argv[1]    
    m_in = float(sys.argv[2])
    rs   = int(sys.argv[3])
except:
    print '[mass] [mode] [energy]'
    print 'mode = [GG, QQ4F, QQ5F, Q3Q3]'

if mode in ['QqN1']: mode = 'QQ4F'
if mode in ['GqqN1']: mode = 'GG'

GG_file = 'GGxsec{rs}.dat'.format(rs=rs)
QQ5F_file = 'QQxsec{rs}_5F.dat'.format(rs=rs)
Q3Q3_file = 'Q3Q3xsec{rs}.dat'.format(rs=rs)

if mode == 'GG': 
    print get_xsfb(GG_file, m_in)
    exit()

if mode == 'QQ5F': 
    print get_xsfb(QQ5F_file, m_in)
    exit()

if mode == 'Q3Q3': 
    print get_xsfb(Q3Q3_file, m_in)
    exit()

if mode == 'QQ4F': 
    QQ5F = get_xsfb(QQ5F_file, m_in)
    BLBL = BRBR = get_xsfb(Q3Q3_file, m_in)
    QQ4F = QQ5F - BLBL - BRBR
    print QQ4F
    exit()
