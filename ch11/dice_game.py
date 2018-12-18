# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:53:01 2018

@author: ottil
"""

 # Define a function game that:
 # Takes no arguments DONE
 # Plays as many rounds as the user wants NEED TO DO
 # Each round requires the user to enter 'odd', 'even', or 'quit' DONE
 # The game then produces two dice values randomly between 1 and 6-
 # and adds them together, and determines if the result is odd/ even.DONE
 # If the user correctly predicted the oddness or evenness it should 
 # print 'You win!' otherwise it should print 'Sorry, you lose!' DONE
 # This should continue until the user types 'quit'. NEED TO DO
 
from random import randint
def guess():
    number1 = randint(1,6)
    number2 = randint(1,6)
    result = number1+number2
    print('Play my game if you dare! Can you guess if my 2 secret numbers add up to an EVEN number or an ODD number?')
    guess = input('Please enter: odd, even, or quit ')
    print(number1, '+', number2, '=', result)
    if guess == 'even' and result % 2 == 0:
        print('You win!')
    elif guess == 'odd' and result % 1 ==0:
        print('You win!')
    elif guess == 'even' and result % 1 ==0:
        print('You lose!')
    elif guess == 'odd' and result % 2 ==0:
        print('You lose!')
    print('END OF GAME: thanks for playing!')
    