# https://www.codewars.com/kata/5970fce80ed776b94000008b/train/python

# Passed

from string import ascii_lowercase

def letters_to_numbers(s):
    lowercase_to_score = {letter: idx + 1 for idx, letter in enumerate(ascii_lowercase)}
    uppercase_to_score = {letter.upper(): (idx + 1) * 2 for idx, letter in enumerate(ascii_lowercase)}

    score = 0
    for char in s:
        if lowercase_to_score.get(char):
            score += lowercase_to_score[char]
        elif uppercase_to_score.get(char):
            score += uppercase_to_score[char]
        elif char.isdigit():
            score += int(char)

    return score

output = letters_to_numbers("ARE YOU HUNGRY?")
print(output)