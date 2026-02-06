# https://www.codewars.com/kata/5899aa695401a83a5c0000c4/train/python

# Passed

from math import pi

def square_area_to_circle(size):
    side = size ** 0.5
    radius = side / 2
    circle_area = round(pi * radius ** 2, 8)
    return circle_area

output = square_area_to_circle(9)
print(output)