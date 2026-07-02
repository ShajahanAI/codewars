# https://www.codewars.com/kata/56a946cd7bd95ccab2000055/train/python

# Passed

def lowercase_count(strng):
    result = sum(char.isalpha() and char.islower() for char in strng)
    return result

output = lowercase_count("abcABC123")
print(output)