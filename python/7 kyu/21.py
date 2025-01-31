# https://www.codewars.com/kata/595aa94353e43a8746000120/train/python

# Passed

def find_deleted_number(arr, mixed_arr):
    difference = set(arr) - set(mixed_arr)
    return difference.pop() if difference else 0

output = find_deleted_number([1, 2, 3, 4, 5], [1, 2, 4, 3])
print(output)