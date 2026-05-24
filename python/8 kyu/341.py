# https://www.codewars.com/kata/5963c18ecb97be020b0000a2/train/python

# Passed

def derive(coefficient, exponent): 
    result = f"{coefficient * exponent}x^{exponent - 1}"
    return result

output = derive(7, 8)
print(output)