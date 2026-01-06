# https://www.codewars.com/kata/569924899aa8541eb200003f/train/python

# Passed

from string import ascii_uppercase

def quicksum(packet):
    alphabet_to_value_dict = {
        alphabet: value for value, alphabet in enumerate(ascii_uppercase, start=1)
    }
    alphabet_to_value_dict.update({" ": 0})
    
    result = 0
    for pos, char in enumerate(packet, start=1):
        if char not in alphabet_to_value_dict:
            result = 0
            return result
        
        result += alphabet_to_value_dict[char] * pos
        
    return result

output = quicksum("ACM")
print(output)