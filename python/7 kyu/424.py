# https://www.codewars.com/kata/5a433c7a8f27f23bb00000dc/train/python

# Passed

def split_by_value(k, elements):
    left_arr, mid_arr, right_arr = [], [], []
    for elem in elements:
        if elem == k and len(mid_arr) != 0:
            mid_arr.append(elem)
        elif elem < k:
            left_arr.append(elem)
        else:
            right_arr.append(elem)
            
    result = left_arr + mid_arr + right_arr
    return result

output = split_by_value(6, [6, 4, 10, 10, 6])
print(output)