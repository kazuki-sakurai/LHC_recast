#!/usr/bin/env python
import sys, os, pickle
from basic_func import *

xsfb = sys.argv[1]
xsfb = float(xsfb)

eff_file = sys.argv[2]
if not os.path.exists(eff_file):
    print eff_file, 'does not exist!!'
    exit()

ana_list = []
ana_list.append('atlas_1605_03814')

for ana in ana_list:
    dirname = os.path.dirname(__file__)
    pickle_path = os.path.join( dirname, '{ana}.pickle'.format(ana=ana) )
    data = pickle.load( open( pickle_path) )
    lumi = data['lumi']
    SRdata = data['SR']
    SR_list = SRdata.keys() 
    eff = get_eff(ana, SR_list, eff_file)

    print '################################'
    print 'Analysis:', ana
    print '################################'    
    for sr in eff:
        print '#--- SR:', sr, '---#'
        print 'sig:', eff[sr] * xsfb * lumi
        print 'Nobs:', SRdata[sr]['Nobs']
        print 'Nbkg:', SRdata[sr]['Nbkg']
        print 'Nbkg_err:', SRdata[sr]['Nbkg_err']        
        print 'S95_obs:', SRdata[sr]['S95_obs']
        print 'S95_exp:', SRdata[sr]['S95_exp']
        print 'p0:', SRdata[sr]['p0']        


