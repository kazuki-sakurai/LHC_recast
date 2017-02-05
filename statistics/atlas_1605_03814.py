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
data['S95_obs'] = 44.
data['S95_exp'] = 54.
data['p0'] = 0.5
data['Nbkg_err'] = 24.

res['SR'][SRname] = data

#-------------------#
SRname = '2jm'
data = {}
data['Nobs'] = 191.
data['Nbkg'] = 191.
data['Nbkg_err'] = 21.
data['S95_obs'] = 48.
data['S95_exp'] = 48.
data['p0'] = 0.5
res['SR'][SRname] = data

#-------------------#
SRname = '2jt'
data = {}
data['Nobs'] = 26.
data['Nbkg'] = 23.
data['Nbkg_err'] = 4.
data['S95_obs'] = 17.
data['S95_exp'] = 14.
data['p0'] = 0.4
res['SR'][SRname] = data

#-------------------#
SRname = '4jt'
data = {}
data['Nobs'] = 7.
data['Nbkg'] = 4.6
data['Nbkg_err'] = 1.1
data['S95_obs'] = 8.7
data['S95_exp'] = 6.3
data['p0'] = 0.17
res['SR'][SRname] = data

#-------------------#
SRname = '5j'
data = {}
data['Nobs'] = 7.
data['Nbkg'] = 13.2
data['Nbkg_err'] = 2.2
data['S95_obs'] = 5.4
data['S95_exp'] = 8.7
data['p0'] = 0.5
res['SR'][SRname] = data

#-------------------#
SRname = '6jm'
data = {}
data['Nobs'] = 5
data['Nbkg'] = 6.9
data['Nbkg_err'] = 1.5
data['S95_obs'] = 5.4
data['S95_exp'] = 6.6
data['p0'] = 0.5
res['SR'][SRname] = data

#-------------------#
SRname = '6jt'
data = {}
data['Nobs'] = 3
data['Nbkg'] = 4.2
data['Nbkg_err'] = 1.2
data['S95_obs'] = 5.0
data['S95_exp'] = 5.7
data['p0'] = 0.5
res['SR'][SRname] = data

f = open('{ananame}.pickle'.format(ananame=ananame), 'wb') 
pickle.dump(res, f)

