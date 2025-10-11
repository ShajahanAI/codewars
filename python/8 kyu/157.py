# https://www.codewars.com/kata/5808e2006b65bff35500008f/train/python 

# Passed

from string import ascii_lowercase

def position(letter):
    position = ascii_lowercase.index(letter) + 1
    result = f"Position of alphabet: {position}"
    return result

output = position("a")
print(output)