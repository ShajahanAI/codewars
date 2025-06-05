# https://www.codewars.com/kata/5864f90473bd9c4b47000057/train/python

# Passed

def connect_four_place(columns):
    board = [["-" for _ in range(7)] for _ in range(6)] # 7 columns and 6 rows
    column_row_dict = {
        column: 5 for column in range(7)
    } # indicates which row to place next coin in
    player = 'Y'
    for move in columns:
        row = column_row_dict[move]
        column_row_dict[move] -= 1
        board[row][move] = player
        player = 'R' if player == 'Y' else 'Y'

    return board
                
output = connect_four_place([0,1,2,5,6,2,0,0])
print(output)