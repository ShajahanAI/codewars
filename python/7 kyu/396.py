# https://www.codewars.com/kata/5681cf0be812b41721000034/train/python

# Passed

def remove_noise(st):
    noise = set("%$&/#·@|º\ª")
    result = "".join([char for char in st if char not in noise])
    return result

output = remove_noise("h%e&·%$·llo w&%or&$l·$%d")
print(output)