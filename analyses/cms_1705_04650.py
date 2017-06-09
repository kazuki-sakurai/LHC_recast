#!/usr/bin/env python
from objects import *
from collections import OrderedDict
from aplanarity import *

class cms_1705_04650:

    #########################################
    #    Define groups of signal regions
    #########################################
    def __init__(self):
        self.ananame = 'cms_1705_04650'
        self.SR = OrderedDict()        
        self.SR['base'] = Cut('base')
        ## Mono jet SR (bins of pT):
        for i in range(1,8): self.SR['1j0b_bin'+str(i)] = Cut('1j0b_bin'+str(i))
        for i in range(1,6): self.SR['1j1b_bin'+str(i)] = Cut('1j1b_bin'+str(i))
        #### Multiple jets SR (bins of MT2): HT: very low (vl),low (l),medium (m),high (h),extreme (e)
        ## Very low HT:
        for i in range(1,4): ## 3 bins of MT2, very low HT
            for j in range(4): self.SR['vlHT_2j'+str(j)+'b_bin'+str(i)] = Cut('vlHT_2j'+str(j)+'b_bin'+str(i)) ## number of Nb (0,1,2,3)
            for j in range(3): self.SR['vlHT_4j'+str(j)+'b_bin'+str(i)] = Cut('vlHT_4j'+str(j)+'b_bin'+str(i)) ## number of Nb (0,1,3)
        ## Low HT:
        for i in range(1,5): ## 4 bins of MT2, low HT
            for j in range(4): self.SR['lHT_2j'+str(j)+'b_bin'+str(i)] = Cut('lHT_2j'+str(j)+'b_bin'+str(i)) ## number of Nb (0,1,2,3)
            for j in range(3): self.SR['lHT_4j'+str(j)+'b_bin'+str(i)] = Cut('lHT_4j'+str(j)+'b_bin'+str(i)) ## number of Nb (0,1,2)
        for i in range(1,4): ## 3 bins of MT2, low HT
            for j in range(4): self.SR['lHT_7j'+str(j)+'b_bin'+str(i)] = Cut('lHT_7j'+str(j)+'b_bin'+str(i)) ## number of Nb (0,1,2,3)
        ## Medium HT:
        for i in range(1,6): ## 5 bins of MT2, medium HT
            for j in range(3): ## number of Nb (0,1,2)
                self.SR['mHT_2j'+str(j)+'b_bin'+str(i)] = Cut('mHT_2j'+str(j)+'b_bin'+str(i)) 
                self.SR['mHT_4j'+str(j)+'b_bin'+str(i)] = Cut('mHT_4j'+str(j)+'b_bin'+str(i))
            self.SR['mHT_7j0b_bin'+str(i)] = Cut('mHT_7j0b_bin'+str(i))
        for i in range(1,5): ## 4 bins of MT2, medium HT
            for j in [1,2,3]: self.SR['mHT_7j'+str(j)+'b_bin'+str(i)] = Cut('mHT_7j'+str(j)+'b_bin'+str(i))
            self.SR['mHT_2j3b_bin'+str(i)] = Cut('mHT_2j3b_bin'+str(i))
        ## High HT:
        for i in range(1,7): ## 6 bins of MT2, high MT
            for j in range(2): ## number of Nb (0,1)
                self.SR['hHT_2j'+str(j)+'b_bin'+str(i)] = Cut('hHT_2j'+str(j)+'b_bin'+str(i)) 
                self.SR['hHT_4j'+str(j)+'b_bin'+str(i)] = Cut('hHT_4j'+str(j)+'b_bin'+str(i))
        for i in range(1,6): ## 5 bins of MT2, high MT
            self.SR['hHT_2j2b_bin'+str(i)] = Cut('hHT_2j2b_bin'+str(i))
            self.SR['hHT_4j2b_bin'+str(i)] = Cut('hHT_4j2b_bin'+str(i))
            self.SR['hHT_7j0b_bin'+str(i)] = Cut('hHT_7j0b_bin'+str(i))
        for i in range(1,5): ## 4 bins of MT2, high MT
            for j in [1,2]: self.SR['hHT_7j'+str(j)+'b_bin'+str(i)] = Cut('hHT_7j'+str(j)+'b_bin'+str(i)) 
        for i in range(1,4): ## 3 bins of MT2, high MT
            for j in [2,7]:  self.SR['hHT_'+str(j)+'j3b_bin'+str(i)] = Cut('hHT_'+str(j)+'j3b_bin'+str(i))
        ## Extreme HT:
        for i in range(1,6): ## 5 bins of MT2, extreme MT
            self.SR['eHT_2j0b_bin'+str(i)] = Cut('eHT_2j0b_bin'+str(i))
            for j in range(2): self.SR['eHT_4j'+str(j)+'b_bin'+str(i)] = Cut('eHT_4j'+str(j)+'b_bin'+str(i))
        for i in range(1,5): ## 4 bins of MT2, extreme HT
            self.SR['eHT_2j1b_bin'+str(i)] = Cut('eHT_2j1b_bin'+str(i))
            self.SR['eHT_7j0b_bin'+str(i)] = Cut('eHT_7j0b_bin'+str(i))
        for i in range(1,4): ## 3 bins of MT2, extreme HT
            self.SR['eHT_4j2b_bin'+str(i)] = Cut('eHT_4j2b_bin'+str(i))
            for j in [1,2]: self.SR['eHT_7j'+str(j)+'b_bin'+str(i)] = Cut('eHT_7j'+str(j)+'b_bin'+str(i)) 
        for i in range(1,3): self.SR['eHT_2j3b_bin'+str(i)] = Cut('eHT_2j3b_bin'+str(i))## 2 bins of MT2, extreme HT
        for i in range(1,2): ## 1 bin of MT2, extreme HT
            self.SR['eHT_2j2b_bin'+str(i)] = Cut('eHT_2j2b_bin'+str(i))
            self.SR['eHT_7j3b_bin'+str(i)] = Cut('eHT_2j3b_bin'+str(i))
                                                

    #########################################
    #    Define jets, leptons, bjets, etc..
    #########################################
    def get_objects(self, objects):
        ## QUESTIONS: R=0.4 for jets, pTsum cone and veto track, and veto muon/electron
        ## QUESTIONS: MT2, pTmiss definition

        jets = []
        for jet in objects['jets']:
            if jet.pT > 30 and jet.abseta < 2.4: jets.append(jet) 

        leps,muons,electrons = [],[],[]
        for lep in objects['leps']:
            if abs(lep.pid) == 11 and lep.pT > 5 and lep.abseta < 2.4:  ## electron
                leps.append(lep)
                electrons.append(lep)
            if abs(lep.pid) == 13 and lep.pT > 5 and lep.abseta < 2.4: ## muon
                leps.append(lep)
                muons.append(lep)

        bjets = []
        for b in objects['bjets']:
            if b.pT > 20 and b.abseta < 2.4: bjets.append(b)

        pTmiss = objects['pTmiss']
        MET = objects['MET']

        return jets, bjets, leps, muons, electrons, pTmiss, MET

    #########################################
    #    Event by event analysis
    #########################################
    def event_analysis(self, base_objects):

        jets, bjets, leps, muons, electrons, pTmiss, MET = self.get_objects(base_objects)
        
        Njet, Nbjet, Nlep = len(jets),len(bjets),len(leps)
        base_cut = False

        #########################        
        #  Variables
        #########################
        
        isolated_leptons = 0 ## muons and leptons
        for lep in leps:
            dPhi,pTl = delta_phi(lep.p.Phi(), pTmiss.Phi()), lep.pT
            mT = np.sqrt(2*pTl*MET*(1 - np.cos(dPhi)))
            isolated_leptons += (pTl > 10) or (mT < 100) ## pT > 5 already imposed when selecing the particles 

        if Njet > 1: ## at least two jets 
            _M,_i,_j = 0.,0,0 ## default value
            for i in xrange(Njet): ## loop over the inv mass
                for j in xrange(Njet):
                    if(i!=j):
                        M = (jets[i].p+jets[j].p).M() 
                        if M < _M : _M,_i,_j = M,i,j
            jet1,jet2 = jets[_i],jets[_j]
            mT2 = MT2(jet1.p.M(),jet1.p.Px(),jet1.p.Py(),jet2.p.M(),jet2.p.Px(),jet2.p.Py(),pTmiss.M(),pTmiss.Px(),pTmiss.Py())
        else : mT2 = 0.0 ## so that it doesnt pass any of the cuts

        HT = sum(map(lambda x:x.pT,jets))

        ## dPhimin
        dPhiMin = 1000 
        for i in xrange(min(Njet, 4)):
            if jets[i].abseta > 4.7 : continue
            dPhi =  delta_phi(jets[i].p.Phi(), pTmiss.Phi())
            if dPhi < dPhiMin: dPhiMin = dPhi

        ## diff_pTmiss_HTmiss
        if Njet >= 1:
            HTmiss = -jets[0].p
            for jet in jets[1:]: HTmiss -= jet.p

            diff_pTmiss_HTmiss = (pTmiss - HTmiss).P() / pTmiss.P() ## tbc

        if Njet >= 1:
            self.SR['base'].Pass('at least 1 jet')
            if HT > 900 or min(map(lambda x:x.pT,jets)) > 450: 
                self.SR['base'].Pass('trigger criteria, HT > 900 GeV or jet pT > 450 GeV')
                if (HT > 1000)*(pTmiss.P() > 250) or pTmiss.P() > 30: 
                    self.SR['base'].Pass('pTmiss cut')
                    if dPhiMin > 0.3:
                        self.SR['base'].Pass('dPhi_min > 0.3')
                        if diff_pTmiss_HTmiss < 0.5:
                            self.SR['base'].Pass('abs(pTmiss - HTmiss)/pTmiss < 0.5')
                            if (mT2 > 200)*(HT < 1500) or mT2 > 400:
                                self.SR['base'].Pass("mT2 cut")
                                if not isolated_leptons:
                                    self.SR['base'].Pass("no isolapted leptons or charged PF candidate")                      
                                    base_cut = True

        if base_cut == False: return
        ## mT2, mT, HT, dPhimin, diff_pTmiss_HTmiss


        #########################
        #  SR: monojets
        #########################        
       
        if Njet == 1:
            for i in range(1,8): self.SR['1j0b_bin'+str(i)].Pass("Njet = 1")
            for i in range(1,6): self.SR['1j1b_bin'+str(i)].Pass("Njet = 1")
            intervals = {1:[250,350],2:[350,450],3:[450,575],4:[575,700],5:[700,1000],6:[1000,1200],7:[1200,1e9]}
            if Nbjet == 0:
                for i in range(1,8):
                    self.SR['1j0b_bin'+str(i)].Pass("Nbjet = 0")
                    if jets[0].pT > intervals[i][0] and jets[0].pT < intervals[i][1]:
                        self.SR['1j0b_bin'+str(i)].Pass("pT inside bin"+str(i))
                        self.SR['1j0b_bin'+str(i)].PassSR()
            if Nbjet == 1: 
                for i in range(1,6):
                    self.SR['1j1b_bin'+str(i)].Pass("Nbjet = 1")  
                    if jets[0].pT > intervals[i][0] and jets[0].pT < intervals[i][1]:
                        self.SR['1j1b_bin'+str(i)].Pass("pT inside bin"+str(i))
                        self.SR['1j1b_bin'+str(i)].PassSR()         
        
        #########################
        #  SR: multijets
        #########################       

        ## QUESTION : [], <= and >=?
                         
        if Njet > 1:
            for key in self.SR.keys(): 
                if 'HT' in key: self.SR[key].Pass('Njet > 1')
                ## Very low HT:
                if HT > 250 and HT < 450:
                    vlintervals = {1:[200,300],2:[300,400],3:[400,1e9]} ## mT2
                    for key in self.SR.keys(): 
                        if 'vlHT' in key: self.SR[key].Pass('Very low HT (HT > 250 GeV and HT < 450 GeV)')
                    if Njet >= 2 and Njet < 4 : ### 2 jets area
                        for i in range(3): ## Nb bins
                            for j in range(1,4): ## mT2 divisions 
                                self.SR['vlHT_2j'+str(i)+'b_bin'+str(j)].Pass('2-3 jets') ## mT2 bins
                                if Nbjet == i:
                                    self.SR['vlHT_2j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > vlintervals[j][0] and mT2 < (vlintervals[j][1] + 1e9*(j == 3)):
                                        self.SR['vlHT_2j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['vlHT_2j'+str(i)+'b_bin'+str(j)].PassSR()   
                    if Njet >= 4 : ### 4 jets area
                        for i in range(3): ## Nb bins
                            for j in range(1,4): ## mT2 divisions 
                                self.SR['vlHT_4j'+str(i)+'b_bin'+str(j)].Pass('more than 4 jets') ## mT2 bins
                                if Nbjet == i: 
                                    self.SR['vlHT_4j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > vlintervals[j][0] and mT2 < (vlintervals[j][1] + 1e9*(j == 3)):
                                        self.SR['vlHT_4j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['vlHT_4j'+str(i)+'b_bin'+str(j)].PassSR()   
                    if Njet >= 2 : ### 2 jets area
                        for j in range(1,4): ## mT2 divisions
                            self.SR['vlHT_2j3b_bin'+str(j)].Pass('more than 2 jets') ## mT2 bins
                            if Nbjet >= 3: 
                                self.SR['vlHT_2j3b_bin'+str(a)].Pass('more than 3 bjets')
                                if mT2 > vlintervals[j][0] and mT2 < (vlintervals[j][1] + 1e9*(j == 3)):
                                    self.SR['vlHT_2j3b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['vlHT_2j3b_bin'+str(j)].PassSR()                                   
                ## Low HT:
                if HT > 450 and HT < 575:
                    lintervals = {1:[200,300],2:[300,400],3:[400,500],4:[500,1e9]} ## mT2
                    for key in self.SR.keys(): 
                        if 'lHT' in key and 'vlHT' not in key: self.SR[key].Pass('Low HT (HT > 450 GeV and HT < 575 GeV)')
                    if Njet >= 2 and Njet < 4 : ### 2 jets area
                        for i in range(3): ## Nb bins
                            for j in range(1,5): ## mT2 divisions
                                self.SR['lHT_2j'+str(i)+'b_bin'+str(j)].Pass('2-3 jets') ## mT2 bins
                                if Nbjet == i: 
                                    self.SR['lHT_2j'+str(i)+'b_bin'+str(a)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > lintervals[j][0] and mT2 < (lintervals[j][1] + 1e9*(j == 4)):
                                        self.SR['lHT_2j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['lHT_2j'+str(i)+'b_bin'+str(j)].PassSR()   
                    if Njet >= 4 and Njet < 7 : ### 4 jets area
                        for i in range(3): ## Nb bins
                            for j in range(1,5): ## mT2 divisions
                                self.SR['lHT_4j'+str(i)+'b_bin'+str(j)].Pass('4-6 jets') ## mT2 bins
                                if Nbjet == i: 
                                    self.SR['lHT_4j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > lintervals[j][0] and mT2 < (lintervals[j][1] + 1e9*(j == 4)):
                                        self.SR['lHT_4j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['lHT_4j'+str(i)+'b_bin'+str(j)].PassSR() 
                    if Njet >= 7 : ### 7 jets area
                        for i in range(3): ## Nb bins
                            for j in range(1,4): ## mT2 divisions
                                self.SR['lHT_7j'+str(i)+'b_bin'+str(j)].Pass('more than 7 jets') ## mT2 bins
                                if Nbjet == i: 
                                    self.SR['lHT_7j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > lintervals[j][0] and mT2 < (lintervals[j][1] + 1e9*(j == 3)):
                                        self.SR['lHT_7j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['lHT_7j'+str(i)+'b_bin'+str(j)].PassSR() 
                    if Njet >= 2 and Njet < 7 : ### 2 jets area II  ## REVISAR
                        for j in range(1,5): ## mT2 divisions 
                            self.SR['lHT_2j3b_bin'+str(j)].Pass('2-6 jets') ## mT2 bins
                            if Nbjet >= 3: 
                                self.SR['lHT_2j3b_bin'+str(j)].Pass('more than 3 bjets')
                                if mT2 > lintervals[j][0] and mT2 < (lintervals[j][1] + 1e9*(j == 4)):
                                    self.SR['lHT_2j3b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['lHT_2j3b_bin'+str(j)].PassSR()   
                    if Njet >= 7 : ### 7 jets area
                        for j in range(1,4): ## mT2 divisions
                            self.SR['lHT_7j3b_bin'+str(j)].Pass('more than 7 jets') ## mT2 bins
                            if Nbjet >= 3: 
                                self.SR['lHT_7j3b_bin'+str(j)].Pass('more than 3 bjets')
                                if mT2 > lintervals[j][0] and mT2 < (lintervals[j][1] + 1e9*(j == 3)):
                                    self.SR['lHT_7j3b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['lHT_7j3b_bin'+str(j)].PassSR()   
                ## Medium HT:
                if HT > 575 and HT < 1000:
                    mintervals = {1:[200,300],2:[300,400],3:[400,600],4:[600,800],5:[800,1e9]} ## mT2
                    for key in self.SR.keys(): 
                        if 'mHT' in key: self.SR[key].Pass('Medium HT (HT > 575 GeV and HT < 1000 GeV)')
                    if Njet >= 2 and Njet < 4 : ### 2 jets area
                        for i in range(3): ## Nb bins
                            for j in range(1,6): ## mT2 divisions 
                                self.SR['mHT_2j'+str(i)+'b_bin'+str(j)].Pass('2-3 jets') ## mT2 bins
                                if Nbjet == i: 
                                    self.SR['mHT_2j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > mintervals[j][0] and mT2 < (mintervals[j][1] + 1e9*(j == 5)):
                                        self.SR['mHT_2j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['mHT_2j'+str(i)+'b_bin'+str(j)].PassSR()  
                    if Njet >= 4 and Njet < 7 : ### 4 jets area
                        for i in range(3): ## Nb bins
                            for j in range(1,6): ## mT2 divisions 
                                self.SR['mHT_4j'+str(i)+'b_bin'+str(j)].Pass('4-6 jets') ## mT2 bins
                                if Nbjet == i: 
                                    self.SR['mHT_4j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > mintervals[j][0] and mT2 < (mintervals[j][1] + 1e9*(j == 5)):
                                        self.SR['mHT_4j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['mHT_4j'+str(i)+'b_bin'+str(j)].PassSR()    
                    if Njet >= 7 : ### 7 jets area
                        for i in range(2): ## Nb bins
                            for j in range(1,5): ## mT2 divisions 
                                self.SR['mHT_7j'+str(i)+'b_bin'+str(j)].Pass('more than 7 jets') ## mT2 bins
                                if Nbjet == i: 
                                    self.SR['mHT_7j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > mintervals[j][0] and mT2 < (mintervals[j][1] + 1e9*(j == 4)):
                                        self.SR['mHT_7j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['mHT_7j'+str(i)+'b_bin'+str(j)].PassSR()
                        ## need separate loop for 7j,0b
                        self.SR['mHT_7j0b_bin'+str(j)].Pass('more than 7 jets')
                        if Nbjet == 0:
                            self.SR['mHT_7j0b_bin'+str(j)].Pass('0 bjets')
                            for a in range(1,6): ## mT2 divisions
                                if mT2 > mintervals[a][0] and mT2 < (mintervals[a][1] + 1e9*(a == 3)):
                                    self.SR['mHT_7j0b_bin'+str(a)].Pass("mT2 inside bin "+str(a))
                                    self.SR['mHT_7j0b_bin'+str(a)].PassSR()
                    if Njet >= 2 and Njet < 7 : ### 2 jets area II
                        for j in range(1,5): ## mT2 divisions 
                            self.SR['mHT_2j3b_bin'+str(j)].Pass('2-6 jets') ## mT2 bins
                            if Nbjet >= 3: 
                                self.SR['mHT_2j3b_bin'+str(j)].Pass('more than 3 bjets')
                                if mT2 > mintervals[j][0] and mT2 < (mintervals[j][1] + 1e9*(j == 4)):
                                    self.SR['mHT_2j3b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['mHT_2j3b_bin'+str(j)].PassSR()   
                    if Njet >= 7 : ### 7 jets area II
                        for j in range(1,5): ## mT2 divisions
                            self.SR['mHT_7j3b_bin'+str(j)].Pass('more than 7 jets') ## mT2 bins
                            if Nbjet >= 3: 
                                self.SR['mHT_7j3b_bin'+str(j)].Pass('more than 3 bjets')
                                if mT2 > mintervals[j][0] and mT2 < (mintervals[j][1] + 1e9*(j == 4)):
                                    self.SR['mHT_7j3b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['mHT_7j3b_bin'+str(j)].PassSR()   
                ## High HT:
                if HT > 1000 and HT < 1500:
                    hintervals = {1:[200,400],2:[400,600],3:[600,800],4:[800,1000],5:[1000,1200],6:[1200,1e9]} ## mT2
                    for key in self.SR.keys(): 
                        if 'hHT' in key: self.SR[key].Pass('High HT (HT > 1000 GeV and HT < 1500 GeV)')
                    if Njet >= 2 and Njet < 4 : ### 2 jets area
                        for i in range(2):
                            for j in range(1,7): 
                                self.SR['hHT_2j'+str(i)+'b_bin'+str(j)].Pass('2-3 jets') ## Nb bins
                                if Nbjet == i: 
                                    self.SR['hHT_2j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > hintervals[j][0] and mT2 < (hintervals[j][1] + 1e9*(j == 6)):
                                        self.SR['hHT_2j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['hHT_2j'+str(i)+'b_bin'+str(j)].PassSR()
                        for j in range(1,6): 
                            self.SR['hHT_2j2b_bin'+str(j)].Pass('2-3 jets') ## Nb bins
                            if Nbjet == 2: 
                                self.SR['hHT_2j2b_bin'+str(j)].Pass('2 bjets') ## bjets divisions
                                if mT2 > hintervals[j][0] and mT2 < (hintervals[j][1] + 1e9*(j == 5)):
                                    self.SR['hHT_2j2b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['hHT_2j2b_bin'+str(j)].PassSR()
                    if Njet >= 4 and Njet < 7 : ### 4 jets area
                        for i in range(2):
                            for j in range(1,7): 
                                self.SR['hHT_4j'+str(i)+'b_bin'+str(j)].Pass('4-6 jets') ## Nb bins
                                if Nbjet == i: 
                                    self.SR['hHT_4j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > hintervals[j][0] and mT2 < (hintervals[j][1] + 1e9*(j == 6)):
                                        self.SR['hHT_4j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['hHT_4j'+str(i)+'b_bin'+str(j)].PassSR()
                        for j in range(1,6): 
                            self.SR['hHT_4j2b_bin'+str(j)].Pass('4-6 jets') ## Nb bins
                            if Nbjet == 2: 
                                self.SR['hHT_4j2b_bin'+str(j)].Pass('2 bjets') ## bjets divisions
                                if mT2 > hintervals[j][0] and mT2 < (hintervals[j][1] + 1e9*(j == 5)):
                                    self.SR['hHT_4j2b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['hHT_4j2b_bin'+str(j)].PassSR()
                    if Njet >= 7 : ### 7 jets area
                        for i in range(1,3):
                            for j in range(1,5): 
                                self.SR['hHT_7j'+str(i)+'b_bin'+str(j)].Pass('more than 7 jets') ## Nb bins
                                if Nbjet == i: 
                                    self.SR['hHT_7j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > hintervals[j][0] and mT2 < (hintervals[j][1] + 1e9*(j == 4)):
                                        self.SR['hHT_7j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['hHT_7j'+str(i)+'b_bin'+str(j)].PassSR()
                        for j in range(1,6): 
                            self.SR['hHT_7j0b_bin'+str(j)].Pass('more than 7 jets') ## Nb bins
                            if Nbjet == 0: 
                                self.SR['hHT_7j0b_bin'+str(j)].Pass('0 bjets') ## bjets divisions
                                if mT2 > hintervals[j][0] and mT2 < (hintervals[j][1] + 1e9*(j == 5)):
                                    self.SR['hHT_7j0b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['hHT_7j0b_bin'+str(j)].PassSR()
                    if Njet >= 2 and Njet < 7 : ### 2 jets area II
                        for j in range(1,4): self.SR['hHT_2j3b_bin'+str(j)].Pass('2-6 jets') ## mT2 bins
                        if Nbjet >= 3: 
                            for a in range(1,4): ## mT2 divisions
                                self.SR['hHT_2j3b_bin'+str(a)].Pass('more than 3 bjets')
                                if mT2 > hintervals[a][0] and mT2 < (hintervals[a][1] + 1e9*(a == 3)):
                                    self.SR['hHT_2j3b_bin'+str(a)].Pass("mT2 inside bin"+str(a))
                                    self.SR['hHT_2j3b_bin'+str(a)].PassSR()   
                    if Njet >= 7 : ### 7 jets area
                        for j in range(1,4): self.SR['hHT_7j3b_bin'+str(j)].Pass('more than 7 jets') ## mT2 bins
                        if Nbjet >= 3: 
                            for a in range(1,4): ## mT2 divisions
                                self.SR['hHT_7j3b_bin'+str(j)].Pass('more than 3 bjets')
                                if mT2 > hintervals[a][0] and mT2 < (hintervals[a][1] + 1e9*(a == 3)):
                                    self.SR['hHT_7j3b_bin'+str(a)].Pass("mT2 inside bin"+str(a))
                                    self.SR['hHT_7j3b_bin'+str(a)].PassSR()   

                ## Extreme HT:
                if HT > 1500 and HT < 1e9:
                    eintervals = {1:[400,600],2:[600,800],3:[800,1000],4:[1000,1400],5:[1400,1e9]} ## mT2
                    for key in self.SR.keys(): 
                        if 'eHT' in key: self.SR[key].Pass('Extreme HT (HT > 1500 GeV)')
                    if Njet >= 2 and Njet < 4 : ### 2 jets area
                        for j in range(1,6): 
                            self.SR['eHT_2j0b_bin'+str(j)].Pass('2-3 jets') ## Nb bins
                            if Nbjet == 0:
                                self.SR['eHT_2j0b_bin'+str(j)].Pass('0 bjets') ## bjets divisions
                                if mT2 > eintervals[j][0] and mT2 < (eintervals[j][1] + 1e9*(j == 5)):
                                    self.SR['eHT_2j0b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['eHT_2j0b_bin'+str(j)].PassSR()
                        for j in range(1,5):
                            self.SR['eHT_2j1b_bin'+str(j)].Pass('2-3 jets') ## Nb bins
                            if Nbjet == 1:
                                self.SR['eHT_2j1b_bin'+str(j)].Pass('1 bjet') ## bjets divisions
                                if mT2 > eintervals[j][0] and mT2 < (eintervals[j][1] + 1e9*(j == 4)):
                                    self.SR['eHT_2j1b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['eHT_2j1b_bin'+str(j)].PassSR()
                        self.SR['eHT_2j2b_bin1'].Pass('2-3 jets') ## Nb bins
                        if Nbjet == 2:
                            self.SR['eHT_2j2b_bin1'].Pass('2 bjets') ## Nb bins
                            if mT2 > 400: 
                                self.SR['eHT_2j2b_bin1'].Pass('mT2 inside bin 1')
                                self.SR['eHT_2j2b_bin1'].PassSR()
                    if Njet >= 4 and Njet < 7 : ### 4 jets area
                        for i in range(2):
                            for j in range(1,6): 
                                self.SR['eHT_4j'+str(i)+'b_bin'+str(j)].Pass('4-6 jets') ## Nb bins
                                if Nbjet == i: 
                                    self.SR['eHT_4j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > eintervals[j][0] and mT2 < (eintervals[j][1] + 1e9*(j == 5)):
                                        self.SR['eHT_4j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['eHT_4j'+str(i)+'b_bin'+str(j)].PassSR()
                        for j in range(1,4): 
                            self.SR['eHT_4j2b_bin'+str(j)].Pass('4-6 jets') ## Nb bins
                            if Nbjet == 2: 
                                self.SR['eHT_4j2b_bin'+str(j)].Pass('2 bjets') ## bjets divisions
                                if mT2 > eintervals[j][0] and mT2 < (eintervals[j][1] + 1e9*(j == 3)):
                                    self.SR['eHT_4j2b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['eHT_4j2b_bin'+str(j)].PassSR()
                    if Njet >= 7 : ### 7 jets area
                        for i in range(1,3):
                            for j in range(1,4): 
                                self.SR['eHT_7j'+str(i)+'b_bin'+str(j)].Pass('more than 7 jets') ## Nb bins
                                if Nbjet == i: 
                                    self.SR['eHT_7j'+str(i)+'b_bin'+str(j)].Pass(str(i)+' bjets') ## bjets divisions
                                    if mT2 > eintervals[j][0] and mT2 < (eintervals[j][1] + 1e9*(j == 3)):
                                        self.SR['eHT_7j'+str(i)+'b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                        self.SR['eHT_7j'+str(i)+'b_bin'+str(j)].PassSR()
                        for j in range(1,5): 
                            self.SR['eHT_7j0b_bin'+str(j)].Pass('more than 7 jets') ## Nb bins
                            if Nbjet == 0: 
                                self.SR['eHT_7j0b_bin'+str(j)].Pass('0 bjets') ## bjets divisions
                                if mT2 > eintervals[j][0] and mT2 < (eintervals[j][1] + 1e9*(j == 4)):
                                    self.SR['eHT_7j0b_bin'+str(j)].Pass("mT2 inside bin "+str(j))
                                    self.SR['eHT_7j0b_bin'+str(j)].PassSR()
                    if Njet >= 2 and Njet < 7 : ### 2 jets area II
                        for j in range(1,3): ## mT2 divisions 
                            self.SR['eHT_2j3b_bin'+str(j)].Pass('2-6 jets') ## mT2 bins
                            if Nbjet >= 3: 
                                self.SR['eHT_2j3b_bin'+str(j)].Pass('more than 3 bjets')
                                if mT2 > eintervals[j][0] and mT2 < (eintervals[j][1] + 1e9*(j == 3)):
                                    self.SR['eHT_2j3b_bin'+str(j)].Pass("mT2 inside bin"+str(j))
                                    self.SR['eHT_2j3b_bin'+str(j)].PassSR()   
                    if Njet >= 7 : ### 7 jets area
                        self.SR['eHT_7j3b_bin1'].Pass('more than 7 jets') ## mT2 bins
                        if Nbjet >= 3: 
                            self.SR['eHT_7j3b_bin1'].Pass('more than 3 bjets')
                            if mT2 > 400:
                                self.SR['eHT_7j3b_bin1'].Pass("mT2 inside bin 1")
                                self.SR['eHT_7j3b_bin1'].PassSR()   
                                        


    #########################################
    #    Output
    #########################################
    def write_result(self, iev):
        print ''
        print 'Analysis: {ananame}'.format(ananame=self.ananame)
        for key, item in self.SR.items(): item.PrintEff(iev)
        





