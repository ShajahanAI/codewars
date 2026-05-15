# https://www.codewars.com/kata/5a0d38c9697598b67a000041/train/python

# Passed

def eliminate_unset_bits(number):
    result_in_binary = number.replace('0', str())
    result = int(result_in_binary if result_in_binary else '0', 2)
    return result

output = eliminate_unset_bits("11010101010101")
print(output)