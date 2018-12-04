#in class work------------------------------------------------

#print ("What's your name?")
#name = input()
#print ("Hello {}!".format(name))
#print (name.lower())

#name = input("What's your name? ")
#print ("Hello {}!".format(name.upper()))

#age = input("What's your age? ")
#print ("Wow, you're {} years old!".format(age))
#
#city = input("What's your city? " )
#print ("Gosh, you're from {}!".format(city))

#a = "please type your age: "

#def hello_world():
#    print("Hello World!")
    
#def introduce():
#    name = input("What's your name? ")
#    print("My name is {}".format(name.upper()))
#    in_ten_years()

#def where_are_you_from():
#    city = input("What city are you from? ")
#    print ("You are from {}".format(city))
#    favourite_food()
#    
#def favourite_food():
#    food = input ("What is your favourite food? ")
#    print ("Your favourite food is {}".format(food))
#    in_ten_years()
    
#def in_ten_years():
#    age = input("What's your age? ")
#    print("Your age is {} ".format(age))
#    add10 = int(age) + 10
#    print ("In ten years you will be "+ str(add10))
#    add20 = int(age) + 20
#    print ("In twenty years you will be " + str(add20))
    
#def hello_world_2args(x, r, s):
#        print ("{} {} {}".format(x, r, s))
#
#a1 = "hello"
#b1 = "world"
#c1 = "yo"
#a2 = "love"
#b2 = "coding"
#c2 = "I do"
#
#hello_world_2args(a1, b1, c1)
#hello_world_2args(a2, b2, c2)

#print (list(range(10)))
#print (range(1,10))
#print (range(1,10,2))

#num1 = 15
#num2 = 20

#def add_two_numbers(num1, num2): 
#    answer = num1 + num2
#    print ("{} plus {} equals {}".format(num1, num2, answer))
#    
#    
#
#def convert_temperature(centigrade):
#    fahrenheit = centigrade * 9.0 / 5.0 + 32
#    kelvin = centigrade + 273.15
#    print ("Converting temperature in centigrade to fahrenheit and kelvin: ")  
#    print ("Temperature in centigrade: ", centigrade)
#    print ("Temperature in fahrenheit: ", fahrenheit)
#    print ("Temperature in kelvin: ", kelvin)
#    return kelvin + fahrenheit
#
#
#
#result = convert_temperature(50)
#print (result + 5)
#
#
#
#def convert_distance(miles):
#    kilometers = (miles*8.0)/5.0
#    print ("Converting distance in miles to kilometers: ")
#    print ("Distance in miles: ", miles)
#    return kilometers
#
#London_ipswich = convert_distance(10)
#print ("Distance from London to Ipswich: ", London_ipswich)
#
#
#
#    
#def convert_distance():
#    miles = input ("Enter the miles you would like to convert: ")
#    kilometers = (int(miles)*8.0)/5.0
#    print ("Converting distance in miles to kilometers: ")
#    print ("Distance in miles: ", miles)
#    print ("Distance in kilometers: ", kilometers)
#
#convert_distance()

#------------------------------------------------------



#Learn Python the Hard Way

#Exercise 7--------------------------------------------

#name = 'Zed A. Shaw'
#age = 35 # not a lie
#height = 74 # inches
#height_in_cm = (height * 2.54)
#weight = 180 # lbs
#eyes = 'Blue'
#teeth = 'White'
#hair = 'Brown'
#
#print ("Let's talk about %s." % name)
#print ("He's {} inches, or {} cm tall.".format(height, height_in_cm))
#print ("He's %d pounds heavy." % weight)
#print ("Actually that's not too heavy.")
#print ("He's got %s eyes and %s hair." % (eyes, hair))
#print ("His teeth are usually %s depending on the coffee." % teeth)
#
## this line is tricky, try to get it exactly right
#print ("If I add %d, %d, and %d I get %d." % (
#        age, height, weight, age + height + weight))

#fleece_colour = "snow"
#
#print ("Mary had a little lamb.")
#print ("Its fleece was white as", fleece_colour)
#print ("And everywhere that Mary went.")
#print ("." * 10)

#Exercise 8--------------------------------------------

#formatter = "%r %r %r %r"
#print (formatter % (1, 2, 3, 4))
#print (formatter % ("one", "two", "three", "four"))
#print (formatter % (True, False, False, True))
#print (formatter % (formatter, formatter, formatter, formatter))
#print (formatter % (
#    "I had this thing.",
#    "That you could type up right.",
#    "But it didn't sing.",
#    "So I said goodnight."
#))

#Exercise 9--------------------------------------------

#days = "Mon Tue Wed Thu Fri Sat Sun"
#months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#
#print ("Here are the days: ", days)
#print ("Here are the months: ", months)
#
#print ("""
#There's something going on here.
#With the three double- quotes.
#We'll be able to type as much as we like.
#Even 4 lines if we want, or 5, or 6.
#""")

#Exercise 10--------------------------------------------

#import math 
#print (math.pi)

#from math import * 
#print (pi)






