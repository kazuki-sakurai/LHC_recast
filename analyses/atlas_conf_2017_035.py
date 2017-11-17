#!/usr/bin/env python
from objects import *
from collections import OrderedDict
from aplanarity import *
from mT2_packages import *
import alyabar as aly
from scipy import random as rnd


class atlas_conf_2017_035:

    #########################################
    #    Define groups of signal regions
    #########################################
    def __init__(self):
        self.ananame = 'atlas_conf_2017_035'
        self.SR = OrderedDict()        
        self.SR['base'] = Cut('base')
        self.SR['lowMass'] = Cut('lowMass')
        self.SR['highMass'] = Cut('highMass')
        
      
     
        
        
        

    #########################################
    #    Define jets, leptons, bjets, etc..
    #########################################
    def get_objects(self, objects):
        
        jets = []
        for jet in objects['jets']:
            if jet.pT > 20 and jet.abseta < 2.8: jets.append(jet)

        leps = []
        taus = []
        
        
        for lep in objects['leps']:
            if abs(lep.pid) == 15: lep.pidBDT = rnd.random()
            if abs(lep.pid) == 11 and lep.pT > 10 and lep.abseta < 2.47:       #electrons
                leps.append(lep)
            if abs(lep.pid) == 13 and lep.pT > 10 and lep.abseta < 2.7:       #muons
                leps.append(lep)
            if abs(lep.pid) == 15 and lep.pT > 20 and lep.abseta < 2.47:     #tau
                
                if lep.abseta < 1.37 or lep.abseta > 1.52:
                    leps.append(lep)
                    taus.append(lep)


        bjets = []
        for b in objects['bjets']:
            if b.pT > 20 and b.abseta < 2.5: bjets.append(b)

        pTmiss = objects['pTmiss']
        MET = objects['MET']

        return jets, bjets, leps, taus, pTmiss, MET

    #########################################
    #    Event by event analysis
    #########################################

   
    
    def event_analysis(self, base_objects_wtaus):

        jets, bjets, leps, taus, pTmiss, MET = self.get_objects(base_objects_wtaus)
        base_cut = False

        Ntau = len(taus)
        Nbjet = len(bjets)
        Njet = len(jets)
        Nlep = len(leps)
    

        if Ntau >= 2:
            self.SR['base'].Pass('Ntau >= 2')
            ditaus = []
            for i in xrange(Ntau):
                for j in xrange(i+1, Ntau):
                    if  np.sign(taus[i].pid) != np.sign(taus[j].pid):
                        m_inv = (taus[i].p + taus[j].p).M()
                        if m_inv < 69. or m_inv > 89.:
                            if m_inv > 12.:         
                                ditaus.append([taus[i], taus[j]])
            if len(ditaus) != 0:
                self.SR['base'].Pass('OS tau pair and Z veto')
                if Nbjet == 0:
                    self.SR['base'].Pass('Nbjet == 0')
                    self.SR['base'].PassSR()
                    base_cut = True

    
           
        if base_cut == False: return

        #########################        
        #  Variables
        #########################
      
        mZ = 91.1876      #PDG 2016 #GeV
        MET_m = 0.
    

    
       # if len(jets) >2: sph, aplanarity = Aplanarity(jets)
        #else: sph, aplanarity = 0, 0


        #########################
        #  SR: lowMass
        #########################

        mtaus = []
        for i in xrange(Ntau):
            if taus[i].pidBDT > 0.525: 
                mtaus.append(taus[i])
            if len(mtaus) >= 2:
                self.SR['lowMass'].Pass('at least 2 medium taus')
            if len(ditaus) > 1:
                mT2_new = 0.
                for i in xrange(len(ditaus)):
                    mT2 = MT2(ditaus[i][0].p.M(), ditaus[i][0].p.Px(), ditaus[i][0].p.Py(), ditaus[i][1].p.M(), ditaus[i][1].p.Px(), ditaus[i][1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                    if mT2 > mT2_new:
                        mT2_new = mT2
                        A = i            #index of the choosen pair, the largest  mT2 pair
                if mT2_new > 70.:
                    self.SR['lowMass'].Pass('mT2 > 70 GeV')
                    if MET > 150.:
                        self.SR['lowMass'].Pass('MET > 150 GeV')
                        if taus[0].pT > 50.:
                            self.SR['lowMass'].Pass('pTtau1 > 50 GeV')
                            if taus[1].pT > 40.:
                                self.SR['lowMass'].Pass('pTtau2 > 40 GeV')
                                self.SR['lowMass'].PassSR()


            if len(ditaus) == 1:
                mT2 = MT2(ditaus[0][0].p.M(), ditaus[0][0].p.Px(), ditaus[0][0].p.Py(), ditaus[0][1].p.M(), ditaus[0][1].p.Px(), ditaus[0][1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                if mT2 > 70.:
                    self.SR['lowMass'].Pass('mT2 > 70 GeV')
                    if MET > 150.:
                        self.SR['lowMass'].Pass('MET > 150 GeV')
                        if taus[0].pT > 50.:
                            self.SR['lowMass'].Pass('pTtau1 > 50 GeV')
                            if taus[1].pT > 40.:
                                self.SR['lowMass'].Pass('pTtau2 > 40 GeV')
                                self.SR['lowMass'].PassSR()

    
        #########################
        #  SR: highMass
        #########################

        mtaus = []
        ttaus = []
        for i in xrange(Ntau):
            if taus[i].pidBDT > 0.525 :
                mtaus.append(taus[i])
            if taus[i].pidBDT > 0.625:
                ttaus.append(taus[i])
        if len(mtaus) > 1 and len(ttaus) > 0:
            self.SR['highMass'].Pass('at least one medium and one tight taus')
            m_inv = (taus[0].p + taus[1].p).M()
            if m_inv > 110.:
                self.SR['highMass'].Pass('m_inv > 110 GeV')
                if len(ditaus) == 1:
                    mT2 = MT2(ditaus[0][0].p.M(), ditaus[0][0].p.Px(), ditaus[0][0].p.Py(), ditaus[0][1].p.M(), ditaus[0][1].p.Px(), ditaus[0][1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                    if mT2 > 90.:
                        self.SR['highMass'].Pass('mT2 > 90 GeV')
                        if MET > 150.:
                           self.SR['highMass'].Pass('MET > 150 GeV')
                           if taus[0].pT > 80.:
                               self.SR['highMass'].Pass('pTtau1 > 80 GeV')
                               if taus[1].pT > 40.:
                                   self.SR['highMass'].Pass('pTtau2 > 40 GeV')
                                   self.SR['highMass'].PassSR
                        if MET > 110.:
                            self.SR['highMass'].Pass('MET > 110 GeV')
                            if taus[0].pT > 95.:
                                self.SR['highMass'].Pass('pTtau1 > 95 GeV')
                                if taus[1].pT > 65.:
                                    self.SR['highMass'].Pass('pTtau2 > 65 GeV')
                                    self.SR['highMass'].PassSR()


                if len(ditaus) > 1:
                    mT2_new = 0.
                    for i in xrange(len(ditaus)):
                        mT2 = MT2(ditaus[i][0].p.M(), ditaus[i][0].p.Px(), ditaus[i][0].p.Py(), ditaus[i][1].p.M(), ditaus[i][1].p.Px(), ditaus[i][1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                        if mT2 > mT2_new:
                            mT2_new = mT2
                            A = i            #index of the choosen pair, the largest  mT2 pair
                    if mT2_new > 90.:
                        self.SR['lowMass'].Pass('mT2 > 90 GeV')
                        if MET > 150.:
                           self.SR['highMass'].Pass('MET > 150 GeV')
                           if taus[0].pT > 80.:
                               self.SR['highMass'].Pass('pTtau1 > 80 GeV')
                               if taus[1].pT > 40.:
                                   self.SR['highMass'].Pass('pTtau2 > 40 GeV')
                                   self.SR['highMass'].PassSR
                        if MET > 110.:
                            self.SR['highMass'].Pass('MET > 110 GeV')
                            if taus[0].pT > 95.:
                                self.SR['highMass'].Pass('pTtau1 > 95 GeV')
                                if taus[1].pT > 65.:
                                    self.SR['highMass'].Pass('pTtau2 > 65 GeV')
                                    self.SR['highMass'].PassSR()



                                                

    #########################################
    #    Output
    #########################################
    def write_result(self, iev):
        print ''
        print 'Analysis: {ananame}'.format(ananame=self.ananame)
        for key, item in self.SR.items(): item.PrintEff(iev)

