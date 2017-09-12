import numpy as np
import scipy as sc
import random as r
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import svd

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
    def draw3DVector(ax, dim1, dim2, dim3, col='blue'):
        soa = np.array([[0, 0, 0, dim1, dim2, dim3]])
        X, Y, Z, U, V, W = zip(*soa)
        ax.quiver(X, Y, Z, U, V, W, color = col) 

    @staticmethod
    def getUnitVector(vector):
        return (vector / math.sqrt(vetor.dot(vector)))

    @staticmethod
    def generateRandomAMatrix():
        r = Helper.generateRandomBetween( -1 * math.pi/4,math.pi/4)
        r1 = Helper.generateRandomBetween(-1 * math.pi/4,math.pi/4)
        s = Stretcher(Helper.generateRandomBetween(0,2), Helper.generateRandomBetween(0,2))
        aligner = PerpFrames(r).aligner
        hanger = PerpFrames(r1).hanger
        A = hanger.dot(s.mat.dot(aligner))
        return hanger, s, aligner, A

    @staticmethod
    def generateRandom3DAMatrix():
        A = np.random.rand(3,3)
        U,s,V = np.linalg.svd(A, full_matrices=True)
        return U, s, V, A

class PerpFrames():
    
    def __init__(self, r, s, t = None):
        self.alignerframe(s)
        if(t is not None):
            self.alignerframe3d(r, s, t)


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


    @staticmethod
    def create3DPerpFrame(perpframe1):
        if(len(perpframe1) != 3):
            print("Please return the correct perp frame: ", perpframe1)
            return
        perpframe2 = [-1 * perpframe1[1], perpframe1[0]]
        return np.array([perpframe1, perpframe2])

        
    def alignerframe(self, s):
        self.alignerframe = np.array([math.cos(s), math.sin(s)])
        
    
    def alignerframe2(self, s):
        self.alignerframe2 = np.array([math.cos(s + (math.pi / 2)),math.sin(s + (math.pi/2))])
    
    #TODO: merge with normal aligner frame
    def alignerframe3d(self, r, s, t):
        self.alignerframe3d = ((math.cos(r) * math.cos(t)) - (math.cos(s) * math.sin(r) * math.sin(t)), (math.cos(s) + math.cos(t) * math.sin(r)) + (math.cos(r) * math.sin(t)), math.sin(r) * math.sin(s))



class Stretcher():

    def __init__(self, xstretch = 1, ystretch = 1, zstretch = 1):
        self.setXYStretch(xstretch, ystretch, zstretch)
    
    def setXYStretch(self, xstretch, ystretch, zstretch):
        self.setXStretch(xstretch)
        self.setYStretch(ystretch)
        if(zstretch != None):
            self.setZStretch(zstretch)
        self.mat = self.getStretchMatrix()
        
    def setZStretch(self, zstretch):
        self.checkValid(zstretch)
        self.zstretch = zstretch

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

    def generateSphere(xorigin=0, yorigin = 0, zorigin=0, radius = 1):
        x = np.linspace(-1 * math.pi, math.pi, 50)
        y = np.linspace(-1 * math.pi, math.pi, 50)

        sphere = []
        for xval in x:
            for yval in y:
                point = ShapeGenerator.sphereEq(xval, yval, xorigin = xorigin, yorigin = yorigin)
                sphere.append(radius * point)
        return np.array(sphere).transpose()

    def generateCircle(xorigin=0, yorigin = 0,radius = 1):
        x = np.linspace(-1 * math.pi, math.pi, 1000)
        circle = []
        for val in x:
            point = ShapeGenerator.circleEq(val, xorigin = xorigin, yorigin = yorigin)
            circle.append(radius * point)
        return np.array(circle).transpose()

    def circleEq(t, xorigin=0, yorigin=0):
        return np.array([math.sin(t) + xorigin , math.cos(t) + yorigin])
    
    def sphereEq(r,t, xorigin=0, yorigin=0, zorigin = 0):
        return np.array([math.sin(r) * math.cos(t) + xorigin , math.sin(r)  * math.sin(t) + yorigin, math.cos(r) + zorigin])
    
    def generateWaveForms(t):
        return np.array([math.cos(t),  math.sin(t)]) 
   
    def generateLine(t, x = 1):
        return np.array([t, t * x])
