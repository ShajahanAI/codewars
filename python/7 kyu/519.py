# https://www.codewars.com/kata/5f3142b3a28d9b002ef58f5e/train/python

# Passed

def word_pattern(word):
    character_to_number_dict = dict()
    current_number = 0
    character_codes = []
    for character in word.lower():
        if character in character_to_number_dict:
            character_code = character_to_number_dict[character]
        else:
            character_code = str(current_number)
            character_to_number_dict[character] = character_code
            current_number += 1
        
        character_codes.append(character_code)
    
    result = ".".join(character_codes)
    return result

output = word_pattern("helLo")
print(output)