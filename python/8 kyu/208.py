# https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python

# Passed

def sum_array(arr):
    result = sum(sorted(arr)[1:-1]) if arr and len(arr) > 2 else 0
    return result

output = sum_array([6, 2, 1, 8, 10])
print(output)