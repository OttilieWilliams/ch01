# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:37:06 2018

@author: ottil
"""

# Adding in the while loop and a break when the player enters 'quit'
 
from random import randint
def guess():
    print('Play my game if you dare! Can you guess if my 2 secret numbers add up to an EVEN number or an ODD number?')
    while True:
        number1 = randint(1,6)
        number2 = randint(1,6)
        result = number1 + number2
        guess = input('Please enter: odd, even, or quit ')
        if guess == 'quit':
            break
        elif guess == 'even' and result % 2 == 0:
            print(number1, '+', number2, '=', result)
            print('You win!')
        elif guess == 'odd' and result % 1 ==0:
            print(number1, '+', number2, '=', result)
            print('You win!')
        elif guess == 'even' and result % 1 ==0:
            print(number1, '+', number2, '=', result)
            print('You lose!')
        elif guess == 'odd' and result % 2 ==0:
            print(number1, '+', number2, '=', result)
            print('You lose!')
    print('END OF GAME: thanks for playing!')
    