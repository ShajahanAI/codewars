# https://www.codewars.com/kata/5971b219d5db74843a000052/train/python

# Passed

from collections import Counter

def added_char(s1, s2):  
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)
    
    for char in s2_counter:
        if (s2_counter[char] - s1_counter[char]) == 3:
            return char

output = added_char("hello","checlclo")
print(output)