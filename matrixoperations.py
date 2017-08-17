import numpy as np
import scipy as sc
import random as r
import math
import matplotlib.pyplot as plt

class Helper():
    
    @staticmethod
    def generateRandomBetween(a, b):
        return (r.random() * (b - a) + 1)

    @staticmethod
    def drawVector(ax, dim1, dim2, col = 'blue'):
        soa = np.array([[0, 0, dim1, dim2]])
        X, Y, U, V = zip(*soa)
        ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color = col) 

    @staticmethod
    def getUnitVector(vector):
        return (vector / math.sqrt(vetor.dot(vector)))


class PerpFrames():
    
    def __init__(self, s):
        self.alignerframe(s)
        self.alignerframe2(s)
        self.aligner = np.array([self.alignerframe, self.alignerframe2])
        self.hanger = np.array([self.alignerframe, self.alignerframe2]).transpose()

    @staticmethod
    def createPerpFrame(perpframe1):
        if(len(perpframe1) != 2):
            print("Please return the correct perp frame: ", perpframe1)
            return
        perpframe2 = [-1 * perpframe1[1], perpframe1[0]]
        return np.array([perpframe1, perpframe2])

        
    def alignerframe(self, s):
        self.alignerframe = np.array([math.cos(s), math.sin(s)])
        
    
    def alignerframe2(self, s):
        self.alignerframe2 = np.array([math.cos(s + (math.pi / 2)),math.sin(s + (math.pi/2))])
        

class Stretcher():
    
    def setXYStretch(self, xstretch, ystretch):
        self.setXStretch(xstretch)
        self.setYStretch(ystretch)
        
    def setXStretch(self, xstretch):
        self.checkValid(xstretch)
        self.xstretch = xstretch
        
    def setYStretch(self, ystretch):
        self.checkValid(ystretch)
        self.ystretch = ystretch
        
    def getStretchMatrix(self):
        return np.array([[self.xstretch, 0], [0, self.ystretch]])
        
    def checkValid(self, num):
         try:
           val = float(num)
         except ValueError:
           print(num , " is invalid. Please choose a number. ")
           exit()
            
class ShapeGenerator():
    # 1 = x^2 - y^2 - y^2 = 1 - x^2 y = sqrt(1-x^2)
    def generateCircle(t, xorigin=0, yorigin=0):
        return np.array([math.sin(t) + xorigin , math.cos(t) + yorigin])
    
    def generateWaveForms(t):
        return np.array([math.cos(t),  math.sin(t)]) 
   
    def generateLine(t, x = 1):
        return np.array([t, t * x])
