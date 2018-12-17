# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:13:43 2018

@author: ottil
"""
#Classmate 1

name = input('What is your name? ') # this will be the key

phoneNo = input('What are the last 3 digits of your phone number? ') #value

luckyNo = input('What is your lucky number? ') #value

postCode = input('What is your postcode? ') #value

townOrCity = input('what is your home town or city? ') #value

#Classmate 2

name2 = input('NEXT PERSON! What is your name? ') # this will be the key

phoneNo2 = input('What are the last 3 digits of your phone number? ') #value

luckyNo2 = input('What is your lucky number? ') #value

postCode2 = input('What is your postcode? ') #value

townOrCity2 = input('what is your home town or city? ') #value

#Classmate 3

name3 = input('NEXT PERSON! What is your name? ') # this will be the key

phoneNo3 = input('What are the last 3 digits of your phone number? ') #value

luckyNo3 = input('What is your lucky number? ') #value

postCode3 = input('What is your postcode? ') #value

townOrCity3 = input('what is your home town or city? ') #value

phoneBook_dict = {} #creating the phonebook dictionary

phoneBook_dict[name] = phoneNo, luckyNo, postCode, townOrCity

phoneBook_dict[name2] = phoneNo2, luckyNo2, postCode2, townOrCity2

phoneBook_dict[name3] = phoneNo3, luckyNo3, postCode3, townOrCity3

print(phoneBook_dict)

print(sorted(phoneBook_dict, key=lambda k:k[0]))

