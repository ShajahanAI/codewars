# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python

# Passed

def factorial(n):
    if n < 0 or n > 12:
        raise ValueError()
        
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
        
    return factorial_result

output = factorial(3)
print(output)