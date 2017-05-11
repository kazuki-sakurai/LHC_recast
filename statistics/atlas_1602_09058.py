#!/usr/bin/env python
import sys, os, pickle
from collections import OrderedDict

ananame = 'atlas_1602_09058'
res = OrderedDict()

res['lumi'] = 3.2
res['ananame'] = ananame
res['SR'] = OrderedDict()

#-------------------#
SRname = '0b3j'
data = {}
data['Nobs'] = 3.
data['Nbkg'] = 1.5
data['Nbkg_err'] = 0.4
data['S95_obs'] = 5.9
data['S95_exp'] = 4.1
data['p0'] = 0.13

res['SR'][SRname] = data

#-------------------#
SRname = '0b5j'
data = {}
data['Nobs'] = 3.
data['Nbkg'] = 0.88
data['Nbkg_err'] = 0.29
data['S95_obs'] = 6.4
data['S95_exp'] = 3.6
data['p0'] = 0.04
res['SR'][SRname] = data

#-------------------#
SRname = '1b'
data = {}
data['Nobs'] = 7.
data['Nbkg'] = 4.5
data['Nbkg_err'] = 1.0
data['S95_obs'] = 8.8
data['S95_exp'] = 6.0
data['p0'] = 0.15
res['SR'][SRname] = data

#-------------------#
SRname = '3b'
data = {}
data['Nobs'] = 1.
data['Nbkg'] = 0.80
data['Nbkg_err'] = 0.25
data['S95_obs'] = 3.8
data['S95_exp'] = 3.7
data['p0'] = 0.36
res['SR'][SRname] = data



f = open('{ananame}.pickle'.format(ananame=ananame), 'w') 
pickle.dump(res, f)

