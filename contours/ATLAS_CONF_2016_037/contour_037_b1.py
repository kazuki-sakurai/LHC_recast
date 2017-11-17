import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import cPickle

import os
shit = os.walk("/scratch18/kazuki2/result/037_b3") ## Directorio no q vai fozar
craps = shit.next()
i = 0
x = np.array([])
y = np.array([])
P = np.array([])
f = {}
for crap in craps[2]: ## o terceiro elmento da lista son os arquivos
    if 'ans' in crap: ##marqueinos coa extension ans para identificalos
        names = crap.split("_")
        x0 = float(names[1])
        y0 = float(names[4].replace('.eff', ''))

        if x0 > (y0 + 171):
             x = np.append(x, x0)
             y = np.append(y, y0)
             dc = cPickle.load(file("/scratch18/kazuki2/result/037_b3/"+crap))
             z = dc['atlas_conf_2016_037']['chi2_i']
             P = 1 - st.chi2.cdf(z,1)
             f[(x0,y0)] = P
      


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

for i in xrange(len(x_new)):
    for j in xrange(len(y_new)):

        if (x_new[i], y_new[j]) in f:
            Prob[i,j] = f[(x_new[i], y_new[j])]

level = np.arange(0.00, 0.9, 0.05)            

plt.figure(1)
G1 = plt.contour(x_new, y_new, Prob.transpose(), levels = level)
plt.clabel(G1, inline = 1, fontsize = 10)
plt.xlabel('Gluino mass (GeV)')
plt.ylabel('Neutralino mass (GeV)')
plt.title('037 (b) GqqC1wN2zN1')
plt.axis([700, 1700, 150, 1800])
plt.grid(True)
plt.show()

q = open('037_b.txt', 'w')
Pt = Prob.transpose()
for i in xrange(len(x_new)):
     for j in xrange(len(y_new)):
          q.write(str(x_new[i]) + '   ' + str(y_new[j]) + '   ' + str(Pt[i,j])+' \n')
