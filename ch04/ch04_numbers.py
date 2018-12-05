#number = input ("Enter a number between 1 and 10: ")
#number = int(number)
#
#if number > 10:
#    print ("Too high!")
#
#elif number <= 0:
#    print ("Too low!")
#    
#else:
#    print ("Just right!")

#age = 20
#isaTeen = age >=13 and age <=19
#print (isaTeen)

age = input("Enter your age here: ")
age = int(age)

if age < 13:
    print ("child")

elif age < 65:
    print ("adult")
    
elif age < 18:
    print("teen") 
    
else:
    print ("pensioner")
    


