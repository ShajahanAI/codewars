# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python

# Passed

from string import ascii_lowercase

def solve(strings : list[str]) -> list[int]:
    alphabet_to_pos_dict = {
        alphabet: alphabet_pos for alphabet, alphabet_pos in enumerate(ascii_lowercase, start=1)
    }
    
    result = []
    for string in strings:
        string = string.lower()
        normal_pos_count = 0
        for char, char_pos in enumerate(string, start=1):
            if char_pos == alphabet_to_pos_dict.get(char, -1):
                normal_pos_count += 1
                
        result.append(normal_pos_count)
        
    return result

output = solve(["abode", "ABc", "xyzD"])
print(output)