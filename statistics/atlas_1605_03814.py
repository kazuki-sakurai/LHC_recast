#!/usr/bin/env python
import sys, os, pickle
from collections import OrderedDict

ananame = 'atlas_1605_03814'
res = OrderedDict()

res['lumi'] = 3.2
res['ananame'] = ananame
res['SR'] = OrderedDict()

#-------------------#
SRname = '2jl'
data = {}
data['Nobs'] = 263.
data['Nbkg'] = 283.
data['Nbkg_err'] = 24.
res['SR'][SRname] = data

#-------------------#
SRname = '2jm'
data = {}
data['Nobs'] = 191.
data['Nbkg'] = 191.
data['Nbkg_err'] = 21.
res['SR'][SRname] = data

#-------------------#
SRname = '2jt'
data = {}
data['Nobs'] = 26.
data['Nbkg'] = 23.
data['Nbkg_err'] = 4.
res['SR'][SRname] = data

#-------------------#
SRname = '4jt'
data = {}
data['Nobs'] = 7.
data['Nbkg'] = 4.6
data['Nbkg_err'] = 1.1
res['SR'][SRname] = data

#-------------------#
SRname = '5j'
data = {}
data['Nobs'] = 7.
data['Nbkg'] = 13.2
data['Nbkg_err'] = 2.2
res['SR'][SRname] = data

#-------------------#
SRname = '6jm'
data = {}
data['Nobs'] = 5
data['Nbkg'] = 6.9
data['Nbkg_err'] = 1.5
res['SR'][SRname] = data

#-------------------#
SRname = '6jt'
data = {}
data['Nobs'] = 3
data['Nbkg'] = 4.2
data['Nbkg_err'] = 1.2
res['SR'][SRname] = data

f = open('{ananame}.pickle'.format(ananame=ananame), 'wb') 
pickle.dump(res, f)

