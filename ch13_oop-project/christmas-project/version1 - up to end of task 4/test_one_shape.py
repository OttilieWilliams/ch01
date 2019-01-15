# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:17:22 2018

@author: ottil
"""
from MovingShapes import *

frame = Frame()
shape1 = Square(frame,100)
for i in range(100):
    shape1.moveTick() 
    

    
