import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
import math

from matrixoperations import *

ax = plt.gca()
perpframes = PerpFrames(4)

#draw point and vector
plt.plot(2,4,'ro', color = 'red')
plt.plot([0,1,2,3,4,5], color = 'blue')

#set limits for axis
ax.grid(True, which='both')
ax.set_aspect('equal')

ax.set_xlim([0, 5])
ax.set_ylim([0, 5])

print(PerpFrames.createPerpFrame([8,3]))

plt.show()
