"""
Creating an empty function
"""

def DataBundlePurchase(truePasscode,balance):
    if passwordCheck(truePasscode) == True:
        transactionType = input('Enter 1 to Check balance, or 2 to Purchase a data bundle: ')
        if transactionType == '1':
            checkBalance(balance)
            return 'Users chooses to see balance.'
        elif transactionType == '2':
            if checkMobileNumber() == True:
                print("Thank you. We have stored your mobile number.")
                chooseDataBundle(balance)
                return 'Customer decides to buy data bundle.'
        else:
            return ('Error')
    else:
        return 'Wrong Password'
    
def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode:
        return True
    else:
        return False
    
def checkBalance(balance):
    print ('Your balance is {}'.format(balance))  
    
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
        return 'New balance is ' + str(balance)
    else:
        print('You must enter a multiple of 5. Please try again.')
        return 'Customer did not enter a multiple of 5.'



#(dataBundleChoice % 5) == 0:


# (int(dataBundleChoice)/5) == int:
        
        
#    if balance > 0:
#        return True
#    else:
#        return False
# 
#        if checkBalance(balance) == True:
#            return ('Your balance is {}'
#                    .format(balance))
#        else:
#            return ('Your balance is not sufficient: {}'
#                    .format(balance))