# https://www.codewars.com/kata/59a1cdde9f922b83ee00003b/train/python

# Passed

def stanton_measure(arr):
    times_one_appears = arr.count(1)
    stanton_measure_value = arr.count(times_one_appears)
    
    return stanton_measure_value

output = stanton_measure([1, 4, 3, 2, 1, 2, 3, 2])
print(output)