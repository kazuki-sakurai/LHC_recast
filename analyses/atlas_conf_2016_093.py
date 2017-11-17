#!/usr/bin/env python
from objects import *
from collections import OrderedDict
from aplanarity import *
from mT2_packages import *



class atlas_conf_2016_093:

    #########################################
    #    Define groups of signal regions
    #########################################
    def __init__(self):
        self.ananame = 'atlas_conf_2016_093'
        self.SR = OrderedDict()        
        self.SR['base'] = Cut('base')
        self.SR['C1C1'] = Cut('C1C1')
        self.SR['C1N2'] = Cut('C1N2')
        

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
            if abs(lep.pid) == 11 and lep.pT > 10 and lep.abseta < 2.47:       #electrons
                leps.append(lep)
            if abs(lep.pid) == 13 and lep.pT > 10 and lep.abseta < 2.4:       #muons
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

        jets, bjets, leps,taus,  pTmiss, MET = self.get_objects(base_objects_wtaus)
        base_cut = False
        if (len(taus) == 2 and np.sign(taus[1].pid) != np.sign(taus[0].pid)) or len(taus) >= 2:
            self.SR['base'].Pass('opposite sign tau pair')
            if taus[0].pT > 35.:
                self.SR['base'].Pass('tau1pT > 35')
                if taus[1].pT > 25.:
                    self.SR['base'].Pass('tau2pT > 25')
                    if MET > 150.: 
                        self.SR['base'].Pass('MET > 150')
                        if len(bjets) == 0:
                            self.SR['base'].Pass('b-jet veto')
                            Ntau = len(taus)
                            if Ntau > 1:
                                ditaus = []
                                for i in xrange(Ntau):
                                    for j in xrange(i+1, Ntau):
                                        m_inv = (taus[i].p + taus[j].p).M()
                                        if abs (m_inv - 79) < 10:  return
                                        if m_inv > 12. : ditaus.append( [taus[i], taus[j]])
                                        self.SR['base'].Pass("Z-veto")
                                if len(ditaus):
                                    self.SR['base'].Pass("ditaus")
                                    mT2_c = []
                                    MET_m = 0.
                                    for i in xrange(len(ditaus)):
                                        mT2_c.append( MT2(ditaus[i][0].p.M(), ditaus[i][0].p.Px(), ditaus[i][0].p.Py(), ditaus[i][1].p.M(), ditaus[i][1].p.Px(), ditaus[i][1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py()))
                                    mT2 = np.max(mT2_c)
                                    if mT2 > 70.:
                                        self.SR['base'].Pass('mT2 > 70')
                                        self.SR['base'].PassSR()
                                        base_cut = True
        if base_cut == False: return

        #########################        
        #  Variables
        #########################
        Njet = len(jets)            
        Nlep = len(leps)
        
        
        if len(jets) >2: sph, aplanarity = Aplanarity(jets)
        else: sph, aplanarity = 0, 0

        
        #########################
        #  SR: C1C1
        #########################        
       
        if Ntau == Nlep:
            self.SR['C1C1'].Pass('Light lepton veto')     #All leptons are taus
            self.SR['C1C1'].PassSR()

        #########################
        #  SR: C1N2
        #########################        

        
        self.SR['C1N2'].PassSR()
       
         

       

      
                

    #########################################
    #    Output
    #########################################
    def write_result(self, iev):
        print ''
        print 'Analysis: {ananame}'.format(ananame=self.ananame)
        for key, item in self.SR.items(): item.PrintEff(iev)






