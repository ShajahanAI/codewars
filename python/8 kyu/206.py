# https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python

# Passed

def grow(arr):
    result = 1
    for num in arr:
        result *= num
        
    return result

output = grow([2, 2, 2, 2, 2, 2])
print(output)