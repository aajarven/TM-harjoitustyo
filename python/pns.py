# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys
from utils import *

if len(sys.argv) !=5 :
    print ("Anna komentoriviargumentteina sovitettavan käyrän aste sekä tiedostot, joissa käytettävät matriisit X, Y ja W ovat")
    sys.exit(1)

aste = int(sys.argv[1])
xHavainto = lueMatriisi(sys.argv[2])
Y = lueMatriisi(sys.argv[3])
W = lueMatriisi(sys.argv[4])

X = np.ones((len(xHavainto), aste+1))
for i in range(0,len(xHavainto)):
    for j in range(1, aste+1):
        X[i][j] = xHavainto[i]**j

beta = np.dot(np.dot(np.dot(np.linalg.inv(np.dot(np.dot(np.transpose(X), W), X)), np.transpose(X)), W), Y)
print "kerroinmatriisi beta:"
print beta

xmin = np.amin(X[:,1])
xmax = np.amax(X[:,1])
ymin = np.amin(Y)
ymax = np.amax(Y)
pad = 0.2

plt.scatter(X[:,1], Y)
plottaaFunktio(xmin-pad, xmax+pad, beta)
axes = plt.gca()
axes.set_xlim([np.amin(X[:,1])-pad, np.amax(X[:,1])+pad])
axes.set_ylim([np.amin(Y)-pad, np.amax(Y)+pad])
plt.show()


