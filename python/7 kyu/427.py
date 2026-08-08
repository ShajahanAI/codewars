# https://www.codewars.com/kata/55960bbb182094bc4800007b/train/python

# Passed

def insert_dash(num):
    result = ""
    is_odd = lambda num: num % 2 == 1
    digits = [int(digit) for digit in str(num)]
    for idx in range(len(digits)):
        result += str(digits[idx])
        if idx == len(digits) - 1:
            break
            
        if is_odd(digits[idx]) and is_odd(digits[idx + 1]):
            result += "-"
            
    return result

output = insert_dash(1003567)
print(output)