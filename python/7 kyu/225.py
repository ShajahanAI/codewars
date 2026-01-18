# https://www.codewars.com/kata/581214d54624a8232100005f/train/python

# Passed

def matrix(array): 
    for diagonal_idx in range(len(array[0])):
        value = array[diagonal_idx][diagonal_idx]
        if value < 0:
            array[diagonal_idx][diagonal_idx] = 0
        else:
            array[diagonal_idx][diagonal_idx] = 1
            
    return array

output = matrix([[-1, 4, -5, -9, 3], 
                 [6, -4, -7, 4, -5], 
                 [3, 5, 4, -9, -1], 
                 [1, 5, -7, -8, -9], 
                 [-3, 2, 1, -5, 6]])
print(output)