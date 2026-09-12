# https://www.codewars.com/kata/589577f0d1b93ae32a000001/train/python

# Passed

def sort_by_height(a):
    heights = []
    tree_indices = set()
    
    for idx, value in enumerate(a):
        if value == -1:
            tree_indices.add(idx)
        else:
            heights.append(value)
    
    heights.sort()
    result = []
    
    height_idx = 0
    for idx in range(len(a)):
        if idx in tree_indices:
            result.append(-1)
        else:
            result.append(heights[height_idx])
            height_idx += 1
    
    return result

output = sort_by_height([-1, 150, 190, 170, -1, -1, 160, 180])
print(output)