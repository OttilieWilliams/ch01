from simpleBundlePurchase_v4 import initiateTransaction

# Test call to programme:
print ('TEST EXAMPLE 1')
# database input, you will still need to check user pin
result = initiateTransaction('1234', 34.55 )

print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 2')
result = initiateTransaction('2345', -22.00)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 3')
result = initiateTransaction('3456', 17.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')