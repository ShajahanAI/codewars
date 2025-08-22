# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

# Passed

def summation(num):
    result = 0
    for n in range(1, num + 1):
        result += n
    
    return result

output = summation(8)
print(output)