# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 09:32:46 2019

@author: ottil
"""

import string
alphabet = list(string.ascii_lowercase)

#third_letter = alphabet[2:27:3]
#print(third_letter)

for letter in alphabet:
    print(letter.upper())
    if letter == third_letter:
        print(letter)
    elif letter == 



for letter in range(0, len(alphabet)):
    if letter % 2 == 0 and letter % 3 == 0:
        print(str(letter) + alphabet[letter])
    elif letter % 3 == 0:
        print(letter)
    elif letter % 2 == 0:
        print(alphabet[letter].lower())
    else:
        print(alphabet[letter].upper())
        
    
#############################################
     #NOTES     
############################################# 
     
#     elif letter % 2 == 1:
#        print(alphabet[letter].upper())
    
#def upper_case():
#    for letter in alphabet:
#        print(letter.upper())
#
#def every_third_letter():
#    for letter in range(0, len(alphabet)):
#        if letter % 2 == 0:
#            print(alphabet[letter].lower())
#
#def every_fourth_letter():
#    for letter in range(0, len(alphabet)):
#        if letter % 3 == 0: 
#            print(letter)
#        
#def every_third_and_every_fourth():
#    for letter in range(0, len(alphabet)):
#        if letter % 2 == 0 and letter % 3 == 0:
#            print(str(letter) + str(alphabet[letter]))

#upper_case()
#every_third_letter()
#every_fourth_letter()
#every_third_and_every_fourth()
