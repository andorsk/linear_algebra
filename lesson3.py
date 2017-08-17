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
 
circle = []
for val in x:
    point = ShapeGenerator.generateCircle(val)
    circle.append(point)
circle = np.array(circle).transpose()

#draw a circle
plt.figure(figsize=(8,8))
plt.plot(circle[0,], circle[1,], 'ro', color = 'purple')

# #stretch the circle
stretched = stretchMat.dot(circle)
plt.plot(stretched[0,], stretched[1,], 'ro', color = 'blue')

#hang it
hung = perpframes2.hanger.dot(stretched)
plt.plot(hung[0,], hung[1,], 'ro', color = 'green')

#align it
aligned = perpframes.aligner.dot(stretched)
plt.plot(aligned[0,], aligned[1,], 'ro', color = 'orange')


#rescale graph to make sure x and y are the same height and width
ax = plt.gca()

lim = 0
if(max(plt.ylim() > max(plt.xlim()))):
	lim = max(plt.ylim())

#draw perp frames
def drawVector(ax, dim1, dim2, col = 'blue'):
    soa = np.array([[0, 0, dim1, dim2]])
    X, Y, U, V = zip(*soa)
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color = col) 


#draw vecotrs
#curtosy of https://stackoverflow.com/questions/12265234/how-to-plot-2d-math-vectors-with-matplotlib
drawVector(ax, perpframes.aligner[0,0], perpframes.aligner[0,1], 'orange')
drawVector(ax, perpframes.aligner[1,0], perpframes.aligner[1,1], 'orange')
drawVector(ax, perpframes.hanger[0,0], perpframes.hanger[0,1], 'green')
drawVector(ax, perpframes.hanger[1,0], perpframes.hanger[1,1], 'green')

plt.draw()
ax.set_ylim(-1 * lim, lim)
ax.set_xlim(-1 * lim, lim)
#show the graph
plt.show()