
#------------------------------------------------------------

#CHAPTER 5 - Object Orientated Programming and using Classes

#------------------------------------------------------------

# Task 1: 

#class Customer(object):
#     """A customer of ABC Bank with a checking account. Customers have the following properties:
#     Attributes:
#     name: A string representing the customer's name.
#     balance: A float tracking the current balance of the customer's account.
#     """
#     def __init__(self, fullName, surname, balance=0.0):
#         """Return a Customer object whose name is *name* and starting balance is *balance*."""
#         self.fullName = fullName
#         self.surname = surname
#         self.balance = balance
#     def withdraw(self, amount):
#         """Return the balance remaining after withdrawing *amount* dollars."""
#         if amount > self.balance:
#             raise RuntimeError('Amount greater than available balance.')
#         self.balance -= amount
#         return self.balance  
#     def deposit(self, amount):
#         """Return the balance remaining after depositing *amount* dollars."""
#         self.balance += amount
#         return self.balance

#Bernie = Customer('Bernie Brown', 500.0)

#Bernie = Customer ('Bernie Brown', 'Brown', 1000.0)

#----------------------------------------------------------------------

# Practice: My own idea:

# A system for employee annual leave and sick day calculations

class employee(object):
     """Employees have the following properties:
     Attributes:
     name: A string representing the customer's name.
     holidayDaysRemaining: A float showing the number of holiday days an employee has left.
     """
     def __init__(self, name, holidayDaysRemaining=20):
         self.name = name
         self.holidayDaysRemaining = holidayDaysRemaining
     def useHolidayDays(self, daysUsed):
         if daysUsed > self.holidayDaysRemaining:
             additionalDaysRequest = input('You do not have enough days available. Consult your manager? Type Yes or No. ')
             if additionalDaysRequest == "Yes":
                 print ("Your manager has had a think and decided you cannot have the extra days. You still have " + str(self.holidayDaysRemaining) + " days remaining.")
             else:
                  print ("Okay. You have " + str(self.holidayDaysRemaining) + " days remaining.")
         else:  
             self.holidayDaysRemaining -= daysUsed
             print('You\'re leave is approved, you have ' + str(self.holidayDaysRemaining) + ' days remaining.')
             return self.holidayDaysRemaining  
     def overtime(self, daysOvertime):
         self.holidayDaysRemaining += daysOvertime
         print('Well done on your extra work! You now have ' + str(self.holidayDaysRemaining) + ' days remaining.')
     def pullSickie(self, daysSickLeave):
         if daysSickLeave > 3:
             print ("You have had more than 3 days sick. You need a Doctor's note!")
             doctorsNote = input ("Do you have a Doctor's Note? Type Yes if you do or No if you don't. ")
             if doctorsNote == "Yes":
                 print("Thank you. Please speak to your manager about statuary sick pay.")
             else:
                 print ("You're fired.")
         else: 
            print ("We hope you get better soon!")
            
class restaurantEmployee(employee):
    def __init__(self, name, holidayDaysRemaining=20):
         self.name = name
         self.holidayDaysRemaining = holidayDaysRemaining
    def workAnEveningShift(self):
        print ("Thank you for helping out with the evening shift. You can come in later on tomorrow.")

Belinda = employee('Belinda')
Ben = restaurantEmployee('Ben')

#Loren = employee('Loren',40)
#print(Loren.holidayDaysRemaining)
#Loren.useHolidayDays(10)
#print(Loren.holidayDaysRemaining)

#------------------------------------------------------------

# More practice

#import sys
#
#class Animal():
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#        
#    def eat(self):
#        print('nomnomnom')
#        
#class Dog(Animal): 
#    def bark(self):
#        print('Woof!')
#
##Sybil = Dog()
##Sybil.eat()

#------------------------------------------------------------

# Task 2 

#class Robot():
#    def move(self):
#        print('...move move move...')
#        
#class CleanRobot(Robot):
#    def clean(self):
#        print ('I vacuum dust')

#------------------------------------------------------------

# Task 3 
          
#class CookRobot(Robot):
#    def cook(self):
#        print ('I cook delicious food')

#------------------------------------------------------------

# Task 4 

#class SuperRobot():
#    
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#        
#        self.o1 = Robot()
#        self.o2 = Dog(name,age)
#        self.o3 = CleanRobot()
#        self.o4 = CookRobot()
#        
#    def playGame(self):
#        print('alphago game')
#    def move(self):
#        return self.o1.move()
#    def bark(self):
#        return self.o2.bark()
#    def clean(self):
#        return self.o3.clean()
#    def cook(self):
#        return self.o4.cook() 
#
#name = input('pet\'s name:')
#age = int(input('pet\'s age: '))
#
#name = sys.argv[1] #input('pet\'s name: ')
#age = sys.argv[2] #int(input('pet\'s age: '))
#
#Martin = SuperRobot('Snoopy',7)
#Martin.bark()
#Martin.cook()
#     
#automatic = SuperRobot(name, age)
#print (automatic.name)
#print (automatic.age)

#Jeeves = CookRobot()
#Jeeves.cook()

#------------------------------------------------------------     

# More practice
        
#class LionPride():
#    def __init__(self, name):
#        self.name = name      
#    
#    def hunt(self):
#        print ('chase')
#        
#class Lioness(LionPride):
#    def __init__(self, name, roarNumber=0, biteNumber=0):
#        self.roarNumber = roarNumber
#        self.biteNumber = biteNumber
#    
#    def roar(self):
#        print('rooooaaaaaar!'*self.roarNumber)    
#        
#    def bite(self):
#        print('chomp!'*self.biteNumber)
#    
#class Cub(Lioness): 
#    def play(self):
#        if self.roarNumber<=3:
#            print('let\'s play!')
#
#name = input('what is the lion\'s name:')        
#roar = int(input('how many times you heard it roar: '))
#bite = int(input('how many times you saw it bite: '))
#
#Simba = Lioness(name, roar,bite) #always inheritant ancester's
#Simba.roar()
#Simba.bite()
#Simba.hunt()

#Ernie = Cub
#Ernie.roar()

        
        


