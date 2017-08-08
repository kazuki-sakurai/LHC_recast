#!/usr/bin/env python
import sys, os, pickle
from collections import OrderedDict

ananame = 'cms_1705_04650'
res = OrderedDict()

res['lumi'] = 35.9  #fb^-1   luminosity
res['ananame'] = ananame
res['SR'] = OrderedDict()


 ## Mono jet SR (bins of pT):

for i in xrange(1,8): 
    SRname = '1j0b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data

for i in xrange(1,6): 
    SRname = '1j1b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data

#### Multiple jets SR (bins of MT2): HT: very low (vl),low (l),medium (m),high (h),extreme (e)
## Very low HT:

for i in xrange(1,4): ## 3 bins of MT2, very low HT
    for j in xrange(4):
        SRname = 'vlHT_2j'+str(j)+'b_bin'+str(i)       ## number of Nb (0,1,2,3)
        data = {}
        res['SR'][SRname] = data

    for j in xrange(3):  ## number of Nb (0,1,3)
        SRname = 'vlHT_4j'+str(j)+'b_bin'+ str(i)
        data = {}
        res['SR'][SRname] = data

## Low HT:
for i in xrange(1,5): ## 4 bins of MT2, low HT
    for j in xrange(4): ## number of Nb (0,1,2,3)
        SRname = 'lHT_2j'+str(j)+'b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data

    for j in xrange(3):  ## number of Nb (0,1,2)
        SRname = 'lHT_4j'+str(j)+'b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data

for i in xrange(1,4): ## 3 bins of MT2, low HT
    for j in xrange(4):  ## number of Nb (0,1,2,3)
        SRname = 'lHT_7j'+str(j)+'b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data

## Medium HT:
for i in xrange(1,6): ## 5 bins of MT2, medium HT
    for j in xrange(3): ## number of Nb (0,1,2)
        SRname = 'mHT_2j'+str(j)+'b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data

    for j in xrange(3):
        SRname = 'mHT_4j'+str(j)+'b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data

    SRname = 'mHT_7j0b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data

for i in xrange(1,5): ## 4 bins of MT2, medium HT
    for j in [1,2,3]: 
        SRname = 'mHT_7j'+str(j)+'b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data

        SRname = 'mHT_2j3b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data
## High HT:
for i in xrange(1,7): ## 6 bins of MT2, high MT
    for j in xrange(2): ## number of Nb (0,1)
        SRname = 'hHT_2j'+str(j)+'b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data

        SRname = 'hHT_4j'+str(j)+'b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data
for i in xrange(1,6): ## 5 bins of MT2, high MT
    SRname = 'hHT_2j2b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data

    SRname = 'hHT_4j2b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data

    SRname = 'hHT_7j0b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data
for i in xrange(1,5): ## 4 bins of MT2, high MT
    for j in [1,2]: 
        SRname = 'hHT_7j'+str(j)+'b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data
for i in xrange(1,4): ## 3 bins of MT2, high MT
    for j in [2,7]:  
        SRname = 'hHT_'+str(j)+'j3b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data
## Extreme HT:
for i in xrange(1,6): ## 5 bins of MT2, extreme MT
    SRname = 'eHT_2j0b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data
    for j in xrange(2): 
        SRname = 'eHT_4j'+str(j)+'b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data
for i in xrange(1,5): ## 4 bins of MT2, extreme HT
    SRname = 'eHT_2j1b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data

    SRname = 'eHT_7j0b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data
for i in xrange(1,4): ## 3 bins of MT2, extreme HT
    SRname = 'eHT_4j2b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data
    for j in [1,2]: 
        SRname = 'eHT_7j'+str(j)+'b_bin'+str(i)
        data = {}
        res['SR'][SRname] = data
for i in xrange(1,3): ## 2 bins of MT2, extreme HT
    SRname = 'eHT_2j3b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data
for i in xrange(1,2): ## 1 bin of MT2, extreme HT
    SRname = 'eHT_2j2b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data

    SRname = 'eHT_7j3b_bin'+str(i)
    data = {}
    res['SR'][SRname] = data




f = open('{ananame}.pickle'.format(ananame=ananame), 'wb') 
pickle.dump(res, f)
