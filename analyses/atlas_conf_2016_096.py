#!/usr/bin/env python
from objects import *
from collections import OrderedDict
from aplanarity import *
from mT2_packages import *



class atlas_conf_2016_096:

    #########################################
    #    Define groups of signal regions
    #########################################
    def __init__(self):
        self.ananame = 'atlas_conf_2016_096'
        self.SR = OrderedDict()        
        self.SR['base'] = Cut('base')
        self.SR['2lASF'] = Cut('2lASF')
        self.SR['2lADF'] = Cut('2lADF')
        self.SR['2lBSF'] = Cut('2lBSF')
        self.SR['2lBDF'] = Cut('2lBDF')
        self.SR['2lCSF'] = Cut('2lCSF')
        self.SR['2lCDF'] = Cut('2lCDF')
        self.SR['3lI'] = Cut('3lI')
        self.SR['3lH'] = Cut('3lH')
        

    #########################################
    #    Define jets, leptons, bjets, etc..
    #########################################
    def get_objects(self, objects):
        
        jets = []
        for jet in objects['jets']:
            if jet.pT > 20 and jet.abseta < 2.8: jets.append(jet)

        leps = []
        
        
        for lep in objects['leps']:
            if abs(lep.pid) == 11 and lep.pT > 10 and lep.abseta < 2.47:       #electrons
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

        for i in xrange(len(leps)):
            for j in xrange(len(leps)):
                if abs(leps[i].pid) != abs(leps[j].pid):
                    PX = np.abs((leps[i].p.Px() - leps[j].p.Px()))/np.abs(leps[j].p.Px())
                    PY = np.abs((leps[i].p.Py() - leps[j].p.Py()))/np.abs(leps[j].p.Py())
                    PZ = np.abs((leps[i].p.Pz() - leps[j].p.Pz()))/np.abs(leps[j].p.Pz())
                    if PX < 0.1 and PY < 0.1 and PZ < 0.1:
                        if abs(leps[i].pid) == 11:
                            del leps[i]
                        else:
                            del leps[j]
                

        if len(leps) > 1:
            self.SR['base'].Pass('lepton veto')
            base_cut = True

    
           
        if base_cut == False: return

        #########################        
        #  Variables
        #########################
        Njet = len(jets)            
        Nlep = len(leps)
        mZ = 91.1876      #PDG 2016 #GeV
        MET_m = 0.
    

    
       # if len(jets) >2: sph, aplanarity = Aplanarity(jets)
        #else: sph, aplanarity = 0, 0

        
        #########################
        #  SR: 2lASF
        #########################        
       
        if len(leps) == 2:
            self.SR['2lASF'].Pass('lepton number')
            if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                self.SR['2lASF'].Pass('lepton sign')
                if leps[0].pT > 25. and leps[1].pT > 20.:
                    self.SR['2lASF'].Pass('lepton pT > 25 (>20)')
                    if abs(leps[0].pid) == abs(leps[1].pid):
                        self.SR['2lASF'].Pass('Same Flavour')
                        for i in xrange(len(jets)):
                            if jets[i].pT >20 and jets[i].abseta < 2.4 and jets[i].pid != 5:
                                return
                        for i in xrange(len(bjets)):
                            if bjets[i].pT > 20 and bjets[i].abseta < 2.4:
                                return
                        for i in xrange(len(jets)):
                            if jets[i].pT > 30 and jets[i].abseta > 2.4 and jets[i].abseta < 4.5:
                                return
                        m_inv = (leps[0].p + leps[1].p).M()
                        if abs(m_inv - mZ) > 10.:
                            self.SR['2lASF'].Pass('Z veto')
                            mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                            if mT2 > 90.:
                                self.SR['2lASF'].Pass('mT2 > 90')
                                self.SR['2lASF'].PassSR()
                                


        #########################
        #  SR: 2lADF
        #########################

        if len(leps) == 2:
            self.SR['2lADF'].Pass('lepton number')
            if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                self.SR['2lADF'].Pass('lepton sign')
                if leps[0].pT > 25. and leps[1].pT > 20.:
                    self.SR['2lADF'].Pass('lepton pT > 25 (>20)')
                    if abs(leps[0].pid) == abs(leps[1].pid):
                        self.SR['2lADF'].Pass('Different Flavour')
                        for i in xrange(len(jets)):
                            if jets[i].pT >20 and jets[i].abseta < 2.4 and jets[i].pid != 5:
                                return
                        for i in xrange(len(bjets)):
                            if bjets[i].pT > 20 and bjets[i].abseta < 2.4:
                                return
                        for i in xrange(len(jets)):
                            if jets[i].pT > 30 and jets[i].abseta > 2.4 and jets[i].abseta < 4.5:
                                return
                        mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())    
                        if mT2 > 90.:
                            self.SR['2lADF'].Pass('mT2 > 90')
                            self.SR['2lADF'].PassSR()
                        

        #########################
        #  SR: 2lBSF
        #########################

        if len(leps) == 2:
           self.SR['2lBSF'].Pass('lepton number')
           if np.sign(leps[0].pid) != np.sign(leps[1].pid):
               self.SR['2lBSF'].Pass('lepton sign')
               if leps[0].pT > 25. and leps[1].pT > 20.:
                   self.SR['2lBSF'].Pass('lepton pT > 25 (>20)')
                   if abs(leps[0].pid) == abs(leps[1].pid):
                       self.SR['2lBSF'].Pass('Same Flavour')
                       for i in xrange(len(jets)):
                           if jets[i].pT >20 and jets[i].abseta < 2.4 and jets[i].pid != 5:
                               return
                       for i in xrange(len(bjets)):
                           if bjets[i].pT > 20 and bjets[i].abseta < 2.4:
                               return
                       for i in xrange(len(jets)):
                           if jets[i].pT > 30 and jets[i].abseta > 2.4 and jets[i].abseta < 4.5:
                               return
                       m_inv = (leps[0].p + leps[1].p).M()
                       if abs(m_inv - mZ) > 10.:
                           self.SR['2lBSF'].Pass('Z veto')
                           mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                           if mT2 > 120.:
                               self.SR['2lBSF'].Pass('mT2 > 120')
                               self.SR['2lBSF'].PassSR()


        #########################
        #  SR: 2lBDF
        #########################

        if len(leps) == 2:
            self.SR['2lBDF'].Pass('lepton number')
            if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                self.SR['2lBDF'].Pass('lepton sign')
                if leps[0].pT > 25. and leps[1].pT > 20.:
                    self.SR['2lBDF'].Pass('lepton pT > 25 (>20)')
                    if abs(leps[0].pid) == abs(leps[1].pid):
                        self.SR['2lBDF'].Pass('Different Flavour')
                        for i in xrange(len(jets)):
                            if jets[i].pT >20 and jets[i].abseta < 2.4 and jets[i].pid != 5:
                                return
                        for i in xrange(len(bjets)):
                            if bjets[i].pT > 20 and bjets[i].abseta < 2.4:
                                return
                        for i in xrange(len(jets)):
                            if jets[i].pT > 30 and jets[i].abseta > 2.4 and jets[i].abseta < 4.5:
                                return
                        mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())    
                        if mT2 > 120.:
                            self.SR['2lBDF'].Pass('mT2 > 120')
                            self.SR['2lBDF'].PassSR()

        #########################
        #  SR: 2lCSF
        #########################

        if len(leps) == 2:
            self.SR['2lCSF'].Pass('lepton number')
            if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                self.SR['2lCSF'].Pass('lepton sign')
                if leps[0].pT > 25. and leps[1].pT > 20.:
                    self.SR['2lCSF'].Pass('lepton pT > 25 (>20)')
                    if abs(leps[0].pid) == abs(leps[1].pid):
                        self.SR['2lCSF'].Pass('Same Flavour')
                        for i in xrange(len(jets)):
                            if jets[i].pT >20 and jets[i].abseta < 2.4 and jets[i].pid != 5:
                                return
                        for i in xrange(len(bjets)):
                            if bjets[i].pT > 20 and bjets[i].abseta < 2.4:
                                return
                        for i in xrange(len(jets)):
                            if jets[i].pT > 30 and jets[i].abseta > 2.4 and jets[i].abseta < 4.5:
                                return
                        m_inv = (leps[0].p + leps[1].p).M()
                        if abs(m_inv - mZ) > 10.:
                            self.SR['2lCSF'].Pass('Z veto')
                            mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                            if mT2 > 150.:
                                self.SR['2lCSF'].Pass('mT2 > 150')
                                self.SR['2lCSF'].PassSR()


        #########################
        #  SR: 2lCDF
        #########################

        if len(leps) == 2:
            self.SR['2lCDF'].Pass('lepton number')
            if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                self.SR['2lCDF'].Pass('lepton sign')
                if leps[0].pT > 25. and leps[1].pT > 20.:
                    self.SR['2lCDF'].Pass('lepton pT > 25 (>20)')
                    if abs(leps[0].pid) == abs(leps[1].pid):
                        self.SR['2lCDF'].Pass('Different Flavour')
                        for i in xrange(len(jets)):
                            if jets[i].pT >20 and jets[i].abseta < 2.4 and jets[i].pid != 5:
                                return
                        for i in xrange(len(bjets)):
                            if bjets[i].pT > 20 and bjets[i].abseta < 2.4:
                                return
                        for i in xrange(len(jets)):
                            if jets[i].pT > 30 and jets[i].abseta > 2.4 and jets[i].abseta < 4.5:
                                return
                        mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())    
                        if mT2 > 150.:
                            self.SR['2lCDF'].Pass('mT2 > 150')
                            self.SR['2lCDF'].PassSR()


        

        #########################
        #  SR: 3lI
        #########################

        if len(leps) == 3:
            self.SR['3lI'].Pass('lepton number')
            dileps = []
            for i in xrange(len(leps)):
                for j in xrange(i+1, len(leps)):
                    if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                        dileps.append([leps[i], leps[j]])
                        l1 = 3 - i - j  # index of the third lepton when len(dileps) = 1
            if len(dileps) > 1:
                Bnew =1000*mZ
                for i in xrange(len(dileps)):
                    m_inv = (dileps[i][0].p + dileps[i][1].p).M()
                    B = abs(m_inv - mZ)
                    if B < Bnew:
                        Bnew = B
                        A = i         # index of the choosen pair
                        l2 = 2 - A    # index of the third lepton when len(dileps) > 1
                leps1 = []        
                for i in xrange(len(leps)):
                    leps1.append(leps[i].p.Clone())
                    leps1[i].SetPz(0)
                mT = (leps1[0] + leps1[1] + leps1[2] + pTmiss).M()
                mSFOS = (dileps[A][0].p + dileps[A][1].p).M()
                if mT > 110.:
                    self.SR['3lI'].Pass('mT > 110')
                    if mSFOS < 81.2 or mSFOS > 101.2:
                        self.SR['3lI'].Pass('mSFOP < 81.2, > 101.2')
                        if leps[l2].pT > 30.:
                            self.SR['3lI'].Pass('pT3l > 30')
                            if MET > 120.:
                                self.SR['3lI'].Pass('MET > 120')
                                self.SR['3lI'].PassSR()
            if len(dileps) == 1:
                leps2 = []
                for i in xrange(len(leps)):
                    leps2.append(leps[i].p.Clone())
                    leps2[i].SetPz(0)
                mT = (leps2[0] + leps2[1] + leps2[2] + pTmiss).M()
                mSFOS = (dileps[0][0].p + dileps[0][1].p).M()
                if mT > 110.:
                    self.SR['3lI'].Pass('mT > 110')
                    if mSFOS < 81.2 or mSFOS > 101.2:
                        self.SR['3lI'].Pass('mSFOP < 81.2, > 101.2')
                        if leps[l1].pT > 30.:
                            self.SR['3lI'].Pass('pT3l > 30')
                            if MET > 120.:
                                self.SR['3lI'].Pass('MET > 120')
                                self.SR['3lI'].PassSR()
                    
                
            
                    



        #########################
        #  SR: 3lH
        #########################

        if len(leps) == 3:
           self.SR['3lH'].Pass('lepton number')
           dileps = []
           for i in xrange(len(leps)):
               for j in xrange(i+1, len(leps)):
                   if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                       dileps.append([leps[i], leps[j]])
                       l1 = 3 - i - j  # index of the third lepton when len(dileps) = 1
           if len(dileps) > 1:
               Bnew =1000* mZ
               for i in xrange(len(dileps)):
                   m_inv = (dileps[i][0].p + dileps[i][1].p).M()
                   B = abs(m_inv - mZ)
                   if B < Bnew:
                       Bnew = B
                       A = i         # index of the choosen pair
                       l2 = 2 - A    # index of the third lepton when len(dileps) > 1
               leps1 = []        
               for i in xrange(len(leps)):
                   leps1.append(leps[i].p.Clone())
                   leps1[i].SetPz(0)
               mT = (leps1[0] + leps1[1] + leps1[2] + pTmiss).M()
               mSFOS = (dileps[A][0].p + dileps[A][1].p).M()
               if mT > 110.:
                   self.SR['3lH'].Pass('mT > 110')
                   if mSFOS > 101.2:
                       self.SR['3lH'].Pass('mSFOP > 101.2')
                       if leps[l2].pT > 80.:
                           self.SR['3lH'].Pass('pT3l > 80')
                           if MET > 60.:
                               self.SR['3lH'].Pass('MET > 60')
                               self.SR['3lH'].PassSR()
           if len(dileps) == 1:
               leps2 = []
               for i in xrange(len(leps)):
                   leps2.append(leps[i].p.Clone())
                   leps2[i].SetPz(0)
               mT = (leps2[0] + leps2[1] + leps2[2] + pTmiss).M()
               mSFOS = (dileps[0][0].p + dileps[0][1].p).M()
               if mT > 110.:
                   self.SR['3lH'].Pass('mT > 110')
                   if mSFOS > 101.2:
                       self.SR['3lH'].Pass('mSFOP > 101.2')
                       if leps[l1].pT > 80.:
                           self.SR['3lH'].Pass('pT3l > 80')
                           if MET > 60.:
                               self.SR['3lH'].Pass('MET > 60')
                               self.SR['3lH'].PassSR()

        
       
               
       
         

       

      
                

    #########################################
    #    Output
    #########################################
    def write_result(self, iev):
        print ''
        print 'Analysis: {ananame}'.format(ananame=self.ananame)
        for key, item in self.SR.items(): item.PrintEff(iev)




