# https://www.codewars.com/kata/582c81d982a0a65424000201/train/python

# Passed

def arr_check(arr):
    is_every_value_an_array = all([type(val) == list for val in arr])
    return is_every_value_an_array

output = arr_check([[1], [2], [3]])
print(output)