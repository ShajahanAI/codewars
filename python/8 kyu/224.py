# https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python

# Passed

def sum_mix(arr):
    modified_arr = [int(item) for item in arr]
    modified_arr_sum = sum(modified_arr)
    return modified_arr_sum

output = sum_mix([9, 3, '7', '3'])
print(output)