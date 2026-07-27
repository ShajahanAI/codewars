# https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0/train/python

# Passed

def solution(n, d):
    result = []
    if d > 0:
        digits = [int(digit) for digit in str(n)]
        result = digits[-d:]
    
    return result

output = solution(123767, 4)
print(output)