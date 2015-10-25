# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys
from utils import *

if len(sys.argv) !=5 :
    print ("Anna komentoriviargumentteina sovitettavan käyrän aste sekä tiedostot, joissa käytettävät matriisit X, Y ja W ovat")
    sys.exit(1)

X = lueMatriisi(sys.argv[2])
Y = lueMatriisi(sys.argv[3])
W = lueMatriisi(sys.argv[4])

#beta = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(X), X)),np.transpose(X)),Y)
beta = np.dot(np.dot(np.dot(np.linalg.inv(np.dot(np.dot(np.transpose(X), W), X)), np.transpose(X)), W), Y)
#print beta
#print beta[0][0]

b = beta.item(0,0)
k = beta.item(1,0)

xmin = np.amin(X[:,1])
xmax = np.amax(X[:,1])
ymin = np.amin(Y)
ymax = np.amax(Y)
pad = 0.2

plt.scatter(X[:,1], Y)
#plt.plot([xmin-pad, xmax+pad], [b+(ymin-pad)*k, b+(ymax+pad)*k] )
plottaaFunktio(xmin-pad, xmax+pad, beta)
axes = plt.gca()
axes.set_xlim([np.amin(X[:,1])-pad, np.amax(X[:,1])+pad])
axes.set_ylim([np.amin(Y)-pad, np.amax(Y)+pad])
plt.show()


