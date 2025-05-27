# https://www.codewars.com/kata/571af500196bb01cc70014fa/train/python

# Passed

from string import ascii_lowercase

def mirror(*code):
    message_to_encrypt = code[0]
    letters_to_cipher = ascii_lowercase if len(code) == 1 else code[1]
    mirrored_cipher = str()
    for letter in message_to_encrypt:
        letter = letter.lower()
        mirrored_alphabet = letter
        if letter in letters_to_cipher:      
            mirror_index = len(letters_to_cipher) - letters_to_cipher.index(letter.lower()) - 1
            mirrored_alphabet = letters_to_cipher[mirror_index]
        
        mirrored_cipher += mirrored_alphabet
    
    return mirrored_cipher
            
            
output = mirror("hello", "abcdefgh")
print(output)