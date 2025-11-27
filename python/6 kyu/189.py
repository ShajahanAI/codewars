# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

# Passed

from string import ascii_lowercase

def alphabet_position(text):
    letter_to_position_dict = {
        letter: position for position, letter in enumerate(ascii_lowercase, start=1)
    }
    alphabet_positions = [str(letter_to_position_dict[letter.lower()]) for letter in text if letter.isalpha()]
    position_string = " ".join(alphabet_positions)
    return position_string
    
output = alphabet_position("The sunset sets at twelve o' clock.")
print(output)