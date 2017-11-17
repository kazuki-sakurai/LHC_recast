import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import cPickle

import os
shit = os.walk("/scratch18/kazuki2/result/cms_1705_04650_h") ## Directorio no q vai fozar
craps = shit.next()
i = 0
x = np.array([])
y = np.array([])
P = np.array([])
Ppos = np.array([])
Pneg = np.array([])
f = {}
fpos = {}
fneg = {}
for crap in craps[2]: ## o terceiro elmento da lista son os arquivos
    if 'ans' in crap: ##marqueinos coa extension ans para identificalos
        names = crap.split("_")
        x0 = float(names[1])
        y0 = float(names[3].replace('.eff', ''))

        if x0 >= (y0):
             x = np.append(x, x0)
             y = np.append(y, y0)
             x = np.append(x, x0)
             y = np.append(y, y0)
             dc = cPickle.load(file("/scratch18/kazuki2/result/cms_1705_04650_h/"+crap))
             z = dc['cms_1705_04650']['chi2_i']
             sigPos = dc['cms_1705_04650']['chi2_i_+1sig']
             sigNeg = dc['cms_1705_04650']['chi2_i_-1sig']
             P = 1 - st.chi2.cdf(z,1)
             Ppos = 1 - st.chi2.cdf(sigPos, 1)
             Pneg = 1 - st.chi2.cdf(sigNeg, 1)
             f[(x0,y0)] = P
             fpos[(x0, y0)] = Ppos
             fneg[(x0, y0)] = Pneg
      

x_new = []
y_new = []

for i in x:
     if i not in x_new:
         x_new.append(i)

for i in y:
    if i not in y_new:
        y_new.append(i)
        
x_new.sort()
y_new.sort()
Prob = np.zeros([len(x_new), len(y_new)])
ProbPos = np.zeros([len(x_new), len(y_new)])
ProbNeg = np.zeros([len(x_new), len(y_new)])

for i in xrange(len(x_new)):
    for j in xrange(len(y_new)):

        if (x_new[i], y_new[j]) in f:
            Prob[i,j] = f[(x_new[i], y_new[j])]
            ProbPos[i,j] = fpos[(x_new[i], y_new[j])]
            ProbNeg[i,j] = fneg[(x_new[i], y_new[j])]

level = np.arange(0.00, 0.9, 0.05)            

plt.figure(1)
G1 = plt.contour(x_new, y_new, Prob.transpose(), levels = level)
#G2 = plt.contour(x_new, y_new, ProbPos.transpose(), levels = level)
#G3 = plt.contour(x_new, y_new, ProbNeg.transpose(), levels = level)
plt.clabel(G1, inline = 1, fontsize = 10)
#plt.clabel(G2, inline = 1, fontsize = 10)
#plt.clabel(G3, inline = 1, fontsize = 10)
plt.xlabel('Squark mass (GeV)')
plt.ylabel('Neutralino mass (GeV)')
plt.title('T1bC1wN1 CMS_1705_04650 ')
plt.axis([300, 1200, 0, 1200])
plt.grid(True)
plt.show()

q = open('cms_1705_04650_h.txt', 'w')
Pt = Prob.transpose()
PtPos = ProbPos.transpose()
PtNeg = ProbNeg.transpose()
for i in xrange(len(x_new)):
     for j in xrange(len(y_new)):
          q.write(str(x_new[i]) + '   ' + str(y_new[j]) + '   ' + str(Pt[j,i]) + '   ' + str(PtPos[j,i]) + '   ' + str(PtNeg[j,i]) + ' \n')
q.close()
