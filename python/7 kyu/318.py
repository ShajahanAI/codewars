# https://www.codewars.com/kata/583989556754d6f4c700018e/train/python

# Passed

from math import gcd

def multiples(s1,s2,s3):
    result = []
    multiplier = 1
    base_val = s1 * s2 / gcd(s1, s2)
    base_val = int(base_val) if base_val.is_integer() else base_val
    val = base_val
    while val < s3:
        result.append(val)
        multiplier += 1
        val = base_val * multiplier
        
    return result

output = multiples(3,4,40)
print(output)