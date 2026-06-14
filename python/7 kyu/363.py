# https://www.codewars.com/kata/5a7778790136a132a00000c1/train/python

# Passed

def single_digit(n):
    result = n
    while len(str(result)) > 1:
        result = sum(int(bit) for bit in bin(result).split('b')[-1])
        
    return result

output = single_digit(5665)
print(output)