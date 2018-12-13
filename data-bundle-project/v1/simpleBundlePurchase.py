
"""
Creating an empty function
"""

def DataBundlePurchase(truePasscode,balance):
    if passwordCheck(truePasscode):
        return 'Password OK'
    else:
        return 'Wrong Password'
    
def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode:
        return True
    else:
        return False
    
    
    
  