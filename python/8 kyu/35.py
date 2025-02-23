# https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/python

# Passed

def no_boring_zeros(n):
    if not n:
        return n
    
    return int(str(n).rstrip('0'))

output = no_boring_zeros(10450)
print(output)