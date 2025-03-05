# https://www.codewars.com/kata/5834315e06f227a6ac000099/train/python

# Passed

from collections import Counter

def elimination(arr):
    if not arr:
        return None
    
    counter = Counter(arr)
    twins = counter.most_common(1)[0]
    return twins[0] if twins[-1] > 1 else None

output = elimination([2, 3, 4, 11, 32, 43, 54, 53, 64, 12, 43, 52])
print(output)