#!/usr/bin/env python
from objects import *
from collections import OrderedDict
from aplanarity import *
from mT2_packages import *
import alyabar as aly



class atlas_conf_2017_039:

    #########################################
    #    Define groups of signal regions
    #########################################
    def __init__(self):
        self.ananame = 'atlas_conf_2017_039'
        self.SR = OrderedDict()        
        self.SR['base'] = Cut('base')
        self.SR['SFa'] = Cut('SFa')
        self.SR['SFb'] = Cut('SFb')
        self.SR['SFc'] = Cut('SFc')
        self.SR['SFd'] = Cut('SFd')
        self.SR['SFe'] = Cut('SFe')
        self.SR['SFf'] = Cut('SFf')
        self.SR['SFg'] = Cut('SFg')
        self.SR['SFh'] = Cut('SFh')
        self.SR['SFi'] = Cut('SFi')
        self.SR['SFj'] = Cut('SFj')
        self.SR['SFk'] = Cut('SFk')
        self.SR['SFl'] = Cut('SFl')
        self.SR['SFm'] = Cut('SFm')
        self.SR['SFloose'] = Cut('SFloose')
        self.SR['SFtight'] = Cut('SFtight')
        self.SR['DF100'] = Cut('DF100')
        self.SR['DF150'] = Cut('DF150')
        self.SR['DF200'] = Cut('DF200')
        self.SR['DF300'] = Cut('DF300')
        self.SR['int'] = Cut('int')
        self.SR['high'] = Cut('high')
        self.SR['low'] = Cut('low')
        self.SR['WZ0Ja'] = Cut('WZ0Ja')
        self.SR['WZ0Jb'] = Cut('WZ0Jb')
        self.SR['WZ0Jc'] = Cut('WZ0Jc')
        self.SR['WZ1Ja'] = Cut('WZ1Ja')
        self.SR['WZ1Jb'] = Cut('WZ1Jb')
        self.SR['WZ1Jc'] = Cut('WZ1Jc')
        self.SR['slepa'] = Cut('slepa')
        self.SR['slepb'] = Cut('slepb')
        self.SR['slepc'] = Cut('slepc')
        self.SR['slepd'] = Cut('slepd')
        self.SR['slepe'] = Cut('slepe')
        
        
        

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

        #Z veto
        ## for i in xrange(len(leps)):
        ##     for j in xrange(len(leps)):
        ##         if abs(leps[i].pid) != abs(leps[j].pid):
        ##             PX = np.abs((leps[i].p.Px() - leps[j].p.Px()))/np.abs(leps[j].p.Px())
        ##             PY = np.abs((leps[i].p.Py() - leps[j].p.Py()))/np.abs(leps[j].p.Py())
        ##             PZ = np.abs((leps[i].p.Pz() - leps[j].p.Pz()))/np.abs(leps[j].p.Pz())
        ##             if PX < 0.1 and PY < 0.1 and PZ < 0.1:
        ##                 if abs(leps[i].pid) == 11:
        ##                     del leps[i]
        ##                 else:
        ##                     del leps[j]


                

        if len(leps) > 1 and len(leps) < 4:
            self.SR['base'].Pass('Nlep = 2 or 3')
            self.SR['base'].PassSR()
            base_cut = True

    
           
        if base_cut == False: return

        #########################        
        #  Variables
        #########################
        Njet = len(jets)
        Nbjet = len(bjets)
        Nlep = len(leps)
        mZ = 91.1876      #PDG 2016 #GeV
        MET_m = 0.
    

    
       # if len(jets) >2: sph, aplanarity = Aplanarity(jets)
        #else: sph, aplanarity = 0, 0


        #########################
        #  SR: SFa
        #########################

    

        if Nlep == 2:
            self.SR['SFa'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFa'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFa'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFa'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFa'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFa'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 111. and m_inv < 150.:
                                    self.SR['SFa'].Pass('111 < m_inv < 150 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 100. and mT2 < 150.:
                                        self.SR['SFa'].Pass('100 < mT2 < 150 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return
                                        self.SR['SFa'].PassSR()


        #########################
        #  SR: SFb
        #########################

        if Nlep == 2:
            self.SR['SFb'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFb'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFb'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFb'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFb'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFb'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 150. and m_inv < 200.:
                                    self.SR['SFb'].Pass('150 < m_inv < 200 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 100. and mT2 < 150.:
                                        self.SR['SFb'].Pass('100 < mT2 < 150 GeV')
                                        if mT2 > 100. and mT2 < 150.:
                                            self.SR['SFa'].Pass('100 < mT2 < 150 GeV')
                                            for i in xrange(len(jets)):
                                                if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                    return
                                            for i in xrange(len(bjets)):
                                                if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                    return
                                            self.SR['SFb'].PassSR()



        #########################
        #  SR: SFc
        #########################

        if Nlep == 2:
            self.SR['SFc'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFc'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFc'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFc'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFc'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFc'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 200. and m_inv < 300.:
                                    self.SR['SFc'].Pass('200 < m_inv < 300 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 100. and mT2 < 150.:
                                        self.SR['SFc'].Pass('100 < mT2 < 150 GeV')
                                        for i in xrange(len(jets)):
                                           if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                               return
                                        for i in xrange(len(bjets)):
                                           if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                               return
                                        self.SR['SFc'].PassSR()



        #########################
        #  SR: SFd
        #########################

        if Nlep == 2:
            self.SR['SFd'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFd'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFd'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFd'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFd'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFd'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 300. :
                                    self.SR['SFd'].Pass('m_inv > 300 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 100. and mT2 < 150.:
                                        self.SR['SFd'].Pass('100 < mT2 < 150 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFd'].PassSR()




        #########################
        #  SR: SFe
        #########################

        if Nlep == 2:
            self.SR['SFe'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFe'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFe'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFe'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFe'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFe'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 111. and m_inv < 150.:
                                    self.SR['SFe'].Pass('111 < m_inv < 150 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 150. and mT2 < 200.:
                                        self.SR['SFe'].Pass('150 < mT2 < 200 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFe'].PassSR()



        #########################
        #  SR: SFf
        #########################

        if Nlep == 2:
            self.SR['SFf'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFf'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFf'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFf'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFf'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFf'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 150. and m_inv < 200.:
                                    self.SR['SFf'].Pass('150 < m_inv < 200 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 150. and mT2 < 200.:
                                        self.SR['SFf'].Pass('150 < mT2 < 200 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFf'].PassSR()





        #########################
        #  SR: SFg
        #########################

        if Nlep == 2:
            self.SR['SFg'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFg'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFg'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFg'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFg'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFg'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 200. and m_inv < 300.:
                                    self.SR['SFg'].Pass('200 < m_inv < 300 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 150. and mT2 < 200.:
                                        self.SR['SFg'].Pass('150 < mT2 < 200 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFg'].PassSR()


        #########################
        #  SR: SFh
        #########################

        if Nlep == 2:
            self.SR['SFh'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFh'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFh'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFh'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFh'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFh'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 300.:
                                    self.SR['SFh'].Pass('m_inv >300 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 150. and mT2 < 200.:
                                        self.SR['SFh'].Pass('150 < mT2 < 200 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFh'].PassSR()






        #########################
        #  SR: SFi
        #########################

        if Nlep == 2:
            self.SR['SFi'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFi'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFi'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFi'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFi'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFi'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 111. and m_inv < 150.:
                                    self.SR['SFi'].Pass('111 < m_inv < 150 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 200. and mT2 < 300.:
                                        self.SR['SFi'].Pass('200 < mT2 < 300 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFi'].PassSR()



        #########################
        #  SR: SFj
        #########################

        if Nlep == 2:
            self.SR['SFj'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFj'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFj'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFj'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFj'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFj'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 150. and m_inv < 200.:
                                    self.SR['SFj'].Pass('150 < m_inv < 200 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 200. and mT2 < 300.:
                                        self.SR['SFj'].Pass('200 < mT2 < 300 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFj'].PassSR()





        #########################
        #  SR: SFk
        #########################

        if Nlep == 2:
            self.SR['SFk'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFk'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFk'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFk'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFk'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFk'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 200. and m_inv < 300.:
                                    self.SR['SFk'].Pass('200 < m_inv < 300 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 200. and mT2 < 300.:
                                        self.SR['SFk'].Pass('200 < mT2 < 300 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFk'].PassSR()


        #########################
        #  SR: SFl
        #########################

        if Nlep == 2:
            self.SR['SFl'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFl'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFl'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFl'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFl'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFl'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 300.:
                                    self.SR['SFl'].Pass('m_inv >300 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 200. and mT2 < 300.:
                                        self.SR['SFl'].Pass('200 < mT2 < 300 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFl'].PassSR()


        #########################
        #  SR: SFm
        #########################

        if Nlep == 2:
            self.SR['SFm'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFm'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFm'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFm'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFm'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFm'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 111.:
                                    self.SR['SFm'].Pass('m_inv > 111 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 300.:
                                        self.SR['SFm'].Pass('mT2 > 300 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFm'].PassSR()



        #########################
        #  SR: SFloose
        #########################

        if Nlep == 2:
            self.SR['SFloose'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFloose'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFloose'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFloose'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFloose'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFloose'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 111.:
                                    self.SR['SFloose'].Pass('m_inv > 111 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 100.:
                                        self.SR['SFloose'].Pass('mT2 > 100 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFloose'].PassSR()


        #########################
        #  SR: SFtight
        #########################

        if Nlep == 2:
            self.SR['SFtight'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['SFtight'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['SFtight'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['SFtight'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['SFtight'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['SFtight'].Pass('pTl2 > 20 GeV')
                                m_inv = (leps[0].p + leps[1].p).M()
                                if m_inv  > 300.:
                                    self.SR['SFtight'].Pass('m_inv > 300 GeV')
                                    mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                    if mT2 > 130.:
                                        self.SR['SFtight'].Pass('mT2 > 130 GeV')
                                        for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                        for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                        self.SR['SFtight'].PassSR()



        #########################
        #  SR: DF100
        #########################

        if Nlep == 2:
            self.SR['DF100'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['DF100'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['DF100'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['DF100'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['DF100'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['DF100'].Pass('pTl2 > 20 GeV')
                                mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                if mT2 > 100.:
                                    self.SR['DF100'].Pass('mT2 > 100 GeV')
                                    for i in xrange(len(jets)):
                                        if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                            return
                                    for i in xrange(len(bjets)):
                                        if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                            return 
                                    self.SR['DF100'].PassSR()




        #########################
        #  SR: DF150
        #########################

        if Nlep == 2:
            self.SR['DF150'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['DF150'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['DF150'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['DF150'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['DF150'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['DF150'].Pass('pTl2 > 20 GeV')
                                mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                if mT2 > 150.:
                                    self.SR['DF150'].Pass('mT2 > 150 GeV')
                                    for i in xrange(len(jets)):
                                        if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                            return
                                    for i in xrange(len(bjets)):
                                        if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                            return 
                                    self.SR['DF150'].PassSR()



        #########################
        #  SR: DF200
        #########################

        if Nlep == 2:
            self.SR['DF200'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['DF200'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['DF200'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['DF200'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['DF200'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['DF200'].Pass('pTl2 > 20 GeV')
                                mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                if mT2 > 100.:
                                    self.SR['DF200'].Pass('mT2 > 200 GeV')
                                    for i in xrange(len(jets)):
                                        if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                            return
                                    for i in xrange(len(bjets)):
                                        if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                            return 
                                    self.SR['DF200'].PassSR()




        #########################
        #  SR: DF300
        #########################

        if Nlep == 2:
            self.SR['DF300'].Pass('Nlep == 2')
            if Njet == 0:
                self.SR['DF300'].Pass('Njet = 0')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['DF300'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['DF300'].Pass('Different sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['DF300'].Pass('pTl1 > 20 GeV')
                            if leps[1].pT > 20.:
                                self.SR['DF300'].Pass('pTl2 > 20 GeV')
                                mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                if mT2 > 300.:
                                    self.SR['DF300'].Pass('mT2 > 300 GeV')
                                    for i in xrange(len(jets)):
                                            if jets[i].pT > 60. and jets[i].abserta < 2.4 and jets[i].pid != 5:
                                                return
                                    for i in xrange(len(bjets)):
                                            if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                                return 
                                    self.SR['DF300'].PassSR()
                                    
                



        #########################
        #  SR: int
        #########################

        if Nlep == 2:
            self.SR['int'].Pass('Nlep == 2')
            if Njet >= 2:
                self.SR['int'].Pass('Njet >= 2')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['int'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['int'].Pass('Opposite sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['int'].Pass('pTl1 > 25 GeV')
                            if leps[1].pT > 25.:
                                self.SR['int'].Pass('pTl2 > 25 GeV')
                                for i in xrange(len(bjets)):                           #bjet veto
                                    if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                        return
                                if jets[0].pT > 30.:
                                    self.SR['int'].Pass('pTj1 > 30 GeV')
                                    if jets[1].pT > 30.:
                                        self.SR['int'].Pass('pTj2 > 30 GeV')
                                        m_inv = (leps[0].p + leps[1].p).M()
                                        if m_inv > 81. and m_inv < 101.:
                                            self.SR['int'].Pass('81 < m_inv < 101 GeV (Z veto)')
                                            mjj = (jets[0].p + jets[1].p).M()
                                            if mjj > 70. and mjj < 100.:
                                                self.SR['int'].Pass('70 < mjj < 100 GeV')
                                                if MET > 150.:
                                                    self.SR['int'].Pass('MET > 150 GeV')
                                                    pZ = leps[0].p + leps[1].p                      #Z boson momenta
                                                    pTZ = aly.vtmod(pZ)                     #transverse momenta of Z boson
                                                    if pTZ > 80.:
                                                        self.SR['int'].Pass('pTZ > 80 GeV')
                                                        pW = jets[0].p + jets[1].p            #W boson momenta
                                                        pTW = aly.vtmod(pW)
                                                        if pTW > 100.:
                                                            self.SR['int'].Pass('pTW > 100 GeV')
                                                            mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                                            if mT2 > 100.:
                                                                self.SR['int'].Pass('mT2 > 100 GeV')
                                                                dPhi = delta_phi(pW.Phi(), pTmiss.Phi())
                                                                if dPhi >= 0.5 and dPhi <= 3.0:
                                                                    self.SR['int'].Pass('0.5 < dPhi(W) < 3.0')
                                                                    self.SR['int'].PassSR()
                                                                    
                                                                    
                                                                    
                                                                

        #########################
        #  SR: high
        #########################

        if Nlep == 2:
            self.SR['high'].Pass('Nlep == 2')
            if Njet >= 2:
                self.SR['high'].Pass('Njet >= 2')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['high'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['high'].Pass('Opposite sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['high'].Pass('pTl1 > 25 GeV')
                            if leps[1].pT > 25.:
                                self.SR['high'].Pass('pTl2 > 25 GeV')
                                for i in xrange(len(bjets)):                           #bjet veto
                                    if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                        return
                                if jets[0].pT > 30.:
                                    self.SR['high'].Pass('pTj1 > 30 GeV')
                                    if jets[1].pT > 30.:
                                        self.SR['high'].Pass('pTj2 > 30 GeV')
                                        m_inv = (leps[0].p + leps[1].p).M()
                                        if m_inv > 81. and m_inv < 101.:
                                            self.SR['high'].Pass('81 < m_inv < 101 GeV (Z veto)')
                                            mjj = (jets[0].p + jets[1].p).M()
                                            if mjj > 70. and mjj < 100.:
                                                self.SR['high'].Pass('70 < mjj < 100 GeV')
                                                if MET > 250.:
                                                    self.SR['high'].Pass('MET > 250 GeV')
                                                    pZ = leps[0].p + leps[1].p                      #Z boson momenta
                                                    pTZ = aly.vtmod(pZ)                     #transverse momenta of Z boson
                                                    if pTZ > 80.:
                                                        self.SR['high'].Pass('pTZ > 80 GeV')
                                                        pW = jets[0].p + jets[1].p            #W boson momenta
                                                        pTW = aly.vtmod(pW)
                                                        if pTW > 100.:
                                                            self.SR['high'].Pass('pTW > 100 GeV')
                                                            mT2 = MT2(leps[0].p.M(), leps[0].p.Px(), leps[0].p.Py(), leps[1].p.M(), leps[1].p.Px(), leps[1].p.Py(), MET_m, pTmiss.Px(), pTmiss.Py())
                                                            if mT2 > 100.:
                                                                self.SR['high'].Pass('mT2 > 100 GeV')
                                                                dPhi = delta_phi(pW.Phi(), pTmiss.Phi())
                                                                if dPhi >= 0.5 and dPhi <= 3.0:
                                                                    self.SR['high'].Pass('0.5 < dPhi(W) < 3.0')
                                                                    self.SR['high'].PassSR()




        #########################
        #  SR: low
        #########################

        if Nlep == 2:
            self.SR['low'].Pass('Nlep == 2')
            if Njet == 2:
                self.SR['low'].Pass('Njet = 2')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['low'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['low'].Pass('Opposite sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['low'].Pass('pTl1 > 25 GeV')
                            if leps[1].pT > 25.:
                                self.SR['low'].Pass('pTl2 > 25 GeV')
                                for i in xrange(len(bjets)):                           #bjet veto
                                    if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                        return
                                if jets[0].pT > 30.:
                                    self.SR['low'].Pass('pTj1 > 30 GeV')
                                    if jets[1].pT > 30.:
                                        self.SR['low'].Pass('pTj2 > 30 GeV')
                                        m_inv = (leps[0].p + leps[1].p).M()
                                        if m_inv > 81. and m_inv < 101.:
                                            self.SR['low'].Pass('81 < m_inv < 101 GeV (Z veto)')
                                            mjj = (jets[0].p + jets[1].p).M()
                                            if mjj > 70. and mjj < 90.:
                                                self.SR['low'].Pass('70 < mjj < 90 GeV')
                                                if MET > 100.:
                                                    self.SR['low'].Pass('MET > 100 GeV')
                                                    pZ = leps[0].p + leps[1].p                      #Z boson momenta
                                                    pTZ = aly.vtmod(pZ)                     #transverse momenta of Z boson
                                                    pW = jets[0].p + jets[1].p
                                                    pTW = aly.vtmod(pW)
                                                    if pTZ > 60.:
                                                        self.SR['low'].Pass('pTZ > 60 GeV')
                                                        dPhiZ = delta_phi(pZ.Phi(), pTmiss.Phi())
                                                        if dPhiZ < 0.8:
                                                            self.SR['low'].Pass('dPhiZ < 0.8')
                                                            dPhiW = delta_phi(pW.Phi(), pTmiss.Phi())
                                                            if dPhiW > 1.5:
                                                                self.SR['low'].Pass('DPhiW > 1.5')
                                                                if MET/pTZ > 0.6 and MET/pTZ < 1.6:
                                                                    self.SR['low'].Pass('0.6 < MET/pTZ < 1.6')
                                                                    if MET/pTW < 0.8:
                                                                        self.SR['low'].Pass('MET/pTW < 0.8')
                                                                        self.SR['low'].PassSR()
        if Nlep == 2:
            self.SR['low'].Pass('Nlep == 2')
            if Njet >= 3 and Njet <= 5:
                self.SR['low'].Pass('3 <= Njet <= 5')
                if abs(leps[0].pid) == abs(leps[1].pid):
                    self.SR['low'].Pass('Same Flavour leptons')
                    if np.sign(leps[0].pid) != np.sign(leps[1].pid):
                        self.SR['low'].Pass('Opposite sign leptons')
                        if leps[0].pT > 25.:
                            self.SR['low'].Pass('pTl1 > 25 GeV')
                            if leps[1].pT > 25.:
                                self.SR['low'].Pass('pTl2 > 25 GeV')
                                for i in xrange(len(bjets)):                           #bjet veto
                                    if bjets[i].pT > 20. and bjets[i].abseta < 2.4:
                                        return
                                if jets[0].pT > 30.:
                                    self.SR['low'].Pass('pTj1 > 30 GeV')
                                    if jets[1].pT > 30.:
                                        self.SR['low'].Pass('pTj2 > 30 GeV')
                                        m_inv = (leps[0].p + leps[1].p).M()
                                        if m_inv > 86. and m_inv < 96.:
                                            self.SR['low'].Pass('86 < m_inv < 96 GeV (Z veto)')
                                            system = leps[0].p + leps[1].p + pTmiss
                                            etasys = -np.log(np.tan(aly.ACO(system, (0,0,1))/2))
                                            dR_new = 1000000000.
                                            mjj_new = 0.
                                            for i in xrange(Njet):
                                                for j in xrange(i+1, Njet):
                                                    mjj = (jets[i].p + jets[j].p).M()
                                                    pjj = jets[i].p + jets[j].p
                                                    if mjj > 70. and mjj < 90.:
                                                        dPhijs = delta_phi(pjj.Phi(), system.Phi())
                                                        etaW = -np.log(np.tan(aly.ACO(pjj, (0,0,1))/2))
                                                        deta = etaW - etasys
                                                        dR = np.sqrt(deta**2 + dPhijs**2)
                                                        if dR < dR_new:
                                                            dR_new = dR
                                                            A = i
                                                            B = j
                                                            mjj_new = mjj
                                            if mjj_new > 70. and mjj_new < 90.:
                                                self.SR['low'].Pass('70 < mjj < 90 GeV')
                                                if MET > 100.:
                                                    self.SR['low'].Pass('MET > 100 GeV')
                                                    pZ = leps[0].p + leps[1].p                      #Z boson momenta
                                                    pTZ = aly.vtmod(pZ)                     #transverse momenta of Z boson  
                                                    pW = jets[A].p + jets[B].p              
                                                    pTW = aly.vtmod(pW)
                                                    if pTZ > 40.:
                                                        self.SR['low'].Pass('pTZ > 40 GeV')
                                                        dPhiW = delta_phi(pW.Phi(), pTmiss.Phi())
                                                        if dPhiW < 2.2:
                                                            self.SR['low'].Pass('dPhiW < 2.2')
                                                            if MET/pTZ > 0.6 and MET/pTZ < 1.6:
                                                                self.SR['low'].Pass('0.6 < MET/pTZ < 1.6')
                                                                if MET/pTW < 0.8:
                                                                    self.SR['low'].Pass('MET/pTW < 0.8')
                                                                    ISR = -jets[A].p -jets[B].p
                                                                    for i in xrange(Njet):
                                                                        ISR = ISR + jets[i].p
                                                                    dPhiISR = delta_phi(ISR.Phi(), pTmiss.Phi())
                                                                    if dPhiISR > 2.4:
                                                                        self.SR['low'].Pass('dPhiISR > 2.4')
                                                                        dPhij1 = delta_phi(jets[0].p.Phi(), pTmiss.Phi())
                                                                        if dPhij1 > 2.6:
                                                                            self.SR['low'].Pass('dPhij1 > 2.6')
                                                                            if MET/ISR[3] > 0.4 and MET/ISR[3] < 0.8:
                                                                                self.SR['low'].Pass('0.4 < MET/ISR < 0.8')
                                                                                theta = aly.ACO(pZ, (0,0,1))
                                                                                eta = abs(-np.log(np.tan(theta/2)))
                                                                                if eta < 1.6:
                                                                                    self.SR['low'].Pass('Pseudorapidity Z < 1.6')
                                                                                    if jets[2].pT > 30.:
                                                                                        self.SR['low'].Pass('pTj3 > 30 GeV')
                                                                                        self.SR['low'].PassSR()
                                                            

                                                        
       
                                                            
        #########################
        #  SR: slepa
        #########################

        if Nlep == 3:
            self.SR['slepa'].Pass('Nlep =3')
            if Nbjet == 0:
                self.SR['slepa'].Pass('Nbjet = 0')
                dileps = []
                mT_min = 10000000000000000000
                for i in xrange(Nlep):
                    for j in xrange(i+1, Nlep):
                        if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                            dileps.append([leps[i], leps[j]])
                            k = 3 - i - j                  #index od the third lepton
                            mT = get_mT(leps[k].p, pTmiss)
                            if mT < mT_min:
                                mT_min = mT
                                A = k
                                m_inv = (leps[i].p + leps[j].p).M()
                    if len(dileps) != 0:
                        self.SR['slepa'].Pass('SFOS pair')
                        if mT_min > 110.:
                            self.SR['slepa'].Pass('mT_min > 110 GeV')
                            if m_inv < 81.2:
                                self.SR['slepa'].Pass('m_inv(SFOS) < 81.2 GeV')
                                if MET > 130.:
                                    self.SR['slepa'].Pass('MET > 130 GeV')
                                    if leps[2].pT > 20. and leps[2].pT < 30.:
                                        self.SR['slepa'].Pass('20 < pTl3 < 30 GeV')
                                        self.SR['slepa'].PassSR()
                            
                        

        #########################
        #  SR: slepb
        #########################

        if Nlep == 3:
            self.SR['slepb'].Pass('Nlep =3')
            if Nbjet == 0:
                self.SR['slepb'].Pass('Nbjet = 0')
                dileps = []
                mT_min = 10000000000000000000
                for i in xrange(Nlep):
                    for j in xrange(i+1, Nlep):
                        if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                            dileps.append([leps[i], leps[j]])
                            k = 3 - i - j                  #index od the third lepton
                            mT = get_mT(leps[k].p, pTmiss)
                            if mT < mT_min:
                                mT_min = mT
                                A = k
                                m_inv = (leps[i].p + leps[j].p).M()
                    if len(dileps) != 0:
                        self.SR['slepb'].Pass('SFOS pair')
                        if mT_min > 110.:
                            self.SR['slepb'].Pass('mT_min > 110 GeV')
                            if m_inv < 81.2:
                                self.SR['slepb'].Pass('m_inv(SFOS) < 81.2 GeV')
                                if MET > 130.:
                                    self.SR['slepb'].Pass('MET > 130 GeV')
                                    if leps[2].pT > 30.:
                                        self.SR['slepb'].Pass('pTl3 > 30 GeV')
                                        self.SR['slepb'].PassSR()



        #########################
        #  SR: slepc
        #########################

        if Nlep == 3:
            self.SR['slepc'].Pass('Nlep =3')
            if Nbjet == 0:
                self.SR['slepc'].Pass('Nbjet = 0')
                dileps = []
                mT_min = 10000000000000000000
                for i in xrange(Nlep):
                    for j in xrange(i+1, Nlep):
                        if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                            dileps.append([leps[i], leps[j]])
                            k = 3 - i - j                  #index od the third lepton
                            mT = get_mT(leps[k].p, pTmiss)
                            if mT < mT_min:
                                mT_min = mT
                                A = k
                                m_inv = (leps[i].p + leps[j].p).M()
                    if len(dileps) != 0:
                        self.SR['slepc'].Pass('SFOS pair')
                        if mT_min > 110.:
                            self.SR['slepc'].Pass('mT_min > 110 GeV')
                            if m_inv > 101.2:
                                self.SR['slepc'].Pass('m_inv(SFOS) > 101.2 GeV')
                                if MET > 130.:
                                    self.SR['slepc'].Pass('MET > 130 GeV')
                                    if leps[2].pT > 20. and leps[2].pT < 50.:
                                        self.SR['slepc'].Pass('20 < pTl3 < 50 GeV')
                                        self.SR['slepc'].PassSR()


        #########################
        #  SR: slepd
        #########################

        if Nlep == 3:
            self.SR['slepd'].Pass('Nlep =3')
            if Nbjet == 0:
                self.SR['slepd'].Pass('Nbjet = 0')
                dileps = []
                mT_min = 10000000000000000000
                for i in xrange(Nlep):
                    for j in xrange(i+1, Nlep):
                        if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                            dileps.append([leps[i], leps[j]])
                            k = 3 - i - j                  #index od the third lepton
                            mT = get_mT(leps[k].p, pTmiss)
                            if mT < mT_min:
                                mT_min = mT
                                A = k
                                m_inv = (leps[i].p + leps[j].p).M()
                    if len(dileps) != 0:
                        self.SR['slepd'].Pass('SFOS pair')
                        if mT_min > 110.:
                            self.SR['slepd'].Pass('mT_min > 110 GeV')
                            if m_inv > 101.2:
                                self.SR['slepd'].Pass('m_inv(SFOS) > 101.2 GeV')
                                if MET > 130.:
                                    self.SR['slepd'].Pass('MET > 130 GeV')
                                    if leps[2].pT > 50. and leps[2].pT < 80.:
                                        self.SR['slepd'].Pass('50 < pTl3 < 80 GeV')
                                        self.SR['slepd'].PassSR()




        #########################
        #  SR: slepe
        #########################

        if Nlep == 3:
            self.SR['slepe'].Pass('Nlep =3')
            if Nbjet == 0:
                self.SR['slepe'].Pass('Nbjet = 0')
                dileps = []
                mT_min = 10000000000000000000
                for i in xrange(Nlep):
                    for j in xrange(i+1, Nlep):
                        if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                            dileps.append([leps[i], leps[j]])
                            k = 3 - i - j                  #index od the third lepton
                            mT = get_mT(leps[k].p, pTmiss)
                            if mT < mT_min:
                                mT_min = mT
                                A = k
                                m_inv = (leps[i].p + leps[j].p).M()
                    if len(dileps) != 0:
                        self.SR['slepe'].Pass('SFOS pair')
                        if mT_min > 110.:
                            self.SR['slepe'].Pass('mT_min > 110 GeV')
                            if m_inv > 101.2:
                                self.SR['slepe'].Pass('m_inv(SFOS) > 101.2 GeV')
                                if MET > 130.:
                                    self.SR['slepe'].Pass('MET > 130 GeV')
                                    if leps[2].pT > 80.:
                                        self.SR['slepe'].Pass('pTl3 > 80 GeV')
                                        self.SR['slepe'].PassSR()
                               


        #########################
        #  SR: WZ0Ja
        #########################

        if Nlep == 3:
            print 'HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
            self.SR['WZ0Ja'].Pass('Nlep = 3')
            if Nbjet == 0:
                self.SR['WZ0Ja'].Pass('Nbjet = 0')
                if Njet == 0:
                    self.SR['WZ0Ja'].Pass('Njet = 0')
                    dileps = []
                    mT_min = 10000000000000000000
                    for i in xrange(Nlep):
                        for j in xrange(i+1, Nlep):
                            if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                                dileps.append([leps[i], leps[j]])
                                k = 3 - i - j                  #index od the third lepton
                                mT = get_mT(leps[k].p, pTmiss)
                                if mT < mT_min:
                                    mT_min = mT
                                    A = k
                                    m_inv = (leps[i].p + leps[j].p).M()
                        if len(dileps) != 0:
                            self.SR['WZ0Ja'].Pass('SFOS pair')
                            if mT_min > 110.:
                                self.SR['WZ0Ja'].Pass('mT_min > 110 GeV')
                                if m_inv > 81.2 and m_inv < 101.2:
                                    self.SR['WZ0Ja'].Pass('81.2 < m_inv(SFOS) < 101.2 GeV')
                                    if MET > 60. and MET < 120.:
                                        self.SR['WZ0Ja'].Pass('60 < MET < 120 GeV')
                                        self.SR['WZ0Ja'].PassSR()


        #########################
        #  SR: WZ0Jb
        #########################

        if Nlep == 3:
            self.SR['WZ0Jb'].Pass('Nlep = 3')
            if Nbjet == 0:
                self.SR['WZ0Jb'].Pass('Nbjet = 0')
                if Njet == 0:
                    self.SR['WZ0Jb'].Pass('Njet = 0')
                    dileps = []
                    mT_min = 10000000000000000000
                    for i in xrange(Nlep):
                        for j in xrange(i+1, Nlep):
                            if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                                dileps.append([leps[i], leps[j]])
                                k = 3 - i - j                  #index od the third lepton
                                mT = get_mT(leps[k].p, pTmiss)
                                if mT < mT_min:
                                    mT_min = mT
                                    A = k
                                    m_inv = (leps[i].p + leps[j].p).M()
                        if len(dileps) != 0:
                            self.SR['WZ0Jb'].Pass('SFOS pair')
                            if mT_min > 110.:
                                self.SR['WZ0Jb'].Pass('mT_min > 110 GeV')
                                if m_inv > 81.2 and m_inv < 101.2:
                                    self.SR['WZ0Jb'].Pass('81.2 < m_inv(SFOS) < 101.2 GeV')
                                    if MET > 120. and MET < 170.:
                                        self.SR['WZ0Jb'].Pass('120 < MET < 170 GeV')
                                        self.SR['WZ0Jb'].PassSR()


        #########################
        #  SR: WZ0Jc
        #########################

        if Nlep == 3:
            self.SR['WZ0Jc'].Pass('Nlep = 3')
            if Nbjet == 0:
                self.SR['WZ0Jc'].Pass('Nbjet = 0')
                if Njet == 0:
                    self.SR['WZ0Jc'].Pass('Njet = 0')
                    dileps = []
                    mT_min = 10000000000000000000
                    for i in xrange(Nlep):
                        for j in xrange(i+1, Nlep):
                            if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                                dileps.append([leps[i], leps[j]])
                                k = 3 - i - j                  #index od the third lepton
                                mT = get_mT(leps[k].p, pTmiss)
                                if mT < mT_min:
                                    mT_min = mT
                                    A = k
                                    m_inv = (leps[i].p + leps[j].p).M()
                        if len(dileps) != 0:
                            self.SR['WZ0Jc'].Pass('SFOS pair')
                            if mT_min > 110.:
                                self.SR['WZ0Jc'].Pass('mT_min > 110 GeV')
                                if m_inv > 81.2 and m_inv < 101.2:
                                    self.SR['WZ0Jc'].Pass('81.2 < m_inv(SFOS) < 101.2 GeV')
                                    if MET > 170.:
                                        self.SR['WZ0Jc'].Pass('MET > 170 GeV')
                                        self.SR['WZ0Jc'].PassSR()


        #########################
        #  SR: WZ1Ja
        #########################

        if Nlep == 3:
            self.SR['WZ1Ja'].Pass('Nlep = 3')
            if Nbjet == 0:
                self.SR['WZ1Ja'].Pass('Nbjet = 0')
                if Njet >= 1:
                    self.SR['WZ1Ja'].Pass('Njet >= 1')
                    dileps = []
                    mT_min = 10000000000000000000
                    for i in xrange(Nlep):
                        for j in xrange(i+1, Nlep):
                            if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                                dileps.append([leps[i], leps[j]])
                                k = 3 - i - j                  #index od the third lepton
                                mT = get_mT(leps[k].p, pTmiss)
                                if mT < mT_min:
                                    mT_min = mT
                                    A = k
                                    m_inv = (leps[i].p + leps[j].p).M()
                        if len(dileps) != 0:
                            self.SR['WZ1Ja'].Pass('SFOS pair')
                            if mT_min > 110.:
                                self.SR['WZ1Ja'].Pass('mT_min > 110 GeV')
                                if m_inv > 81.2 and m_inv < 101.2:
                                    self.SR['WZ1Ja'].Pass('81.2 < m_inv(SFOS) < 101.2 GeV')
                                    if MET > 120. and MET < 200.:
                                        self.SR['WZ1Ja'].Pass('120 < MET < 200 GeV')
                                        ptot = leps[0].p + leps[1].p + leps[2].p
                                        if aly.vtmod(ptot) < 120.:
                                            self.SR['WZ1Ja'].Pass('pTlll < 120 GeV')
                                            if jets[0].pT > 70.:
                                                self.SR['WZ1Ja'].Pass('pTj1 > 70 GeV')
                                                self.SR['WZ1Ja'].PassSR()
                                        

        #########################
        #  SR: WZ1Jb
        #########################

        if Nlep == 3:
            self.SR['WZ1Jb'].Pass('Nlep = 3')
            if Nbjet == 0:
                self.SR['WZ1Jb'].Pass('Nbjet = 0')
                if Njet >= 1:
                    self.SR['WZ1Jb'].Pass('Njet >= 1')
                    dileps = []
                    mT_min = 10000000000000000000
                    for i in xrange(Nlep):
                        for j in xrange(i+1, Nlep):
                            if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                                dileps.append([leps[i], leps[j]])
                                k = 3 - i - j                  #index od the third lepton
                                mT = get_mT(leps[k].p, pTmiss)
                                if mT < mT_min:
                                    mT_min = mT
                                    A = k
                                    m_inv = (leps[i].p + leps[j].p).M()
                        if len(dileps) != 0:
                            self.SR['WZ1Jb'].Pass('SFOS pair')
                            if mT_min > 110. and mT_min < 160.:
                                self.SR['WZ1Jb'].Pass('110 < mT_min < 160 GeV')
                                if m_inv > 81.2 and m_inv < 101.2:
                                    self.SR['WZ1Jb'].Pass('81.2 < m_inv(SFOS) < 101.2 GeV')
                                    if MET > 200.:
                                        self.SR['WZ1Jb'].Pass('MET > 200 GeV')
                                        self.SR['WZ1Jb'].PassSR()



        #########################
        #  SR: WZ1Jc
        #########################

        if Nlep == 3:
            self.SR['WZ1Jc'].Pass('Nlep = 3')
            if Nbjet == 0:
                self.SR['WZ1Jc'].Pass('Nbjet = 0')
                if Njet >= 1:
                    self.SR['WZ1Jc'].Pass('Njet >= 1')
                    dileps = []
                    mT_min = 10000000000000000000
                    for i in xrange(Nlep):
                        for j in xrange(i+1, Nlep):
                            if abs(leps[i].pid) == abs(leps[j].pid) and np.sign(leps[i].pid) != np.sign(leps[j].pid):
                                dileps.append([leps[i], leps[j]])
                                k = 3 - i - j                  #index od the third lepton
                                mT = get_mT(leps[k].p, pTmiss)
                                if mT < mT_min:
                                    mT_min = mT
                                    A = k
                                    m_inv = (leps[i].p + leps[j].p).M()
                        if len(dileps) != 0:
                            self.SR['WZ1Jc'].Pass('SFOS pair')
                            if mT_min > 160.:
                                self.SR['WZ1Jc'].Pass('mT_min > 160 GeV')
                                if m_inv > 81.2 and m_inv < 101.2:
                                    self.SR['WZ1Jc'].Pass('81.2 < m_inv(SFOS) < 101.2 GeV')
                                    if MET > 200.:
                                        self.SR['WZ1Jc'].Pass('MET > 200 GeV')
                                        if leps[2].pT > 35.:
                                            self.SR['WZ1Jc'].Pass('pTl3 > 35 GeV')
                                        self.SR['WZ1Jc'].PassSR()
                
                
                
            
       
                
            
               
       
         

       

      
                

    #########################################
    #    Output
    #########################################
    def write_result(self, iev):
        print ''
        print 'Analysis: {ananame}'.format(ananame=self.ananame)
        for key, item in self.SR.items(): item.PrintEff(iev)




