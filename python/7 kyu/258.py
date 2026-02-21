# https://www.codewars.com/kata/56d5166ec87df55dbe000063/train/python

# Passed

from math import floor

def sum_average(arr):
    averages = []
    for sub_arr in arr:
        average = sum(sub_arr) / len(sub_arr)
        averages.append(average)
        
    result = floor(sum(averages))
    return result

output = sum_average([[52, 64, 84, 21, 54], [44, 87, 46, 90, 43]])
print(output)