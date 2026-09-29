# https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python

# Passed

def sort_by_length(arr):
    result = list(sorted(arr, key=len))
    return result

output = sort_by_length(["", "pizza", "brains", "moderately"])
print(output)