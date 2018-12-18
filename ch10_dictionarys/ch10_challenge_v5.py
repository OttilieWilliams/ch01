# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:40:20 2018

@author: ottil
"""

# Trying to use a while loop to repeat the question

phoneBook_dict = {}
queenAge = 100

def add_classmate_info(phoneBook_dict):
    while True:
        nextClassmate = input ('Would you like to enter another student? Y/N ')
        if nextClassmate == 'N':
            break
        name = input('What is your name? ')
        phoneNo = input('What are the last 3 digits of your phone number? ') 
        luckyNo = input('What is your lucky number? ') 
        postCode = input('What is your postcode? ') 
        townOrCity = input('what is your home town or city? ')
        age = int(input('What is your age? '))
        phoneBook_dict[name] = phoneNo, luckyNo, postCode, townOrCity, age
        print(str('The queen has had ') + str(queenAge - age) + str(' more years on earth than you.'))
        print(phoneBook_dict)
        