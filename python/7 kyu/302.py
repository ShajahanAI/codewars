# https://www.codewars.com/kata/5f8a15c06dbd530016be0c19/train/python

# Passed

def duplicate_sandwich(arr):
    seen = set()
    elem_to_start_idx_dict = dict()
    result = []
    for idx, elem in enumerate(arr):
        if elem in seen:
            elem_start_idx = elem_to_start_idx_dict[elem]
            result = arr[elem_start_idx + 1:idx]
            break
            
        elem_to_start_idx_dict[elem] = idx
        seen.add(elem)
    
    return result

output = duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8])
print(output)