# https://www.codewars.com/kata/5d1e1560c193ae0015b601a2/train/python

# Passed

def count(a, t, x):
    absolute_differences = [abs(num - t) for num in a]
    result = len([1 for diff in absolute_differences if (x != 0 and diff % x == 0 ) or (x == 0 and diff == 0)])
    return result

output = count([11, 5, 3], 7, 2)
print(output)