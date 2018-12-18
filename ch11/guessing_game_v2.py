# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:17:53 2018

@author: ottil
"""

# Trying to complete remaining part of game:

# Tell the player how many guesses they have left


#--------------------------------------------------
# VERSION 2 - now remembers number of guesses left but doesn't loop.

attempts = 3 

from random import randint
def guess(attempts, range):
    number = randint(1,range)
    print("Welcome! Can you guess my secret number?", "You have ", attempts, " guesses remaining.")
    guess = int(input('Make a guess: '))
    if guess == number:
        print('Well done! You got it right.')
    elif guess < number:
        print('No - too low!')
        attempts = attempts - 1
        print('You have ', attempts, ' attempts remaining.')
    elif guess > number:
        print('No - too high!')
        attempts = attempts - 1
        print('You have ', attempts, ' attempts remaining.')
    print("END OF GAME: thanks for playing! ")
    
#------------------------------------------------------------


    
    
    