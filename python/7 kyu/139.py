# https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2/train/python

# Passed

def direction(facing, turn):
    direction_to_degree_dict = {direction.strip(): degree for direction, degree in  zip("N, NE, E, SE, S, SW, W, NW".split(","), list(range(0, 361, 45)))}
    degree_to_direction_dict = {degree: direction for direction, degree in direction_to_degree_dict.items()}
    current_degree = direction_to_degree_dict[facing]
    simplified_turn = current_degree + turn
    if simplified_turn < 0:
        simplified_turn = -(abs(simplified_turn) % 360)
        simplified_turn -= (360 if simplified_turn >= 0 else -360)
        simplified_turn %= 360
    else:
        if simplified_turn >= 360:
            simplified_turn = simplified_turn % 360
             
    final_direction = degree_to_direction_dict[simplified_turn]
    return final_direction
    
output = direction("S", 180)
print(output)