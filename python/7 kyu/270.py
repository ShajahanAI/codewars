# https://www.codewars.com/kata/59706036f6e5d1e22d000016/train/python

# Passed

from string import ascii_lowercase

def words_to_marks(s):
    letter_to_score_dict = {
        letter: pos for pos, letter in enumerate(ascii_lowercase, start=1)
    }
    
    score = sum([letter_to_score_dict[letter] for letter in s.lower()])
    return score

output = words_to_marks('attitude')
print(output)