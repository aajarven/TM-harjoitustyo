import matplotlib.pyplot as plt
import numpy as np

def lueMatriisi(tiedosto):
    f = open ( tiedosto , 'r')
    matriisi = [ map(float,line.split(',')) for line in f ] 
    return  np.array(matriisi)

def plottaaFunktio(xmin, xmax, kertoimet):
    pisteet = 100
    x = np.arange(xmin, xmax, (xmax-xmin)/pisteet)
    y = np.zeros(pisteet)

    for i in range(0, pisteet):
        for k in range(0, len(kertoimet)):
            y[i] += x[i]**k*kertoimet[k]
    plt.plot(x, y)
