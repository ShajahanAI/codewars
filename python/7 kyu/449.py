# https://www.codewars.com/kata/5ab363ff6a176b29880000dd/train/python

# Passed

def hex_hash(code):
    hex_characters = [hex(ord(char))[2:] for char in code]
    hex_code = "".join(hex_characters)
    digits = [int(char) for char in hex_code if char.isdigit()]
    result = sum(digits)
    return result

output = hex_hash('kcxnjsklsHskjHDkl7878hHJk')
print(output)