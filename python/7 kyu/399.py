# https://www.codewars.com/kata/6a54d3e91e9fb16ca31cc912/train/python

# Passed

HEX = set("0123456789ABCDEF")

def find_corrupted_byte(dump):
    result = -1
    for idx, possible_hex in enumerate(dump):
        if len(possible_hex) != 2 or any(char not in HEX for char in possible_hex):
            result = idx
            break
            
    return result

output = find_corrupted_byte(["48", "65", "6G", "6C", "6F"])
print(output)