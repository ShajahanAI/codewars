# https://www.codewars.com/kata/595877be60d17855980013d3/train/python

# Passed

def euclidean_distance(point1, point2):
    dist = 0
    for coordinate1, coordinate2 in zip(point1, point2):
        dist += (coordinate2 - coordinate1) ** 2

    dist = round(dist ** 0.5, 2) # taking the square root
    return dist

output = euclidean_distance([-1, 2, 5], [2, 4, 9])
print(output)