# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:08:29 2018

@author: ottil
"""

from shape import *
import random

class MovingShape(object):
    def __init__(self,frame,shape,diameter):        
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 550)
        self.dx = random.randint(-15,15) 
        self.dy = random.randint(-15,15) 
        self.shape = shape
        self.diameter = diameter
        self.ﬁgure = Shape(shape,diameter)
    def goto(self,x,y):
        self.ﬁgure.goto(self.x, self.y)
    def moveTick(self):  
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        if self.x < 50:
            self.x = self.x - self.dx
        elif self.x > 750:
            self.x = self.x - self.dx
        elif self.y < 50:
            self.y = self.y - self.dy
        elif self.y > 550:
            self.y = self.y - self.dy
        else:
            pass
        
        self.figure.goto(self.x, self.y)

class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        

class Diamond(MovingShape):
     def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
        

class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
    
    
    
    
    