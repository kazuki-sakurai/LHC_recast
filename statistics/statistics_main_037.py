#!/usr/bin/env python
import sys, os, pickle
from basic_func import *
import numpy as np
from sympy import oo

def LL(s,b0,s0,N):
    b = 0.5*(b0-s-s0**2) + 0.5*np.sqrt((b0-s-s0**2)**2 + 4*(N*s0**2 - s*s0**2 + 
s*b0))
    pb = -0.5*((b-b0)/s0)**2
    L1 =-(s+b)
    L2 = N*np.log(s+b)
    return L1 + L2 + pb

def chi2(s,b0,s0,N):
    sb = max(N-b0,0) ## best fit value on the s domain
    DLL = LL(s,b0,s0,N)-LL(sb,b0,s0,N)
    return -2*DLL
    

xsfb = sys.argv[1]
xsfb = float(xsfb)

eff_file = sys.argv[2]
if not os.path.exists(eff_file):
    print eff_file, 'does not exist!!'
    exit()

ana_list = []
#ana_list.append('atlas_1605_03814')
#ana_list.append('atlas_1602_09058')
#ana_list.append('atlas_1605_04285')
#ana_list.append('atlas_conf_2016_093')
#ana_list.append('atlas_conf_2016_096')
#ana_list.append('atlas_conf_2016_054')
ana_list.append('atlas_conf_2016_037')
out = {}

for ana in ana_list:
    dirname = os.path.dirname(__file__)
    pickle_path = os.path.join( dirname, '{ana}.pickle'.format(ana=ana) )
    print pickle_path
    data = pickle.load( open( pickle_path) )
    lumi = data['lumi']
    SRdata = data['SR']
    SR_list = SRdata.keys()
    print SR_list
    eff = get_eff(ana, SR_list, eff_file)
    print eff.keys()
    print '################################'
    print 'Analysis:', ana
    print '################################'
    choices = []
    for sr in eff:
        SRdata[sr]["Nsig"] = eff[sr] * xsfb * lumi
        print '#--- SR:', sr, '---#'
        print 'sig:', SRdata[sr]["Nsig"]
        print 'Nobs:', SRdata[sr]['Nobs']
        print 'Nbkg:', SRdata[sr]['Nbkg']
        print 'Nbkg_err:', SRdata[sr]['Nbkg_err']        
        print 'S95_obs:', SRdata[sr]['S95_obs']
        print 'S95_exp:', SRdata[sr]['S95_exp']
        print 'p0:', SRdata[sr]['p0']        
        if eff[sr]: choices.append([SRdata[sr]['S95_exp']*1./eff[sr],sr ])
        else: choices.append([oo,sr ])
    choices.sort()
    sr = choices[0][1]
    print "Chosen analysis:",sr
    chi2isa = chi2(eff[sr] * xsfb * lumi, 1.*SRdata[sr]['Nbkg'], 1.*SRdata[sr]['Nbkg_err'] ,  1.*SRdata[sr]['Nobs'])    
    print "Chi2_isa:", chi2isa
    out[ana] = SRdata.copy()
    out[ana]["chi2_i"] = chi2isa
    out[ana]["chosen_sr"] = sr
    out[ana]["Xs"] = xsfb
    out[ana]["eff_file"] = eff_file

import cPickle
cPickle.dump(out, file( eff_file + "_"+ str(xsfb) +".ans", "w"))

