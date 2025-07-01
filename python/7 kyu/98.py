# https://www.codewars.com/kata/5a805631ba1bb55b0c0000b8/train/python

# Passed

def case_sensitive(s):
    uppercase_letters = []
    result = []
    for letter in s:
        if letter.isupper():
            uppercase_letters.append(letter)

    if uppercase_letters:
        result.append(False)
    else:
        result.append(True)

    result.append(uppercase_letters)
    return result
            
output = case_sensitive('cellS')
print(output)