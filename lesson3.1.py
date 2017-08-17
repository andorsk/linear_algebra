import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
import math

from matrixoperations import *
ax = plt.gca()
#setup   
s = Helper.generateRandomBetween(-10,10)
perpframes = PerpFrames(s)
s = Helper.generateRandomBetween(-1.5,1.5)
perpframes2 = PerpFrames(s)

#get stretcher matrix
stretcher = Stretcher()
stretcher.setXYStretch(1, 1)
stretchMat = stretcher.getStretchMatrix()



lim = 0
if(max(plt.ylim() > max(plt.xlim()))):
	lim = max(plt.ylim())

x = np.linspace( -math.pi, math.pi, 1000)


line = []
for val in x:
    point = ShapeGenerator.generateLine(val, x = 4)
    line.append(point)
line = np.array(line).transpose()

circle = []
for val in x:
    point = ShapeGenerator.generateCircle(val, xorigin = 2, yorigin = 2)
    circle.append(point)
line = np.array(circle).transpose()


# drawVector(ax, 0, 1, 'orange')
Helper.drawVector(ax, 3 * perpframes.aligner[0,0], 3 * perpframes.aligner[0,1], 'blue')
Helper.drawVector(ax, - 3 * perpframes.aligner[0,0],-3* perpframes.aligner[0,1], 'blue')

Helper.drawVector(ax, perpframes.aligner[0,0], perpframes.aligner[0,1], 'orange')
Helper.drawVector(ax, perpframes.aligner[1,0], perpframes.aligner[1,1], 'orange')

# inverted Vector for reflection
pa = -1 * perpframes.aligner
Helper.drawVector(ax, pa[0,0], pa[0,1], 'green')
Helper.drawVector(ax, pa[1,0], pa[1,1], 'green')


plt.plot(line[0,], line[1,],  color = 'pink')

A = perpframes.aligner.dot(stretchMat.dot(pa.transpose())) 
line = A.dot(line)
plt.plot(line[0,], line[1,],  color = 'yellow')

plt.draw()

ax.set_aspect('equal')
ax.grid(True, which='both')
#show the graph

plt.show()