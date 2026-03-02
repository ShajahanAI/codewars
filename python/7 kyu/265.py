# https://www.codewars.com/kata/54d3bb4dfc75996c1c000c6d/train/python

# Passed

def midpoint_sum(ints):
    if len(ints) in [0, 1, 2]:
        return -1
    
    left_sum, right_sum = ints[0], sum(ints[2:])
    mid_idx = 1
    
    for _ in range(1, len(ints)):
        if mid_idx + 1 >= len(ints):
            break
        
        if left_sum == right_sum:
            return mid_idx
        
        left_sum += ints[mid_idx]
        right_sum -= ints[mid_idx + 1]
        mid_idx += 1
        
    return -1

output = midpoint_sum([9,0,1,2,3,4])
print(output)