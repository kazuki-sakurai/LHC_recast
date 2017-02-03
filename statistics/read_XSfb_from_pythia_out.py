#!/usr/bin/env python
import sys, os

try:
    infile = sys.argv[1]
except:
    print 'imput error!!'
    print '[pythia output]'
    exit()

if not os.path.exists(infile):
    print infile, 'does not exist!!'
    exit()

for line in open(infile):
    #print line
    if len(line.split(' sum ')) == 2:
        xsmb = float(line.split()[7])
        xsfb = xsmb * 10**15 * 10**-3
print xsfb
