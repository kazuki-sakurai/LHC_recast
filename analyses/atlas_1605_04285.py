#!/usr/bin/env python
from objects import *
from collections import OrderedDict
from aplanarity import *

class atlas_1605_04285:

    #########################################
    #    Define groups of signal regions
    #########################################
    def __init__(self):
        self.ananame = 'atlas_1605_04285'
        self.SR = OrderedDict()        
        self.SR['base'] = Cut('base')
        self.SR['2js'] = Cut('2js')
        self.SR['5js'] = Cut('5js')
        self.SR['4jh'] = Cut('4jh')
        self.SR['4jl'] = Cut('4jl')
        self.SR['5jh'] = Cut('5jh')
        self.SR['6jh'] = Cut('6jh')
      

    #########################################
    #    Define jets, leptons, bjets, etc..
    #########################################
    def get_objects(self, objects):
        
        jets = []
        for jet in objects['jets']:
            if jet.pT > 25 and jet.abseta < 2.8: jets.append(jet)

        leps = []
        for lep in objects['leps']:
            if abs(lep.pid) == 11 and lep.pT > 7 and lep.abseta < 2.47: leps.append(lep)     #electron
            if abs(lep.pid) == 13 and lep.pT > 6 and lep.abseta < 2.4: leps.append(lep)      #muon

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
        if len(leps) == 1:
            self.SR['base'].Pass('lepton veto')
            if MET > 200.: 
                self.SR['base'].Pass('MET > 200')
                if len(jets) > 0 and jets[0].pT > 125: 
                    self.SR['base'].Pass('pTj1 > 125')
                    base_cut = True

        if base_cut == False: return

        #########################        
        #  Variables
        #########################
        Njet = len(jets)
        Nlep = len(leps)
        pTl = leps[0].pT


        H_T = pTl
        meff_inc = MET + pTl
        for i in xrange(Njet):
            H_T += jets[i].pT
            meff_inc += jets[i].pT * (jets[i].pT > 30)

        dPhi = delta_phi(leps[0].p.Phi(), pTmiss.Phi())

        mT = np.sqrt(2*pTl*MET*(1 - np.cos(dPhi)))        

        if len(jets) >2: sph, aplanarity = Aplanarity(jets)
        else: sph, aplanarity = 0, 0


        ### Soft-lepton signal regions ###
        
        #########################
        #  SR: 2js
        #########################        
        if len(jets) >= 2: 
            self.SR['2js'].Pass('Nj >= 2')
            if pTl < 35:
                self.SR['2js'].Pass('pTl < 35') 
                if jets[0].pT > 180.:
                    self.SR['2js'].Pass('pTj1 > 180')
                    if jets[1].pT > 30.:
                        self.SR['2js'].Pass('pTj2 > 30')
                        if MET > 530.:
                            self.SR['2js'].Pass('MET > 530')
                            if mT > 100.:
                                self.SR['2js'].Pass('mT > 100')
                                if MET/meff_inc > 0.38:
                                    self.SR['2js'].Pass('MET/meff_inc > 0.38')
                                    self.SR['2js'].PassSR()
                                
                                
                            

        #########################
        #  SR: 5js
        #########################        
        if len(jets) >= 5: 
            self.SR['5js'].Pass('Nj >= 5')
            if pTl < 35:
                self.SR['5js'].Pass('pTl < 35') 
                if jets[0].pT > 200.:
                    self.SR['5js'].Pass('pTj1 > 200')
                    if jets[1].pT > 200.:
                        self.SR['5js'].Pass('pTj2 > 200')
                        if jets[2].pT > 200.:
                            self.SR['5js'].Pass('pTj3 > 200')
                            if jets[3].pT > 30.:
                                self.SR['5js'].Pass('pTj4 > 30')
                                if jets[4].pT > 30.:
                                    self.SR['5js'].Pass('pTj5 > 30')
                                    if MET > 375.:
                                        self.SR['5js'].Pass('MET > 375')
                                        if H_T > 1100.:
                                            self.SR['5js'].Pass('H_T > 1100')
                                            if aplanarity > 0.02:
                                                self.SR['5js'].Pass('Aplanarity > 0.02')
                                                self.SR['5js'].PassSR()
                                            
                            

        ### Hard-lepton signal regions ###

        #########################
        #  SR: 4jh
        #########################
        if len(jets) >= 4: 
            self.SR['4jh'].Pass('Nj >= 4')
            if pTl >= 35:
                self.SR['4jh'].Pass('pTl >= 35') 
                if jets[0].pT > 325.:
                    self.SR['4jh'].Pass('pTj1 > 325')
                    if jets[1].pT > 30.:
                        self.SR['4jh'].Pass('pTj2 > 30')
                        if jets[2].pT > 30.:
                            self.SR['4jh'].Pass('pTj3 > 30')
                            if jets[3].pT > 30.:
                                self.SR['4jh'].Pass('pTj4 > 30')
                                if MET > 200.:
                                    self.SR['4jh'].Pass('MET > 200')
                                    if mT > 425.:
                                        self.SR['4jh'].Pass('mT > 425')
                                        if MET/meff_inc > 0.3:
                                            self.SR['4jh'].Pass('MET/meff_inc > 0.3')
                                            if meff_inc > 1800.:
                                                self.SR['4jh'].Pass('meff_inc > 1800')
                                                self.SR['4jh'].PassSR()
        
      

        #########################
        #  SR: 4jl
        #########################        
        if len(jets) >= 4: 
            self.SR['4jl'].Pass('Nj >= 4')
            if pTl >= 35:
                self.SR['4jl'].Pass('pTl >= 35') 
                if jets[0].pT > 325.:
                    self.SR['4jl'].Pass('pTj1 > 325')
                    if jets[1].pT > 150.:
                        self.SR['4jl'].Pass('pTj2 > 150')
                        if jets[2].pT > 150.:
                            self.SR['4jl'].Pass('pTj3 > 150')
                            if jets[3].pT > 150.:
                                self.SR['4jl'].Pass('pTj4 > 150')
                                if MET > 200.:
                                    self.SR['4jl'].Pass('MET > 200')
                                    if mT > 125.:
                                        self.SR['4jl'].Pass('mT > 125')
                                        if meff_inc > 2000.:
                                            self.SR['4jl'].Pass('meff_inc > 2000')
                                            if aplanarity > 0.04:
                                                self.SR['4jl'].Pass('Aplanarity > 0.04')
                                                self.SR['4jl'].PassSR()
                             

        #########################
        #  SR: 5jh
        #########################        
        
        if len(jets) >= 5: 
            self.SR['5jh'].Pass('Nj >= 5')
            if pTl >= 35:
                self.SR['5jh'].Pass('pTl >= 35') 
                if jets[0].pT > 225.:
                    self.SR['5jh'].Pass('pTj1 > 225')
                    if jets[1].pT > 50.:
                        self.SR['5jh'].Pass('pTj2 > 50')
                        if jets[2].pT > 50.:
                            self.SR['5jh'].Pass('pTj3 > 50')
                            if jets[3].pT > 50.:
                                self.SR['5jh'].Pass('pTj4 > 50')
                                if jets[4].pT > 50.:
                                    self.SR['5jh'].Pass('pTj5 >50')
                                    if MET > 250.:
                                        self.SR['5jh'].Pass('MET > 250')
                                        if mT > 275.:
                                            self.SR['5jh'].Pass('mT > 275')
                                            if MET/meff_inc > 0.1:
                                                self.SR['5jh'].Pass('MET/meff_inc > 0.1')
                                                if meff_inc > 1800.:
                                                    self.SR['5jh'].Pass('meff_inc > 1800')
                                                    if aplanarity > 0.04:
                                                        self.SR['5jh'].Pass('Aplanarity > 0.04')
                                                        self.SR['5jh'].PassSR()
                                            

        #########################
        #  SR: 6jh
        #########################

        if len(jets) >= 6: 
            self.SR['6jh'].Pass('Nj >= 6')
            if pTl >= 35:
                self.SR['6jh'].Pass('pTl >= 35') 
                if jets[0].pT > 125.:
                    self.SR['6jh'].Pass('pTj1 > 125')
                    if jets[1].pT > 30.:
                        self.SR['6jh'].Pass('pTj2 > 30')
                        if jets[2].pT > 30.:
                            self.SR['6jh'].Pass('pTj3 > 30')
                            if jets[3].pT > 30.:
                                self.SR['6jh'].Pass('pTj4 > 30')
                                if jets[4].pT > 30.:
                                    self.SR['6jh'].Pass('pTj5 >30')
                                    if jets[5].pT > 30.:
                                        self.SR['6jh'].Pass('pTj6 > 30')
                                        if MET > 250.:
                                            self.SR['6jh'].Pass('MET > 250')
                                            if mT > 225.:
                                                self.SR['6jh'].Pass('mT > 225')
                                                if MET/meff_inc > 0.2:
                                                    self.SR['6jh'].Pass('MET/meff_inc > 0.2')
                                                    if meff_inc > 1000.:
                                                        self.SR['6jh'].Pass('meff_inc > 1000')
                                                        if aplanarity > 0.04:
                                                            self.SR['6jh'].Pass('Aplanarity > 0.04')
                                                            self.SR['6jh'].PassSR()
        
        
                                        


                                        


    #########################################
    #    Output
    #########################################
    def write_result(self, iev):
        print ''
        print 'Analysis: {ananame}'.format(ananame=self.ananame)
        for key, item in self.SR.items(): item.PrintEff(iev)







