# https://www.codewars.com/kata/58b8cc7e8e7121740700002d/train/python

# Passed

def rank_of_element(arr,i):
    result = 0
    element = arr[i]
    for before_idx in range(i):
        if arr[before_idx] <= element:
            result += 1
            
    for after_idx in range(i + 1, len(arr)):
        if arr[after_idx] < element:
            result += 1
            
    return result

output = rank_of_element([2, 1, 2, 1, 2], 2)
print(output)