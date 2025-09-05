# https://www.codewars.com/kata/5b728f801db5cec7320000c7/train/python

# Passed

from string import ascii_lowercase

def solve(st,k):
    indexes_to_remove = set()
    for alphabet in ascii_lowercase:
        if len(indexes_to_remove) == k:
            break

        for idx, letter in enumerate(st):
            if len(indexes_to_remove) == k:
                break
            
            if letter == alphabet:
                indexes_to_remove.add(idx)


    modified_st = "".join([char for idx, char in enumerate(st) if idx not in indexes_to_remove])
    return modified_st

output = solve('abracadabra', 6)
print(output)