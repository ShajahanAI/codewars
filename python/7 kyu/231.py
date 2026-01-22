# https://www.codewars.com/kata/56e56756404bb1c950000992/train/python

# Passed

from math import gcd

def sum_differences_between_products_and_LCMs(pairs):
    result = 0
    for pair in pairs:
        num1, num2 = pair
        gcd_value = gcd(num1, num2)
        lcm = (num1 / gcd_value) * (num2 / gcd_value) * gcd_value if gcd_value != 0 else 0
        result += (num1 * num2 - lcm)
        
    return result

output = sum_differences_between_products_and_LCMs([[15,18], [4,5], [12,60]])
print(output)