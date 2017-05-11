#!/usr/bin/env python
import sys, os, pickle
from collections import OrderedDict

ananame = 'atlas_conf_2016_096'
res = OrderedDict()

res['lumi'] = 13.3
res['ananame'] = ananame
res['SR'] = OrderedDict()

#-------------------#
SRname = '2lASF'
data = {}
data['Nobs'] =56.
data['Nbkg'] = 70.
data['Nbkg_err'] = 12.
data['S95_obs'] = 25.1
data['S95_exp'] = 35
data['p0'] = 0.17

res['SR'][SRname] = data

#-------------------#
SRname = '2lADF'
data = {}
data['Nobs'] = 55.
data['Nbkg'] = 57.6
data['Nbkg_err'] = 8.5
data['S95_obs'] = 25.1
data['S95_exp'] = 35
data['p0'] = 0.17

res['SR'][SRname] = data

#-------------------#


SRname = '2lBSF'
data = {}
data['Nobs'] = 19.
data['Nbkg'] = 20.7
data['Nbkg_err'] = 5.0
data['S95_obs'] = 16.5
data['S95_exp'] = 17.0
data['p0'] = 0.41

res['SR'][SRname] = data

#-------------------#
SRname = '2lBDF'
data = {}
data['Nobs'] = 8.
data['Nbkg'] = 8.5
data['Nbkg_err'] = 3.6
data['S95_obs'] = 16.5
data['S95_exp'] = 17.0
data['p0'] = 0.41

res['SR'][SRname] = data

#-------------------#


SRname = '2lCSF'
data = {}
data['Nobs'] = 9.
data['Nbkg'] = 10.2
data['Nbkg_err'] = 3.3
data['S95_obs'] = 11.6
data['S95_exp'] = 12.7
data['p0'] = 0.36

res['SR'][SRname] = data

#-------------------#
SRname = '2lCDF'
data = {}
data['Nobs'] = 2.
data['Nbkg'] = 3.1
data['Nbkg_err'] = 2.3
data['S95_obs'] = 11.6
data['S95_exp'] = 12.7
data['p0'] = 0.36

res['SR'][SRname] = data

#-------------------#

SRname = '3lI'
data = {}
data['Nobs'] = 2.
data['Nbkg'] = 4.41
data['Nbkg_err'] = 1.14
data['S95_obs'] = 3.7
data['S95_exp'] = 5.5
data['p0'] = 0.16

res['SR'][SRname] = data

#-------------------#
SRname = '3lH'
data = {}
data['Nobs'] = 0.
data['Nbkg'] = 0.98
data['Nbkg_err'] = 0.50
data['S95_obs'] = 3.0
data['S95_exp'] = 3.4
data['p0'] = 0.22

res['SR'][SRname] = data

#-------------------#




f = open('{ananame}.pickle'.format(ananame=ananame), 'wb') 
pickle.dump(res, f)
