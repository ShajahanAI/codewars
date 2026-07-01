# https://www.codewars.com/kata/63d1bac72de941033dbf87ae/train/python

# Passed

import math

def validate_sudoku(board):
    section_id_to_indexes_dict = dict()
    for row_idx in range(9):
        for col_idx in range(9):
            row_id = math.floor(row_idx / 3)
            col_id = math.floor(col_idx / 3)
            
            section_id = f"{row_id}{col_id}"
            if section_id not in section_id_to_indexes_dict:
                section_id_to_indexes_dict[section_id] = []
                
            section_id_to_indexes_dict[section_id].append([row_idx, col_idx])
    
    result = True
    sudoku_digits = set(range(10))
    # checking each row
    for row in board:
        difference = sudoku_digits - set(row)
        if difference != {0}: # 0 should only remain
            result = False
            break
            
    if result:
        # checking each col
        for col_idx in range(9):
            col = [board[row_idx][col_idx] for row_idx in range(9)]
            difference = sudoku_digits - set(col)
            if difference != {0}: # 0 should only remain
                result = False
                break
        
    if result:
        # checking grids
        for section_indexes in section_id_to_indexes_dict.values():
            section_values = set([board[section_index[0]][section_index[1]] for section_index in section_indexes])
            difference = sudoku_digits - section_values
            if difference != {0}: # 0 should only remain
                result = False
                break
            
    return result

output = validate_sudoku([[1,7,3,2,6,8,9,5,4],
                          [4,2,5,1,9,3,7,6,8],
                          [8,6,9,7,4,5,1,2,3],
                          [6,1,2,8,3,7,4,9,5],
                          [3,9,8,4,5,6,2,1,7],
                          [5,4,7,9,1,2,3,8,6],
                          [9,5,4,3,8,1,6,7,2],
                          [2,3,6,5,7,9,8,4,1],
                          [7,8,1,6,2,4,5,3,9]])
print(output)