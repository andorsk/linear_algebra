import numpy as np
import scipy as sc
import random as r
import math
import matplotlib.pyplot as plt

class Helper():
    
    @staticmethod
    def generateRandomBetween(a, b):
        return (r.random() * (b - a) + 1)

class PerpFrames():
    
    def __init__(self, s):
        self.alignerframe(s)
        self.alignerframe2(s)
        self.aligner = np.array([self.alignerframe, self.alignerframe2])
        self.hanger = np.array([self.alignerframe, self.alignerframe2]).transpose()

        
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
    def generateCircle(t):
        return np.array([math.sin(t) , math.cos(t)])
    
    def generateWaveForms(t):
        return np.array([math.cos(t),  math.sin(t)]); 
    
    def generateLine(t):
        return np.array([t, t]); 