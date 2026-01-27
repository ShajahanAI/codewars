# https://www.codewars.com/kata/58663693b359c4a6560001d6/train/python

# Passed

def maze_runner(maze, directions):
    FINISH = 'Finish'
    DEAD = 'Dead'
    LOST = 'Lost'
    
    column_coordinate, row_coordinate = 0, 0
    for row in maze:
        if 2 in row:
            column_coordinate = row.index(2)
            break
            
        row_coordinate += 1
        
    for direction in directions:
        if direction == 'N':
            row_coordinate -= 1
        elif direction == 'S':
            row_coordinate += 1
        elif direction == 'W':
            column_coordinate -= 1
        elif direction == 'E':
            column_coordinate += 1
            
        # validating row_coordinate and column_coordinate
        if row_coordinate >= len(maze) or row_coordinate < 0:
            return DEAD
        
        if column_coordinate >= len(maze[0]) or column_coordinate < 0:
            return DEAD
        
        current_position = maze[row_coordinate][column_coordinate]
        if current_position == 3:
            return FINISH
        elif current_position == 1:
            return DEAD
        
    return LOST

output = maze_runner(
    [[1,1,1,1,1,1,1],
     [1,0,0,0,0,0,3],
     [1,0,1,0,1,0,1],
     [0,0,1,0,0,0,1],
     [1,0,1,0,1,0,1],
     [1,0,0,0,0,0,1],
     [1,2,1,0,1,0,1]],
    ["N","N","N","N","N","E","E","E","E","E"]
)
print(output)