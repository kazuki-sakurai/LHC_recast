#!/usr/bin/env python
from objects import *
from collections import OrderedDict
from aplanarity import *

class atlas_1602_09058:

    #########################################
    #    Define groups of signal regions
    #########################################
    def __init__(self):
        self.ananame = 'atlas_1602_09058'
        self.SR = OrderedDict()        
        self.SR['base'] = Cut('base')
        self.SR['0b3j'] = Cut('0b3j')
        self.SR['0b5j'] = Cut('0b5j')
        self.SR['1b'] = Cut('1b')
        self.SR['3b'] = Cut('3b')
        

    #########################################
    #    Define jets, leptons, bjets, etc..
    #########################################
    def get_objects(self, objects):
        
        jets = []
        for jet in objects['jets']:
            if jet.pT > 20 and jet.abseta < 2.8: jets.append(jet)

        leps = []
        for lep in objects['leps']:
            if abs(lep.pid) == 11 and lep.pT > 10 and lep.abseta < 2.:       #electrons
                if lep.abseta < 1.37 or lep.abseta > 1.52:
                    leps.append(lep)
            if abs(lep.pid) == 13 and lep.pT > 10 and lep.abseta < 2.5: leps.append(lep)     #muons

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
        if (len(leps) == 2 and np.sign(leps[1].pid) == np.sign(leps[0].pid)) or len(leps) >= 2:
            self.SR['base'].Pass('lepton number')
            if MET > 125.: 
                self.SR['base'].Pass('MET > 125')
                self.SR['base'].PassSR()
                base_cut = True

        if base_cut == False: return

        #########################        
        #  Variables
        #########################
        Njet = len(jets)
        Nbjet = len(bjets)            
        Nlep = 0
        
        meff = MET
        Njet50 = 0
        for i in xrange(Njet):
            meff = meff + jets[i].pT
            Njet50 = Njet50 + 1*(jets[i].pT > 50)
        for i in xrange(len(leps)):
            meff = meff + leps[i].pT*(leps[i].pT > 20)
            Nlep = Nlep + 1*(leps[i].pT > 20)
     
        
      

        
        #########################
        #  SR: 0b3j
        #########################        
       
        if Nlep >= 3:
            self.SR['0b3j'].Pass('Nlept >= 3')
            if Nbjet == 0:
                self.SR['0b3j'].Pass('Nbjet == 0')
                if Njet50 >= 3:
                    self.SR['0b3j'].Pass('Njet50 >= 3')
                    if MET > 200.:
                        self.SR['0b3j'].Pass('MET > 200')
                        if meff > 550.:
                            self.SR['0b3j'].Pass('meff > 550')
                            self.SR['0b3j'].PassSR()

        #########################
        #  SR: 0b5j
        #########################        

        if Nlep >= 2:         
            self.SR['0b5j'].Pass('Nlept >= 2')
            if Nbjet == 0:
                self.SR['0b5j'].Pass('Nbjet == 0')
                if Njet50 >= 5:
                    self.SR['0b5j'].Pass('Njet50 >= 5')
                    if MET > 125.:
                        self.SR['0b5j'].Pass('MET > 125')
                        if meff > 650.:
                            self.SR['0b5j'].Pass('meff > 650')
                            self.SR['0b5j'].PassSR()


        #########################
        #  SR: 1b
        #########################        

        if Nlep >= 2:
           self.SR['1b'].Pass('Nlept >= 2')
           if Nbjet >= 1:
               self.SR['1b'].Pass('Nbjet >= 1')
               if Njet50 >= 4:
                   self.SR['1b'].Pass('Njet50 >= 4')
                   if MET > 150.:
                       self.SR['1b'].Pass('MET > 150')
                       if meff > 550.:
                           self.SR['1b'].Pass('meff > 550')
                           self.SR['1b'].PassSR()

        #########################
        #  SR: 3b
        #########################        

        if Nlep >= 2:
            self.SR['3b'].Pass('Nlept >= 2')
            if Nbjet >= 3:
                self.SR['3b'].Pass('Nbjet >= 3')
                if MET > 125.:
                    self.SR['3b'].Pass('MET > 125')
                    if meff > 650.:
                            self.SR['3b'].Pass('meff > 650')
                            self.SR['3b'].PassSR()
                                        
                             

        
                                        
                                            
                                        
                                        


    #########################################
    #    Output
    #########################################
    def write_result(self, iev):
        print ''
        print 'Analysis: {ananame}'.format(ananame=self.ananame)
        for key, item in self.SR.items(): item.PrintEff(iev)






