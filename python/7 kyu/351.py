# https://www.codewars.com/kata/6a1f03fac18f58f98ad9d21a/train/python

# Passed

from math import log2

def entropy(password):
    character_sets_used = {
        "lowercase_alphabets": False,
        "uppercase_alphabets": False,
        "digits": False,
        "special_characters": False
    }
    for char in password:
        if char.isalpha():
            if char.islower():
                character_sets_used["lowercase_alphabets"] = True
            else:
                character_sets_used["uppercase_alphabets"] = True
        elif char.isdigit():
            character_sets_used["digits"] = True
        else:
            character_sets_used["special_characters"] = True
    
    character_pool_size = 0
    character_set_to_pool_size = {
        "lowercase_alphabets": 26,
        "uppercase_alphabets": 26,
        "digits": 10,
        "special_characters": 32  
    }
    for possible_character_set_used in character_sets_used:
        if character_sets_used[possible_character_set_used]:
            character_pool_size += character_set_to_pool_size[possible_character_set_used]
            
    entropy = len(password) * log2(character_pool_size)
    return entropy

output = entropy('hello')
print(output)