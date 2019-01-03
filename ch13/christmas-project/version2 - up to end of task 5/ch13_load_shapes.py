# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:35:59 2018

@author: ottil
"""
#FIRST OPTION

#import shape 
#
#frame = shape.Frame()
#s1 = shape.Shape('square',100)
#s1.goto(200,100)

#SECOND OPTION

from shape import *
import time

frame = Frame() # This creates an instance of the Frame
# class from the shape module and opens a graphics window 
#containing an outer'frame' line. 
s1 = Shape('square',100)
#s1.goto(200,100)

x = 0
y = 0

for i in range(100):
    s1.goto(x,y)
    x += 5
    y += 5
#    time.sleep(0.03)

