# https://www.codewars.com/kata/588453ea56daa4af920000ca/train/python

# Passed

def array_packing(arr):
    binary_nums = [bin(num).split("b")[1].zfill(8) for num in arr[::-1]]
    result_binary = "".join(binary_nums)
    result = int(result_binary, 2)
    return result

output = array_packing([23, 45, 39])
print(output)