# https://www.codewars.com/kata/52f3a8e1f85fadcdf7001e31/train/python

# Passed

def factorial_division(n, d):
    result = 1
    
    # 5! / 3! = 5 * 4 * 3!/3! = 5 * 4
    for i in range(n, d, -1):
        result *= i

    return result

output = factorial_division(6, 3)
print(output)