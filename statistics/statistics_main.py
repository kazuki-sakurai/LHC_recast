#!/usr/bin/env python
import sys, os, pickle
from basic_func import *
import numpy as np
from sympy import oo
from  funcion_diego import *

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


eff_file = sys.argv[1]
print eff_file
if not os.path.exists(eff_file):
    print eff_file, 'does not exist!!'
    exit()

xsfb = sys.argv[2]
xsfb = float(xsfb)

xs_err = sys.argv[3]
xs_err = float(xs_err)

ana_list = []
ana_list1 = []
## for line in open(eff_file):
##     elems = line.split()
##     if len(elems) != 2: continue
##     if elems[0] == 'Analysis:': ana_list.append(elems[1])

#ana_list.append('atlas_1605_03814')
ana_list.append('atlas_1602_09058')
#ana_list.append('atlas_1605_04285')
#ana_list.append('atlas_conf_2016_093')
#ana_list.append('atlas_conf_2016_096')
#ana_list.append('atlas_conf_2016_054')
#ana_list.append('atlas_conf_2016_037')
ana_list.append('atlas_1706_03731')
ana_list1.append('cms_1705_04650')

out = {}
DC = {}
k = 0
#Monojet
for i in xrange(1,8):
    k = k + 1
    DC['1j0b_bin'+str(i)] = k
for i in xrange(1,6):
    k = k + 1
    DC['1j1b_bin'+str(i)] = k
    
#Very Low HT
for i in xrange(1,4): 
    for j in range(4):
        k = k + 1
        DC['vlHT_2j'+str(j)+'b_bin'+str(i)] = k 
for i in xrange(1,4):
    for j in range(3):
        k = k + 1
        DC['vlHT_4j'+str(j)+'b_bin'+str(i)] = k
        
#Low HT
for i in xrange(1,5): 
    for j in xrange(4):
        k = k + 1
        DC['lHT_2j'+str(j)+'b_bin'+str(i)] = k
for i in xrange(1,5):
    for j in xrange(3):
        k = k + 1 
        DC['lHT_4j'+str(j)+'b_bin'+str(i)] = k
for i in xrange(1,4):
    for j in xrange(4):
        k = k + 1
        DC['lHT_7j'+str(j)+'b_bin'+str(i)] = k

#Medium HT
for i in xrange(1,6): 
    for j in xrange(3): 
        k = k + 1
        DC['mHT_2j'+str(j)+'b_bin'+str(i)] = k
for i in xrange(1,6):
    for j in xrange(3):
        k = k + 1
        DC['mHT_4j'+str(j)+'b_bin'+str(i)] = k
for i in xrange(1,6):
    k = k + 1
    DC['mHT_7j0b_bin'+str(i)] = k
for i in xrange(1,5): 
    for j in [1,2,3]:
        k = k + 1
        DC['mHT_7j'+str(j)+'b_bin'+str(i)] = k
for i in xrange(1,5):
    k = k + 1
    DC['mHT_2j3b_bin'+str(i)] = k

#High HT
for i in xrange(1,7): 
    for j in xrange(2):
        k = k + 1
        DC['hHT_2j'+str(j)+'b_bin'+str(i)] = k
for i in xrange(1,7): 
    for j in xrange(2):
        k = k + 1
        DC['hHT_4j'+str(j)+'b_bin'+str(i)] = k
for i in xrange(1,6):
    k = k + 1
    DC['hHT_2j2b_bin'+str(i)] = k
for i in xrange(1,6):
    k = k + 1
    DC['hHT_4j2b_bin'+str(i)] = k
for i in xrange(1,6):
    k = k + 1
    DC['hHT_7j0b_bin'+str(i)] = k
for i in xrange(1,5): 
    for j in [1,2]:
        k = k + 1
        DC['hHT_7j'+str(j)+'b_bin'+str(i)] = k
for i in xrange(1,4): 
    for j in [2,7]:
        k = k + 1
        DC['hHT_'+str(j)+'j3b_bin'+str(i)] = k

#Ulta-High / Extreme HT
for i in xrange(1,6):
    k = k + 1
    DC['eHT_2j0b_bin'+str(i)] = k
for i in xrange(1,6):
    for j in xrange(2):
        k = k + 1
        DC['eHT_4j'+str(j)+'b_bin'+str(i)] = k
for i in xrange(1,5):
    k = k + 1
    DC['eHT_2j1b_bin'+str(i)] = k
for i in xrange(1,5):
    k = k + 1
    DC['eHT_7j0b_bin'+str(i)] = k
for i in xrange(1,4):
    k = k + 1
    DC['eHT_4j2b_bin'+str(i)] = k
for i in xrange(1,4):
    for j in [1,2]:
        k = k + 1
        DC['eHT_7j'+str(j)+'b_bin'+str(i)] = k
for i in xrange(1,3):
    k = k + 1
    DC['eHT_2j3b_bin'+str(i)] = k
for i in xrange(1,2):
    k = k + 1
    DC['eHT_2j2b_bin'+str(i)] = k
for i in xrange(1,2):
    k = k + 1
    DC['eHT_7j3b_bin'+str(i)] = k


    
for ana in ana_list:
    dirname = os.path.dirname(__file__)
    pickle_path = os.path.join( dirname, '{ana}.pickle'.format(ana=ana) )
    print pickle_path
    data = pickle.load( open( pickle_path) )
    lumi = data['lumi']
    SRdata = data['SR']
    SR_list = SRdata.keys()
    print 'NoCMS', SR_list
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


for ana in ana_list1:
    dirname = os.path.dirname(__file__)
    pickle_path = os.path.join( dirname, '{ana}.pickle'.format(ana=ana) )
    print pickle_path
    data = pickle.load( open( pickle_path) )
    lumi = data['lumi']
    SRdata = data['SR']
    SR_list = SRdata.keys()
    print "SRList:", len(SR_list)
    print 'CMS', SR_list
    eff, mc_err_p, mc_err_m = get_eff(ana, SR_list, eff_file)
    print eff.keys()
    print "Effs", len(eff.keys())
    print '################################'
    print 'Analysis:', ana
    print '################################'
    choices = []
    for sr in eff:
        SRdata[sr]["Nsig"] = eff[sr] * xsfb * lumi
        print '#--- SR:', sr, '---#'
        print 'sig:', SRdata[sr]["Nsig"]
        #print 'Nobs:', SRdata[sr]['Nobs']
        #print 'Nbkg:', SRdata[sr]['Nbkg']
        #print 'Nbkg_err:', SRdata[sr]['Nbkg_err']        
        #print 'S95_obs:', SRdata[sr]['S95_obs']
        #print 'S95_exp:', SRdata[sr]['S95_exp']
        #print 'p0:', SRdata[sr]['p0']        
        #if eff[sr]: choices.append([SRdata[sr]['S95_exp']*1./eff[sr],sr ])
        #else: choices.append([oo,sr ])
    #choices.sort()
    #sr = choices[0][1]
    #print 'Chosen analysis:',sr
    sig = len(eff.keys())*[0.]
    sigp = len(eff.keys())*[0.]
    sigm = len(eff.keys())*[0.]
    print "-_'", len(sig)
    for sr in eff.keys():
        ibin = DC[sr] ## DC : Diccionario q pasa de SR a bin
        #print sr
        sig[ibin-1]= SRdata[sr]['Nsig']
        sigp[ibin-1] = (eff[sr] + mc_err_p[sr]) * xsfb * (1. + xs_err)* lumi
        sigm[ibin-1] = (eff[sr] - mc_err_m[sr]) * xsfb * (1. - xs_err) * lumi
    print "Here"
    chi2isa = funcion_diego(sig)#, 1.*SRdata[sr]['Nbkg'], 1.*SRdata[sr]['Nbkg_err'] ,  1.*SRdata[sr]['Nobs'])    
    chi2isa_pos = funcion_diego(sigp)# chi2(sig_pos, 1.*SRdata[sr]['Nbkg'], 1.*SRdata[sr]['Nbkg_err'] ,  1.*SRdata[sr]['Nobs'])    
    chi2isa_neg = funcion_diego(sigm)#chi2(sig_neg, 1.*SRdata[sr]['Nbkg'], 1.*SRdata[sr]['Nbkg_err'] ,  1.*SRdata[sr]['Nobs'])    
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

