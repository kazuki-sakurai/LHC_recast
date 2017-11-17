#!/usr/bin/env python
from objects import *
from collections import OrderedDict
from aplanarity import *
from mT2_packages import *



class atlas_1706_03731:

    #########################################
    #    Define groups of signal regions
    #########################################
    def __init__(self):
        self.ananame = 'atlas_1706_03731'
        self.SR = OrderedDict()        
        self.SR['base'] = Cut('base')
        self.SR['Rpc2L2bS'] = Cut('Rpc2L2bS')
        self.SR['Rpc2L2bH'] = Cut('Rpc2L2bH')
        self.SR['Rpc2Lsoft1b'] = Cut('Rpc2Lsoft1b')
        self.SR['Rpc2Lsoft2b'] = Cut('Rpc2Lsoft2b')
        self.SR['Rpc2L0bS'] = Cut('Rpc2L0bS')
        self.SR['Rpc2L0bH'] = Cut('Rpc2L0bH')
        self.SR['Rpc3L0bS'] = Cut('Rpc3L0bS')
        self.SR['Rpc3L0bH'] = Cut('Rpc3L0bH')
        self.SR['Rpc3L1bS'] = Cut('Rpc3L1bS')
        self.SR['Rpc3L1bH'] = Cut('Rpc3L1bH')
        self.SR['Rpc2L1bS'] = Cut('Rpc2L1bS')
        self.SR['Rpc2L1bH'] = Cut('Rpc2L1bH')
        self.SR['Rpc3LSS1b'] = Cut('Rpc3LSS1b')
        
        

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

        ## if len(leps) > 1:
        ##     self.SR['base'].Pass('Leptons')             #At least two leptons
        self.SR['base'].PassSR()
        base_cut = True
                         
        if base_cut == False: return

        if len(leps) == 2:
            if np.sign(leps[0].pid) != np.sign(leps[1].pid):              #Two same sign leptons
                return 

        #########################        
        #  Variables
        #########################
        Njet = len(jets)            
        Nlep = len(leps)
        Nbjet = len(bjets)

        #meff
        meff = MET
        for i in xrange(Njet):
            meff = meff + jets[i].pT

        for j in xrange(Nlep):
            meff = meff + leps[j].pT

        

        

    
       # if len(jets) >2: sph, aplanarity = Aplanarity(jets)
        #else: sph, aplanarity = 0, 0

        
        #########################
        #  SR: Rpc2L2bS
        #########################        
       
        if Nlep >= 2:
            self.SR['Rpc2L2bS'].Pass('>= 2 SS leptons')
            if Nbjet >= 2:
                self.SR['Rpc2L2bS'].Pass('Nbjet >= 2')
                if Njet >= 6:
                    self.SR['Rpc2L2bS'].Pass('Njet >= 6')
                    if jets[0].pT > 25.:
                        self.SR['Rpc2L2bS'].Pass('pTj1 > 25 GeV')
                        if jets[1].pT > 25.:
                            self.SR['Rpc2L2bS'].Pass('pTj2 > 25 GeV')
                            if jets[2].pT > 25.:
                                self.SR['Rpc2L2bS'].Pass('pTj3 > 25 GeV')
                                if jets[3].pT > 25.:
                                    self.SR['Rpc2L2bS'].Pass('pTj4 > 25 GeV')
                                    if jets[4].pT > 25.:
                                        self.SR['Rpc2L2bS'].Pass('pTj5 > 25 GeV')
                                        if jets[5].pT > 25.:
                                            self.SR['Rpc2L2bS'].Pass('pTj6 > 25 GeV')
                                            if MET > 200.:
                                                self.SR['Rpc2L2bS'].Pass('MET > 200 GeV')
                                                if meff > 600.:
                                                    self.SR['Rpc2L2bS'].Pass('meff > 600 GeV')
                                                    if MET/meff > 0.25:
                                                        self.SR['Rpc2L2bS'].Pass('MET/meff > 0.25')
                                                        self.SR['Rpc2L2bS'].PassSR()
                


        #########################
        #  SR: Rpc2L2bH
        #########################
                                

        if Nlep >= 2:
            self.SR['Rpc2L2bH'].Pass('>= 2 SS leptons')
            if Nbjet >= 2:
                self.SR['Rpc2L2bH'].Pass('Nbjet >= 2')
                if Njet >= 6:
                    self.SR['Rpc2L2bH'].Pass('Njet >= 6')
                    if jets[0].pT > 25.:
                        self.SR['Rpc2L2bH'].Pass('pTj1 > 25 GeV')
                        if jets[1].pT > 25.:
                            self.SR['Rpc2L2bH'].Pass('pTj2 > 25 GeV')
                            if jets[2].pT > 25.:
                                self.SR['Rpc2L2bH'].Pass('pTj3 > 25 GeV')
                                if jets[3].pT > 25.:
                                    self.SR['Rpc2L2bH'].Pass('pTj4 > 25 GeV')
                                    if jets[4].pT > 25.:
                                        self.SR['Rpc2L2bH'].Pass('pTj5 > 25 GeV')
                                        if jets[5].pT > 25.:
                                            self.SR['Rpc2L2bH'].Pass('pTj6 > 25 GeV')
                                            if meff > 1800.:
                                                self.SR['Rpc2L2bH'].Pass('meff > 1800 GeV')
                                                if MET/meff > 0.15:
                                                    self.SR['Rpc2L2bH'].Pass('MET/meff > 0.15')
                                                    self.SR['Rpc2L2bH'].PassSR()



                                                    
        #########################
        #  SR: Rpc2Lsoft1b
        #########################

        if Nlep >= 2:
            self.SR['Rpc2Lsoft1b'].Pass('>= 2 SS leptons')
            if Nbjet >= 1:
                self.SR['Rpc2Lsoft1b'].Pass('Nbjet >= 1')
                if Njet >= 6:
                    self.SR['Rpc2Lsoft1b'].Pass('Njet >= 6')
                    if jets[0].pT > 25.:
                        self.SR['Rpc2Lsoft1b'].Pass('pTj1 > 25 GeV')
                        if jets[1].pT > 25.:
                            self.SR['Rpc2Lsoft1b'].Pass('pTj2 > 25 GeV')
                            if jets[2].pT > 25.:
                                self.SR['Rpc2Lsoft1b'].Pass('pTj3 > 25 GeV')
                                if jets[3].pT > 25.:
                                    self.SR['Rpc2Lsoft1b'].Pass('pTj4 > 25 GeV')
                                    if jets[4].pT > 25.:
                                        self.SR['Rpc2Lsoft1b'].Pass('pTj5 > 25 GeV')
                                        if jets[5].pT > 25.:
                                            self.SR['Rpc2Lsoft1b'].Pass('pTj6 > 25 GeV')
                                            if MET > 100.:
                                                self.SR['Rpc2Lsoft1b'].Pass('MET > 100 GeV')
                                                if MET/meff > 0.3:
                                                    self.SR['Rpc2Lsoft1b'].Pass('MET/meff > 0.3')
                                                    if leps[0].pT > 20. and leps[0].pT < 100.:
                                                        self.SR['Rpc2Lsoft1b'].Pass('20 < pTl1 < 100 GeV ')
                                                        if leps[1].pT > 10. and leps[1].pT < 100.:
                                                            self.SR['Rpc2Lsoft1b'].Pass('10 < pTl2 < 100 GeV')
                                                            self.SR['Rpc2Lsoft1b'].PassSR()
                                                
            
                    
                

      
        #########################
        #  SR: Rpc2Lsoft2b
        #########################


        if Nlep >= 2:
            self.SR['Rpc2Lsoft2b'].Pass('>= 2 SS leptons')
            if Nbjet >= 2:
                self.SR['Rpc2Lsoft2b'].Pass('Nbjets >= 2')
                if Njet >= 6:
                    self.SR['Rpc2Lsoft2b'].Pass('Njet >= 6')
                    if jets[0].pT > 25.:
                        self.SR['Rpc2Lsoft2b'].Pass('pTj1 > 25 GeV')
                        if jets[1].pT > 25.:
                            self.SR['Rpc2Lsoft2b'].Pass('pTj2 > 25 GeV')
                            if jets[2].pT > 25.:
                                self.SR['Rpc2Lsoft2b'].Pass('pTj3 > 25 GeV')
                                if jets[3].pT > 25.:
                                    self.SR['Rpc2Lsoft2b'].Pass('pTj4 > 25 GeV')
                                    if jets[4].pT > 25.:
                                        self.SR['Rpc2Lsoft2b'].Pass('pTj5 > 25 GeV')
                                        if jets[5].pT > 25.:
                                            self.SR['Rpc2Lsoft2b'].Pass('pTj6 > 25 GeV')
                                            if MET > 200.:
                                                self.SR['Rpc2Lsoft2b'].Pass('MET > 200 GeV')
                                                if meff > 600.:
                                                    self.SR['Rpc2Lsoft2b'].Pass('meff > 600 GeV')
                                                    if MET/meff > 0.25:
                                                        self.SR['Rpc2Lsoft2b'].Pass('MET/meff > 0.25')
                                                        if leps[0].pT > 20. and leps[0].pT < 100.:
                                                            self.SR['Rpc2Lsoft2b'].Pass('20 < pTl1 < 100 GeV')
                                                            if leps[1].pT > 10. and leps[1].pT < 100.:
                                                                self.SR['Rpc2Lsoft2b'].Pass('10 < pTl2 < 100 GeV')
                                                                self.SR['Rpc2Lsoft2b'].PassSR()
                                                
            


        #########################
        #  SR: Rpc2L0bS
        #########################


        if Nlep >= 2:
            self.SR['Rpc2L0bS'].Pass('>= 2 SS leptons')
            if Nbjet == 0:
                self.SR['Rpc2L0bS'].Pass('Nbjet = 0')
                if Njet >= 6:
                    self.SR['Rpc2L0bS'].Pass('Njet >= 6')
                    if jets[0].pT > 25.:
                        self.SR['Rpc2L0bS'].Pass('pTj1 > 25 GeV')
                        if jets[1].pT > 25.:
                            self.SR['Rpc2L0bS'].Pass('pTj2 > 25 GeV')
                            if jets[2].pT > 25.:
                                self.SR['Rpc2L0bS'].Pass('pTj3 > 25 GeV')
                                if jets[3].pT > 25.:
                                    self.SR['Rpc2L0bS'].Pass('pTj4 > 25 GeV')
                                    if jets[4].pT > 25.:
                                        self.SR['Rpc2L0bS'].Pass('pTj5 > 25 GeV')
                                        if jets[5].pT > 25.:
                                            self.SR['Rpc2L0bS'].Pass('pTj6 > 25 GeV')
                                            if MET > 150.:
                                                self.SR['Rpc2L0bS'].Pass('MET > 150 GeV')
                                                if MET/meff > 0.25:
                                                    self.SR['Rpc2L0bS'].Pass('MET/meff > 0.25')
                                                    self.SR['Rpc2L0bS'].PassSR()
                                                
                
                
        #########################
        #  SR: Rpc2L0bH
        #########################


        if Nlep >= 2:
            self.SR['Rpc2L0bH'].Pass('>= 2 SS leptons')
            if Nbjet == 0:
                self.SR['Rpc2L0bH'].Pass('Nbjet == 0')
                if Njet >= 6:
                    self.SR['Rpc2L0bH'].Pass('Njet >= 6')
                    if jets[0].pT > 40.:
                        self.SR['Rpc2L0bH'].Pass('pTj1 > 40 GeV')
                        if jets[1].pT > 40.:
                            self.SR['Rpc2L0bH'].Pass('pTj2 > 40 GeV')
                            if jets[2].pT > 40.:
                                self.SR['Rpc2L0bH'].Pass('pTj3 > 40 GeV')
                                if jets[3].pT > 40.:
                                    self.SR['Rpc2L0bH'].Pass('pTj4 > 40 GeV')
                                    if jets[4].pT > 40.:
                                        self.SR['Rpc2L0bH'].Pass('pTj5 > 40 GeV')
                                        if jets[5].pT > 40.:
                                            self.SR['Rpc2L0bH'].Pass('pTj6 > 40 GeV')
                                            if MET > 250.:
                                                self.SR['Rpc2L0bH'].Pass('MET > 250 GeV')
                                                if meff > 900.:
                                                    self.SR['Rpc2L0bH'].Pass('meff > 900 GeV')
                                                    self.SR['Rpc2L0bH'].PassSR()
                                                

        #########################
        #  SR: Rpc3L0bS
        #########################

        if Nlep >= 3:
            self.SR['Rpc3L0bS'].Pass('Nlep >= 3')
            if Nbjet == 0:
                self.SR['Rpc3L0bS'].Pass('Nbjet == 0')
                if Njet >= 4:
                    self.SR['Rpc3L0bS'].Pass('Njet >= 4')
                    if jets[0].pT > 40.:
                        self.SR['Rpc3L0bS'].Pass('pTj1 > 40 GeV')
                        if jets[1].pT > 40.:
                            self.SR['Rpc3L0bS'].Pass('pTj2 > 40 GeV')
                            if jets[2].pT > 40.:
                                self.SR['Rpc3L0bS'].Pass('pTj3 > 40 GeV')
                                if jets[3].pT > 40.:
                                    self.SR['Rpc3L0bS'].Pass('pTj4 > 40 GeV')
                                    if MET > 200.:
                                        self.SR['Rpc3L0bS'].Pass('MET > 200 GeV')
                                        if meff > 600.:
                                            self.SR['Rpc3L0bS'].Pass('meff > 600 GeV')
                                            self.SR['Rpc3L0bS'].PassSR()



        #########################
        #  SR: Rpc3L0bH
        #########################

        if Nlep >= 3:
            self.SR['Rpc3L0bH'].Pass('Nlep >= 3')
            if Nbjet == 0:
                self.SR['Rpc3L0bH'].Pass('Nbjet == 0')
                if Njet >= 4:
                    self.SR['Rpc3L0bH'].Pass('Njet >= 4')
                    if jets[0].pT > 40.:
                        self.SR['Rpc3L0bH'].Pass('pTj1 > 40 GeV')
                        if jets[1].pT > 40.:
                            self.SR['Rpc3L0bH'].Pass('pTj2 > 40 GeV')
                            if jets[2].pT > 40.:
                                self.SR['Rpc3L0bH'].Pass('pTj3 > 40 GeV')
                                if jets[3].pT > 40.:
                                    self.SR['Rpc3L0bH'].Pass('pTj4 > 40 GeV')
                                    if MET > 200.:
                                        self.SR['Rpc3L0bH'].Pass('MET > 200 GeV')
                                        if meff > 1600.:
                                            self.SR['Rpc3L0bH'].Pass('meff > 1600 GeV')
                                            self.SR['Rpc3L0bH'].PassSR()


        #########################
        #  SR: Rpc3L1bS
        #########################

        if Nlep >= 3:
            self.SR['Rpc3L1bS'].Pass('Nlep >= 3')
            if Nbjet >= 1:
                self.SR['Rpc3L1bS'].Pass('Nbjet >= 1')
                if Njet >= 4:
                    self.SR['Rpc3L1bS'].Pass('Njet >= 4')
                    if jets[0].pT > 40.:
                        self.SR['Rpc3L1bS'].Pass('pTj1 > 40 GeV')
                        if jets[1].pT > 40.:
                            self.SR['Rpc3L1bS'].Pass('pTj2 > 40 GeV')
                            if jets[2].pT > 40.:
                                self.SR['Rpc3L1bS'].Pass('pTj3 > 40 GeV')
                                if jets[3].pT > 40.:
                                    self.SR['Rpc3L1bS'].Pass('pTj4 > 40 GeV')
                                    if MET > 200.:
                                        self.SR['Rpc3L1bS'].Pass('MET > 200 GeV')
                                        if meff > 600.:
                                            self.SR['Rpc3L1bS'].Pass('meff > 600 GeV')
                                            self.SR['Rpc3L1bS'].PassSR()
                






        #########################
        #  SR: Rpc3L1bH
        #########################

        if Nlep >= 3:
            self.SR['Rpc3L1bH'].Pass('Nlep >= 3')
            if Nbjet >= 1:
                self.SR['Rpc3L1bH'].Pass('Nbjet >= 1')
                if Njet >= 4:
                    self.SR['Rpc3L1bH'].Pass('Njet >= 4')
                    if jets[0].pT > 40.:
                        self.SR['Rpc3L1bH'].Pass('pTj1 > 40 GeV')
                        if jets[1].pT > 40.:
                            self.SR['Rpc3L1bH'].Pass('pTj2 > 40 GeV')
                            if jets[2].pT > 40.:
                                self.SR['Rpc3L1bH'].Pass('pTj3 > 40 GeV')
                                if jets[3].pT > 40.:
                                    self.SR['Rpc3L1bH'].Pass('pTj4 > 40 GeV')
                                    if MET > 200.:
                                        self.SR['Rpc3L1bH'].Pass('MET > 200 GeV')
                                        if meff > 1600.:
                                            self.SR['Rpc3L1bH'].Pass('meff > 1600 GeV')
                                            self.SR['Rpc3L1bH'].PassSR()




        #########################
        #  SR: Rpc2L1bS
        #########################

        if Nlep >= 2:
            self.SR['Rpc2L1bS'].Pass('>= 2 SS leptons')
            if Nbjet >= 1:
                self.SR['Rpc2L1bS'].Pass('Nbjet >= 1')
                if Njet >= 6:
                    self.SR['Rpc2L1bS'].Pass('Njet >= 6')
                    if jets[0].pT > 25.:
                        self.SR['Rpc2L1bS'].Pass('pTj1 > 25 GeV')
                        if jets[1].pT > 25.:
                            self.SR['Rpc2L1bS'].Pass('pTj2 > 25 GeV')
                            if jets[2].pT > 25.:
                                self.SR['Rpc2L1bS'].Pass('pTj3 > 25 GeV')
                                if jets[3].pT > 25.:
                                    self.SR['Rpc2L1bS'].Pass('pTj4 > 25 GeV')
                                    if jets[4].pT > 25.:
                                        self.SR['Rpc2L1bS'].Pass('pTj5 > 25 GeV')
                                        if jets[5].pT > 25.:
                                            self.SR['Rpc2L1bS'].Pass('pTj6 > 25 GeV')
                                            if MET > 150.:
                                                self.SR['Rpc2L1bS'].Pass('MET > 150 GeV')
                                                if meff > 600.:
                                                    self.SR['Rpc2L1bS'].Pass('meff > 600 GeV')
                                                    if MET/meff > 0.25:
                                                        self.SR['Rpc2L1bS'].Pass('MET/meff > 0.25')
                                                        self.SR['Rpc2L1bS'].PassSR()                                            
                
        
                
        
        #########################
        #  SR: Rpc3LSS1b
        #########################

        if Nlep >= 3 and np.sign(leps[0].pid) == np.sign(leps[1].pid) and np.sign(leps[0].pid) == np.sign(leps[2].pid):
            self.SR['Rpc3LSS1b'].Pass('>= 3 SS leptons')
            if Nbjet >= 1:
                self.SR['Rpc3LSS1b'].Pass('Nbjet >= 1')
                m_inv = (leps[0].p + leps[1].p).M()
                if m_inv < 81. and m_inv > 101.:
                    self.SR['Rpc3LSS1b'].Pass('Z-veto')
                    self.SR['Rpc3LSS1b'].PassSR()


                    
                
            
            






        

    #########################################
    #    Output
    #########################################
    def write_result(self, iev):
        print ''
        print 'Analysis: {ananame}'.format(ananame=self.ananame)
        for key, item in self.SR.items(): item.PrintEff(iev)




