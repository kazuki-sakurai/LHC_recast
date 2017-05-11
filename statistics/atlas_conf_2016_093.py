#!/usr/bin/env python
import sys, os, pickle
from collections import OrderedDict

ananame = 'atlas_conf_2016_093'
res = OrderedDict()

res['lumi'] = 14.8
res['ananame'] = ananame
res['SR'] = OrderedDict()

#-------------------#
SRname = 'C1C1'
data = {}
data['Nobs'] = 3.
data['Nbkg'] = 5.1
data['Nbkg_err'] = 2.0
data['S95_obs'] = 4.9
data['S95_exp'] = 4.9*0.41/0.33
data['p0'] = 0.28

res['SR'][SRname] = data

#-------------------#
SRname = 'C1N2'
data = {}
data['Nobs'] = 3.
data['Nbkg'] = 5.9
data['Nbkg_err'] = 2.1
data['S95_obs'] = 4.7
data['S95_exp'] = 4.7*0.43/0.32
data['p0'] = 0.22

res['SR'][SRname] = data

#-------------------#




f = open('{ananame}.pickle'.format(ananame=ananame), 'wb') 
pickle.dump(res, f)
