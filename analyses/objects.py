#!/usr/bin/env python
from ROOT import gROOT, TH1F, gRandom, TNamed, TLorentzVector, gStyle, TCanvas, TFile, TEfficiency
from LHCO_reader import LHCO_reader
from collections import OrderedDict
from prettytable import PrettyTable
from math import *
#from math import pi, sqrt, cos, sin
from mT2_packages import *

class Structure(): pass

class Cut:
    def __init__(self, SRname):
        self.SRname = SRname
        self.cut = OrderedDict()
        self.id = OrderedDict()
        self.cut[SRname] = 0.
        self.id[SRname] = 0

    def Pass(self, name, idd=-1):
        if name in self.cut.keys():
            self.cut[name] += 1
        else:
            if idd < 0: idd = len(self.cut.keys())
            self.id[name] = idd
            self.cut[name] = 1

    def PassSR(self):
        self.cut[self.SRname] += 1

    def PrintEff(self, Nev):

        table = PrettyTable([self.SRname, 'cut-name', 'Eff'])
        table.padding_width = 2        
        nden = int(Nev)
        OrderedDict(sorted(self.id.items(), key=lambda t: t[1]))
        for name, idd in self.id.iteritems():
            nsel = int(self.cut[name])
            
            Eff = float(nsel) / float(Nev)
            err_plus = TEfficiency.FeldmanCousins(nden, nsel, .6827, True)
            err_minus = TEfficiency.FeldmanCousins(nden, nsel, .6827, False)

            
            Eff = str(Eff) + ' + ' + str(err_plus) +" - " +str(err_minus)
            table.add_row( [idd, name, Eff] )

        #print '='*10 +' '+ self.SRname +' '+ '='*10 
        print table


def get_mT(p1, p2):

    pt1 = sqrt(p1.Px()**2 + p1.Py()**2)
    pt2 = sqrt(p2.Px()**2 + p2.Py()**2)
    delPhi = delta_phi(p1.Phi(), p2.Phi())
    mT = 2. * pt1 * pt2 * (1. - cos(delPhi))
    mT = sqrt(mT)

    # px = p1.Px() + p2.Px()
    # py = p1.Py() + p2.Py()
    # ee = p1.E() + p2.E()
    # mT = sqrt(ee**2 - px**2 - py**2)

    return mT

def get_amt2(lep, j1, j2, pTmiss):
    mt2bl_1 = get_mT2bl(lep, j1, j2, pTmiss)
    mt2bl_2 = get_mT2bl(lep, j2, j1, pTmiss)
    return min(mt2bl_1, mt2bl_2)

def get_mT2bl(lep, b1, b2, pTmiss):

    args = {}
    args['lepE'] = lep.p.E()
    args['lepPx'] = lep.p.Px()
    args['lepPy'] = lep.p.Py()
    args['lepPz'] = lep.p.Pz()

    args['b1E'] = b1.p.E()
    args['b1Px'] = b1.p.Px()
    args['b1Py'] = b1.p.Py()
    args['b1Pz'] = b1.p.Pz()

    args['b2E'] = b2.p.E()
    args['b2Px'] = b2.p.Px()
    args['b2Py'] = b2.p.Py()
    args['b2Pz'] = b2.p.Pz()

    args['MET_x'] = pTmiss.Px()
    args['MET_y'] = pTmiss.Py()

    mt2bl = MT2bl(**args)
    return mt2bl    


def delta_phi(phi_1, phi_2):
    # Consider difference on [0., 2.*pi)
    delta_phi = (phi_1 - phi_2) % (2. * pi)
    # Consider acute angle
    delta_phi = min(delta_phi, 2. * pi - delta_phi)
    assert 0. <= delta_phi <= pi, r"Angle \Delta\phi not in [0, \pi)"
    return delta_phi

# def delta_phi(phi_1, phi_2):
#     return acute(phi_1, phi_2)


def get_base_objects(event, add_taus = 0):

    objects = {}

    #Jets
    jets, bjets, non_bjets = [], [], []        
    for obj in event['jet']:
        Data = Structure()
        Data.pid = 5 if obj['btag'] == 1 else 1
        Data.p = TLorentzVector()
        Data.p.SetPtEtaPhiM(obj['PT'], obj['eta'], obj['phi'], obj['jmass'])
        Data.pT = obj['PT']
        Data.abseta = abs(obj['eta'])
        jets.append( Data )
        if obj['btag'] == 1:
            bjets.append( Data )
        else:
            non_bjets.append( Data )

    #Leptons
    leps = []    
    for obj in event['electron']:
        Data = Structure()
        sign = - obj.charge()
        Data.pid = sign * 11
        Data.p = TLorentzVector()
        Data.p.SetPtEtaPhiM(obj['PT'], obj['eta'], obj['phi'], obj['jmass'])
        Data.pT = obj['PT']
        Data.abseta = abs(obj['eta'])
        leps.append( Data )

    for obj in event['muon']:
        Data = Structure()
        sign = - obj.charge()
        Data.pid = sign * 13
        Data.p = TLorentzVector()
        Data.p.SetPtEtaPhiM(obj['PT'], obj['eta'], obj['phi'], obj['jmass'])
        Data.pT = obj['PT']
        Data.abseta = abs(obj['eta'])
        leps.append( Data )
    if add_taus:
        for obj in event['tau']:
            Data = Structure()
            sign = - obj.charge()
            Data.pid = sign * 15
            Data.p = TLorentzVector()
            Data.p.SetPtEtaPhiM(obj['PT'], obj['eta'], obj['phi'], obj['jmass'])
            Data.pT = obj['PT']
            Data.abseta = abs(obj['eta'])
            leps.append( Data )
    #MET
    pTmiss = TLorentzVector()
    obj = event['MET'][0]
    pTmiss.SetPtEtaPhiM(obj['PT'], obj['eta'], obj['phi'], obj['jmass'])
    MET = obj['PT']

    objects['jets'] = jets
    objects['bjets'] = bjets
    objects['non_bjets'] = non_bjets
    objects['leps'] = leps
    objects['pTmiss'] = pTmiss
    objects['MET'] = MET

    return objects



def histogram_plot(hist, outFile):

    ###############################
    # initialisation 
    ###############################
    gROOT.SetStyle("Plain") ;
    gStyle.SetOptStat(0)
    gStyle.SetTitleXOffset (1.25);
    gStyle.SetTitleYOffset (1.5);

    c1 = TCanvas('title', 'name', 600, 500)
    c1.SetTicks(1,1);
    #c1.SetBottomMargin(0.3);
    c1.SetLeftMargin(0.2);   
    c1.SetLogy(1); 
    ###############################

    key_list = hist.keys()
    nhist = len(key_list)

    for i in range(nhist):
        key = key_list[i]
        fName = outFile
        if i == 0: fName = outFile + '('
        if i == nhist - 1: fName = outFile + ')'
        hist[key].Draw()
        c1.Print(fName)

    return
