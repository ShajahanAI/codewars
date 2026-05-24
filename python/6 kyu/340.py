# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

# Passed

def move_zeros(lst):
    result = []
    counter = 0
    for elem in lst:
        if elem == 0:
            counter += 1
        else:
            result.append(elem)
        
    result.extend([0] * counter)
    return result

output = move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
print(output)