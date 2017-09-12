import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
import math
from matrixoperations import *
from numpy.linalg import inv
from mpl_toolkits.mplot3d import Axes3D
import random

#Play in off seperate .py file to get rotating shape.
fig = plt.figure(figsize=(10, 10))
subplt = fig.add_subplot(111,aspect='equal', projection = '3d')

#generate sphere
sphere = ShapeGenerator.generateSphere(xorigin = 0, yorigin = 0, zorigin =0)
sphere = np.array(sphere).transpose()
subplt.plot(sphere[:,0], sphere[:,1],sphere[:,2], color = 'pink')

#plot random points
idx = np.random.randint(2500, size=100)
sphere_points = sphere[idx,: ]
#subplt.scatter(sphere_points[:,0], sphere_points[:,1],sphere_points[:,2], color = 'red', marker= 'o')
  
hanger, stretcher, aligner,A  = Helper.generateRandom3DAMatrix()

Helper.draw3DVector(subplt, hanger[0][0], hanger[0][1], hanger[0][2], col = 'green')
Helper.draw3DVector(subplt, hanger[1][0], hanger[1][1], hanger[1][2], col = 'green')
Helper.draw3DVector(subplt, hanger[2][0], hanger[2][1], hanger[2][2], col = 'green')


Helper.draw3DVector(subplt, aligner[0][0], aligner[0][1], aligner[0][2], col = 'purple')
Helper.draw3DVector(subplt, aligner[1][0], aligner[1][1], aligner[1][2], col = 'purple')
Helper.draw3DVector(subplt, aligner[2][0], aligner[2][1], aligner[2][2], col = 'purple')

hit_sphere = sphere.dot(A)
subplt.plot(hit_sphere[:,0], hit_sphere[:,1],hit_sphere[:,2], color = 'yellow')
hit_sphere_pts = hit_sphere[idx,: ]
#subplt.scatter(hit_sphere_pts[:,0], hit_sphere_pts[:,1],hit_sphere_pts[:,2], color = 'blue', marker= 'o')

plt.show()