# https://www.codewars.com/kata/573f5c61e7752709df0005d2/train/python

# Passed

def merge_arrays(first, second): 
    result = list(set(first + second))
    result.sort()
    return result

output = merge_arrays([1, 3, 5], [2, 4, 6])
print(output)