# https://www.codewars.com/kata/5596700a386158e3aa000011/train/python

# Passed

def binary_pyramid(m ,n):
    result = 0
    for num in range(m, n + 1):
        binary_num = bin(num)
        result += int(binary_num.split('b')[-1])

    result = bin(result).split('b')[-1]

    return result

output = binary_pyramid(1, 4)
print(output)