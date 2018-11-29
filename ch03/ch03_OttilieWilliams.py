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
    
def introduce():
    name = input("What's your name? ")
    print("My name is {}".format(name))
    in_ten_years()

#def where_are_you_from():
#    city = input("What city are you from? ")
#    print ("You are from {}".format(city))
#    favourite_food()
#    
#def favourite_food():
#    food = input ("What is your favourite food? ")
#    print ("Your favourite food is {}".format(food))
#    in_ten_years()
    
def in_ten_years():
    age = input("What's your age? ")
    print("Your age is {} ".format(age))
    add10 = int(age) + 10
    print ("In ten years you will be "+ str(add10))
    
    

        
    