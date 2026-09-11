# https://www.codewars.com/kata/66e793bba4b1a6f2e8f890e5/train/python

# Passed

def trailing_zeros(n) -> int:
    binary_num = bin(n)
    result = 0
    for digit in binary_num.split("b")[-1][::-1]:
        if digit == "1":
            break
            
        result += 1
    
    return result

output = trailing_zeros(32)
print(output)