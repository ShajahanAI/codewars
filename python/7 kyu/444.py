# https://www.codewars.com/kata/6925ba5fcee28ebed6e18e7d/train/python

# Passed

import math

from collections import Counter

def entropy(message: str) -> float:
    result = 0.0
    modified_message = "".join(char for char in message if char.strip())
    char_counter = Counter(modified_message)
    modified_message_length = len(modified_message)
    for char in char_counter:
        char_count = char_counter[char]
        char_probability = char_count / modified_message_length
        
        result += char_probability * math.log2(char_probability)
    
    result *= -1
    return result

output = entropy("hello world")
print(output)