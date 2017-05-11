#!/usr/bin/env python
import sys, os, pickle
from collections import OrderedDict

ananame = 'atlas_conf_2016_037'
res = OrderedDict()

res['lumi'] = 13.2  #fb^-1   luminosity
res['ananame'] = ananame
res['SR'] = OrderedDict()

#-------------------#
SRname = '3L1'
data = {}
data['Nobs'] = 6.
data['Nbkg'] = 6.1
data['Nbkg_err'] = 2.2
data['S95_obs'] = 7.8
data['S95_exp'] = 7.6
data['p0'] = 0.5          #didn't find
res['SR'][SRname] = data

#-------------------#
SRname = '3L2'
data = {}
data['Nobs'] = 2.
data['Nbkg'] = 1.2
data['Nbkg_err'] = 0.5
data['S95_obs'] = 5.1
data['S95_exp'] = 4.0
data['p0'] = 0.5
res['SR'][SRname] = data

#-------------------#
SRname = '0b1'
data = {}
data['Nobs'] = 5.
data['Nbkg'] = 8.8
data['Nbkg_err'] = 2.9
data['S95_obs'] = 6.2
data['S95_exp'] = 7.9
data['p0'] = 0.5
res['SR'][SRname] = data

#-------------------#
SRname = '0b2'   
data = {}
data['Nobs'] = 0.
data['Nbkg'] = 1.6
data['Nbkg_err'] = 0.8
data['S95_obs'] = 3.2
data['S95_exp'] = 3.9
data['p0'] = 0.5
res['SR'][SRname] = data

#-------------------#
SRname = '1b'
data = {}
data['Nobs'] = 12.
data['Nbkg'] = 11.4
data['Nbkg_err'] = 2.8
data['S95_obs'] = 10.3
data['S95_exp'] = 9.7
data['p0'] = 0.5
res['SR'][SRname] = data

#-------------------#
SRname = '3b'
data = {}
data['Nobs'] = 2.
data['Nbkg'] = 1.6
data['Nbkg_err'] = 0.6
data['S95_obs'] = 4.9
data['S95_exp'] = 4.2
data['p0'] = 0.5
res['SR'][SRname] = data

#-------------------#
SRname = '1b-GG'
data = {}
data['Nobs'] = 2.
data['Nbkg'] = 1.7
data['Nbkg_err'] = 0.5
data['S95_obs'] = 4.8
data['S95_exp'] = 4.1
data['p0'] = 0.5
res['SR'][SRname] = data

#-------------------#
SRname = '1b-DD'
data = {}
data['Nobs'] = 12.
data['Nbkg'] = 12.0
data['Nbkg_err'] = 2.7
data['S95_obs'] = 9.9
data['S95_exp'] = 9.8
data['p0'] = 0.5
res['SR'][SRname] = data

#-------------------#
SRname = '3b-DD'
data = {}
data['Nobs'] = 4.
data['Nbkg'] = 1.9
data['Nbkg_err'] = 0.8
data['S95_obs'] = 7.4
data['S95_exp'] = 4.7
data['p0'] = 0.5
res['SR'][SRname] = data

f = open('{ananame}.pickle'.format(ananame=ananame), 'wb') 
pickle.dump(res, f)
