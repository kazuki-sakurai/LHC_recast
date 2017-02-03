#!/usr/bin/env python

###############################################################################

from __future__ import print_function
from __future__ import division

import os
import inspect

from scipy.weave import inline

###############################################################################


def MT2bl_wrapper(lepE, lepPx, lepPy, lepPz, 
                  b1E, b1Px, b1Py, b1Pz, 
                  b2E, b2Px, b2Py, b2Pz,
                  MET_x, MET_y):

    code = """
            double pl[4]  = { lepE, lepPx, lepPy, lepPz};  // El, plx, ply, plz,     (visible lepton)
            double pb1[4] = { b1E, b1Px, b1Py, b1Pz };  // Eb1, pb1x, pb1y, pb1z  (bottom on the same side as the visible lepton)
            double pb2[4] = { b2E, b2Px, b2Py, b2Pz };  // Eb2, pb2x, pb2y, pb2z  (other bottom, paired with the invisible W)
            double pmiss[3] = { 0., MET_x, MET_y };                  // <unused>, pmx, pmy     (missing pT)
            mt2bl_bisect::mt2bl mt2bl;
            mt2bl.set_momenta(pl, pb1, pb2, pmiss);
            return_val = mt2bl.get_mt2bl();
           """

    # Pass all Python arguments to C++
    frame = inspect.currentframe()
    args = inspect.getargvalues(frame)[0]

    lib_MT2bl = inline(code,args,
                    headers=['"MT2bl.h"'],                    
                    include_dirs=["Users/kazuki/Projects/lhc_recast/analyses/mT2_packages"],
                    verbose=0                    
                    )

    return lib_MT2bl


def MT2bl(lepE, lepPx, lepPy, lepPz, 
          b1E, b1Px, b1Py, b1Pz, 
          b2E, b2Px, b2Py, b2Pz,
          MET_x, MET_y):

    # Make argument list for MT2 function
    args = {'lepE': lepE, 'lepPx': lepPx, 'lepPy': lepPy, 'lepPz': lepPz, 
            'b1E': b1E, 'b1Px': b1Px, 'b1Py': b1Py, 'b1Pz': b1Pz, 
            'b2E': b2E, 'b2Px': b2Px, 'b2Py': b2Py, 'b2Pz': b2Pz,             
            'MET_x': MET_x, 'MET_y': MET_y}

    # Call wrapper function
    # print(args)
    return MT2bl_wrapper(**args)




def MT2_wrapper(m1, p1x, p1y, m2, p2x, p2y, MET_m, MET_x, MET_y):

    code = """
           mt2_bisect::mt2 mt2_event;;           

           double pa[3] = { m1, p1x, p1y };
           double pb[3] = { m2, p2x, p2y };
           double pmiss[3] = { 0, MET_x, MET_y };
           double mn    = MET_m;

           mt2_event.set_momenta(pa,pb,pmiss);
           mt2_event.set_mn(mn);
           //mt2_event.print();

           const double mt2 = mt2_event.get_mt2();
           // std::cout << endl << " mt2 = " << mt2 << std::endl;
           return_val = mt2;
           """

    # Pass all Python arguments to C++
    frame = inspect.currentframe()
    args = inspect.getargvalues(frame)[0]

    # print(args)

    lib_MT2 = inline(code,args,
                    headers=['"mt2_bisect.h"','"mt2_bisect_main.h"'],
                    include_dirs=["/Users/kazuki/Projects/lhco_analysis/mT2_packages"],
                    verbose=0
                    )

    return lib_MT2



def MT2(m1, p1x, p1y, m2, p2x, p2y, MET_m, MET_x, MET_y):

    # Make argument list for MT2 function
    args = {'m1': m1, 'p1x': p1x, 'p1y': p1y, 'm2': m2, 'p2x': p2x, 'p2y': p2y, 'MET_m': MET_m, 'MET_x': MET_x, 'MET_y': MET_y}

    # Call wrapper function
    #print(args)
    return MT2_wrapper(**args)

###############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
