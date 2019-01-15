# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:11:59 2018

@author: ottil
"""

#Task 1 - Initialise person class

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.isMale = None
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else:
            print('Gender not recognised!')

# Task 2 - More functionalities for person class

    def greetingInformal(self):
        print('Hi', self.name)
    
    def greetingFormal(self):
        if self.isMale:
            print('Welcome, Mr ', self.name)
        else:
            print('Welome, Ms ', self.name)
            
# Task 3 - Greeting filter
            
    def greetingAgeBased(self): 
        if self.age > 60: 
            print('Welcome, venerable ', self.name)
        elif  self.age < 18:
            print('Welcome, young ', self.name)
        else:
            self.greetingFormal()
            
# Task 4 - subclass - wizard

#class Wizard(Person):
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#        self.isMale = True
#    def greetingFormal(self):
#        print("Welcome, Mr ", self.name, end=" ")
#        print("- you're a fine wizard!")
        
# Task 5 and 6 - redefine __init__ and create new methods for wizard
            
class Wizard(Person):
    def __init__(self,name,age, gender =''): 
        Person.__init__(self, name, age, gender= 'm')
    def greetingFormal(self):
        print("Welcome, Mr ", self.name, end=" ")
        print("- you're a fine wizard!")   
    def spell(self):
        print('Expelliarmus!')
    def playQuidditch(self):
        print('I\'ve caught the golden snitch!')
    def fightVoldemort(self):
        if self.name == 'Harry':
            print('Expecto, Patronum!')
        else:
            print('Ahhhhh!')


gerry = Person('Gerry', 70, 'm')
print(gerry.age) 
gerry.greetingInformal()
gerry.greetingFormal()
gerry.isMale
gerry.greetingAgeBased()

harry = Wizard('Harry', 20)
harry.greetingFormal()
harry.fightVoldemort()

ron = Wizard('Ron', 20, 'm')
ron.fightVoldemort()





