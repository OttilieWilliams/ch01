#Lists and Tuples

#How to create a list:

#my_favourite_fruits = ['apple', 'orange', 'banana']
#x = ['this', 55, 'that', my_favourite_fruits]

#how to select parts of the list to call:

#print (x[-1][-2][-2])

#print(my_favourite_fruits[2])


#List is a mutable data type (can be changed)
#Tuple is a immutable data type(cannot be changed)
#Str is immutable

#-----------------------------------------

#How to remove items or add them:

#my_favourite_fruits = ['apple', 'orange', 'banana']
#
#x = ['this', 55, 'that', my_favourite_fruits]
#
#x.remove('this')
#
#x.append('amazing') 
#
#print (x)

#-----------------------------------------

#You can also perform some operators on a list:

#x = ['the','cat','sat']
#y = ['on','the','mat']
#
#z = (x*5)
#
#print(z)

#-----------------------------------------

#You can also slice sections out of lists:

#x = ['this', 'and', 'that', 'once', 'again']
#
#print (x[-3:-1])

#-----------------------------------------

#You can also sort your lists:

#x = [7,11,3,9,2]
#y = sorted(x)
#print(y)

#x = [7,11,3,9,2]
#x.sort()
#print(x)

x = [7,11,3,9,2]
print(sorted(x, reverse=True))

#x = ['ab', 'cs', 'yw', 'zs', 'hd']
#y = sorted(x)
#print(y)

#-----------------------------------------

#This does not give an error message as it is a list:
#a = [0,1,2,3,4,5,6,7,8,9]
#del a[-1]
#print(a)

#This gives an error message as it is a tuple:
#b = (0,1,2,3,4,5,6,7,8,9)
#del b[-1]
#print(b)

#This does not give an error message as it is a list:
#a = [0,1,2,3,4,5,6,7,8,9]
#a[0]=50
#print(a)

#This gives an error message as it is a tuple:
#b = (0,1,2,3,4,5,6,7,8,9)
#a[0]=50
#print(b)

#This does not give an error message as it is a list:
#a = [0,1,2,3,4,5,6,7,8,9]
#a.append('z')
#print(a)

#This gives an error message as it is a tuple:
#b = (0,1,2,3,4,5,6,7,8,9)
#a.append('z')
#print(b)

#a = [0,1,2,3,4,5,6,7,8,9]
#b = (0,1,2,3,4,5,6,7,8,9)

#c = list(b)
#print(c)

#d = tuple(a)
#print(d)




