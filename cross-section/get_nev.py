#!/usr/bin/env python

import sys, os

xsec = float(sys.argv[1])
lumi = float(sys.argv[2])
nev_cut = int(sys.argv[3])

nev_min = xsec * lumi * 5.
nev = max(nev_cut, nev_min)

print int(nev)

