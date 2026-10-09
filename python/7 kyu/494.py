# https://www.codewars.com/kata/55e9529cbdc3b29d8c000016/train/python

# Passed

def char_to_ascii(s):
    result = {
        char: ord(char) for char in s if char.isalpha()
    } if s else None

    return result

output = char_to_ascii("hello world")
print(output)