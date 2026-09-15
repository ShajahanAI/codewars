# https://www.codewars.com/kata/69c2f04a1294ffc95c526d9e/train/python

# Passed

import math

def find_quarter_notes(time_signature):
    numerator, denominator = map(int, time_signature.split("/"))
    if denominator == 0:
        return None
    
    pow = math.log2(denominator)
    if not int(pow) == pow:
        return None
    
    quarter_note = 0.25
    result = math.floor((numerator / denominator) / quarter_note)
    return result

output = find_quarter_notes('9/8')
print(output)