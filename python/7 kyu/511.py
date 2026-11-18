# https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python

# Passed

def factorial(n):
    if n <= 0:
        return 1
    
    return n * factorial(n - 1)

output = factorial(7)
print(output)