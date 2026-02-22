# https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f/train/python

# Passed

def compute_sum(n):
    total_sum = 0
    for num in range(1, n + 1):
        total_sum += sum([int(digit) for digit in str(num)])
        
    return total_sum

output = compute_sum(12)
print(output)