# https://www.codewars.com/kata/53d32bea2f2a21f666000256/train/python

# Passed

def largest(n, xs):
    sorted_list = sorted(xs)
    result = sorted_list[-n:] if n != 0 else []
    return result

output = largest(7, [9, 1, 50, 22, 3, 13, 2, 63, 5])
print(output)