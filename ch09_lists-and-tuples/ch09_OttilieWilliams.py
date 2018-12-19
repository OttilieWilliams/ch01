
#---------------------------------------------------

# CHAPTER 9 - Lists, Tuples and Lambdas

#---------------------------------------------------

#A list is a mutable data type (can be changed)
#A tuple is a immutable data type(cannot be changed)
#Str is immutable
  
#Task 1 - How to create a list:

my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits]

#how to select parts of the list to call:

print(x[0]) # print the data at position 0 in x (this)

print (x[-1][-2][-2])

print(my_favourite_fruits[2])

#-----------------------------------------

# Task 2 - How to remove items or add them:

x.remove('this')

x.append('amazing') 

print (x)

#-----------------------------------------

#You can also perform some operators on a list:

#x = ['the','cat','sat']
#y = ['on','the','mat']
#
#z = (x*5)
#
#print(z)

#---------------------------------------------------

#Task 3: Slicing a list:
# This is the syntax to print a slice:
# print(x[start: stop: step])

x = ['this', 'and', 'that', 'once', 'again']

print (x[1:4])
print (x[-3:-1])

#---------------------------------------------------

#Task 4: Sorting a list:

x = [7,11,3,9,2]
y = sorted(x)
print(y)

x = [7,11,3,9,2]
x.sort()
print(x)

x = [7,11,3,9,2]
print(sorted(x, reverse=True))

x = ['ab', 'cs', 'yw', 'zs', 'hd']
y = sorted(x)
print(y)

#-----------------------------------------

#Task 5: Using tuples vs lists

#This does not give an error message as it is a list:
a = [0,1,2,3,4,5,6,7,8,9]
del a[-1]
print(a)

#This gives an error message as it is a tuple:
#b = (0,1,2,3,4,5,6,7,8,9)
#del b[-1]
#print(b)

#This does not give an error message as it is a list:
a = [0,1,2,3,4,5,6,7,8,9]
a[0]=50
print(a)

#This gives an error message as it is a tuple:
#b = (0,1,2,3,4,5,6,7,8,9)
#b[0]=50
#print(b)

#This does not give an error message as it is a list:
a = [0,1,2,3,4,5,6,7,8,9]
a.append('z')
print(a)

#This gives an error message as it is a tuple:
#b = (0,1,2,3,4,5,6,7,8,9)
#b.append('z')
#print(b)

#-----------------------------------------

# Extra Practice 

#a = [0,1,2,3,4,5,6,7,8,9]
#b = (0,1,2,3,4,5,6,7,8,9)
#
#c = list(b)
#print(c)
#
#d = tuple(a)
#print(d)

#-----------------------------------------

#Task 6: Using the lambda function to sort a list

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [0, 1 , 2, 3, 4, 5, 6, 7, 8, 9]
my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['aa', 'sb', 'lf', 'hw', 'ed', 'fy']
y = sorted(x)
z = ['fg', 'uj', 'sx', 'uj', 'ww', 'cf']
x2 = [('a',3,z),('c',1,y),('b',5,x)]

print(sorted(x2,key=lambda s:s[2][1]))

# the part s:s [2] means it should sort by the 2nd item in the list
# (position 0, then position 1, then position 2)
# the part s:s [2][1] means it should sort by the 2nd item in the list
# and then within it, sort by the first item. 


