#!/usr/bin/env python
import sys, os, pickle
from collections import OrderedDict

ananame = 'atlas_1605_04285'
res = OrderedDict()

res['lumi'] = 3.2
res['ananame'] = ananame
res['SR'] = OrderedDict()

#-------------------#
SRname = '2js'
data = {}
data['Nobs'] = 2.
data['Nbkg'] = 3.6
data['Nbkg_err'] = 0.7
data['S95_obs'] = 4.3
data['S95_exp'] = 5.3
data['p0'] = 0.50


res['SR'][SRname] = data

#-------------------#
SRname = '5js'
data = {}
data['Nobs'] = 9.
data['Nbkg'] = 7.7
data['Nbkg_err'] = 1.9
data['S95_obs'] = 9.3
data['S95_exp'] = 8.1
data['p0'] = 0.34
res['SR'][SRname] = data

#-------------------#
SRname = '4jl'
data = {}
data['Nobs'] = 1.
data['Nbkg'] = 1.3
data['Nbkg_err'] = 0.5
data['S95_obs'] = 3.9
data['S95_exp'] = 4.1
data['p0'] = 0.50
res['SR'][SRname] = data

#-------------------#
SRname = '4jh'
data = {}
data['Nobs'] = 0.
data['Nbkg'] = 0.9
data['Nbkg_err'] = 0.5
data['S95_obs'] = 2.8
data['S95_exp'] = 2.9
data['p0'] = 0.50
res['SR'][SRname] = data

#-------------------#
SRname = '5jh'
data = {}
data['Nobs'] = 0.
data['Nbkg'] = 1.3
data['Nbkg_err'] = 0.6
data['S95_obs'] = 2.8
data['S95_exp'] = 3.5
data['p0'] = 0.50
res['SR'][SRname] = data

#-------------------#
SRname = '6jh'
data = {}
data['Nobs'] = 10.
data['Nbkg'] = 4.4
data['Nbkg_err'] = 1.0
data['S95_obs'] = 12.5
data['S95_exp'] = 6.5
data['p0'] = 0.02
res['SR'][SRname] = data



f = open('{ananame}.pickle'.format(ananame=ananame), 'wb') 
pickle.dump(res, f)
f = open('{ananame}.pickle'.format(ananame=ananame), 'r') 
c = pickle.load(f)

