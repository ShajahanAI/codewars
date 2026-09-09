# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

# Passed

def count_bits(n):
    binary_num = bin(n)
    result = binary_num.split('b')[-1].count('1')
    return result

output = count_bits(10)
print(output)