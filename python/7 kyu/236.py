# https://www.codewars.com/kata/553e8b195b853c6db4000048/train/python

# Passed

def has_unique_chars(string):
    is_unique = len(string) == len(set(string))
    return is_unique

output = has_unique_chars("abcdef")
print(output)