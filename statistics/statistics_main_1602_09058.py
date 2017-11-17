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
print sys.argv    
eff_file = sys.argv[1]
if not os.path.exists(eff_file):
    print eff_file, 'does not exist!!'
    exit()

xsfb = sys.argv[2]
xsfb = float(xsfb)

xs_err = sys.argv[3]
xs_err = float(xs_err)

ana_list = []
for line in open(eff_file):
    elems = line.split()
    if len(elems) != 2: continue
    if elems[0] == 'Analysis:': ana_list.append(elems[1])
#ana_list.append('atlas_1605_03814')
ana_list.append('atlas_1602_09058')
#ana_list.append('atlas_1605_04285')
#ana_list.append('atlas_conf_2016_093')
#ana_list.append('atlas_conf_2016_096')
#ana_list.append('atlas_conf_2016_054')
#ana_list.append('atlas_conf_2016_037')
#ana_list.append('atlas_1706_03731')
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
    eff, mc_err_p, mc_err_m = get_eff(ana, SR_list, eff_file)
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
    print 'Chosen analysis:',sr
    sig_cent = eff[sr] * xsfb * lumi
    sig_pos = (eff[sr] + mc_err_p[sr]) * xsfb * (1. + xs_err)* lumi
    sig_neg = (eff[sr] - mc_err_m[sr]) * xsfb * (1. - xs_err) * lumi
    chi2isa = chi2(sig_cent, 1.*SRdata[sr]['Nbkg'], 1.*SRdata[sr]['Nbkg_err'] ,  1.*SRdata[sr]['Nobs'])    
    chi2isa_pos = chi2(sig_pos, 1.*SRdata[sr]['Nbkg'], 1.*SRdata[sr]['Nbkg_err'] ,  1.*SRdata[sr]['Nobs'])    
    chi2isa_neg = chi2(sig_neg, 1.*SRdata[sr]['Nbkg'], 1.*SRdata[sr]['Nbkg_err'] ,  1.*SRdata[sr]['Nobs'])    
    print 'Chi2_isa:', chi2isa
    print 'Chi2_+1sig:', chi2isa_pos
    print 'Chi2_-1sig:', chi2isa_neg
    out[ana] = SRdata.copy()
    out[ana]['chi2_i'] = chi2isa
    out[ana]['chi2_i_+1sig'] = chi2isa_pos
    out[ana]['chi2_i_-1sig'] = chi2isa_neg
    out[ana]['chosen_sr'] = sr
    out[ana]['Xs'] = xsfb
    out[ana]['eff_file'] = eff_file

import cPickle
cPickle.dump(out, file( eff_file + '_'+ str(xsfb) +'.ans', 'w'))

