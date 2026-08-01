# https://www.codewars.com/kata/5959ec605595565f5c00002b/train/python

# Passed

def reverse_bits(n):
    n_binary = bin(n).split('b')[-1]
    result = int(n_binary[::-1], 2)
    return result

output = reverse_bits(417)
print(output)