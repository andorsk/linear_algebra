import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import math
from matrixoperations import *
from numpy.linalg import inv

#get unit vector from line directionvector/Sqrt[directionvector . directionvector]
# ax = plt.gca()
aligner_perp = PerpFrames(math.pi * (1/4))
hanger_perp = PerpFrames(math.pi * (5/3) )

circle = ShapeGenerator.generateCircle(xorigin = 0, yorigin = 0)
circle = np.array(circle).transpose()


fig = plt.figure(figsize=(10, 10))
subplt = fig.add_subplot(111,aspect='equal')

#draw point 
Helper.drawVector(subplt,aligner_perp.aligner[0][0], aligner_perp.aligner[0][1], 'orange')
Helper.drawVector(subplt,aligner_perp.aligner[1][0], aligner_perp.aligner[1][1], 'orange')
Helper.drawVector(subplt,hanger_perp.aligner[0][0], hanger_perp.aligner[0][1], 'orange')
Helper.drawVector(subplt,hanger_perp.aligner[1][0], hanger_perp.aligner[1][1], 'orange')

#draw axis
Helper.drawVector(subplt,0, 4, 'red')
Helper.drawVector(subplt,4, 0, 'red')
Helper.drawVector(subplt,0, -4, 'red')
Helper.drawVector(subplt,-4, 0, 'red')

#Create stretcher direction 1 perp 0 perp2
s = Stretcher(1.8, .7)
A = (s.mat).dot(hanger_perp.hanger)
s = Stretcher(1.2, .7)
B = (s.mat).dot(aligner_perp.hanger)

subplt.plot(circle[:,0], circle[:,1],  color = 'yellow')
original_circle = circle
circle = circle.dot(A)
circle_new = circle.dot(B)

#work backward
circle_mid = circle.dot(inv(A)).dot(B)

subplt.plot(circle[:,0], circle[:,1],  color = 'green')
subplt.plot(circle_new[:,0], circle_new[:,1],  color = 'brown')
subplt.plot(circle_mid[:,0], circle_mid[:,1],  color = 'purple')

lim = 4
subplt.set_xlim([-1 * lim, lim])
subplt.set_ylim([-1 * lim, lim])
plt.show()

fig1 = plt.figure()

def update_plot(num, data, line):
	d = data[num]
	line.set_data(d[...,:])
	return line,
    

data = [original_circle.transpose(), circle.transpose(), circle_mid.transpose(), circle_new.transpose()]

sphere = ShapeGenerator.generateSphere(xorigin = 0, yorigin = 0, zorigin=0)
sphere = np.array(sphere).transpose()


l, = plt.plot([], [], 'r-')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel('x')
plt.title('Test')
line_ani = animation.FuncAnimation(fig1, update_plot, 2, fargs=(data, l),
                                   interval=1000, blit=True)



plt.show()