
#---------------------------------------------------

# CHAPTER 10- Dictionaries

#---------------------------------------------------

#Task 1: How to create them and amend them 

salary = {} # creates a dictionary called salary

salary['al'] = 20500 # adds a key called al and assigns it the value 20500

salary[7] = ('Joke', 'Chen', 'Bond') 

salary[7] = ('Joke', 'Chen', 'Ben') # updating the values

print(salary['al']) # retrieving the value

print(salary) # prints the whole dictionary


#------------------------------------------------------

# Task 2: Creating a dictionary of your own

tel = {'Amanda':858, 'Loren':264, 'Mabel':914, 'Ottilie':344}

#------------------------------------------------------

# Task 3: Updating the values of the dictionary

tel['Ottilie'] = 8344 # this updates Ottilie's phone number

tel['Ottilie'] += 10 # this adds 10 to Ottilie's phone number

del tel['Amanda'] # this deletes Amanda's phone number
#tel.pop('Amanda') # this also deletes Amanda

tel.update({'Amanda':123, 'Loren':345, 'Jane':789})# this updates
#the whole list.

print(len(tel)) # shows the number of items in a list

print(tel) # prints the whole dictionary
 
#------------------------------------------------------

# Task 4: retrieve keys and values from a dictionary

print(tel.keys()) # this lists all the keys
print(tel.values()) # this lists all the values

# the tel keys are immutable, so to make this
#work it needs to be turned into a list. 

#------------------------------------------------------

# What is the data type for keys and values?

print(type(tel.values())) # checks what type of data the values are

#------------------------------------------------------

# Task 5: Converting keys and values to list data type

print(list(tel.keys())[3]) 

print(list(tel.values())[2])

#------------------------------------------------------

#Errors and how to avoid them

#tel['Dave'] # this will give an error

# Think about how you can avoid this using if and else statements.

#------------------------------------------------------

# Task 6

#How to check if a name is in the dictionary: 

k = 'Dave'
if k in tel:
    print(k, ':', tel[k])
else:
    print(k, 'not found!')


#print(tel.get(k, 'not found'))


#k = 'Amanda'
#if k in tel:
#    print(k, ':', tel[k])
#else:
#    print(k, 'not found!')

#------------------------------------------------------

# Practice

#students_birthMonth = {'Amanda':('November'), 'Loren':('August')}

#Sorting a  dictionary by keys

#counts = {'a':3, 'c':1, 'b':5}
#labels = list(counts.keys()) #this turns it into a list
#labels.sort(key=lambda v:counts[v]) # this sorts it
#
#print(labels)

#------------------------------------------------------

#Sorting a  dictionary by values
#
#counts = {'a':3, 'c':1, 'b':5}
#labels = list(counts.values()) 
#sorted(counts.items(), key=lambda kv: kv[1])
#print(labels)

#------------------------------------------------------

# Sorting both the keys and the values.

#counts = {'a':3, 'c':1, 'b':5}
#labels = list(counts.values())

#print(counts['a']) 
#print(sorted(counts.items(), key=lambda kv: kv[1])) 

counts = {'a':3, 'c':1, 'b':5}
labels = list(counts.values()) 
print(sorted(counts.items(), key=lambda kv: kv[1])) 


#Example
#print(sorted(counts.items(), key=lambda kv:kv[1]))

#counts = {'Amanda':("November", 9), 'Loren':("August", 1), 'Mabel':("April", 8)}
#labels = list(counts.keys())
#labels.sort(key=lambda k:counts[k])
#print(labels)

#------------------------------------------------------

## Task 7: Sorting dictionary values in descending order 
#
densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
metals = list(densities.keys())
metals.sort(reverse=True,key=lambda m:densities[m])  # this sorts them by 
# value, in descending order.
#print(metals)
print(sorted(densities.items(), key=lambda kv: kv[1],reverse=True)) 
# This does the same but prints the whole key out.
#
## Task 8:
## Add two more values to each key, and ten sort the dictionary's 2nd 
## value in descending order. Do this using both methods used above.
#
#densities = {'iron':(7.8, 200,3), 'gold':(19.3, 1000, 0), 'zinc':(7.13,500, 80), 'lead':(11.4, 1,50)}
#metals = list(densities.keys())
#metals.sort(reverse=True,key=lambda m:densities[m][1])
#print(metals)  
#print(sorted(densities.items(), key=lambda kv: kv[1][1],reverse=True))













