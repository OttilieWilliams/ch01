# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:49:25 2018

@author: ottil
"""

#VERSION 3 

#Complete the game! It must:

# Tell the player how many guesses they have left DONE
# Read their guess DONE
# Tell them if their guess is right DONE
# If not, whether it is too low or too high DONE

attempts = 3 

from random import randint
def guess(attempts, endrange):
    number = randint(1, endrange)
    print("Welcome! Can you guess my secret number?", "You have ", attempts, " guesses remaining.")
    while attempts > 0:
        guess = int(input('Make a guess: '))
        if guess == number:
            print('Well done! You got it right.')
            break
        elif guess < number:
            print('No - too low!')
            attempts = attempts - 1
            print('You have ', attempts, ' attempts remaining.')
        elif guess > number:
            print('No - too high!')
            attempts = attempts - 1
            print('You have ', attempts, ' attempts remaining.')
    print("END OF GAME: thanks for playing! ")    
    