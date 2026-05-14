# https://www.codewars.com/kata/5e030f77cec18900322c535d/train/python

# Passed

from math import ceil

def minimum(a, x):
    result = min(a % x, x * ceil(a/x) - a)
    return result

output = minimum(10, 6)
print(output)