from ROOT import *
from MCLimit import *  ### Works w/ Urania v2r4 and gcc48
#import numpy as np
#gROOT.ProcessLine(".L ../mclimit/junkInterface.cpp++")
#gSystem.Load("/scratch19/URANIA/URANIA_HEAD/Math/MCLimit/x86_64-slc6-gcc48-opt/libMCLimit")
bkgpdf = TH1D("bkg pdf", "bkg pdf",1,0,1) ### importante empezar por 1
sigpdf = TH1D("sig pdf", "sig pdf",1,0,1)
DataHist = TH1D("deita", "deita",1,0,1)


bkgpdf.SetBinContent(1,1.0)
sigpdf.SetBinContent(1,1.0)

Nb = 283. ## bkg
sb = 24. ## erro bkg
Nobs = 263  ## 

DataHist.SetBinContent(1,Nobs)

bkg_no_syst = csm_template(0)   ### No systematics (used for the test statistic)
bkg = csm_template(1)   ### in this case, 1 systematics (error in bin 3) 

bkg.make(bkgpdf, Nb, 0,0, "mytest")
bkg_no_syst.make(bkgpdf, Nb, 0,0, "mytest")

bkg.set_np("bkg error", -sb/Nb, sb/Nb,NULL, 1, NULL, -1)
nul = csm_model()
nul_no_syst = csm_model()

bkg_no_syst.add_to(nul_no_syst) #adding to the null hypothesis
bkg.add_to(nul) #adding to the null hypothesis

#BREAK
##### Some dictionaries used to store S+B models
dc = {}
dc_no_syst = {}  
test = {}
test_no_syst = {} #used to collect different test hypothesis.

def doCL(Ns,DataHist):
    dc_no_syst[Ns] = csm_template(0) #for a given br hypothesis, model
    dc[Ns] = csm_template(0) 
    ## no systematics here 
    Ns = Ns
    dc[Ns].make(sigpdf,Ns,0,1,"mytest") #(pdf,events,0, is_signal,channel_name)
    dc_no_syst[Ns].make(sigpdf,Ns,0,1,"mytest")
    #### Set the "test" hypothesis (S+B)
    ## Notice that so far only signal model used. bkg stuff done before.
    
    ## Adding both bkg and signal (final model built):
    test[Ns] = csm_model()
    test_no_syst[Ns] = csm_model()

    bkg.add_to(test[Ns])
    dc[Ns].add_to(test[Ns])
    bkg_no_syst.add_to(test_no_syst[Ns])
    dc_no_syst[Ns].add_to(test_no_syst[Ns])
   
   
    ### Prepare the stuff that calculates the limits
    
    CL = mclimit_csm()
    
    ## nul and test hypothesis for test statistics. If you put models with systematics here, you activate
    ## refitting of the nuisance parameters ---> computationaly QUITE expensive, plus the fit might not converge
    
    CL.set_null_hypothesis(nul_no_syst)   
    CL.set_test_hypothesis(test_no_syst[Ns])
    ## if systematics here, it'll refit trying to recover the lost information --> painful
    ## nul and test hypothesis for pseudoexperiments (toy generation, systematics included)
    CL.set_null_hypothesis_pe(nul)
    CL.set_test_hypothesis_pe(test[Ns])
    
    ### Add the observed data
    
    CL.set_datahist(DataHist, "TheData")
    CL.set_npe(2000)

    CL.run_pseudoexperiments()
    return CL#.cls(), CL.clb(), CL.clsb()
## CLs = 0.05 --> sinal excluido ao 95% CL

def do_scan():
    """ Fill a text file with the BR vs CL curve
    """
    from XTuple import XTuple

    tup = XTuple("tau23mu",["ns/F","cls/F","clb/F","clsb/F"])
    dc = {}
    for i in range(200):
        ns = float(5+0.5*i)
        print ns
        CL = doCL(ns,DataHist )
        print "still alive"
        tup.fillItem("ns",ns)
        tup.fillItem("cls", CL.cls())
        tup.fillItem("clb", CL.clb())
        tup.fillItem("clsb", CL.clsb())
        tup.fill()
        print " ---- DONE", cls, clb
    tup.close()
    return dc
#do_scan()

CL = doCL(44,DataHist)
#print CL.s95()

## ################################
## Analysis: atlas_1605_03814
## ################################
## #--- SR: 2jt ---#
## sig: 65.1845376
## Nobs: 26.0
## Nbkg: 23.0
## Nbkg_err: 4.0
## S95_obs: 17.0
## S95_exp: 14.0
## p0: 0.4
## #--- SR: 2jm ---#
## sig: 132.1598592
## Nobs: 191.0
## Nbkg: 191.0
## Nbkg_err: 21.0
## S95_obs: 48.0
## S95_exp: 48.0
## p0: 0.5
## #--- SR: 2jl ---#
## sig: 146.844288
## Nobs: 263.0
## Nbkg: 283.0
## Nbkg_err: 24.0
## S95_obs: 44.0
## S95_exp: 54.0
## p0: 0.5

