# https://www.codewars.com/kata/5aee96e22c5061ee90000024/train/python

# Passed

def quadratic_gen(a, b, c, start=0, step=1):
    while True:
        result = [start, a * start ** 2 + b * start + c]
        start += step
        yield result

output = next(quadratic_gen(1, 0, 0))
print(output)