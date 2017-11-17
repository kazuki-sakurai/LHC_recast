#!/usr/bin/env python
import sys, os, pickle
from collections import OrderedDict

ananame = 'atlas_conf_2016_054'
res = OrderedDict()

res['lumi'] = 14.8 
res['ananame'] = ananame
res['SR'] = OrderedDict()

#-------------------#
## SRname = 'GG2J'
## data = {}
## data['Nobs'] = 47.
## data['Nbkg'] = 46.
## data['Nbkg_err'] = 7.
## data['S95_obs'] = 21.3
## data['S95_exp'] = 20.2
## data['p0'] = 0.41
## res['SR'][SRname] = data

#-------------------#
SRname = 'GG6J_bulk'
data = {}
data['Nobs'] = 32.
data['Nbkg'] = 24.
data['Nbkg_err'] = 5.
data['S95_obs'] = 22.1
data['S95_exp'] = 14.7
data['p0'] = 0.11
res['SR'][SRname] = data

## #-------------------#
## SRname = 'GG6J_high_mass'
## data = {}
## data['Nobs'] = 3.
## data['Nbkg'] = 3.8
## data['Nbkg_err'] = 1.2
## data['S95_obs'] = 5.1
## data['S95_exp'] = 5.5
## data['p0'] = 0.90
## res['SR'][SRname] = data

## #-------------------#
## SRname = 'GG4J_low-x'   
## data = {}
## data['Nobs'] = 4.
## data['Nbkg'] = 6.
## data['Nbkg_err'] = 1.6
## data['S95_obs'] = 5.5
## data['S95_exp'] = 6.6
## data['p0'] = 0.83
## res['SR'][SRname] = data

## #-------------------#
## SRname = 'GG4J_high-x'
## data = {}
## data['Nobs'] = 2.
## data['Nbkg'] = 3.4
## data['Nbkg_err'] = 0.9
## data['S95_obs'] = 4.2
## data['S95_exp'] = 5.2
## data['p0'] = 0.77
## res['SR'][SRname] = data

#-------------------#
## SRname = 'SS4J_x=1/2'
## data = {}
## data['Nobs'] = 6.
## data['Nbkg'] = 5.4
## data['Nbkg_err'] = 1.7
## data['S95_obs'] = 7.5
## data['S95_exp'] = 6.9
## data['p0'] = 0.4
## res['SR'][SRname] = data

## #-------------------#
## SRname = 'SS5J_x=1/2'
## data = {}
## data['Nobs'] = 8.
## data['Nbkg'] = 13.2
## data['Nbkg_err'] = 2.5
## data['S95_obs'] = 6.3
## data['S95_exp'] = 9.1
## data['p0'] = 0.88
## res['SR'][SRname] = data

## #-------------------#
## SRname = 'SS4J_low-x'
## data = {}
## data['Nobs'] = 8.
## data['Nbkg'] = 11.1
## data['Nbkg_err'] = 2.7
## data['S95_obs'] = 8.8
## data['S95_exp'] = 6.6
## data['p0'] = 0.18
## res['SR'][SRname] = data

## #-------------------#
## SRname = 'SS5J_high-x'
## data = {}
## data['Nobs'] = 7.
## data['Nbkg'] = 4.6
## data['Nbkg_err'] = 1.4
## data['S95_obs'] = 7.2
## data['S95_exp'] = 8.8
## data['p0'] = 0.91
## res['SR'][SRname] = data

f = open('{ananame}.pickle'.format(ananame=ananame), 'wb') 
pickle.dump(res, f)
