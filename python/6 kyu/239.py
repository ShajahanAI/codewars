# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

# Passed

from collections import Counter 

def duplicate_encode(word):
    word = word.lower()
    counter_dict = Counter(word)
    result = ""
    
    for char in word:
        char_count = counter_dict[char]
        if char_count > 1:
            result += ")"
        else:
            result += "("
            
    return result

output = duplicate_encode("Success")
print(output)