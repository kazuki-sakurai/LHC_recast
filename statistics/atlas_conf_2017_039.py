#!/usr/bin/env python
import sys, os, pickle
from collections import OrderedDict
from get_S95 import *

ananame = 'atlas_conf_2017_039'
res = OrderedDict()

res['lumi'] = 36.1
res['ananame'] = ananame
#res['SR'] = OrderedDict()
res['SRa'] = OrderedDict()
res['SRb'] = OrderedDict()
res['SRc'] = OrderedDict()
res['SRd'] = OrderedDict()
res['SRe'] = OrderedDict()


#-------------------# 
SRname = 'SFa'
data = {}
data['Nobs'] = 56.
data['Nbkg'] = 47.
data['Nbkg_err'] = 12.

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFb'
data = {}
data['Nobs'] = 28.
data['Nbkg'] = 25.
data['Nbkg_err'] = 5.

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFc'
data = {}
data['Nobs'] = 19.
data['Nbkg'] = 25.
data['Nbkg_err'] = 4.

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFd'
data = {}
data['Nobs'] = 13.
data['Nbkg'] = 14.
data['Nbkg_err'] = 7.

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFe'
data = {}
data['Nobs'] = 10.
data['Nbkg'] = 5.2
data['Nbkg_err'] = 1.4

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFf'
data = {}
data['Nobs'] = 6.
data['Nbkg'] = 1.9
data['Nbkg_err'] = 1.2

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFg'
data = {}
data['Nobs'] = 6.
data['Nbkg'] = 3.8
data['Nbkg_err'] = 1.9

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFh'
data = {}
data['Nobs'] = 0.
data['Nbkg'] = 3.1
data['Nbkg_err'] = 1.0

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFi'
data = {}
data['Nobs'] = 1.
data['Nbkg'] = 1.9
data['Nbkg_err'] = 0.9

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFj'
data = {}
data['Nobs'] = 3.
data['Nbkg'] = 1.6
data['Nbkg_err'] = 0.5

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFk'
data = {}
data['Nobs'] = 2.0
data['Nbkg'] = 1.5
data['Nbkg_err'] = 0.6

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFl'
data = {}
data['Nobs'] = 2.
data['Nbkg'] = 1.8
data['Nbkg_err'] = 0.8

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFm'
data = {}
data['Nobs'] = 7.
data['Nbkg'] = 2.6
data['Nbkg_err'] = 0.9

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFloose'
data = {}
data['Nobs'] = 153.
data['Nbkg'] = 133.
data['Nbkg_err'] = 22.

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'SFtight'
data = {}
data['Nobs'] = 9.
data['Nbkg'] = 9.8
data['Nbkg_err'] = 2.9

res['SRa'][SRname] = data
res['SRc'][SRname] = data
#-------------------# 
SRname = 'DFa'
data = {}
data['Nobs'] = 67.
data['Nbkg'] = 57.
data['Nbkg_err'] = 7.

res['SRa'][SRname] = data
#-------------------# 
SRname = 'DFb'
data = {}
data['Nobs'] = 5.
data['Nbkg'] = 9.6
data['Nbkg_err'] = 1.9

res['SRa'][SRname] = data
#-------------------# 
SRname = 'DFc'
data = {}
data['Nobs'] = 4.
data['Nbkg'] = 1.5
data['Nbkg_err'] = 1.6

res['SRa'][SRname] = data
#-------------------# 
SRname = 'DFd'
data = {}
data['Nobs'] = 2.
data['Nbkg'] = 0.6
data['Nbkg_err'] = 0.6

res['SRa'][SRname] = data
#-------------------# 
SRname = 'DF100'
data = {}
data['Nobs'] = 78.
data['Nbkg'] = 68.
data['Nbkg_err'] = 7.

res['SRa'][SRname] = data
#-------------------# 
SRname = 'DF150'
data = {}
data['Nobs'] = 11.
data['Nbkg'] = 11.5
data['Nbkg_err'] = 3.1

res['SRa'][SRname] = data
#-------------------# 
SRname = 'DF200'
data = {}
data['Nobs'] = 6.
data['Nbkg'] = 2.1
data['Nbkg_err'] = 1.9

res['SRa'][SRname] = data
#-------------------# 
SRname = 'DF300'
data = {}
data['Nobs'] = 2.
data['Nbkg'] = 0.6
data['Nbkg_err'] = 0.6

res['SRa'][SRname] = data
#-------------------# 
SRname = 'slepa'
data = {}
data['Nobs'] = 4.
data['Nbkg'] = 2.23
data['Nbkg_err'] = 0.79

res['SRb'][SRname] = data
#-------------------# 
SRname = 'slepb'
data = {}
data['Nobs'] = 3.
data['Nbkg'] = 2.79
data['Nbkg_err'] = 0.43

res['SRb'][SRname] = data
#-------------------# 
SRname = 'slepc'
data = {}
data['Nobs'] = 9.
data['Nbkg'] = 5.41
data['Nbkg_err'] = 0.93

res['SRb'][SRname] = data
#-------------------# 
SRname = 'slepd'
data = {}
data['Nobs'] = 0.
data['Nbkg'] = 1.42
data['Nbkg_err'] = 0.38

res['SRb'][SRname] = data
#-------------------# 
SRname = 'slepe'
data = {}
data['Nobs'] = 0.
data['Nbkg'] = 1.14
data['Nbkg_err'] = 0.23

res['SRb'][SRname] = data
#-------------------# 
SRname = 'int'
data = {}
data['Nobs'] = 2.
data['Nbkg'] = 4.1
data['Nbkg_err'] = 2.6
data['S95_obs'] = 0.
data['S95_exp'] = get_S95(4.1, 2.6)
data['p0'] = 0.

res['SRd'][SRname] = data
#-------------------#
SRname = 'high'
data = {}
data['Nobs'] = 0.
data['Nbkg'] = 1.6
data['Nbkg_err'] = 1.6
data['S95_obs'] = 0.
data['S95_exp'] = get_S95(1.6, 1.6)
data['p0'] = 0.

res['SRd'][SRname] = data
#-------------------#
SRname = 'low'
data = {}
data['Nobs'] = 11.
data['Nbkg'] = 4.2
data['Nbkg_err'] = 3.8
data['S95_obs'] = 0.
data['S95_exp'] = get_S95(4.2, 3.8)
data['p0'] = 0.

res['SRd'][SRname] = data

#-------------------#
SRname = 'WZ0Ja'
data = {}
data['Nobs'] = 21.
data['Nbkg'] = 21.74
data['Nbkg_err'] = 2.85

res['SRe'][SRname] = data

#-------------------#
SRname = 'WZ0Jb'
data = {}
data['Nobs'] = 1.
data['Nbkg'] = 2.68
data['Nbkg_err'] = 0.46

res['SRe'][SRname] = data

#-------------------#
SRname = 'WZ0Jc'
data = {}
data['Nobs'] = 2.
data['Nbkg'] = 1.56
data['Nbkg_err'] = 0.33

res['SRe'][SRname] = data

#-------------------#
SRname = 'WZ1Ja'
data = {}
data['Nobs'] = 1.
data['Nbkg'] = 2.21
data['Nbkg_err'] = 0.53

res['SRe'][SRname] = data

#-------------------#
SRname = 'WZ1Jb'
data = {}
data['Nobs'] = 3.
data['Nbkg'] = 1.82
data['Nbkg_err'] = 0.26

res['SRe'][SRname] = data

#-------------------#
SRname = 'WZ1Jc'
data = {}
data['Nobs'] = 4.
data['Nbkg'] = 1.26
data['Nbkg_err'] = 0.34

res['SRe'][SRname] = data

#-------------------#





f = open('{ananame}.pickle'.format(ananame=ananame), 'wb') 
pickle.dump(res, f)
f = open('{ananame}.pickle'.format(ananame=ananame), 'r') 
a = pickle.load( f)
