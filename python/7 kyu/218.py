# https://www.codewars.com/kata/558ee8415872565824000007/train/python

# Passed

def is_divisible(n, *other_numbers):    
    for num in other_numbers:
        if n % num != 0:
            return False
    return True

output = is_divisible(12, 3, 4)
print(output)