# https://www.codewars.com/kata/57f6ad55cca6e045d2000627/train/python

# Passed

def square_or_square_root(arr):
    result = []
    for num in arr:
        square_root = num ** 0.5
        if int(square_root) == square_root:
            result.append(int(square_root))
        else:
            num_squared = num ** 2
            result.append(num_squared)
            
    return result

output = square_or_square_root([100, 101, 5, 5, 1, 1])
print(output)