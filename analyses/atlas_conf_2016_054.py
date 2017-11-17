#!/usr/bin/env python
from objects import *
from collections import OrderedDict
from aplanarity import *

class atlas_conf_2016_054:

    #########################################
    #    Define groups of signal regions
    #########################################
    def __init__(self):
        self.ananame = 'atlas_conf_2016_054'
        self.SR = OrderedDict()        
        self.SR['base'] = Cut('base')
        self.SR['GG2J'] = Cut('GG2J')
        self.SR['GG6J_bulk'] = Cut('GG6J_bulk')
        self.SR['GG6J_high_mass'] = Cut('GG6J_high_mass')
        self.SR['GG4J_low-x'] = Cut('GG4J_low-x')
        #self.SR['GG4J_low-x_b-veto'] = Cut('GG4J_low-x_b-veto')
        self.SR['GG4J_high-x'] = Cut('GG4J_high-x')
        ## self.SR['SS4J_x=1/2'] = Cut('SS4J_x=1/2')
        ## self.SR['SS5J_x=1/2'] = Cut('SS5J_x=1/2')
        ## self.SR['SS4J_low-x'] = Cut('SS4J_low-x')
        ## self.SR['SS5J_high-x'] = Cut('SS5J_high-x')
        

    #########################################
    #    Define jets, leptons, bjets, etc..
    #########################################
    def get_objects(self, objects):
        
        jets = []
        for jet in objects['jets']:
            if jet.pT > 30 and jet.abseta < 2.8: jets.append(jet)

        leps = []
        for lep in objects['leps']:
            if abs(lep.pid) == 11 and lep.pT > 7 and lep.abseta < 2.47:       #electrons
                leps.append(lep)
            if abs(lep.pid) == 13 and lep.pT > 6 and lep.abseta < 2.5:        #muons
                leps.append(lep)    

        bjets = []
        for b in objects['bjets']:
            if b.pT > 30 and b.abseta < 2.5: bjets.append(b)

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
            self.SR['base'].Pass('One single lepton')
            if MET > 250.: 
                self.SR['base'].Pass('MET > 250')
                self.SR['base'].PassSR()
                base_cut = True

        if base_cut == False: return

        #########################        
        #  Variables
        #########################
        Njet = len(jets)
        Nbjet = len(bjets)
        pTl = leps[0].pT                                 #Lepton transverse momentum
        dPhi = delta_phi(leps[0].p.Phi(),pTmiss.Phi())   #Angle between pTlepton and pTmiss
        
        meff = MET + pTl                                 #Inclusive effective mass
        for i in xrange(Njet):
            meff = meff + jets[i].pT

        mT = np.sqrt(2*leps[0].pT*MET*(1 - np.cos(dPhi)))  #Transverse mass

        if Njet > 2: sph, aplanarity = Aplanarity(jets)    #Jet aplanarity
        else: sph, aplanarity = 0, 0

        JL = jets + leps
        if len(JL) > 2: Laplanarity = Aplanarity(JL)       #Lepton aplanarity
        else: Laplanarity = 0

        
           
        #########################
        #  SR: GG2J
        #########################        
       
        ## if Njet > 1:
        ##     self.SR['GG2J'].Pass('Njet > 1')
        ##     if leps[0].pT < 35.:
        ##         self.SR['GG2J'].Pass('lepton pT < 35')
        ##         if jets[0].pT > 200.:
        ##             self.SR['GG2J'].Pass('pTj0 > 200')
        ##             if jets[1].pT > 30.:
        ##                 self.SR['GG2J'].Pass('pTj1 > 30')
        ##                 if mT > 100.:
        ##                     self.SR['GG2J'].Pass('mT > 100')
        ##                     if MET > 460.:
        ##                         self.SR['GG2J'].Pass('MET > 460')
        ##                         if MET/meff > 0.35:
        ##                             self.SR['GG2J'].Pass('MET/meff . 0.35')
        ##                             self.SR['GG2J'].PassSR()

        #########################
        #  SR: GG6J_bulk
        #########################        

        if pTl > 35.:
            self.SR['GG6J_bulk'].Pass('pTl > 35')
            if Njet >= 6:
                self.SR['GG6J_bulk'].Pass('Njet >= 6')
                if jets[0].pT > 125.:
                    self.SR['GG6J_bulk'].Pass('pTj1 > 125')
                    if mT > 225.:
                        self.SR['GG6J_bulk'].Pass('mT > 225')
                        if meff > 1000.:
                            self.SR['GG6J_bulk'].Pass('meff > 1000')
                            if MET/meff > 0.2:
                                self.SR['GG6J_bulk'].Pass('MET/meff > 0.2')
                                if aplanarity > 0.04:
                                    self.SR['GG6J_bulk'].Pass('Jet Aplanarity > 0.04')
                                    self.SR['GG6J_bulk'].PassSR()


        #########################
        #  SR: GG6J_high_mass
        #########################        

        ## if pTl > 35.:
        ##     self.SR['GG6J_high_mass'].Pass('pTl > 35')
        ##     if Njet >= 6:
        ##         self.SR['GG6J_high_mass'].Pass('Njet >= 6')
        ##         if jets[0].pT > 125.:
        ##             self.SR['GG6J_high_mass'].Pass('pTj1 > 125')
        ##             if mT > 225.:
        ##                 self.SR['GG6J_high_mass'].Pass('mT > 225')
        ##                 if meff > 2000.:
        ##                     self.SR['GG6J_high_mass'].Pass('meff > 2000')
        ##                     if MET/meff > 0.1:
        ##                         self.SR['GG6J_high_mass'].Pass('MET/meff > 0.1')
        ##                         if aplanarity > 0.04:
        ##                             self.SR['GG6J_high_mass'].Pass('Jet aplanarity > 0.04')
        ##                             self.SR['GG6J_high_mass'].PassSR()
                                        

                           

        ## #########################
        ## #  SR: GG4J_low-x
        ## #########################        

        ## if Njet >= 4:
        ##     self.SR['GG4J_low-x'].Pass('Njet >= 4')
        ##     if jets[0].pT > 100.:
        ##         self.SR['GG4J_low-x'].Pass('pTj1 > 100')
        ##         if jets[1].pT > 100.:
        ##             self.SR['GG4J_low-x'].Pass('pTj2 > 100')
        ##             if jets[2].pT > 100.:
        ##                 self.SR['GG4J_low-x'].Pass('pTj3 > 100')
        ##                 if jets[3].pT > 100.:
        ##                     self.SR['GG4J_low-x'].Pass('pTj4 > 100')
        ##                     if mT > 125.:
        ##                         self.SR['GG4J_low-x'].Pass('mT > 125')
        ##                         if meff > 2000.:
        ##                             self.SR['GG4J_low-x'].Pass('meff > 2000')
        ##                             if aplanarity > 0.06:
        ##                                 self.SR['GG4J_low-x'].Pass('Jet aplanarity > 0.06')
        ##                                 self.SR['GG4J_low-x'].PassSR()


        ## #########################
        ## #  SR: GG4J_low-x b-veto
        ## #########################

        ## ## if Njet >= 4:
        ## ##     self.SR['GG4J_low-x_b-veto'].Pass('Njet >= 4')
        ## ##     if jets[0].pT > 100.:
        ## ##         self.SR['GG4J_low-x_b-veto'].Pass('pTj1 > 100')
        ## ##         if jets[1].pT > 100.:
        ## ##             self.SR['GG4J_low-x_b-veto'].Pass('pTj2 > 100')
        ## ##             if jets[2].pT > 100.:
        ## ##                 self.SR['GG4J_low-x_b-veto'].Pass('pTj3 > 100')
        ## ##                 if jets[3].pT > 100.:
        ## ##                     self.SR['GG4J_low-x_b-veto'].Pass('pTj4 > 100')
        ## ##                     if len(bjets) == 0:
        ## ##                         self.SR['GG4J_low-x_b-veto'].Pass('b-jets veto')
        ## ##                         if mT > 125.:
        ## ##                             self.SR['GG4J_low-x_b-veto'].Pass('mT > 125')
        ## ##                             if meff > 2000.:
        ## ##                                 self.SR['GG4J_low-x_b-veto'].Pass('meff > 2000')
        ## ##                                 if aplanarity > 0.03:
        ## ##                                     self.SR['GG4J_low-x_b-veto'].Pass('Jet aplanarity > 0.03')
        ## ##                                     self.SR['GG4J_low-x_b-veto'].PassSR()


        ## #########################
        ## #  SR: GG4J_high-x
        ## #########################

        ## if pTl > 35.:
        ##     self.SR['GG4J_high-x'].Pass('pTl > 35')
        ##     if Njet >= 4:
        ##         self.SR['GG4J_high-x'].Pass('Njet >= 4')
        ##         if jets[0].pT > 400.:
        ##             self.SR['GG4J_high-x'].Pass('pTj1 > 400')
        ##             if jets[3].pT < 100.:
        ##                 self.SR['GG4J_high-x'].Pass('pTj4 < 100')
        ##                 if mT > 475.:
        ##                     self.SR['GG4J_high-x'].Pass('mT > 475')
        ##                     if meff > 1600.:
        ##                         self.SR['GG4J_high-x'].Pass('meff > 1600')
        ##                         if MET/meff > 0.3:
        ##                             self.SR['GG4J_high-x'].Pass('MET/meff > 0.3')
        ##                             self.SR['GG4J_high-x'].PassSR()




        #########################
        #  SR: SS4J_x=1/2
        #########################

        ## if pTl > 35.:
        ##     self.SR['SS4J_x=1/2'].Pass('pTl > 35')
        ##     if Njet >= 4:
        ##         self.SR['SS4J_x=1/2'].Pass('Njet >= 4')
        ##         if jets[0].pT > 50.:
        ##             self.SR['SS4J_x=1/2'].Pass('pTj1 > 50')
        ##             if jets[1].pT > 50.:
        ##                 self.SR['SS4J_x=1/2'].Pass('pTj2 > 50')
        ##                 if jets[2].pT > 50.:
        ##                     self.SR['SS4J_x=1/2'].Pass('pTj3 > 50')
        ##                     if jets[3].pT > 50.:
        ##                         self.SR['SS4J_x=1/2'].Pass('pTj4 > 50')
        ##                         if len(bjets) == 0:
        ##                             self.SR['SS4J_x=1/2'].Pass('b-jets veto')
        ##                             if mT > 175.:
        ##                                 self.SR['SS4J_x=1/2'].Pass('mT > 175')
        ##                                 if MET > 300.:
        ##                                     self.SR['SS4J_x=1/2'].Pass('MET > 300')
        ##                                     if meff > 1200.:
        ##                                         self.SR['SS4J_x=1/2'].Pass('meff > 1200')
        ##                                         if Laplanarity > 0.08:
        ##                                             self.SR['SS4J_x=1/2'].Pass('Lepton aplanarity > 0.08')
        ##                                             self.SR['SS4J_x=1/2'].PassSR()


        ## #########################
        ## #  SR: SS5J_x=1/2
        ## #########################

        ## if pTl > 35.:
        ##     self.SR['SS5J_x=1/2'].Pass('pTl > 35')
        ##     if Njet >= 5:
        ##         self.SR['SS5J_x=1/2'].Pass('Njet >= 5')
        ##         if jets[0].pT > 50.:
        ##             self.SR['SS5J_x=1/2'].Pass('pTj1 > 50')
        ##             if jets[1].pT > 50.:
        ##                 self.SR['SS5J_x=1/2'].Pass('pTj2 > 50')
        ##                 if jets[2].pT > 50.:
        ##                     self.SR['SS5J_x=1/2'].Pass('pTj3 > 50')
        ##                     if jets[3].pT > 50.:
        ##                         self.SR['SS5J_x=1/2'].Pass('pTj4 > 50')
        ##                         if jets[4].pT > 50.:
        ##                             self.SR['SS5J_x=1/2'].Pass('pTj5 > 50')
        ##                             if len(bjets) == 0:
        ##                                 self.SR['SS5J_x=1/2'].Pass('b-jets veto')
        ##                                 if mT > 175.:
        ##                                     self.SR['SS5J_x=1/2'].Pass('mT > 175')
        ##                                     if MET > 300.:
        ##                                         self.SR['SS5J_x=1/2'].Pass('MET > 300')
        ##                                         if MET/meff > 0.2:
        ##                                             self.SR['SS5J_x=1/2'].Pass('MET/meff > 0.2')
        ##                                             self.SR['SS5J_x=1/2'].PassSR()
                                                    


        ## #########################
        ## #  SR: SS4J_low-x
        ## #########################

        ## if pTl > 35.:
        ##     self.SR['SS4J_low-x'].Pass('pTl > 35')
        ##     if Njet >= 4:
        ##         self.SR['SS4J_low-x'].Pass('Njet >= 4')
        ##         if jets[0].pT > 250.:
        ##             self.SR['SS4J_low-x'].Pass('pTj1 > 250')
        ##             if jets[1].pT > 250.:
        ##                 self.SR['SS4J_low-x'].Pass('pTj2 > 250')
        ##                 if len(bjets) == 0:
        ##                     self.SR['SS4J_low-x'].Pass('b-jets veto')
        ##                     if mT > 150. and mT < 400.:
        ##                         self.SR['SS4J_low-x'].Pass('mT [150, 400]')
        ##                         if Laplanarity > 0.03:
        ##                             self.SR['SS4J_low-x'].Pass('Lepton aplanarity > 0.03')
        ##                             self.SR['SS4J_low-x'].PassSR()


        ## #########################
        ## #  SR: SS5J_high-x
        ## #########################

        ## if pTl > 35.:
        ##     self.SR['SS5J_high-x'].Pass('pTl > 35')
        ##     if Njet >= 5:
        ##         self.SR['SS5J_high-x'].Pass('Njet >= 5')
        ##         if mT > 400.:
        ##             self.SR['SS5J_high-x'].Pass('mT > 400')
        ##             if MET > 400.:
        ##                 self.SR['SS5J_high-x'].Pass('MET > 400')
        ##                 if Laplanarity > 0.03:
        ##                     self.SR['SS5J_high-x'].Pass('Lepton aplanarity > 0.03')
        ##                     self.SR['SS5J_high-x'].PassSR()
                             

        
                                        
                                            
                                        
                                        


    #########################################
    #    Output
    #########################################
    def write_result(self, iev):
        print ''
        print 'Analysis: {ananame}'.format(ananame=self.ananame)
        for key, item in self.SR.items(): item.PrintEff(iev)
