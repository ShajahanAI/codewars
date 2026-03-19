# https://www.codewars.com/kata/598d91785d4ce3ec4f000018/train/python

# Passed

from string import ascii_lowercase

def name_value(my_list):
    letter_to_value = {
        letter: val for val, letter in enumerate(ascii_lowercase, start=1)        
    }
    calc_word_value = lambda word, multiplier: sum(letter_to_value.get(letter, 0) for letter in word) * multiplier
    result = []
    for pos, word in enumerate(my_list, start=1):
        result.append(calc_word_value(word, pos))
        
    return result

output = name_value(["codewars","abc","xyz"])
print(output)