# https://www.codewars.com/kata/67fb86b6564f0bd70dc615b1/train/python

# Passed

from string import ascii_uppercase

def validate_euro(serial_number):
    letter_to_pos_dict = {
        letter: pos for pos, letter in enumerate(ascii_uppercase, start=1)
    }
    
    total_sum = 0
    for char in serial_number:
        if char.isdigit():
            total_sum += int(char)
        else:
            total_sum += letter_to_pos_dict[char.upper()]
        
    while (len(str(total_sum)) != 1):
        total_sum = sum(int(digit) for digit in str(total_sum))
        
    result = total_sum == 7
    return result

output = validate_euro("VA0436214792")
print(output)