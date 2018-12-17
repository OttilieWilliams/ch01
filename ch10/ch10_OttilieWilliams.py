#------------------------------------------------------

#Dictionaries-------------------------------------------

#how to create them and amend them 

#{'bo':50000, 'al':20000,7:('Joke', 'Chen', 'Bond')}
#
#salary = {}
#
#salary['al'] = 20500 # this changes the al key
#
#salary[7] = ('Joke', 'Chen', 'Bond')
#
#print(salary)

#------------------------------------------------------

#tel = {'Amanda':858, 'Loren':264, 'Mabel':914, 'Ottilie':344}
#tel['Ottilie'] = 8344 # this updates Ottilie's phone number
#
#tel['Ottilie'] += 10 # this adds 10 to Ottilie's phone number

#del tel['Amanda'] # this deletes Amanda's phone number
#tel.pop('Amanda') # this also deletes Amana

#tel.update({'Amanda':123, 'Loren':345, 'Jane':789})# this updates
##the whole list.
#
#print(len(tel)) # shows the number of items in a list

#print(tel)
#print(tel.keys()) 

# the tel keys are immutable, so to make this
#work it needs to be turned into a list. 

#print(type(tel.values())) # checks what type of data the values are
#
#print(list(tel.keys())[3]) # 
#
#print(list(tel.values())[2])

#print(tel.keys()) # this lists all the keys
#print(tel.values()) # this lists all the values

#------------------------------------------------------

#Errors and how to avoid them--------------------------

#tel['Dave'] # this will give an error

#How to check if a name is in the dictionary: 

#k = 'Dave'
#if k in tel:
#    print(k, ':', tel[k])
#else:
#    print(k, 'not found!')


#print(tel.get(k, 'not found'))


#k = 'Amanda'
#if k in tel:
#    print(k, ':', tel[k])
#else:
#    print(k, 'not found!')

#------------------------------------------------------
#students_birthMonth = {'Amanda':('November'), 'Loren':('August')}

#Sorting a  dictionary by keys

#counts = {'a':3, 'c':1, 'b':5}
#labels = list(counts.keys()) #this turns it into a list
#labels.sort(key=lambda v:counts[v]) # this sorts it
#
#print(labels)

#------------------------------------------------------

#Sorting a  dictionary by values?
#
#counts = {'a':3, 'c':1, 'b':5}
#labels = list(counts.values()) 
#sorted(counts.items(), key=lambda kv: kv[1])
#print(labels)

#------------------------------------------------------

# Sorting both the keys and the values.

#counts = {'a':3, 'c':1, 'b':5}
#labels = list(counts.values())
#
#print(counts['a']) 
#print(sorted(counts.items(), key=lambda kv: kv[1])) 

#counts = {'a':3, 'c':1, 'b':5}
#labels = list(counts.values()) 
#print(sorted(counts.items(), key=lambda kv: kv[1])) 


#Example
#print(sorted(counts.items(), key=lambda kv:kv[1]))


#counts = {'Amanda':("November", 9), 'Loren':("August", 1), 'Mabel':("April", 8)}
#labels = list(counts.keys())
#labels.sort(key=lambda k:counts[k])
#print(labels)















