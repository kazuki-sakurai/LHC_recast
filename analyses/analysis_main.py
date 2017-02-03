#!/usr/bin/env python

import sys, os, gzip
import ROOT
from LHCO_reader import LHCO_reader
from objects import *
from atlas_1605_03814 import * 

a = Structure()

inFiles = sys.argv
inFiles.pop(0)

atlas_1605_03814 = atlas_1605_03814()

#########################################
#    Event Loop
#########################################
iev = 0
for inFile in inFiles:

    if not os.path.exists(inFile):
        print inFile, 'does not exist!!'
        exit()

    events = LHCO_reader.Events(f_name = os.path.join(inFile))
    print events
    
    for event in events:

        iev += 1
        base_objects = get_base_objects(event)
        atlas_1605_03814.event_analysis(base_objects)        

#########################################
#    Output
#########################################
atlas_1605_03814.write_result(iev)
