# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

# Passed

def sum_two_smallest_numbers(numbers):
    num_1 = min(numbers)
    numbers.remove(num_1)
    num_2 = min(numbers)
    return num_1 + num_2

output = sum_two_smallest_numbers([2, 4, 312, 53, 132, 53])
print(output)