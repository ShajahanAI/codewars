# https://www.codewars.com/kata/59eb28fb0a2bffafbb0000d6/train/python

# Passed

from math import log2

def sort_by_binary_ones(numList):
    def convert_to_binary(decimal_num):
        if decimal_num == 0:
            return "0"
        binary_length = int(log2(decimal_num)) + 1
        binary_num_arr = ["0"] * binary_length
        
        while decimal_num > 0:
            idx = int(log2(decimal_num))
            decimal_num -= 2 ** idx
            binary_num_arr[binary_length - 1 - idx] = "1"
        
        binary_num = "".join(binary_num_arr)
        return binary_num
        
    binary_strings = [convert_to_binary(decimal_num) for decimal_num in numList]
    sorted_binary_strings = sorted(binary_strings, key = lambda binary_str: (binary_str.count("1"), 
                                                                  -len(binary_str), 
                                                                  -int(binary_str), 2),
                                                   reverse=True)
    result = [int(binary_string, 2) for binary_string in sorted_binary_strings]
    return result

output = sort_by_binary_ones([1, 2, 3, 4])
print(output)