# https://www.codewars.com/kata/58bcdc65f6d3b11fce000045/train/python

# Passed

import math

def mn_lcm(m, n):
    m, n = sorted([m, n])
    least_common_multiple = math.lcm(*list(range(m, n + 1)))
    return least_common_multiple

output = mn_lcm(1,5)
print(output)