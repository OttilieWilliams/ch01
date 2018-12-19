#---------------------------------------------------

# CHAPTER 3 - functions

#---------------------------------------------------

# How to create a function

# To work, a function needs:
# - to start with 'Def'
# - a unique name
# - brackets and a colon right after the name

#---------------------------------------------------

# Task 2: Writing a function

def hello_world():
    print("Hello World!")

#---------------------------------------------------

# Task 4: adding two numbers together

def add_two_numbers(num1, num2): 
    answer = num1 + num2
    print ("{} plus {} equals {}".format(num1, num2, answer)) 
    return answer

#---------------------------------------------------

# Task 5: Temperature conversion 

def convert_temperature(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32
    kelvin = centigrade + 273.15
    print ("Converting temperature in centigrade to fahrenheit and kelvin: ")  
    print ("Temperature in centigrade: ", centigrade)
    print ("Temperature in fahrenheit: ", fahrenheit)
    print ("Temperature in kelvin: ", kelvin)
    return kelvin + fahrenheit

#result = convert_temperature(50)
#print (result + 5)

def convert_distance(miles):
    kilometers = (miles*8.0)/5.0
    print ("Converting distance in miles to kilometers: ")
    print ("Distance in miles: ", miles)
    return kilometers

#London_ipswich = convert_distance(10)
#print ("Distance from London to Ipswich: ", London_ipswich)


