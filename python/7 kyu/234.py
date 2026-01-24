# https://www.codewars.com/kata/5d9f95424a336600278a9632/train/python

# Passed

from math import floor, log2

def powers(n):
    power_array = []
    while n != 0:
        nearest_exponent = floor(log2(n))
        value = 2 ** nearest_exponent
        power_array.append(value)
        n -= value
    
    power_array = power_array[::-1]
    return power_array

output = powers(99)
print(output)