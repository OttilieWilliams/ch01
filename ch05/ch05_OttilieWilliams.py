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

#class employee(object):
#     """A person with a job. People with jobs have the following properties:
#     Attributes:
#     name: A string representing the customer's name.
#     holidayDays: A float showing the number of holiday days an employee has left.
#     extraTime: A float tracking the number of extra hours a person works.
#     """
#     def __init__(self, name, holidayDays, balance=0.0):
#         """Return a Customer object whose name is *name* and starting balance is *balance*."""
#         self.name = name
#         self.holidayDays = holidayDays
#     def useHoliday(self, amount):
#         """Return the balance remaining after withdrawing *amount*."""
#         if amount > self.holidayDays:
#             raise RuntimeError('Amount greater than available balance.')
#         self.holidayDays -= amount
#         return self.holidayDays  
#     def workExtraTime(self, holidayDays):
#         """Return the balance remaining after working *amount* extra time."""
#         self.holidayDays += amount
#         return self.holidayDays
#     
#Belinda = employee('Belinda', 20)

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print('nomnomnom')
        
class Dog(Animal):
    def bark(self):
        print('Woof!')

#Sybil = Dog()
#Sybil.eat()

class Robot():
    def move(self):
        print('...move move move...')
        
class CleanRobot(Robot):
    def clean(self):
        print ('I vacuum dust')
        
class CookRobot(Robot):
    def cook(self):
        print ('I cook delicious food')

class SuperRobot():
    
    def __init__(self):
        self.name = name
        self.age = age
        
        self.o1 = Robot()
        self.o2 = Dog(name,age)
        self.o3 = CleanRobot()
        self.o4=CookRobot()
    def playGame(self):
        print('alphago game')
    def move(self):
        return self.o1.move()
    def bark(self):
        return self.o2.bark()
    def clean(self):
        return self.o3.clean()
    def cook(self):
        return self.o4.cook() 

name = input('pet\'s name:')
age = int(input('pet\'s age: '))

Martin = SuperRobot(name,age)
Martin.bark()
Martin.cook()
     
#Jeeves = CookRobot()
#Jeeves.cook()
      

        
#class LionPride():
#    def __init__(self, name):
#        self.name = name      
#    
#    def hunt(self):
#        print ('chase')
#        
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

        
        


