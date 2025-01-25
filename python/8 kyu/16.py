# https://www.codewars.com/kata/59811fd8a070625d4c000013/train/python

# Passed

def integrate(coefficient, exponent):
    return f"{coefficient//(exponent + 1)}x^{exponent + 1}"

output = integrate(40, 3)
print(output)