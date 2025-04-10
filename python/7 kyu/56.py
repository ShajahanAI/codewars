# https://www.codewars.com/kata/57eb936de1051801d500008a/train/python

# Passed

def explode(arr):  
    numbers_type = [type(i) == int for i in arr]
    if all(numbers_type):
        # all values are integers
        score = sum(arr)
    elif any(numbers_type):
        # one value is a number
        score = [i for i in arr if type(i) == int][0]
    else:
        return 'Void!'
    
    return [arr for _ in range (score)]

output = explode([9, 3])
print(output)