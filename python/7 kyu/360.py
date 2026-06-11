# https://www.codewars.com/kata/54b45c37041df0caf800020f/train/python

# Passed

from math import gcd

def binary_gcd(x, y):
    value = gcd(x, y)
    value_binary = bin(value)
    result = value_binary.split("b")[1].count('1')
    return result

output = binary_gcd(666666, 333111)
print(output)