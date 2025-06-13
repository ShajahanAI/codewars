# https://www.codewars.com/kata/67757660c552a3a7ef9aaceb/train/python

# Passed

from string import ascii_uppercase

def validate_base(num: str, base: int) -> bool:
    base_string = "0123456789" + ascii_uppercase
    current_base_digits= set(base_string[:base]) # will let us know which all digits are valid for current base
    
    for digit in num:
        if digit not in current_base_digits:
            # num is not valid for current base
            return False

    return True
    
output = validate_base('6124', 5)
print(output)