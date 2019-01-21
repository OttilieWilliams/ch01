# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:12:41 2019

@author: ottil
"""

# TASK 1: COUNTING WORDS

# With for loops in a text file, they will automatically
# iterate at the end of each line. So you need to 
# do an embedded for loop to iterate each word. 

word_counter = {}

def countWords(filename):
    file = open(filename,'r')
    for line in file: 
        for word in line.split():
            if word not in word_counter:
                word_counter[word] = 1
            else:
                word_counter[word] +=1
#    print(word_counter)
    return(word_counter)
    
word_counter_dict = countWords('mobydick.txt')

def printTopTwenty(word_counter_dict):
    li_word_counter = list(word_counter_dict.keys())
    li_word_counter.sort(reverse=True,key=lambda v:word_counter_dict[v]) 
    for i in range(20):
        word = li_word_counter[i] # this gets the key (alone) from the list
        print(word.upper(), "has a frequency of: ", word_counter_dict[word]) 
        
printTopTwenty(word_counter_dict)













# NOT IN FUNCTIONS

# TASK 1
#file = open('mobypara.txt','r')
#word_counter = {}
#for line in file: 
#    for word in line.split():
#        if word not in word_counter:
#            word_counter[word] = 1
#        else:
#            word_counter[word] +=1
#print(word_counter)

#TASK 2:

#sorted keys and values from word_counter:
#print(sorted(word_counter.items(), key=lambda kv:kv[1]))

#print(word_counter.keys())
#print(word_counter.items())
#print(word_counter.values())




