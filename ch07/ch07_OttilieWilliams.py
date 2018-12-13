userInput = input('please give a number ')
print(type(userInput))

userInput = input('please give a number ')

def simpleOperation(userInput):
    
    result = userInput - 2
    
    return result

def nestedOperation():
    
    result = simpleOperation(userInput)
    
    result2 = result * 2
    
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation()

print(result2)