# https://www.codewars.com/kata/544a54fd18b8e06d240005c0/train/python

# Passed

def find_smallest(numbers, to_return):
    idx_num_arr = zip(range(len(numbers)), numbers)
    smallest_idx_num = min(idx_num_arr, key=lambda idx_num: idx_num[1])
    
    result = smallest_idx_num[0] if to_return == 'index' else smallest_idx_num[1]
    return result

output = find_smallest([8, 0, 9], "index")
print(output)