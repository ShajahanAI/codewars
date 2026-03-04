# https://www.codewars.com/kata/55486cb94c9d3251560000ff/train/python

# Passed

import math

def calculate_ratio(w, h):
    if w == 0 or h == 0:
        raise Exception('You threw an error')
    
    while (greatest_common_denominator:= math.gcd(w, h)) != 1:
        w = int(w/greatest_common_denominator)
        h = int(h/greatest_common_denominator)
        
    ratio_string = f"{w}:{h}"
    return ratio_string

output = calculate_ratio(1024, 768)
print(output)