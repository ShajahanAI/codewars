# https://www.codewars.com/kata/57eead3b5f79f6d977001fb7/train/python

# Passed

def digit_all(x):
    result = "Invalid input !"
    if type(x) == str:
        result = "".join(char for char in x if char.isdigit())
    
    return result

output = digit_all('a1b2c3d4e')
print(output)