# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

# Passed

def find_next_square(sq):
    square_root = sq ** 0.5
    result = -1
    if square_root.is_integer():
        result = int((square_root + 1) ** 2)
    
    return result

output = find_next_square(625)
print(output)