# https://www.codewars.com/kata/5a33ec23ee1aaebecf000130/train/python

# Passed

from collections import Counter

def count_feelings(st, arr):
    available_characters_counter = Counter(st)
    feeling_count = 0
    for feeling in arr:
        available_characters = available_characters_counter.copy()
        for character in feeling:
            if available_characters.get(character, 0):
                available_characters[character] -= 1
            else:
                break
        else:
            feeling_count += 1
    
    if feeling_count == 1:
        return "1 feeling."

    return f"{feeling_count} feelings."

output = count_feelings('yliausoenvjw', ['anger', 'awe', 'joy', 'love', 'grief'])
print(output)