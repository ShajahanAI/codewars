# https://www.codewars.com/kata/56d58a16e8f2d6957100093f/train/python

# Passed

def calculate_time(p1, p2):
    calculate_distance = lambda x1, y1, x2, y2: ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    speed = calculate_distance(*p1, *p2) / 5
    
    distance_from_origin = calculate_distance(*(0, 0), *p2)
    result = round(distance_from_origin / speed, 3)
    return result

output = calculate_time([100, 100], [90, 90])
print(output)