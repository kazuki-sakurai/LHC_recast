#!/usr/bin/env python

import sys, os, gzip
import ROOT
from LHCO_reader import LHCO_reader
from objects import *
#from atlas_1605_03814 import *
from atlas_1602_09058 import *
#from atlas_1605_04285 import *
#from atlas_conf_2016_096 import *
import numpy as np

a = Structure()

#inFile = "/scratch16/diego/kazuki/result/GqqN1_1000_140.lhco"
inFile = "../result/GqqN2lLlN1_750_615_547_480.lhco"

#inFiles.pop(0)

#atlas_1605_03814 = atlas_1605_03814()

#########################################
#    Event Loop
#########################################
#iev = 0

#if not os.path.exists(inFile):
#    print inFile, 'does not exist!!'

events = LHCO_reader.Events(f_name = os.path.join(inFile))
print events
    

def do(jets):
    #4-momentum components ##LAB
    Plab =np.matrix(( np.zeros([4, len(jets)])))

    for i in xrange(len(jets)):

        Plab[0,i] = jets[i].p.E()     ##Fila coas enerxias
        Plab[1,i] = jets[i].p.Px()    ## Fila cos Px
        Plab[2,i] = jets[i].p.Py()    ## Fila cos Py
        Plab[3,i] = jets[i].p.Pz()    ## Fila cos Pz
    

    Pt = jets[0].p

    for i in xrange(1,len(jets)): Pt = Pt + jets[i].p
   
    Ptx = Pt.Px()
    Pty = Pt.Py()
    Ptz = Pt.Pz()
    Et = Pt.E()


    Bz = Ptz/Et
    Gz = 1./np.sqrt(1-Bz**2)
    Lz = np.matrix(([Gz, 0, 0, -Bz*Gz], [0, 1, 0, 0], [0, 0, 1, 0], [-Bz*Gz, 0, 0, Gz]))

    Ptot = np.matrix((Et, Ptx, Pty, Ptz)).transpose()
    Ptot1 = Lz*Ptot

    By =float( Ptot1[2]/Ptot1[0])
    Gy = 1./np.sqrt(1-By**2)
    Ly = np.matrix(([Gy, 0, -By*Gy, 0], [0, 1, 0, 0], [-By*Gy, 0, Gy, 0], [0, 0, 0, 1]))

    Ptot2 = Ly*Lz*Ptot
    
    Bx =float( Ptot2[1]/Ptot2[0])
    Gx = 1./np.sqrt(1-Bx**2)
    Lx = np.matrix(([Gx, -Bx*Gx, 0, 0], [-Bx*Gx, Gx, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]))
    L = Lx*Ly*Lz

    Prest =np.matrix(( np.zeros([4, len(jets)])))
    for i in xrange(len(jets)):
        Prest[:,i] = L*Plab[:,i]
   
        #Sphericity tensor

    S = np.zeros([3, 3])

    for i in xrange(0,3):
        for j in xrange(0,3):
            sum1 = 0.
            sum2 = 0.
            for k in xrange(len(jets)):

                sum1 = sum1 +float(Prest[:,k][i])*float(Prest[:,k][j])
                sum2 = sum2 + (float(Prest[:,k][1]))**2 + (float(Prest[:,k][2]))**2 + (float(Prest[:,k][3]))**2

            S[i,j] = sum1/sum2

    Eig = np.linalg.eig(S)
    Lambda = Eig[0]
    Eigenvectors = Eig[1]

    #Sphericity

    s =(3./2)*(Lambda[1]/Lambda[2])

    #Aplanarity
    
    A = 3.0*min(Lambda)/2

    return s, A
## from ROOT import *
## hs = TH1F("S","S",100, 0,1)
## hA = TH1F("A","A",100,0,0.5)
## for event in events:
##     base_objects = get_base_objects(event)
##     jets = base_objects['jets']
##     s, A = do(jets)
##     hs.Fill(s)
##     hA.Fill(A)
for event in events:
    base_objects = get_base_objects(event, add_taus = 1)
    leps = base_objects['leps']
    if len(leps) > 0 :
           break
    ## for lep in leps:
    ##     if abs(lep.pid) > 13 :
    ##        # print "Maybe this is a tau:", lep.pid
    ##         break
#tau = lep
bjet = base_objects['bjets']
    
    

#atlas_1605_03814.event_analysis(base_objects)        

#########################################
#    Output
#########################################
#atlas_1605_03814.write_result(iev)
