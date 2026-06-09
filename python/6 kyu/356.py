# https://www.codewars.com/kata/5816f2580e80c5e075000a4f/train/python

# Passed

from math import gcd, lcm

def add_fracs(*fractions):
    result = str()
    if len(fractions) == 0:
        return result
    
    numerators_denominators = [fraction.split("/") for fraction in fractions]
    denominators = [int(numerator_denominator[1]) for numerator_denominator in numerators_denominators]
    
    final_denominator = lcm(*denominators)
    final_numerator = 0
    for numerator_denominator in numerators_denominators:
        numerator, denominator = numerator_denominator
        numerator, denominator = int(numerator), int(denominator)
        final_numerator += numerator * (final_denominator / denominator)
    
    greatest_common_denominator = gcd(int(final_numerator), int(final_denominator))
    simplified_numerator = int(final_numerator / greatest_common_denominator)
    simplified_denominator = int(final_denominator / greatest_common_denominator)
    
    result = f"{simplified_numerator}/{simplified_denominator}" if simplified_denominator != 1 else str(simplified_numerator)
    return result

output = add_fracs('2/3', '1/3', '4/6')
print(output)