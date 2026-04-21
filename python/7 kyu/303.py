# https://www.codewars.com/kata/69cda5b85599f307742ce70a/train/python

# Passed

from collections import Counter
from string import ascii_lowercase

def count_lonely_letters(text):
    text = text.lower()
    counter_dict = Counter(text)
    letter_to_idx_dict = {
        letter: idx for idx, letter in enumerate(ascii_lowercase)
    }
    
    idx_to_letter_dict = {
        idx: letter for idx, letter in enumerate(ascii_lowercase)
    }
    
    lonely_letters = 0
    for char in text:
        if counter_dict[char] > 1:
            continue
            
        if char in letter_to_idx_dict:
            letter_idx = letter_to_idx_dict[char]
        else:
            continue
        
        if char == "a":    
            neighbouring_letters = ["b"]
        elif char == "z":
            neighbouring_letters = ["y"]
        else:
            neighbouring_letters = [idx_to_letter_dict[letter_idx - 1], idx_to_letter_dict[letter_idx + 1]]
            
        if all(counter_dict[neighbour_letter] == 0 for neighbour_letter in neighbouring_letters):
            lonely_letters += 1
                
    return lonely_letters

output = count_lonely_letters("Hello, World!")
print(output)