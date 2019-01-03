# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:08:29 2018

@author: ottil
"""

from shape import *
from pylab import random as r

class MovingShape(object):
    def __init__(self,frame,shape,diameter):
        self.x = 0
        self.y = 0
        self.dx = 5 + 10 * r()
        self.dy = 5 + 10 * r()
        self.shape = shape
        self.diameter = diameter
        self.ﬁgure = Shape(shape,diameter)
    def goto(self,x,y):
        self.ﬁgure.goto(self.x, self.y)
    def moveTick(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.goto(self.x, self.y) 

class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        

class Diamond(MovingShape):
     def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
        

class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
    
    
    
    
    