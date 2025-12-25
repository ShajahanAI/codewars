# https://www.codewars.com/kata/5601409514fc93442500010b/train/python

# Passed

def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    whether_i_am_better = your_points > average
    return whether_i_am_better

output = better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)
print(output)