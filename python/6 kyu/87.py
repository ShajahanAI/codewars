# https://www.codewars.com/kata/595fb7d8de9d34743f000162/train/python

# Passed

from math import gcd

def treasure_code(clue):
    numbers = []
    letter_reels = []
    number_reel = str()
    for char in clue:
        if char.isalpha():
            letter_reels.append(char)
            if number_reel:
                numbers.append(int(number_reel))
                number_reel = str()
        else:
            number_reel += char
    
    if number_reel:
        numbers.append(int(number_reel))

    greatest_common_denominator = gcd(*numbers)
    decoded_numbers = [number//greatest_common_denominator for number in numbers]
    code = str()
    for letter_reel, decoded_number in zip(letter_reels, decoded_numbers):
        code += letter_reel + str(decoded_number)

    return code

output = treasure_code('Y14U7I7P21')
print(output)