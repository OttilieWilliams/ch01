"""
Creating an empty function
"""    
def initiateTransaction(truePasscode, balance):
    for x in range(1,4):
        if passwordCheck(truePasscode, balance) == False:
            return ("User has entered incorrect password")
        else:
            transactionType(balance)
            return("Customer has completed transaction")

def passwordCheck(truePasscode, balance):
    attempt = input('Please enter your password ')
    if attempt == truePasscode:
        return True
    else:
        print("Incorrect password")
        return False
    
def passwordCheckAgain(truePasscode,balance):
    if passwordCheck(truePasscode, balance):
        return True 
    print("\n Please try again (second attempt).")
    if passwordCheck(truePasscode, balance):
        return True 
    print("\n Please try again (final attempt).")
    if passwordCheck(truePasscode, balance):
        return True 
    return False

def transactionType(balance):
    transactionTypeCheck = input("Enter 1 to Check balance, or 2 to Purchase a data bundle: ")
    if transactionTypeCheck == '1':
        return showBalance(balance)
    elif transactionTypeCheck == '2':
        return dataBundleTransaction(balance)
        
def showBalance(balance):
    print ('Your balance is {}'.format(balance))  
    return('User shown balance')

def dataBundleTransaction(balance):
    if checkMobileNumber() == True:
        print("Thank you. We have stored your mobile number.")
        chooseDataBundle(balance)
        return ('Customer has completed data transaction')
    else:
        return ('Error')
    
def checkMobileNumber():
    mobileNumber1 = input('Enter your mobile number, with no spaces: ')
    mobileNumber2 = input('Please re-confirm your mobile number, with no spaces: ')
    if mobileNumber1 == mobileNumber2:
        return True 
    else:
        return False 

def chooseDataBundle(balance):
    dataBundleChoice = int(input('You have £{} in your balance. Choose an amount to spend on data. It must be a multiple of 5: '.format(balance)))
    if dataBundleChoice > balance:
        print('Your balance is not sufficient. Please choose again.')
        return 'Choice exceeds balance.'
    elif (dataBundleChoice/5).is_integer():
        balance = round(balance - dataBundleChoice,3) 
        print('You have successfully bought £' + str(dataBundleChoice) + ' worth of data. You have £' + str(balance) + ' left in your balance.')
        return 'New balance is ' + str(balance) + 'Customer decides to buy data bundle.'
    else:
        print('You must enter a multiple of 5. Please try again.')
        return 'Customer did not enter a multiple of 5.' 










#####################################################
        
#NOTES

#def passwordCheck(truePasscode,balance):
#    passwordCheck = input("Please enter your password: ")     
#    if passwordCheck == truePasscode:
#        print("Correct password.")
#        return transactionType(balance)
#    else:
#        print("Incorrect password")
#        return("Customer has entered incorrect password")

#####################################################


