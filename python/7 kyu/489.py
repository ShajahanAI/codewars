# https://www.codewars.com/kata/58a30be22d5b6ca8d9000012/train/python

# Passed

from math import gcd

def gcd_matrix(a,b):
    total_numbers = 0
    total_sum = 0
    for row_num in b:
        for col_num in a:
            greatest_common_denominator = gcd(col_num, row_num)
            total_sum += greatest_common_denominator
            total_numbers += 1
    
    result = round(total_sum / total_numbers, 3)
    return result

output = gcd_matrix([1, 2, 3], [4, 5, 6])
print(output)