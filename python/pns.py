# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys
from utils import *

if len(sys.argv) !=5 :
    print "Anna komentoriviargumentteina sovitettavan käyrän aste sekä tiedostot, joissa käytettävät matriisit X, Y ja W ovat"
    sys.exit(1)

aste = int(sys.argv[1])
xHavainto = lueMatriisi(sys.argv[2])
Y = lueMatriisi(sys.argv[3])
W = lueMatriisi(sys.argv[4])

if len(np.transpose(xHavainto)) == 1 : # jos annetussa X-matriisissa on vain yksi sarake, oletetaan n. asteen käyrä y=f(x) ja luodaan X-matriisi sen mukaan
    X = np.ones((len(xHavainto), aste+1))
    for i in range(0,len(xHavainto)):
        for j in range(1, aste+1):
            X[i][j] = xHavainto[i]**j
else : # muuten käytetään annettua sellaisenaan
    X = xHavainto

if len(X) != len(Y) or len(Y) != len(W):
    print "Annettujen matriisien dimensiot eivät täsmää"
    sys.exit(1)

beta = np.dot( np.dot( np.dot( np.linalg.inv( np.dot( np.dot( np.transpose(X), W), X)), np.transpose(X)), W), Y)
print "kerroinmatriisi beta:"
print beta
