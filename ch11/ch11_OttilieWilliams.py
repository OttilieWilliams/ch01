
# While loops

#How to write a while loop:

# while CONDITION:
    #(Indent) CODE-BLOCK
    
#------------------------------------
    
# Example

#x = 33
#
#while x>= 1:
#    print(x,':', end='')
#    x = x/2
#    
#print(x)

#------------------------------------

#Creating triangular numbers:

#n= 3
#result = 0
#
#while n > 0:
#    result = result + n
#    n = n - 1
#    
#print(result)

#------------------------------------

#Challenge: create a system to advise pupils of whether they have
#passed or failed. 
    
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

#didYouPass = 'Yes'
#
#while didYouPass == 'Yes':
#
#    mark = int(input('What is your pass? '))
#    if mark >= 70:
#        print('FIRST CLASS')
#
#    elif mark >= 40:
#        print('PASS')
#
#    elif mark < 40:
#        print('FAIL')
#    
#    didYouPass = input('Did you pass? ')

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

# Practice: Write an application that prints a greeting for the
# name entered, until the user enters 'Done'. 

#while True:
#    name = input('What is your name? ')
#    print(name)
#    if name == 'Done':
#        break

#------------------------------------


  

