
#---------------------------------------------------

# CHAPTER 11- While loops

#---------------------------------------------------

#How to write a while loop:

# while CONDITION:
    #(Indent) CODE-BLOCK
#------------------------------------
    
# Task 1

x = 33

while x>= 1:
    print(x,':', end='')
    x = x/2
    
print(x)

#------------------------------------

#Task 2: Creating triangular numbers:

n= 3
result = 0

while n > 0:
    result = result + n
    n = n - 1
    
print(result)

#------------------------------------

# Task 3:
# Challenge: create a system to advise pupils of whether they have
# passed or failed. 
    
# VERSION 1

#mark = 0
#
#while mark > -1:
#    mark = int(input('What is your mark? '))
#    if mark >= 70:
#        print('FIRST CLASS')
#
#    elif mark >= 40:
#        print('PASS')
#
#    elif mark < 40:
#        print('FAIL')
    
#------------------------------------
 
#VERSION 2

didYouPass = 'Yes'

while didYouPass == 'Yes':

    mark = int(input('What is your pass? '))
    if mark >= 70:
        print('FIRST CLASS')

    elif mark >= 40:
        print('PASS')

    elif mark < 40:
        print('FAIL')
    
    didYouPass = input('Did you pass? ')

#------------------------------------

# VERSION 3

#didYouPass = 'YES'
#mark = 1
#
#while didYouPass == 'YES':
#    didYouPass = input('Did you pass? YES or NO ')
#    while mark == 1: 
#        mark = int(input('Please type in your mark (1-100) here: '))
#        if mark >= 70:
#            print('Well done - firt class!')
#        elif mark >= 40:
#            print('That\'s alright, a pass!')
#        elif mark <= 30:
#            print('Oh no, you failed this class')

#------------------------------------

# How to create a  break in your code:

#i = 55
#
#while i > 10:
#    
#    print(i)
#    
#    i = i * 0.8
#    
#    if i == 35.2:
#        
#        break
    
#------------------------------------

# Task 4: Write an application that prints a greeting for the
# name entered, until the user enters 'Done'. 

while True:
    name = input('What is your name? ')
    print(name)
    if name == 'Done':
        break

#------------------------------------

# Guessing game:
        
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
  

