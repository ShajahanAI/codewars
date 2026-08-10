# https://www.codewars.com/kata/5ce6728c939bf80029988b57/train/python

# Passed

def solve(st):
    character_codes = list(sorted(map(ord, st)))
    result = True
    for idx in range(len(character_codes)):
        if idx == len(character_codes) - 1:
            break
            
        if character_codes[idx + 1] - character_codes[idx] != 1:
            result = False
            break
    
    return result

output = solve("dabc")
print(output)