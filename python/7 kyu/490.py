# https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python

# Passed

def flatten_and_sort(array):
    result = []
    for item in array:
        result.extend(item)
    
    result.sort()
    return result

output = flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]])
print(output)