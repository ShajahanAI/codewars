# https://www.codewars.com/kata/5660aa3d5e011dfd6e000063/train/python

# Passed

def find_spaceship(astromap):
    rows = astromap.splitlines()[::-1]
    row_coordinate = 0
    spaceship = 'X'
    for row in rows:
        if spaceship in row:
            column_coordinate = row.index(spaceship)
            return [column_coordinate, row_coordinate]

        row_coordinate += 1 # moving to next row

    # spaceship not found
    return "Spaceship lost forever."

output = find_spaceship('''..........\n..........\n..........\n.......X..\n..........\n..........''')
print(output)