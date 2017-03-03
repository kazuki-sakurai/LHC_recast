#!/usr/bin/env python
import sys, os

def get_eff(ana_target, SR_list, eff_file):
    eff = {}
    ana, mode, sr_current = '', '', ''
    for line in open(eff_file):
        elems = line.split() 
        if len(elems) == 0: continue
        if elems[0] == 'Analysis:': ana = elems[1]
        if ana == ana_target:
            if len(elems) > 3:
                #print elems[3]
                if elems[3] in SR_list:
                    print elems[3]
                    sr_current = elems[3]
                    eff[sr_current] = float(elems[5])               
    return eff
