# https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc/train/python

# Passed

from collections import Counter, defaultdict

def solve(arr):
    result = list()
    num_to_frequency_dict = dict(Counter(arr))
    frequency_to_num_dict = defaultdict(list)
    
    for num in num_to_frequency_dict:
        frequency = num_to_frequency_dict[num]
        frequency_to_num_dict[frequency].append(num)
    
    for frequency in sorted(frequency_to_num_dict.keys(), reverse=True):
        num_arr = frequency_to_num_dict[frequency]
        num_arr.sort()
        for num in num_arr:
            result.extend([num] * frequency)
        
    return result   

output = solve([2,3,5,3,7,9,5,3,7])
print(output)