# https://www.codewars.com/kata/5661cde807c4e28efa0000d0/train/python

# Passed

def crazy_formula(n):
    n = abs(n)
    if len(str(n)) == 1:
        return n
        
    digits = [int(digit) for digit in str(n)]
    if len(digits) % 2 == 0:
        new_n = int("".join([str(digit) for digit in digits[:-1]]))
        return crazy_formula(new_n)
    
    first_digit = digits[0]
    middle_digit = digits[len(digits) // 2]
    last_digit = digits[-1]
    if middle_digit % 2 == 1:
        result = sum(digits) - middle_digit * 2 
    else:
        if last_digit % 2 == 0:
            result = sum(digits[:-1]) - last_digit
        else:
            result = first_digit ** 2 + sum(digits[1:])
    
    if len(str(result)) > 1:
        return crazy_formula(result)
    
    return result

output = crazy_formula(7852)
print(output)