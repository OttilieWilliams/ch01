# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:56:25 2018

@author: ottil
"""

#Import a Python module and funtion

#from random import randint
#def guess(attempts, range):
#    number = randint(1,range)
#    print ("Welcome! Can you guess my secret number? ")
#    print(number)
#    # ... YOUR CODE GOES HERE ...
#    print("END OF GAME: thanks for playing! ")

#-----------------------------------------------------------

#Complete the game! It must:

# Tell the player how many guesses they have left NOT DONE
# Read their guess DONE
# Tell them if their guess is right DONE
# If not, whether it is too low or too high DONE

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
    elif guess > number:
        print('No - too high!')    
    print("END OF GAME: thanks for playing! ")
    
    
    
    
    
    
    
    
    
    
    
    