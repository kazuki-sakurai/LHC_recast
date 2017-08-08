import numpy as np
from timeit import default_timer as timer
import cPickle
from os import system as shell
from iminuit import *
#import pymultinest as mnest

def cuRead(thing, **kwargs): return SourceModule(file(thing,"r").read(), **kwargs)
def getName(par): return par.name

class Parameter:
    def __init__(self, name, var = 0, limits = (), stepsize = 0, constant = True, dtype = np.float64, blind_offset = 0., blind_sc = 1):
        self.name = name
        self.dtype = dtype
        self.setVal(var)
        self.limits = limits
        self.constant = constant
        self.blind_offset0 = blind_offset
        self.blind_sc0 = blind_sc
        if limits: self.autoStepSize()
        else: self.stepsize = stepsize
        if stepsize: self.stepsize = stepsize
    def setVal(self, var):
        self.default = self.dtype(var)
        self.fit_init = self.dtype(var)
        self.val = self.dtype(var)
    def BlindOffset(self): return (not self.constant)*self.blind_offset0
    def BlindScale(self): return (not self.constant)*self.blind_sc0
    def autoStepSize(self):
        self.stepsize = abs(self.limits[1]-self.limits[0])*1./10
    def setLimits(self,m,M, constant = False):
        if m > M:
            print self.name, " Warning: Upper Bound lower than lower bound. Reverting"
            m_ = M*1.
            M_ = m*1.
            m = m_
            M = M_
        self.limits = (m,M)
        self.constant = constant
        if m > self.fit_init or M < self.fit_init:
            print self.name, ": Init value not inside Boundaries, setting to ", 0.5*(M-m)
            self.fit_init = 0.5*(M-m)
        self.autoStepSize()
        
    def getSettings(self):
        out = {self.name: self.fit_init}
        if self.limits: out .update ({"limit_" + self.name: self.limits})
        if self.stepsize: out.update({"error_" + self.name: self.stepsize})
        if self.constant: out .update({"fix_" + self.name: True})
        return out

class Free(Parameter):
    def __init__(self, name, var = 0, limits = (), stepsize = 0, dtype = np.float64, blind_offset = 0, blind_sc = 1): Parameter.__init__(self, name, var = var, limits = limits, stepsize = stepsize, constant = False, dtype = dtype, blind_offset = blind_offset, blind_sc = 1)


class BinFitBox:
    def __init__(self, params, ary_s, ary_b, ary_d,cinv):
        self.params = params
        self.sig = ary_s
        self.bkg = ary_b
        self.dat = ary_d
        self.cinv = cinv
        self.func_code = Struct(
            co_varnames = map(getName, self.params),
            co_argcount = len(self.params)
            )
        self.dc = {}
        self.Params = {}
        for i in range(len(self.params)):
            self.dc[self.params[i].name] = i
            self.Params[self.params[i].name] = self.params[i]
        self.b = np.float64(len(self.sig)*[0]) 
        self.Nbins = len(self.sig)
    def freeThese(self, pars):
        for par in pars: self.Params[par].constant = False
    def lock_to_init(self, pars):
        for par in pars: self.Params[par].constant = True
        
    def __call__(self,*args):
        chi2 = np.float64(0.)
        N = self.dc
        mu = args[N["mu"]]
        for i in range(self.Nbins):
            stri = str(i)
            self.b[i] = np.float64(args[N["b_" + stri]])
        d = np.matrix(self.b - self.bkg)
        chi2b = np.float64((d*self.cinv*d.transpose())[0][0])
        chi2 += chi2b
        m = mu *self.sig + self.b
        if min(m) < 0:
            print "Negative expected events, asigning large chi2"
            return np.float64(1.e09)
        poissLL = sum(self.dat*np.log(m) - m)
        chi2 += -2*poissLL
        return chi2

 
    def createFit(self, **kwargs):
        config = {}
        for par in self.params: config.update(par.getSettings())
        config.update(kwargs)
        self.fit = Minuit(self, **config)
   
