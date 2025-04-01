# https://www.codewars.com/kata/57e2dd0bec7d247e5600013a/train/python

# Passed

def unflatten(flat_array):
    array_to_return = list()
    idx = 0
    while idx < len(flat_array):
        num = flat_array[idx]
        if num < 3:
            array_to_return.append(num)
            idx += 1
        else:
            sub_array = flat_array[idx: idx + num]
            array_to_return.append(sub_array)
            idx += num
    
    return array_to_return

output = unflatten([3, 21, 4, 1, 23, 43, 1, 2, 334, 45, 23])
print(output)