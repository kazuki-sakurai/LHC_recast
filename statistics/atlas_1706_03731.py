#!/usr/bin/env python
import sys, os, pickle
from collections import OrderedDict

ananame = 'atlas_1706_03731'
res = OrderedDict()

res['lumi'] = 36.1  #fb^-1   luminosity
res['ananame'] = ananame
res['SR'] = OrderedDict()

#-------------------#
SRname = 'Rpc2L2bS'
data = {}
data['Nobs'] = 3.
data['Nbkg'] = 3.3
data['Nbkg_err'] = 1.0
data['S95_obs'] = 5.5
data['S95_exp'] = 5.6
data['p0'] = 0.71          
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc3L0bH'
data = {}
data['Nobs'] = 0.
data['Nbkg'] = 1.08
data['Nbkg_err'] = 0.32
data['S95_obs'] = 3.6
data['S95_exp'] = 3.9
data['p0'] = 0.91
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc2Lsoft1b'
data = {}
data['Nobs'] = 4.
data['Nbkg'] = 5.8
data['Nbkg_err'] = 2.5
data['S95_obs'] = 6.3
data['S95_exp'] = 7.1
data['p0'] = 0.69
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc2Lsoft2b'   
data = {}
data['Nobs'] = 5.
data['Nbkg'] = 3.8
data['Nbkg_err'] = 1.6
data['S95_obs'] = 7.7
data['S95_exp'] = 6.2
data['p0'] = 0.30
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc2L0bS'
data = {}
data['Nobs'] = 7.
data['Nbkg'] = 6.0
data['Nbkg_err'] = 1.8
data['S95_obs'] = 8.3
data['S95_exp'] = 7.5
data['p0'] = 0.36
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc2L0bH'
data = {}
data['Nobs'] = 3.
data['Nbkg'] = 2.4
data['Nbkg_err'] = 1.0
data['S95_obs'] = 6.1
data['S95_exp'] = 5.3
data['p0'] = 0.35
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc3L0bS'
data = {}
data['Nobs'] = 9.
data['Nbkg'] = 11.0
data['Nbkg_err'] = 3.0
data['S95_obs'] = 8.3
data['S95_exp'] = 9.3
data['p0'] = 0.72
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc3L0bH'
data = {}
data['Nobs'] = 3.
data['Nbkg'] = 3.3
data['Nbkg_err'] = 0.8
data['S95_obs'] = 5.4
data['S95_exp'] = 5.5
data['p0'] = 0.85
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc3L1bS'
data = {}
data['Nobs'] = 20.
data['Nbkg'] = 17.
data['Nbkg_err'] = 4.
data['S95_obs'] = 14.7
data['S95_exp'] = 12.6
data['p0'] = 0.32
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc3L1bH'
data = {}
data['Nobs'] = 4.
data['Nbkg'] = 3.9
data['Nbkg_err'] = 0.9
data['S95_obs'] = 6.1
data['S95_exp'] = 5.9
data['p0'] = 0.38
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc2L1bS'
data = {}
data['Nobs'] = 14.
data['Nbkg'] = 9.8
data['Nbkg_err'] = 2.9
data['S95_obs'] = 13.7
data['S95_exp'] = 10.0
data['p0'] = 0.17
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc2L1bH'
data = {}
data['Nobs'] = 13.
data['Nbkg'] = 9.8
data['Nbkg_err'] = 2.6
data['S95_obs'] = 12.4
data['S95_exp'] = 9.7
data['p0'] = 0.21
res['SR'][SRname] = data

#-------------------#
SRname = 'Rpc3LSS1b'
data = {}
data['Nobs'] = 1.
data['Nbkg'] = 1.6
data['Nbkg_err'] = 0.8
data['S95_obs'] = 3.9
data['S95_exp'] = 4.0
data['p0'] = 0.56
res['SR'][SRname] = data

f = open('{ananame}.pickle'.format(ananame=ananame), 'wb') 
pickle.dump(res, f)
