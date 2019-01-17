# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:08:29 2018

@author: ottil
"""

from shape import *
from pylab import random as r
import random

class MovingShape(object):
    def __init__(self,frame,shape,diameter): 
        
        self.diameter = diameter
        self.shape = shape
        self.ﬁgure = Shape(shape,diameter)
        
        # Variable to be used to stop shapes going beyond border
        self.minx = self.diameter/2
        self.maxx = frame.width - self.minx
        self.miny = self.diameter/2
        self.maxy = frame.height - self.miny
        
        # Starting positions for x and y
        self.x = random.randint(self.minx, self.maxx)
        self.y = random.randint(self.miny, self.maxy)
        
        #An alternative solution for the above code.
#        self.x = self.minx + r() * (self.maxx - self.minx) 
#        self.y = self.miny + r() * (self.maxy - self.miny)
        
        # Variable to determine velocity
        self.dx = 5 + 10 * r()
        self.dy = 5 + 10 * r()  
    
#        self.starting_direction()
#
#    def starting_direction():
#        if r() < 0.5:
#            self.dx = -self.dx
#            self.dy = -self.dy
#        else:
#            self.dx= self.dx
#            self.dy = self.dy
    
    def goto(self,x,y):
        self.ﬁgure.goto(self.x, self.y)
        
    def moveTick(self):
    # a list of ifs for if the shape hits one of the four walls.
        
        if self.x > self.maxx:
            self.dx = self.dx * -1
            
        if self.x < self.minx:
            self.dx = self.dx * -1
            
        if self.y > self.maxy:
            self.dy = self.dy * -1
            
        if self.y < self.miny:
            self.dy = self.dy * -1
           
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        
        self.ﬁgure.goto(self.x, self.y)
        

            
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        

class Diamond(MovingShape):
     def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
        self.minx = diameter #07/9
        self.miny = diameter #07/9
        self.maxx = frame.width - diameter #07/9
        self.maxy = frame.height- diameter #07/9
        self.x = self.minx + r() * (self.maxx - self.minx) #07/9
        self.y = self.miny + r() * (self.maxy - self.miny) #07/9
        self.goto(self.x, self.y)
        

class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
    
    
    
    
    