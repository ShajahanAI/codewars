# https://www.codewars.com/kata/5ab3495595df9ec78f0000b4/train/python

# Passed

def binary_to_string(binary):
    characters_in_binary = binary.split('0b')
    characters = [chr(int(char_in_binary, 2)) for char_in_binary in characters_in_binary if char_in_binary]
    result = "".join(characters)
    return result

output = binary_to_string('0b10000110b11000010b1110100')
print(output)