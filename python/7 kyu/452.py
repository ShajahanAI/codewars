# https://www.codewars.com/kata/58b8db810f40ea7788000126/train/python

# Passed

import math

def fraction(a, b):
    common_factor = math.gcd(a, b)
    reduced_numerator, reduced_denominator = a / common_factor, b / common_factor
    
    result = reduced_numerator + reduced_denominator
    return result

output = fraction(3, 15)
print(output)