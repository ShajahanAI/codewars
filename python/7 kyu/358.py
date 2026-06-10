# https://www.codewars.com/kata/58d5e6c114286c8594000027/train/python

# Passed

def array_manip(array):
    result = []
    for num_idx, num in enumerate(array):
        right_side_arr = array[num_idx + 1:]
        right_side_filtered_arr = [right_num for right_num in right_side_arr if right_num > num]
        least_greatest_num = min(right_side_filtered_arr) if right_side_filtered_arr else -1
        
        result.append(least_greatest_num)
        
    return result

output = array_manip([8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28])
print(output)