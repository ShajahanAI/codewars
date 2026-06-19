# https://www.codewars.com/kata/59fa8e2646d8433ee200003f/train/python

# Passed

def sort_by_bit(arr):
    arr.sort(key = lambda decimal_num: (bin(decimal_num).count('1'), decimal_num))
    return arr

output = sort_by_bit([3, 8, 3, 6, 5, 7, 9, 1])
print(output)