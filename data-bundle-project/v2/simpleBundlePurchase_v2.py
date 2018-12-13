"""
Creating an empty function
"""

def DataBundlePurchase(truePasscode,balance):
    if passwordCheck(truePasscode) == True:
        transactionType = input('Enter 1 to Check balance, or 2 to Purchase a data bundle: ')
        if transactionType == '1':
            return checkBalance(balance)
        else:
            return purchaseDataBundle()
    else:
        return 'Wrong Password'
    
def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode:
        return True
    else:
        return False
    
def checkBalance(balance):
    return ('Your balance is {}'.format(balance))  
    
def purchaseDataBundle():
    return ('Service unavailable')
    
    
#    if balance > 0:
#        return True
#    else:
#        return False
    
#        if checkBalance(balance) == True:
#            return ('Your balance is {}'
#                    .format(balance))
  
#        else:
#            return ('Your balance is not sufficient: {}'
#                    .format(balance))