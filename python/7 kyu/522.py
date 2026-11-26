# https://www.codewars.com/kata/5866c6cf442e3f16f9000089/train/python

# Passed

def hypotenuse(a, b):
    result = (a ** 2 + b ** 2) ** 0.5
    return result

def leg(c, a):
    result = (c ** 2 - a ** 2) ** 0.5
    return result

output1 = hypotenuse(4, 3)
output2 = leg(5, 3)
print(output1, output2)