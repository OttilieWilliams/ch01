# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:45:11 2018

@author: ottil
"""

#Sorting the dictionary by Name: 

phoneBook_dict = {} #creating the phonebook dictionary

#def add_classmate_info(phoneBook_dict):
#    for x in range(0, 2):
#        name = input('What is your name? ')# this will be the key
#        phoneNo = input('What are the last 3 digits of your phone number? ') #value
#        luckyNo = input('What is your lucky number? ') #value
#        postCode = input('What is your postcode? ') #value
#        townOrCity = input('what is your home town or city? ') #value
#        phoneBook_dict[name] = phoneNo, luckyNo, postCode, townOrCity
#    phoneBook_dict = (sorted(phoneBook_dict.items(), key=lambda k:k[0]))
#    return phoneBook_dict


#Sorting the dictionary by Town/City: 

#def add_classmate_info(phoneBook_dict):
#    for x in range(0, 2):
#        name = input('What is your name? ')# this will be the key
#        phoneNo = input('What are the last 3 digits of your phone number? ') #value
#        luckyNo = input('What is your lucky number? ') #value
#        postCode = input('What is your postcode? ') #value
#        townOrCity = input('what is your home town or city? ') #value
#        phoneBook_dict[name] = phoneNo, luckyNo, postCode, townOrCity
#    phoneBook_dict = (sorted(phoneBook_dict.items(), key=lambda k:k[1][0]))
#    return phoneBook_dict
    
#Sorting the dictionary by Lucky Number: 
    
def add_classmate_info(phoneBook_dict):
    for x in range(0, 2):
        name = input('What is your name? ')# this will be the key
        phoneNo = input('What are the last 3 digits of your phone number? ') #value
        luckyNo = input('What is your lucky number? ') #value
        postCode = input('What is your postcode? ') #value
        townOrCity = input('what is your home town or city? ') #value
        phoneBook_dict[name] = phoneNo, luckyNo, postCode, townOrCity
    phoneBook_dict = (sorted(phoneBook_dict.items(), key=lambda k:k[1])[2])
    return phoneBook_dict



