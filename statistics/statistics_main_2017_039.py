#!/usr/bin/env python
import sys, os, pickle
from basic_func import *
import numpy as np
from sympy import oo

def LL(s,b0,s0,N):
    b = 0.5*(b0-s-s0**2) + 0.5*np.sqrt((b0-s-s0**2)**2 + 4*(N*s0**2 - s*s0**2 + s*b0))
    #print "-_-", b
    b = max(b, 1e-03)
    pb = -0.5*((b-b0)/s0)**2
    L1 =-(s+b)
    L2 = N*np.log(s+b)
    return L1 + L2 + pb

def chi2(s,b0,s0,N):
    sb = max(N-b0,0) ## best fit value on the s domain
    DLL = LL(s,b0,s0,N)-LL(sb,b0,s0,N)
    return -2*DLL
    
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
#ana_list.append('atlas_1602_09058')
#ana_list.append('atlas_1605_04285')
#ana_list.append('atlas_conf_2016_093')
#ana_list.append('atlas_conf_2016_096')
#ana_list.append('atlas_conf_2016_054')
#ana_list.append('atlas_conf_2016_037')
ana_list.append('atlas_conf_2017_039')
outa = {}
outb = {}
outc = {}
outd = {}
oute = {}

for ana in ana_list:
    dirname = os.path.dirname(__file__)
    pickle_path = os.path.join( dirname, '{ana}.pickle'.format(ana=ana) )
    print pickle_path
    data = pickle.load( open( pickle_path) )
    lumi = data['lumi']
    #SRdata = data['SR']
    SRdataa = data['SRa']
    SRdatab = data['SRb']
    SRdatac = data['SRc']
    SRdatad = data['SRd']
    SRdatae = data['SRe']
    #SR_list = SRdata.keys()
    SR_lista = SRdataa.keys()
    SR_listb = SRdatab.keys()
    SR_listc = SRdatac.keys()
    SR_listd = SRdatad.keys()
    SR_liste = SRdatae.keys()
    #print SR_list
    print 'SR list a:', SR_lista
    print 'SR list b:', SR_listb
    print 'SR list c:', SR_listc
    print 'SR list d:', SR_listd
    print 'SR list e:', SR_liste
    #eff, mc_err_p, mc_err_m = get_eff(ana, SR_list, eff_file)
    effa, mc_err_pa, mc_err_ma = get_eff(ana, SR_lista, eff_file)
    effb, mc_err_pb, mc_err_mb = get_eff(ana, SR_listb, eff_file)
    effc, mc_err_pc, mc_err_mc = get_eff(ana, SR_listc, eff_file)
    effd, mc_err_pd, mc_err_md = get_eff(ana, SR_listd, eff_file)
    effe, mc_err_pe, mc_err_me = get_eff(ana, SR_liste, eff_file)
    #print eff.keys()
    print 'effa:', effa.keys()
    print 'effb:', effb.keys()
    print 'effc:', effc.keys()
    print 'effd:', effd.keys()
    print 'effe:', effe.keys()
    print '################################'
    print 'Analysis:', ana
    print '################################'
    choices = []
    for sr in effd:
        SRdatad[sr]["Nsig"] = effd[sr] * xsfb * lumi
        print '#--- SR:', sr, '---#'
        print 'sig:', SRdatad[sr]["Nsig"]
        print 'Nobs:', SRdatad[sr]['Nobs']
        print 'Nbkg:', SRdatad[sr]['Nbkg']
        print 'Nbkg_err:', SRdatad[sr]['Nbkg_err']        
        print 'S95_obs:', SRdatad[sr]['S95_obs']
        print 'S95_exp:', SRdatad[sr]['S95_exp']
        print 'p0:', SRdatad[sr]['p0']        
        if effd[sr]: choices.append([SRdatad[sr]['S95_exp']*1./effd[sr],sr ])
        else: choices.append([oo,sr ])
    choices.sort()
    sr = choices[0][1]
    print 'Chosen analysis:',sr
    print effd[sr], xsfb, lumi, 1.*SRdatad[sr]['Nbkg'], 1.*SRdatad[sr]['Nbkg_err'] ,  1.*SRdatad[sr]['Nobs']
    sig_centd = effd[sr] * xsfb * lumi
    sig_posd = (effd[sr] + mc_err_pd[sr]) * xsfb * (1. + xs_err)* lumi
    sig_negd = (effd[sr] - mc_err_md[sr]) * xsfb * (1. - xs_err) * lumi
    chi2isad = chi2(sig_centd, 1.*SRdatad[sr]['Nbkg'], 1.*SRdatad[sr]['Nbkg_err'] ,  1.*SRdatad[sr]['Nobs'])    
    chi2isa_posd = chi2(sig_posd, 1.*SRdatad[sr]['Nbkg'], 1.*SRdatad[sr]['Nbkg_err'] ,  1.*SRdatad[sr]['Nobs'])    
    chi2isa_negd = chi2(sig_negd, 1.*SRdatad[sr]['Nbkg'], 1.*SRdatad[sr]['Nbkg_err'] ,  1.*SRdatad[sr]['Nobs'])    
    print 'Chi2_isad:', chi2isad
    print 'Chi2_+1sigd:', chi2isa_posd
    print 'Chi2_-1sigd:', chi2isa_negd
    outd[ana + '_d'] = SRdatad.copy()
    outd[ana + '_d']['chi2_id'] = chi2isad
    outd[ana + '_d']['chi2_i_+1sigd'] = chi2isa_posd
    outd[ana + '_d']['chi2_i_-1sigd'] = chi2isa_negd
    outd[ana + '_d']['chosen_sr'] = sr
    outd[ana + '_d']['Xs'] = xsfb
    outd[ana + '_d']['eff_file'] = eff_file

    chi2isaa = 0.
    chi2isa_posa = 0.
    chi2isa_nega = 0.
    for sr in effa:
        sig_centa = effa[sr] * xsfb * lumi
        sig_posa = (effa[sr] + mc_err_pa[sr]) * xsfb * (1. + xs_err)* lumi
        sig_nega = (effa[sr] - mc_err_ma[sr]) * xsfb * (1. - xs_err) * lumi
        chi2isaa =chi2isaa +  chi2(sig_centa, 1.*SRdataa[sr]['Nbkg'], 1.*SRdataa[sr]['Nbkg_err'] ,  1.*SRdataa[sr]['Nobs'])    
        chi2isa_posa = chi2isa_posa + chi2(sig_posa, 1.*SRdataa[sr]['Nbkg'], 1.*SRdataa[sr]['Nbkg_err'] ,  1.*SRdataa[sr]['Nobs'])    
        chi2isa_nega = chi2isa_nega + chi2(sig_nega, 1.*SRdataa[sr]['Nbkg'], 1.*SRdataa[sr]['Nbkg_err'] ,  1.*SRdataa[sr]['Nobs'])    
    print 'Chi2_isaa:', chi2isaa
    print 'Chi2_+1siga:', chi2isa_posa
    print 'Chi2_-1siga:', chi2isa_nega
    outa[ana + '_a'] = SRdataa.copy()
    outa[ana + '_a']['chi2_ia'] = chi2isaa
    outa[ana + '_a']['chi2_i_+1siga'] = chi2isa_posa
    outa[ana + '_a']['chi2_i_-1siga'] = chi2isa_nega
    outa[ana + '_a']['Xs'] = xsfb
    outa[ana + '_a']['eff_file'] = eff_file

    chi2isab = 0.
    chi2isa_posb = 0.
    chi2isa_negb = 0.
    for sr in effb:
        sig_centb = effb[sr] * xsfb * lumi
        sig_posb = (effb[sr] + mc_err_pb[sr]) * xsfb * (1. + xs_err)* lumi
        sig_negb = (effb[sr] - mc_err_mb[sr]) * xsfb * (1. - xs_err) * lumi
        chi2isab =chi2isab +  chi2(sig_centb, 1.*SRdatab[sr]['Nbkg'], 1.*SRdatab[sr]['Nbkg_err'] ,  1.*SRdatab[sr]['Nobs'])    
        chi2isa_posb = chi2isa_posb + chi2(sig_posb, 1.*SRdatab[sr]['Nbkg'], 1.*SRdatab[sr]['Nbkg_err'] ,  1.*SRdatab[sr]['Nobs'])    
        chi2isa_negb = chi2isa_negb + chi2(sig_negb, 1.*SRdatab[sr]['Nbkg'], 1.*SRdatab[sr]['Nbkg_err'] ,  1.*SRdatab[sr]['Nobs'])    
    print 'Chi2_isab:', chi2isab
    print 'Chi2_+1sigb:', chi2isa_posb
    print 'Chi2_-1sigb:', chi2isa_negb
    outb[ana + '_b'] = SRdatab.copy()
    outb[ana + '_b']['chi2_ib'] = chi2isab
    outb[ana + '_b']['chi2_i_+1sigb'] = chi2isa_posb
    outb[ana + '_b']['chi2_i_-1sigb'] = chi2isa_negb
    outb[ana + '_b']['Xs'] = xsfb
    outb[ana + '_b']['eff_file'] = eff_file

    chi2isac = 0.
    chi2isa_posc = 0.
    chi2isa_negc = 0.
    for sr in effc:
        sig_centc = effc[sr] * xsfb * lumi
        sig_posc = (effc[sr] + mc_err_pc[sr]) * xsfb * (1. + xs_err)* lumi
        sig_negc = (effc[sr] - mc_err_mc[sr]) * xsfb * (1. - xs_err) * lumi
        chi2isac =chi2isac +  chi2(sig_centc, 1.*SRdatac[sr]['Nbkg'], 1.*SRdatac[sr]['Nbkg_err'] ,  1.*SRdatac[sr]['Nobs'])    
        chi2isa_posc = chi2isa_posc + chi2(sig_posc, 1.*SRdatac[sr]['Nbkg'], 1.*SRdatac[sr]['Nbkg_err'] ,  1.*SRdatac[sr]['Nobs'])    
        chi2isa_negc = chi2isa_negc + chi2(sig_negc, 1.*SRdatac[sr]['Nbkg'], 1.*SRdatac[sr]['Nbkg_err'] ,  1.*SRdatac[sr]['Nobs'])    
    print 'Chi2_isac:', chi2isac
    print 'Chi2_+1sigc:', chi2isa_posc
    print 'Chi2_-1sigc:', chi2isa_negc
    outc[ana + '_c'] = SRdatac.copy()
    outc[ana + '_c']['chi2_ic'] = chi2isac
    outc[ana + '_c']['chi2_i_+1sigc'] = chi2isa_posc
    outc[ana + '_c']['chi2_i_-1sigc'] = chi2isa_negc
    outc[ana + '_c']['Xs'] = xsfb
    outc[ana + '_c']['eff_file'] = eff_file

    chi2isae = 0.
    chi2isa_pose = 0.
    chi2isa_nege = 0.
    for sr in effe:
        sig_cente = effe[sr] * xsfb * lumi
        sig_pose = (effe[sr] + mc_err_pe[sr]) * xsfb * (1. + xs_err)* lumi
        sig_nege = (effe[sr] - mc_err_me[sr]) * xsfb * (1. - xs_err) * lumi
        chi2isae = chi2isae +  chi2(sig_cente, 1.*SRdatae[sr]['Nbkg'], 1.*SRdatae[sr]['Nbkg_err'] ,  1.*SRdatae[sr]['Nobs'])    
        chi2isa_pose = chi2isa_pose + chi2(sig_pose, 1.*SRdatae[sr]['Nbkg'], 1.*SRdatae[sr]['Nbkg_err'] ,  1.*SRdatae[sr]['Nobs'])    
        chi2isa_nege = chi2isa_nege + chi2(sig_nege, 1.*SRdatae[sr]['Nbkg'], 1.*SRdatae[sr]['Nbkg_err'] ,  1.*SRdatae[sr]['Nobs'])    
    print 'Chi2_isae:', chi2isae
    print 'Chi2_+1sige:', chi2isa_pose
    print 'Chi2_-1sige:', chi2isa_nege
    oute[ana + '_e'] = SRdatae.copy()
    oute[ana + '_e']['chi2_ie'] = chi2isae
    oute[ana + '_e']['chi2_i_+1sige'] = chi2isa_pose
    oute[ana + '_e']['chi2_i_-1sige'] = chi2isa_nege
    oute[ana + '_e']['Xs'] = xsfb
    oute[ana + '_e']['eff_file'] = eff_file
    
import cPickle
cPickle.dump(outb, file( eff_file + '_'+ str(xsfb) +'.ansb', 'w'))
cPickle.dump(outc, file( eff_file + '_'+ str(xsfb) +'.ansc', 'w'))
cPickle.dump(outa, file( eff_file + '_'+ str(xsfb) +'.ansa', 'w'))
cPickle.dump(outd, file( eff_file + '_'+ str(xsfb) +'.ansd', 'w'))
cPickle.dump(oute, file( eff_file + '_'+ str(xsfb) +'.anse', 'w'))

