# https://www.codewars.com/kata/57efcb78e77282f4790003d8/train/python

# Passed

import math

def how_many_times(annual_price, individual_price):
    return math.ceil(annual_price / individual_price)

output = how_many_times(40,15)
print(output)