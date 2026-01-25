# https://www.codewars.com/kata/59ca8e8e1a68b7de740001f4/train/python

# Passed

from collections import Counter

def solve(a,b):
    counter_dict = Counter(a)
    count_arr = []
    for item in b:
        item_count = counter_dict[item]
        count_arr.append(item_count)
        
    return count_arr

output = solve(['abc', 'xyz','abc', 'xyz','cde'], ['abc', 'cde', 'xyz'])
print(output)