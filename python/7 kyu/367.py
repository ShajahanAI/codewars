# https://www.codewars.com/kata/69269262ced9e95dc63abd1e/train/python

# Passed

def jumbler(indices):
    result = 0
    while indices[0] != 0:
        search_index = indices[0]
        value = indices[search_index]
        del indices[search_index]
        
        indices = [value] + indices
        result += 1
    
    return result

output = jumbler([2, 6, 8, 3, 5, 4, 0, 7, 1])
print(output)