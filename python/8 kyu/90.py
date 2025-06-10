# https://www.codewars.com/kata/57cff961eca260b71900008f/train/python

# Passed

def is_vow(inp):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [char_code if chr(char_code) not in vowels else chr(char_code) for char_code in inp]

output = is_vow([100,100,116,105,117,121])
print(output)