from ModelBricks import *
from iminuit import *
from ROOT import *
from read_file import *
f = TFile("/scratch18/kazuki2/statistics/CMS-PAS-SUS-16-036_merged.root")

#sig = []    input, n'umero de sinal lista
## def funcion_diego(sig):
##     params, ary_s, ary_b, ary_d,cinv = read_file(sig)

##     manager = BinFitBox(params, ary_s, ary_b, ary_d,cinv)
##     manager.createFit()
##     manager.fit.migrad()
##     #manager.fit.hesse()
##     #manager.fit.minos()

##     chi2sb = manager.fit.get_fmin()['fval']
##     manager.Params["mu"].setVal(0)
##     manager.Params["mu"].constant = True
##     manager.createFit()
##     manager.fit.migrad()
##     chi2b = manager.fit.get_fmin()['fval']
##     chi_new = chi2sb - chi2b
##     return chi_new

def funcion_diego(sig):
    params, ary_s, ary_b, ary_d,cinv = read_file(sig)
    manager = BinFitBox(params, ary_s, ary_b, ary_d,cinv)
    manager.Params["mu"].setVal(1)
    manager.Params["mu"].constant = True

    manager.createFit()
    manager.fit.migrad()
    #manager.fit.hesse()
    #manager.fit.minos()
    chi2sb = manager.fit.get_fmin()['fval']
    manager.Params["mu"].setVal(0)
    
    manager.createFit()
    manager.fit.migrad()
    chi2b = manager.fit.get_fmin()['fval']
    chi_new = chi2sb - chi2b
    return chi_new



