# https://www.codewars.com/kata/564e7fc20f0b53eb02000106/train/python

# Passed

def consonant_count(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants_in_string = [letter for letter in s if letter.isalpha() and letter.lower() not in vowels]
    consonants_count = len(consonants_in_string)
    return consonants_count

output = consonant_count('h^$&^#$&^elLo world')
print(output)