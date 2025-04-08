# https://www.codewars.com/kata/55f2a1c2cb3c95af75000045/train/python

# Passed

from math import lcm

def greatest(x, y, n):
    lowest_common_multiple = lcm(x, y)
    remainder = n % lowest_common_multiple 
    return n - (remainder if remainder else n)

def smallest(x, y, n):
    lowest_common_multiple = lcm(x, y)
    return n - n % lowest_common_multiple + lowest_common_multiple

output = greatest(2, 3, 20)
print(output)
output = smallest(2, 3, 20)
print(output)