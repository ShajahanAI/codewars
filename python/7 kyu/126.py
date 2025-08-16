# https://www.codewars.com/kata/6329437e3b59a10065e63a2f/train/python

# Passed

def normalize(arr, fill_value=None):
    normalized_array = []
    if not arr:
        return normalized_array

    biggest_arr = max(arr, key=len)
    for sub_array in arr:
        multiplier = len(biggest_arr) - len(sub_array)
        if multiplier:
            sub_array += [fill_value] * multiplier
        normalized_array.append(sub_array)
    return normalized_array

output = normalize([[1, 4, 2, 6, 7, 2], [3, 1, 4], [8, 9, 4, 4, 0, 9, 8]])
print(output)