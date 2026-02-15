# https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python

# Passed

from collections import Counter

def is_anagram(test, original):
    test_letter_counter = Counter(test.lower())
    original_letter_counter = Counter(original.lower())
    result = test_letter_counter == original_letter_counter
    return result

output = is_anagram("foefet", "toffee")
print(output)