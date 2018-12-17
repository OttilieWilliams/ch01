# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:55:39 2018

@author: ottil
"""

#Classmate 1

def add_classmate_info():
    name = input('What is your name? ')# this will be the key
    phoneNo = input('What are the last 3 digits of your phone number? ') #value
    luckyNo = input('What is your lucky number? ') #value
    postCode = input('What is your postcode? ') #value
    townOrCity = input('what is your home town or city? ') #value
    phoneBook_dict = {} #creating the phonebook dictionary
    phoneBook_dict[name] = phoneNo, luckyNo, postCode, townOrCity
    return phoneBook_dict
    print(phoneBook_dict)
    
    

#print(sorted(phoneBook_dict, key=lambda k:k[0]))