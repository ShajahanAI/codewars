# https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a/train/python

# Passed

def solution(stones):
    stones_to_remove = 0
    for idx in range(len(stones) - 1):
        if stones[idx] == stones[idx + 1]:
            stones_to_remove += 1

    return stones_to_remove

output = solution("RGBRGBRGGB")
print(output)