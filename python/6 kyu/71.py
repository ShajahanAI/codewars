# https://www.codewars.com/kata/52de9bd621c71b919c000592/train/python

# Passed

def in_sphere(coords, radius):
    squares = list(map(lambda coord: coord ** 2, coords))
    return sum(squares) <= radius ** 2

output = in_sphere([0.5, 0.5, 0.5], 1)
print(output)