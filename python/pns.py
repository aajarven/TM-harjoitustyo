# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

havaintoX = np.matrix('1; 2; 3; 4; 5')
Y = np.matrix('1.2; 2.5; 2.8; 4.5; 5.1')

X = np.zeros(shape=(5,2))

for i in range(0, 5):
	for j in range(0, 2):
		X[i][j] = havaintoX[i][0]**j

beta = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(X), X)),np.transpose(X)),Y)
print beta
print beta[0][0]

b = beta.item(0,0)
k = beta.item(1,0)

plt.scatter(np.array(havaintoX), np.array(Y))
plt.plot([0, 5], [b, b+5*k] )
axes = plt.gca()
axes.set_xlim([0,5])
axes.set_ylim([0,5])
plt.show()
