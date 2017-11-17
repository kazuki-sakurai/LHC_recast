#!/usr/bin/env python
import sys, os, pickle
from collections import OrderedDict

ananame = 'atlas_conf_2017_035'
res = OrderedDict()

res['lumi'] = 36.1
res['ananame'] = ananame
res['SR'] = OrderedDict()

#-------------------#       # We are using sigma95 instead of S95
SRname = 'lowMass'
data = {}
data['Nobs'] = 10.
data['Nbkg'] = 14.
data['Nbkg_err'] = 6.0
data['S95_obs'] = 0.26    
data['S95_exp'] = 0.31
data['p0'] = 0.5

res['SR'][SRname] = data

#-------------------#
SRname = 'highMass'
data = {}
data['Nobs'] = 5.
data['Nbkg'] = 3.7
data['Nbkg_err'] = 1.4
data['S95_obs'] = 0.20
data['S95_exp'] = 0.17
data['p0'] = 0.3

res['SR'][SRname] = data

#-------------------#




f = open('{ananame}.pickle'.format(ananame=ananame), 'wb') 
pickle.dump(res, f)
