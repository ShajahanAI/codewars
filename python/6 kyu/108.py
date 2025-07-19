# https://www.codewars.com/kata/528d9adf0e03778b9e00067e/train/python

# Passed

def mine_location(field):
    mine = 1
    for idx, row in enumerate(field):
        if mine in row:
            x_coordinate = idx
            break

    y_coordinate = field[idx].index(1)
    coordinates = [x_coordinate, y_coordinate]
    return coordinates

output = mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
print(output)