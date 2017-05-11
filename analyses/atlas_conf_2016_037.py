#!/usr/bin/env python
from objects import *
from collections import OrderedDict
from aplanarity import *
from mT2_packages import *



class atlas_conf_2016_037:

    #########################################
    #    Define groups of signal regions
    #########################################
    def __init__(self):
        self.ananame = 'atlas_conf_2016_037'
        self.SR = OrderedDict()        
        self.SR['base'] = Cut('base')
        self.SR['3L1'] = Cut('3L1')
        self.SR['3L2'] = Cut('3L2')
        self.SR['0b1'] = Cut('0b1')
        self.SR['0b2'] = Cut('0b2')
        self.SR['1b'] = Cut('1b')
        self.SR['3b'] = Cut('3b')
        self.SR['1b-DD'] = Cut('1b-DD')
        self.SR['3b-DD'] = Cut('3b-DD')
        self.SR['1b-GG'] = Cut('1b-GG')
        

    #########################################
    #    Define jets, leptons, bjets, etc..
    #########################################
    def get_objects(self, objects):
        
        jets = []
        for jet in objects['jets']:
            if jet.pT > 20 and jet.abseta < 2.8:
                jets.append(jet)

        leps = []        
        for lep in objects['leps']:
            if abs(lep.pid) == 11 and lep.pT > 10 and lep.abseta < 2.:       #electrons
                if lep.abseta < 1.37 or lep.abseta > 1.52:
                    leps.append(lep)
                    
            if abs(lep.pid) == 13 and lep.pT > 10 and lep.abseta < 2.5:       #muons
                leps.append(lep)               

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

        if len(leps) > 1:
            self.SR['base'].Pass('Leptons')
            if len(jets) > 3: 
                self.SR['base'].Pass('Njet >= 4')
                base_cut = True
                         
        if base_cut == False: return

        if len(leps) == 2:
            if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                return 

        #########################        
        #  Variables
        #########################
        Njet = len(jets)            
        Nlep = len(leps)
        Nbjet = len(bjets)

        meff = MET
        for i in xrange(Njet):
            meff = meff + jets[i].pT

        for j in xrange(Nlep):
            meff = meff + leps[j].pT

        

        

    
       # if len(jets) >2: sph, aplanarity = Aplanarity(jets)
        #else: sph, aplanarity = 0, 0

        
        #########################
        #  SR: 3L1
        #########################        
       
        if Nlep >= 3:
            self.SR['3L1'].Pass('>= 3 leptons')
            if Nbjet == 0:
                self.SR['3L1'].Pass('0 bjets')
                if jets[0].pT > 40.:                    
                    self.SR['3L1'].Pass('pTj1 > 40')
                    if jets[1].pT > 40.:
                        self.SR['3L1'].Pass('pTj2 > 40')
                        if jets[2].pT > 40.:
                            self.SR['3L1'].Pass('pTj3 > 40')
                            if jets[3].pT > 40.:
                                self.SR['3L1'].Pass('pTj4 > 40')
                                if MET > 150.:
                                    self.SR['3L1'].Pass('MET > 150')
                                    self.SR['3L1'].PassSR()
                
        
                                


        #########################
        #  SR: 3L2
        #########################

        if Nlep >= 3:
            self.SR['3L2'].Pass('>= 3 leptons')
            if Nbjet == 0:
                self.SR['3L2'].Pass('0 bjets')
                if jets[0].pT > 40.:
                    self.SR['3L2'].Pass('pTj1 > 40')
                    if jets[1].pT > 40.:
                        self.SR['3L2'].Pass('pTj2 > 40')
                        if jets[2].pT > 40.:
                            self.SR['3L2'].Pass('pTj3 > 40')
                            if jets[3].pT > 40.:
                                self.SR['3L2'].Pass('pTj4 > 40')
                                if MET > 200.:
                                    self.SR['3L2'].Pass('MET > 200')
                                    if meff > 1500.:
                                        self.SR['3L2'].Pass('meff > 1500')
                                        self.SR['3L2'].PassSR()
                        

        #########################
        #  SR: 0b1
        #########################

        if Nbjet == 0:
            self.SR['0b1'].Pass('0 bjets')
            if Njet >= 6:
                self.SR['0b1'].Pass('Njet >= 6')
                if jets[0].pT > 25.:
                    self.SR['0b1'].Pass('pTj1 > 25')
                    if jets[1].pT > 25.:
                        self.SR['0b1'].Pass('pTj2 > 25')
                        if jets[2].pT > 25.:
                            self.SR['0b1'].Pass('pTj3 > 25')
                            if jets[3].pT > 25.:
                                self.SR['0b1'].Pass('pTj4 > 25')
                                if jets[4].pT > 25.:
                                    self.SR['0b1'].Pass('pTj5 > 25')
                                    if jets[5].pT > 25.:
                                        self.SR['0b1'].Pass('pTj6 > 25')
                                        if MET > 150.:
                                            self.SR['0b1'].Pass('MET > 150')
                                            if meff > 500.:
                                                self.SR['0b1'].Pass('meff > 500')
                                                self.SR['0b1'].PassSR()
            


        #########################
        #  SR: 0b2
        #########################

        if Nbjet == 0:
            self.SR['0b2'].Pass('0 bjets')
            if Njet >= 6:
                self.SR['0b2'].Pass('Njet >= 6')
                if jets[0].pT > 40.:
                    self.SR['0b2'].Pass('pTj1 > 40')
                    if jets[1].pT > 40.:
                        self.SR['0b2'].Pass('pTj2 > 40')
                        if jets[2].pT > 40.:
                            self.SR['0b2'].Pass('pTj3 > 40')
                            if jets[3].pT > 40.:
                                self.SR['0b2'].Pass('pTj4 > 40')
                                if jets[4].pT > 40.:
                                    self.SR['0b2'].Pass('pTj5 > 40')
                                    if jets[5].pT > 40.:
                                        self.SR['0b2'].Pass('pTj6 > 40')
                                        if MET > 150.:
                                            self.SR['0b2'].Pass('MET > 150')
                                            if meff > 900.:
                                                self.SR['0b2'].Pass('meff > 900')
                                                self.SR['0b2'].PassSR()

                            

        #########################
        #  SR: 1b
        #########################

        if Nbjet >= 1:
            self.SR['1b'].Pass('Nbjet >= 1')
            if Njet >=6:
                self.SR['1b'].Pass('Njet >= 6')
                if jets[0].pT > 25.:
                    self.SR['1b'].Pass('pTj1 > 25')
                    if jets[1].pT > 25.:
                        self.SR['1b'].Pass('pTj2 > 25')
                        if jets[2].pT > 25.:
                            self.SR['1b'].Pass('pTj3 > 25')
                            if jets[3].pT > 25.:
                                self.SR['1b'].Pass('pTj4 > 25')
                                if jets[4].pT > 25.:
                                    self.SR['1b'].Pass('pTj5 > 25')
                                    if jets[5].pT > 25.:
                                        self.SR['1b'].Pass('pTj6 > 25')
                                        if MET > 200.:
                                            self.SR['1b'].Pass('MET > 200')
                                            if meff > 650.:
                                                self.SR['1b'].Pass('meff > 650')
                                                self.SR['1b'].PassSR()


        #########################
        #  SR: 3b
        #########################

        if Nbjet >= 3:
            self.SR['3b'].Pass('Nbjet >= 3')
            if Njet >= 6:
                self.SR['3b'].Pass('Njet >= 6')
                if jets[0].pT > 25.:
                    self.SR['3b'].Pass('pTj1 > 25')
                    if jets[1].pT > 25.:
                        self.SR['3b'].Pass('pTj2 > 25')
                        if jets[2].pT > 25.:
                            self.SR['3b'].Pass('pTj3 > 25')
                            if jets[3].pT > 25.:
                                self.SR['3b'].Pass('pTj4 > 25')
                                if jets[4].pT > 25.:
                                    self.SR['3b'].Pass('pTj5 > 25')
                                    if jets[5].pT > 25.:
                                        self.SR['3b'].Pass('pTj6 > 25')
                                        if MET > 150.:
                                            self.SR['3b'].Pass('MET > 150')
                                            if meff > 600.:
                                                self.SR['3b'].Pass('meff > 600')
                                                self.SR['3b'].PassSR()


        

        #########################
        #  SR: 1b-DD
        #########################

        charge = []
        for i in xrange(Nlep):
            if np.sign(leps[i].pid) == -1:
                charge = np.append(charge, -1)

        if len(charge) >= 2:
            self.SR['1b-DD'].Pass('>= 2 negative leptons')
            if Nbjet >= 1:
               self.SR['1b-DD'].Pass('Nbjet >= 1')
               if jets[0].pT > 50.:
                   self.SR['1b-DD'].Pass('pTj1 > 50')
                   if jets[1].pT > 50.:
                       self.SR['1b-DD'].Pass('pTj2 > 50')
                       if jets[2].pT > 50.:
                           self.SR['1b-DD'].Pass('pTj3 > 50')
                           if jets[3].pT > 50.:
                               self.SR['1b-DD'].Pass('pTj4 > 50')
                               if meff > 1200.:
                                   self.SR['1b-DD'].Pass('meff > 1200')
                                   self.SR['1b-DD'].PassSR()
                
                    
                
            
                    



        #########################
        #  SR: 3b-DD
        #########################

        charge1 = []

        for i in xrange(Nlep):
            if np.sign(leps[i].pid) == -1:
                charge1 = np.append(charge1, -1)

        if len(charge1) >= 2:
            self.SR['3b-DD'].Pass('>= 2 negative leptons')
            if Nbjet >= 3:
                self.SR['3b-DD'].Pass('Nbjet >= 3')
                if jets[0].pT > 50.:
                    self.SR['3b-DD'].Pass('pTj1 > 50')
                    if jets[1].pT > 50.:
                        self.SR['3b-DD'].Pass('pTj2 > 50')
                        if jets[2].pT > 50.:
                            self.SR['3b-DD'].Pass('pTj3 > 50')
                            if jets[3].pT > 50.:
                                self.SR['3b-DD'].Pass('pTj4 > 50')
                                if meff > 1000.:
                                    self.SR['3b-DD'].Pass('meff > 1000')
                                    self.SR['3b-DD'].PassSR()



        #########################
        #  SR: 1b-GG
        #########################

        if Nbjet >= 1:
            self.SR['1b-GG'].Pass('Nbjet >= 1')
            if Njet >= 6:
                self.SR['1b-GG'].Pass('Njet >= 6')
                if jets[0].pT > 50.:
                    self.SR['1b-GG'].Pass('pTj1 > 50')
                    if jets[1].pT > 50.:
                        self.SR['1b-GG'].Pass('pTj2 > 50')
                        if jets[2].pT > 50.:
                            self.SR['1b-GG'].Pass('pTj3 > 50')
                            if jets[3].pT > 50.:
                                self.SR['1b-GG'].Pass('pTj4 > 50')
                                if jets[4].pT > 50.:
                                    self.SR['1b-GG'].Pass('pTj5 > 50')
                                    if jets[5].pT > 50.:
                                        self.SR['1b-GG'].Pass('pTj6 > 50')
                                        if meff > 1800.:
                                            self.SR['1b-GG'].Pass('meff > 1800')
                                            self.SR['1b-GG'].PassSR()
            
           
                      

    #########################################
    #    Output
    #########################################
    def write_result(self, iev):
        print ''
        print 'Analysis: {ananame}'.format(ananame=self.ananame)
        for key, item in self.SR.items(): item.PrintEff(iev)




