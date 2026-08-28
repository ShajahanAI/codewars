# https://www.codewars.com/kata/600444d8f654f60008a0a83c/train/python

# Passed

def common_distance(n, m, pointA, pointB):
    get_distance = lambda x1, y1, x2, y2: ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    result = []
    for x_coord in range(n):
        for y_coord in range(m):
            point = (x_coord, y_coord)
            distance_from_a = get_distance(*point, *pointA)
            distance_from_b = get_distance(*point, *pointB)
            if distance_from_a == distance_from_b:
                result.append(point)
    
    return result

output = common_distance(10, 10, (0,9), (9,4))
print(output)