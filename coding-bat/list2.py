# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:49:16 2019

@author: ottil
"""

def count_evens(nums):
    total_evens = 0
    for num in nums:
        if num % 2 == 0:
            total_evens += 1
    return total_evens  

def big_diff(nums):
  nums.sort()
  return(nums[-1] - nums[0])
  
def centered_average(nums):
  nums.sort()
  nums= nums[1:-1]
  total = sum(nums)
  number_of_nums = len(nums)
  return total/number_of_nums

def sum13(nums):
    
  for i in range(0, len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      
      if i+1 < len(nums):     # i + 1 refers to the index position, not the actual value of i+1
        nums[i+1] = 0 p09
        
  return sum(nums)


