# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:33:49 2018

@author: ottil
"""

#How many years does your age differ from the Queen's?

# Trying to combine the two functions to make one.

phoneBook_dict = {}
queenAge = 100

def add_classmate_info(phoneBook_dict):
    name = input('What is your name? ')
    phoneNo = input('What are the last 3 digits of your phone number? ') 
    luckyNo = input('What is your lucky number? ') 
    postCode = input('What is your postcode? ') 
    townOrCity = input('what is your home town or city? ')
    age = int(input('What is your age? '))
    phoneBook_dict[name] = phoneNo, luckyNo, postCode, townOrCity, age
    print(str('The queen has had ') + str(queenAge - age) + str(' more years on earth than you.'))
    print(phoneBook_dict)

        