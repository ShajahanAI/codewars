# https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

# Passed

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    if (a < b + c) and (b < a + c) and (c < b + a):
        return True
    
    return False

output = is_triangle(1, 2, 2)
print(output)