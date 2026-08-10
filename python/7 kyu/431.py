# https://www.codewars.com/kata/58870402c81516bbdb000088/train/python

# Passed

from collections import Counter

def strings_construction(a, b):
    b_counter = Counter(b)
    result = 0
    max_strings_constructed = False
    while True:
        for char in a:
            if b_counter[char] == 0:
                max_strings_constructed = True
                break
                
            b_counter[char] -= 1
        else:
            result += 1
            
        if max_strings_constructed:
            break
        
    return result

output = strings_construction("abc","abccba")
print(output)