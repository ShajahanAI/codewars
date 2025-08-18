# https://www.codewars.com/kata/57fd696e26b06857eb0011e7/train/python

# Passed

def dative(word):
    nek_vowels = {'e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű'}
    nak_vowels = {'a', 'á', 'o', 'ó', 'u', 'ú'}
    suffix = str()
    for char in word[::-1]:
        if char in nek_vowels:
            suffix = 'nek'
        elif char in nak_vowels:
            suffix = 'nak'

        if suffix:
            break

    word += suffix
    return word

output = dative("ablak")
print(output)