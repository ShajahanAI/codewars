# https://www.codewars.com/kata/558ffec0f0584f24250000a0/train/python

# Passed

from string import ascii_lowercase

def decode(string_):
    idx_to_letter_dict = {
        idx: letter for idx, letter in enumerate(ascii_lowercase)
    }
    
    letter_to_idx_letter = {
        letter: idx for idx, letter in enumerate(ascii_lowercase)
    }
    
    if type(string_) != str:
        result = "Input is not a string"
    else:
        result = ""
        for char in string_:
            decoded_character = char
            if char.lower() in letter_to_idx_letter:
                decoded_character = idx_to_letter_dict[(25 - letter_to_idx_letter.get(char.lower()))]
                if char.isupper():
                    decoded_character = decoded_character.upper()

            result += decoded_character
    
    return result

output = decode("Ovg'h hdrn rm gsv ulfmgzrm!")
print(output)