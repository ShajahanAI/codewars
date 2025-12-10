# https://www.codewars.com/kata/59778cb1b061e877c50000cc/train/python

# Passed

def arr_adder(arr):
    words = [str()] * len(arr[0])
    for row in arr:
        for idx, char in enumerate(row):
            words[idx] += char
            
    sentence = " ".join(words)
    return sentence

output = arr_adder([
    ['J','L','L','M'],
    ['u','i','i','a'],
    ['s','v','f','n'],
    ['t','e','e','' ]
])
print(output)