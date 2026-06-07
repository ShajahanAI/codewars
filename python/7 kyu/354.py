# https://www.codewars.com/kata/5e28b3ff0acfbb001f348ccc/train/python

# Passed

def is_solved(board):
    current_num = 0
    for row in board:
        for val in row:
            if val != current_num:
                return False
            
            current_num += 1
            
    return True

output = is_solved([[0,1],[2,3]])
print(output)