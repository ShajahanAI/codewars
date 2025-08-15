# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

# Passed

from string import ascii_lowercase

def is_pangram(st):
    all_alphabets = set(ascii_lowercase)
    all_characters_in_string = set(st.lower())
    result = True if len(all_alphabets - all_characters_in_string) == 0 else False
    return result

output = is_pangram("The quick brown fox jumps over the lazy dog.")
print(output)