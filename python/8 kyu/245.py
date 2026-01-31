# https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python

# Passed

def find_difference(a, b):
    calculate_volume = lambda dimensions: dimensions[0] * dimensions[1] * dimensions[2]
    volume_difference = abs(calculate_volume(a) - calculate_volume(b))
    return volume_difference

output = find_difference([3, 2, 5], [1, 4, 4])
print(output)