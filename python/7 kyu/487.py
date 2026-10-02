# https://www.codewars.com/kata/56853c44b295170b73000007/train/python

# Passed

def is_square(arr):
    for num in arr:
        square_root = num ** 0.5
        if square_root != int(square_root):
            return False
    
    
    result = True if len(arr) else None
    return result

output = is_square([1, 4, 9, 16, 25, 36])
print(output)