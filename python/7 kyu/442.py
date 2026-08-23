# https://www.codewars.com/kata/5aff237c578a14752d0035ae/train/python

# Passed

import math

def predict_age(*ages):
    result = 0
    for age in ages:
        result += age ** 2
        
    result **= 0.5
    result /= 2
    result = math.floor(result) 
    return result

output = predict_age(65, 60, 75, 55, 60, 63, 64, 45)
print(output)