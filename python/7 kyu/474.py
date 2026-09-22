# https://www.codewars.com/kata/5769a78c6f2dea72b3000027/train/python

# Passed

def is_bouncy(number):
    digits = list(map(int, str(number)))
    
    is_increasing = True
    is_decreasing = True
    for idx in range(len(digits)):
        if idx == len(digits) - 1:
            break
            
        if digits[idx] < digits[idx + 1]:
            is_decreasing = False
        elif digits[idx] > digits[idx + 1]:
            is_increasing = False
    
    result = not(is_increasing or is_decreasing)
    return result

output = is_bouncy(129347924210)
print(output)