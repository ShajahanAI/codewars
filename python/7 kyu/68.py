# https://www.codewars.com/kata/565b9d6f8139573819000056/train/python

# Passed

from string import ascii_lowercase

def decode(message):
    alphabets = list(ascii_lowercase)
    decoded_message = str()
    for letter in message:
        decoded_letter = letter
        if letter in alphabets:
            decoded_index = 25 - alphabets.index(letter)
            decoded_letter = alphabets[decoded_index]
            
        decoded_message += decoded_letter
    
    return decoded_message

output = decode("svool")
print(output)