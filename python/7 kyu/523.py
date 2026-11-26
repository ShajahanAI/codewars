# https://www.codewars.com/kata/64f41ad92b610b64c1067590/train/python

# Passed

def full_cycle(lst):
    visited_indices = set()
    current_idx = lst[0]
    while current_idx not in visited_indices:
        visited_indices.add(current_idx)
        current_idx = lst[current_idx]
    
    result = len(visited_indices) == len(lst)
    return result

output = full_cycle([2, 17, 7, 19, 18, 9, 5, 15, 16, 8, 11, 6, 14, 4, 3, 13, 0, 12, 1, 10])
print(output)