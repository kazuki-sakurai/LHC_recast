#!/usr/bin/env python

import sys, os, math
from math import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as cls
from scipy.interpolate import interp1d

ananame = 'atlas_1602_09058'
sms_topo = r'$\tilde g  \to tt \tilde \chi^0_1 $'
#sms_topo = r'$\tilde \chi ^{\pm}_1 \to ??$'

plot_name = '1602_09058_d.pdf'
infile = '1602_09058_d.txt'

# load data
data = np.loadtxt(infile)
#yar, xar, zar = data.transpose()
xar, yar, zar, zp, zn = data.transpose()

# kinematical constraint
cond = np.where( xar > yar + 2*172 )
xar = xar[cond]        
yar = yar[cond]        
zar = zar[cond]
zp = zp[cond]
zn = zn[cond]

###################################################################################
###################################################################################
###################################################################################
###################################################################################

# declare plot
fig = plt.figure()
ax = fig.add_subplot(111) 

# plot size
fig.subplots_adjust(bottom=0.13, right=0.97, top=0.95, left=0.15)
# axes labels
#ax.set_xlabel(r'$m_{\tilde g} [\rm GeV]$', fontsize=23)
#ax.set_ylabel(r'$m_{\tilde \chi_1^0} [\rm GeV]$', fontsize=23)
ax.set_xlabel(r'$m_{\tilde g} [\rm GeV]$', fontsize=23)
ax.set_ylabel(r'$m_{\tilde \chi_1^0} [\rm GeV]$', fontsize=23)
# axes ranges
ax.set_xlim([min(xar)*0.5, max(xar)*1.05])
ax.set_ylim([min(yar)*0.9, max(yar)*1.05])

# ticks font
plt.xticks(fontsize = 14) 
plt.yticks(fontsize = 14) 

 
obs0 = np.loadtxt('1602_09058_d_obs.dat', delimiter=',').transpose()
obsup = np.loadtxt('1602_09058_d_obsSup.dat', delimiter=',').transpose()
obsdw = np.loadtxt('1602_09058_d_obsInf.dat', delimiter=',').transpose()

lw_exp_0 = 2.5
lw_exp_er = 2.
op = 1.
c_exp = 'dodgerblue'
#c_exp = 'b'
ax.plot(obs0[0], obs0[1], lw=lw_exp_0, ls='-', c=c_exp, alpha=op)
ax.plot(obsup[0], obsup[1], lw=lw_exp_er, ls='--', c=c_exp, alpha=op)
ax.plot(obsdw[0], obsdw[1], lw=lw_exp_er, ls='--', c=c_exp, alpha=op)



# scatter plot
sc = ax.scatter(xar, yar, s=30, c=zar, norm=cls.LogNorm(), lw=1, marker='o', alpha=0.7, rasterized=False)    
# color bar
cb = plt.colorbar(sc)        

# chi2 = 0.05 contour
lw_0 = 3.5
lw_er = 2.5

levels = [0.05]
ax.tricontour(xar,yar,zar,  levels, linewidths=lw_0, colors='r', linestyles='-')
ax.tricontour(xar,yar,zp,  levels, linewidths=lw_er, colors='r', linestyles='--')
ax.tricontour(xar,yar,zn,  levels, linewidths=lw_er, colors='r', linestyles='--')

# texting chi2 values 
## for i in xrange(len(xar)):
##     ax.text(xar[i], yar[i], '{zval}'.format(zval=zar[i]), fontsize=3, rotation=20)

# diagonal lines
#ax.plot([0,3000],[0,3000],lw=1,c='gray')
#ax.fill_between([0,3000], [0,3000], [3000,3000], lw=1, hatch='xxx', facecolor='', edgecolor="k")
#ax.fill_between([0,3000], [0,3000], [3000,3000], lw=1, alpha=0.3, facecolor='gray')
ax.fill_between([0,3000], [-2*172,3000 - 2*172], [3000,3000], lw=1, alpha=0.3, facecolor='gray')
#ax.fill_between([0,3000], 200, 300)

# legend
xwid = (max(xar) - min(xar))
ywid = (max(yar) - min(yar))
x0 = min(xar) - 0.01*xwid
y0 = min(yar) + 0.95*ywid
ax.text(x0, y0, ananame, fontsize=13)
y1 = y0 - 0.08*ywid
ax.text(x0, y1, sms_topo, fontsize=13)
y2 = y1 - 0.08*ywid
x1 = x0 + 0.1*xwid
ax.plot([x0,x1],[y2,y2],lw=lw_exp_0-0.5,c='r')
dy = 0.02*ywid
ax.plot([x0,x1],[y2+dy,y2+dy],lw=lw_exp_er-0.5,ls='--',c='r')
ax.plot([x0,x1],[y2-dy,y2-dy],lw=lw_exp_er-0.5,ls='--',c='r')
x2 = x1 + 0.03*xwid
ax.text(x2, y2*0.99, 'LHC_recast w. MC-err', fontsize=13)

y2 = y2 - 0.09*ywid
ax.plot([x0,x1],[y2,y2],lw=lw_exp_0,c=c_exp)
dy = 0.02*ywid
ax.plot([x0,x1],[y2+dy,y2+dy],lw=lw_exp_er,ls='--',c=c_exp)
ax.plot([x0,x1],[y2-dy,y2-dy],lw=lw_exp_er,ls='--',c=c_exp)
x2 = x1 + 0.03*xwid
ax.text(x2, y2*0.99, 'ATLAS w. theo-err', fontsize=13)

##########################################

tag = infile.split('.')[0]
fig.savefig(plot_name)
print plot_name
plt.show()

#exit()
