#!/usr/bin/env python
from objects import *
from collections import OrderedDict
from aplanarity import *

class atlas_1605_03814:

    #########################################
    #    Define groups of signal regions
    #########################################
    def __init__(self):
        self.ananame = 'atlas_1605_03814'
        self.SR = OrderedDict()        
        self.SR['base'] = Cut('base')
        self.SR['2jl'] = Cut('2jl')
        self.SR['2jm'] = Cut('2jm')
        self.SR['2jt'] = Cut('2jt')
        self.SR['4jt'] = Cut('4jt')
        self.SR['5j'] = Cut('5j')
        self.SR['6jm'] = Cut('6jm')
        self.SR['6jt'] = Cut('6jt')

    #########################################
    #    Define jets, leptons, bjets, etc..
    #########################################
    def get_objects(self, objects):
        
        jets = []
        for jet in objects['jets']:
            if jet.pT > 20 and jet.abseta < 2.5: jets.append(jet)

        leps = []
        for lep in objects['leps']:
            if abs(lep.pid) == 11 and lep.pT > 10 and lep.abseta < 2.47: leps.append(lep)
            if abs(lep.pid) == 13 and lep.pT > 10 and lep.abseta < 2.4: leps.append(lep)

        bjets = []
        for b in objects['bjets']:
            if b.pT > 20 and b.abseta < 2.5: bjets.append(b)

        pTmiss = objects['pTmiss']
        MET = objects['MET']

        return jets, bjets, leps, pTmiss, MET

    #########################################
    #    Event by event analysis
    #########################################
    def event_analysis(self, base_objects):

        jets, bjets, leps, pTmiss, MET = self.get_objects(base_objects)

        base_cut = False
        if len(leps) == 0:
            self.SR['base'].Pass('lepton veto')
            if MET > 200.: 
                self.SR['base'].Pass('MET > 200')
                if len(jets) > 0 and jets[0].pT > 200: 
                    self.SR['base'].Pass('pTj1 > 200')
                    base_cut = True

        if base_cut == False: return

        #########################        
        #  Variables
        #########################
        Njet = len(jets)

        meff_Nj = []
        for i in xrange(min(Njet, 6)):
            meff = MET
            for j in xrange(i+1): meff += jets[j].pT             
            meff_Nj.append(meff)

        H_T = 0
        for i in xrange(Njet): H_T += jets[i].pT
        meff_inc = H_T + MET 

        dPhiMin_123 = 1000;        
        for i in xrange(min(Njet, 3)):
            dPhi =  delta_phi(jets[i].p.Phi(), pTmiss.Phi())
            if dPhi < dPhiMin_123: dPhiMin_123 = dPhi;


        dPhiMin_all = 1000;
        for i in xrange(Njet):
            dPhi =  delta_phi(jets[i].p.Phi(), pTmiss.Phi())
            if dPhi < dPhiMin_all: dPhiMin_all = dPhi;        

        sph, aplanarity = Aplanarity(jets)

        #########################
        #  SR: 2jl
        #########################        
        if len(jets) > 1: 
            self.SR['2jl'].Pass('Nj >= 2')
            if dPhiMin_123 > 0.8: 
                self.SR['2jl'].Pass('dPhiMin_123 > 0.8') 
                if jets[1].pT > 200.:
                    self.SR['2jl'].Pass('pTj2 > 200')
                    if MET/sqrt(H_T) > 8.:
                        self.SR['2jl'].Pass('MET/sqrt(HT) > 15')
                        if meff_inc > 1200.:
                            self.SR['2jl'].Pass('meff_inc > 1200')
                            self.SR['2jl'].PassSR()

        #########################
        #  SR: 2jm
        #########################        
        if jets[0].pT > 300.:
            self.SR['2jm'].Pass('pTj1 > 300') 
            if len(jets) >= 2:
                self.SR['2jm'].Pass('Nj >= 2')
                if dPhiMin_123 > 0.4: 
                    self.SR['2jm'].Pass('dPhiMin_123 > 0.4') 
                    if jets[1].pT > 50.: 
                        self.SR['2jm'].Pass('pTj2 > 50') 
                        if MET/sqrt(H_T) > 15.: 
                            self.SR['2jm'].Pass('MET/sqrt(H_T) > 15') 
                            if meff_inc > 1600.:
                                self.SR['2jm'].Pass('meff_inc > 1600') 
                                self.SR['2jm'].PassSR()


        #########################
        #  SR: 2jt
        #########################        
        if len(jets) >= 2:
            self.SR['2jt'].Pass('Nj >= 2')
            if dPhiMin_123 > 0.8: 
                self.SR['2jt'].Pass('dPhiMin_123 > 0.8') 
                if jets[1].pT > 200.: 
                    self.SR['2jt'].Pass('pTj2 > 200') 
                    if MET/sqrt(H_T) > 20.: 
                        self.SR['2jt'].Pass('MET/sqrt(H_T) > 20') 
                        if meff_inc > 2000.:
                            self.SR['2jt'].Pass('meff_inc > 2000') 
                            self.SR['2jt'].PassSR() 

        #########################
        #  SR: 4jt
        #########################        
        if len(jets) >= 4:
            self.SR['4jt'].Pass('Nj >= 4')
            if dPhiMin_123 > 0.4: 
                self.SR['4jt'].Pass('dPhiMin_123 > 0.4') 
                if dPhiMin_all > 0.2: 
                    self.SR['4jt'].Pass('dPhiMin_all > 0.2') 
                    if jets[1].pT > 100.: 
                        self.SR['4jt'].Pass('pTj2 > 100') 
                        if aplanarity > 0.04:                         
                            self.SR['4jt'].Pass('Aplanarity > 0.04') 
                            if MET/meff_Nj[3] > 0.2:
                                self.SR['4jt'].Pass('MET/meff_Nj > 0.2') 
                                if meff_inc > 2200.:
                                    self.SR['4jt'].Pass('meff_inc > 2200') 
                                    self.SR['4jt'].PassSR()

        #########################
        #  SR: 5j
        #########################        
        if len(jets) >= 5:
            self.SR['5j'].Pass('Nj >= 5')
            if dPhiMin_123 > 0.4: 
                self.SR['5j'].Pass('dPhiMin_123 > 0.4') 
                if dPhiMin_all > 0.2: 
                    self.SR['5j'].Pass('dPhiMin_all > 0.2') 
                    if jets[1].pT > 100.: 
                        self.SR['5j'].Pass('pTj2 > 100') 
                        if jets[4].pT > 50.: 
                            self.SR['5j'].Pass('pTj5 > 50') 
                            if aplanarity > 0.04:                         
                                self.SR['5j'].Pass('Aplanarity > 0.04') 
                                if MET/meff_Nj[4] > 0.25:
                                    self.SR['5j'].Pass('MET/meff_Nj > 0.25') 
                                    if meff_inc > 1600.:
                                        self.SR['5j'].Pass('meff_inc > 1600') 
                                        self.SR['5j'].PassSR()

        #########################
        #  SR: 6jm
        #########################        
        if len(jets) >= 6:
            self.SR['6jm'].Pass('Nj >= 6')
            if dPhiMin_123 > 0.4: 
                self.SR['6jm'].Pass('dPhiMin_123 > 0.4') 
                if dPhiMin_all > 0.2: 
                    self.SR['6jm'].Pass('dPhiMin_all > 0.2') 
                    if jets[1].pT > 100.: 
                        self.SR['6jm'].Pass('pTj2 > 100') 
                        if jets[5].pT > 50.: 
                            self.SR['6jm'].Pass('pTj6 > 50') 
                            if aplanarity > 0.04:                         
                                self.SR['6jm'].Pass('Aplanarity > 0.04') 
                                if MET/meff_Nj[5] > 0.25:
                                    self.SR['6jm'].Pass('MET/meff_Nj > 0.25') 
                                    if meff_inc > 1600.:
                                        self.SR['6jm'].Pass('meff_inc > 1600') 
                                        self.SR['6jm'].PassSR()

        #########################
        #  SR: 6jt
        #########################        
        if len(jets) >= 6:
            self.SR['6jt'].Pass('Nj >= 6')
            if dPhiMin_123 > 0.4: 
                self.SR['6jt'].Pass('dPhiMin_123 > 0.4') 
                if dPhiMin_all > 0.2: 
                    self.SR['6jt'].Pass('dPhiMin_all > 0.2') 
                    if jets[1].pT > 100.: 
                        self.SR['6jt'].Pass('pTj2 > 100') 
                        if jets[5].pT > 50.: 
                            self.SR['6jt'].Pass('pTj6 > 50') 
                            if aplanarity > 0.04:                         
                                self.SR['6jt'].Pass('Aplanarity > 0.04') 
                                if MET/meff_Nj[5] > 0.2:
                                    self.SR['6jt'].Pass('MET/meff_Nj > 0.2') 
                                    if meff_inc > 2000.:
                                        self.SR['6jt'].Pass('meff_inc > 2000') 
                                        self.SR['6jt'].PassSR()


    #########################################
    #    Output
    #########################################
    def write_result(self, iev):
        print ''
        print 'Analysis: {ananame}'.format(ananame=self.ananame)
        for key, item in self.SR.items(): item.PrintEff(iev)






