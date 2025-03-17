from math import gcd

# https://www.codewars.com/kata/576400f2f716ca816d001614/train/python

# Passed

def reduce_fraction(fraction):
    greatest_common_divisor = gcd(*fraction)
    if greatest_common_divisor != 1:
        numerator = int(fraction[0]/greatest_common_divisor)
        denominator = int(fraction[1]/greatest_common_divisor)
        return reduce_fraction([numerator, denominator])

    return fraction

output = reduce_fraction([9, 27])
print(output)