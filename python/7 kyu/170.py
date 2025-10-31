# https://www.codewars.com/kata/58a6742c14b042a042000038/train/python

# Passed

def s2n(m, n):
    result = 0
    for base in range(m + 1):
        for power in range(n + 1):
            result += base ** power
            
    return result

output = s2n(3,5)
print(output)