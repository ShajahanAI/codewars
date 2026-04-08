# https://www.codewars.com/kata/5b097da6c3323ac067000036/train/python

# Passed

def solve(a, b):
    a_points, b_points = 0, 0
    for a_point, b_point in zip(a, b):
        if a_point > b_point:
            a_points += 1
        elif b_point > a_point:
            b_points += 1

    if a_points > b_points:
        result = f'{a_points}, {b_points}: Alice made "Kurt" proud!'
    elif b_points > a_points:
        result = f'{a_points}, {b_points}: Bob made "Jeff" proud!'
    else:
        result = f'{a_points}, {b_points}: that looks like a "draw"! Rock on!'
        
    return result

output = solve([25, 50, 22], [34, 49, 50])
print(output)