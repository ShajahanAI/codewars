# https://www.codewars.com/kata/57b2cef5d2a31c3965000a43/train/python 

# Passed

def n_mod9(m, n):
    sum_of_range = sum(range(m, n + 1))
    return sum_of_range % 9

output = n_mod9(1, 2016)
print(output)