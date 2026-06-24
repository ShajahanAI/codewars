# https://www.codewars.com/kata/5d6f49d85e45290016bf4718/train/python

# Passed

def any_odd(x):
    binary_num = bin(x).split('b')[-1]
    result = any(bit == "1" and idx % 2 == 1 for idx, bit in enumerate(binary_num[::-1]))
    return result

output = any_odd(131)
print(output)