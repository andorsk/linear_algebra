import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
import math

from matrixoperations import *


#setup   
s = Helper.generateRandomBetween(-10,10)
perpframes = PerpFrames(s)
s = Helper.generateRandomBetween(-1.5,1.5)
perpframes2 = PerpFrames(s)

#get stretcher matrix
stretcher = Stretcher()
stretcher.setXYStretch(Helper.generateRandomBetween(2.2, 2.7), Helper.generateRandomBetween(.6, 1.6))
stretchMat = stretcher.getStretchMatrix()

#generate points
x = np.linspace( -math.pi, math.pi, 100)
 
pointmatrix = []
for val in x:
    point = ShapeGenerator.generateCircle(val)
    pointmatrix.append(point)
pointmatrix = np.array(pointmatrix).transpose()

#draw a circle
plt.figure(figsize=(8,8))
plt.plot(pointmatrix[0,], pointmatrix[1,], 'ro')

#stretch the circle
stretched = stretchMat.dot(pointmatrix)
plt.plot(stretched[0,], stretched[1,], 'ro', color = 'blue')

#hang it
hung = perpframes2.hanger.dot(stretched)
plt.plot(hung[0,], hung[1,], 'ro', color = 'green')

#align it
aligned = perpframes.hanger.dot(stretched)
plt.plot(aligned[0,], aligned[1,], 'ro', color = 'orange')

#draw perp frames

#rescale graph to make sure x and y are the same height and width

ax = plt.gca()

lim = 0
if(max(plt.ylim() > max(plt.xlim()))):
	lim = max(plt.ylim())


print("Max is " , lim)
ax.set_ylim(-1 * lim, lim)
ax.set_xlim(-1 * lim, lim)
# recompute the ax.dataLim

#show the graph
plt.show()