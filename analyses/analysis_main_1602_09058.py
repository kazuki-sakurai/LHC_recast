#!/usr/bin/env python

import sys, os, gzip
import ROOT
from LHCO_reader import LHCO_reader
from objects import *
## from atlas_1605_03814 import * 
from atlas_1602_09058 import *
## from atlas_1605_04285 import *
## #from atlas_conf_2016_093 import *
## from atlas_conf_2016_096 import *
## from atlas_conf_2016_054 import *
## from atlas_conf_2016_037 import *
## from atlas_1706_03731 import *

a = Structure()

inFiles = sys.argv
inFiles.pop(0)

## atlas_1605_03814 = atlas_1605_03814()
atlas_1602_09058 = atlas_1602_09058()
## atlas_1605_04285 = atlas_1605_04285()
## #atlas_conf_2016_093 = atlas_conf_2016_093()
## atlas_conf_2016_096 = atlas_conf_2016_096()
## atlas_conf_2016_054 = atlas_conf_2016_054()
## atlas_conf_2016_037 = atlas_conf_2016_037()
## atlas_1706_03731 = atlas_1706_03731()


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
    print len(events)
    for event in events:

        iev += 1
        base_objects = get_base_objects(event)
        base_objects_wtaus = get_base_objects(event,add_taus = 1)

        ## atlas_1605_03814.event_analysis(base_objects)
        atlas_1602_09058.event_analysis(base_objects)
        ## atlas_1605_04285.event_analysis(base_objects)
        ## #atlas_conf_2016_093.event_analysis(base_objects_wtaus)
        ## atlas_conf_2016_096.event_analysis(base_objects)
        ## atlas_conf_2016_054.event_analysis(base_objects)
        ## atlas_conf_2016_037.event_analysis(base_objects)
        ## atlas_1706_03731.event_analysis(base_objects)
    
#########################################
#    Output
#########################################
## atlas_1605_03814.write_result(iev)
atlas_1602_09058.write_result(iev)
## atlas_1605_04285.write_result(iev)
## #atlas_conf_2016_093.write_result(iev)
## atlas_conf_2016_096.write_result(iev)
## atlas_conf_2016_054.write_result(iev)
## atlas_conf_2016_037.write_result(iev)
## atlas_1706_03731.write_result(iev)
