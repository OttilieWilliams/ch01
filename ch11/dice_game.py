# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:53:01 2018

@author: ottil
"""

 # Define a function game that:
 # Takes no arguments
 # Plays as many rounds as the user wants
 # Each round requires the user to enter 'odd', 'even', or 'quit'
 # The game then produces two dice values randomly between 1 and 6
 # and adds them together, and determines if the result is odd or even.
 # If the user correctly predicted the oddness or evenness it should 
 # print 'You win!' otherwise it should print 'Sorry, you lose!'
 # This should continue until the user types 'quit'.
 
from random import randint
def guess():
    number = randint(1,range)