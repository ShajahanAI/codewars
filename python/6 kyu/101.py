# https://www.codewars.com/kata/58f6e7e455d7597dcc000045/train/python

# Passed

def get_password(grid, directions):
    # locating x (current position)
    for row_idx, row in enumerate(grid):
        if 'x' in row:
            current_pos = [row_idx, row.index('x')]
    
    password = str()
    for direction in directions:
        if "right" in direction:
            current_pos[1] = min(current_pos[1] + 1, len(grid[0]))
        elif "left" in direction:
            current_pos[1] = max(current_pos[1] - 1, 0)
        elif "up" in direction:
            current_pos[0] = max(current_pos[0] - 1, 0)
        elif "down" in direction:
            current_pos[0] = min(current_pos[0] + 1, len(grid[0]))

        if direction.endswith("T"):
            # grabbing value for password
            x, y = current_pos
            password += grid[x][y]

    return password

output = get_password([
            ["x", "l", "m"],
            ["o", "f", "c"],
            ["k", "i", "t"]
          ], ["rightT", "down", "leftT", "right", "rightT", "down", "left", "leftT"])
print(output)