# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 16:08:34 2018

@author: ottil
"""

#---------------------------------------------------

# CHAPTER 12- For loops

#---------------------------------------------------

# For loops are widely used to implement counting loops. 
# They don't return anything - they are not functions.

# FOR x in NAMEOFTHINGTOGOTHROUGH:
    #...Code...e.g. print(x)

# Task 1: loop through a list using a for loop

my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]

for item in my_shopping_cart:
    print(item)
    
#---------------------------------------------------

# Task 2: Update the list values:


values = [875, 23, 451]
for val in values:
    print('--->' + str(val+50))

#---------------------------------------------------

# Task 3: Create your own list:


course = ['Loren', 'Mabel', 'Amanda', 'Katie']
for student in course:
    print(student)
#    
other_values = ['this', 55, 'that']
for item in other_values:
    print('***', item)

#---------------------------------------------------

# Task 4: Loop through a string type:
    
for char in "Yes":
    print(char)

for char in 'I like codey codey!':
    print(char)

# Task 5: Loop through a tuple:
    
colours = ('orange', 'yellow', 'red')
for item in colours:
    print(item)
    
#---------------------------------------------------    
# Recap of how SORT/SORTED works:

# SORTED
    
#number_list = [5, 2, 3, 1, 4]
#print(sorted(number_list)) 
#
## However, it CREATES a new list in a separate place. It does not modify the original.
## Therefore if you print the list again, it will go back to the original one. 
#
#print(number_list)
#
# SORT
#
## This amends the original list:
#
#number_list.sort()
#print(number_list)

#---------------------------------------------------

# Task 6: Create a salary dictionary

salaries = {'al': 20000, 'bo': 50000, 'ced':1500} # Creating a dictionary called 'salaries'
salariesKeys = list(salaries.keys()) # Creating a list of the keys from the salaries dictionary.
print(salariesKeys)

salariesKeys.sort(key=lambda m:salaries[m]) #Sorting the list
print(salariesKeys) 

for salary in salariesKeys:
    print('{0} = {1:1.0f}'.format(salary, salaries[salary])) #printing both the keys and values 

#---------------------------------------------------

# Task 7: sort the densities dictionary

densities = {'iron': 7.8, 'gold': 19.3, 'zinc': 7.13, 'lead': 11.4}

metals = list(densities.keys())
print(metals)

metals.sort(reverse=True, key=lambda m:densities[m])
print(metals)

for metal in metals:
    print('{0} = {1:5.1f}'.format(metal, densities[metal]))

#keyValue = sorted(densities.items(), key=lambda kv:kv[1], reverse=True)

#---------------------------------------------------
    
# Task 8: Combine counting loop and conditionals to filter out values:

metalValues = list(densities.values())
print(metalValues)

for metal in metalValues:
    if metal < 8:
        print(metal)
    
#---------------------------------------------------
    
# Task 9: Design a sum function: 

values = [3, 12, 9]
total = 0
for val in values:
    total += val
print('TOTAL:' + str(total))

def sumValues(list):
    total=0
    for val in list:
        total+=val
    return total

# the test case:
print(sumValues([2,3,4]))
# will then output 9  
     
# Task 10: Using a loop with index values

for i in range(len(values)):
    values[i] = values[i]*2
    print(values)

# Task 11: Using a loop with the range function

for i in range(5): #prints out 0 to 4. Automatically starts at 0.
    print(i)

for i in range(1,5): #prints out 1 to 4.
    print(i)

for i in range(5,10,2): #prints out 5 to 9, but skips every other number.
    print(i)

# Task 12: Using break in for loops

nums = [150, 8, 80, 200]
for num in nums:
    if num>100:
        print(num)
        break

# Task 13: Using nested loops 

outer_vals = [1,2,3]
inner_vals = ['a', 'b', 'c']
for oval in outer_vals:
    for ival in inner_vals:
        print(oval, ival)

# Task 14: Multiplication table with a for loop
    
for i in range(1,11):
    for j in range(1,11):
        print('{0:>3}'.format(i*j), end='')
    print('\n')
    
# VERSION 2

table = int(input("Please enter a times table: "))
for x in range(0, 5):
    print(x, "x", table, "=", x*table)
    

    
    
    
 




