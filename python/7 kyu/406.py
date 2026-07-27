# https://www.codewars.com/kata/58e0cb3634a3027180000040/train/python

# Passed

def sort_by_value_and_index(arr):
    nums_with_pos_arr = [[num, pos] for pos, num in enumerate(arr, start=1)]
    sorted_arr = list(sorted(nums_with_pos_arr, key = lambda num_pos: num_pos[0] * num_pos[1]))
    result = [num_pos[0] for num_pos in sorted_arr]
    return result

output = sort_by_value_and_index([ 23, 2, 3, 4, 5 ])
print(output)