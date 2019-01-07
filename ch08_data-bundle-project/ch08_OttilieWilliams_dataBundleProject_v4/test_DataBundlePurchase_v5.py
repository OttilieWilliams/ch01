# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 20:05:58 2019

@author: ottil
"""

from simpleBundlePurchase_v5 import DataBundlePurchase

# Test call to programme:  
print ('TEST EXAMPLE 1')
# database input, you will still need to check user pin
result = DataBundlePurchase('1234', 34.55 )

print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 2')
result = DataBundlePurchase('2345', -22.00)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 3')
result = DataBundlePurchase('3456', 17.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')