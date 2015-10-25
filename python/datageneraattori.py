# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

pisteita = 100
xmin = -1
xmax = 4

X = np.zeros(pisteita)
Y = np.zeros(pisteita)
W = np.identity(pisteita)

fX = open('X-05txt', 'w')
fY = open('Y-05.txt', 'w')
fW = open('W-05.txt', 'w')

for i in range(0, pisteita):
    X[i] = xmin + i*(1.0*(xmax-xmin)/pisteita)
    Y[i]=1.5*X[i]**3-5*X[i]**2+3*X[i]+1.5+np.random.normal(0, .5)
    fX.write(str(X[i])+'\n')
    fY.write(str(Y[i])+'\n')
    for j in range(0, pisteita):
        fW.write(str(W[i][j]))
        if j < pisteita-1 :
            fW.write(',')
    fW.write('\n')

plt.scatter(X, Y)
plt.show()




