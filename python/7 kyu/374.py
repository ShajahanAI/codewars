# https://www.codewars.com/kata/564e22e30e686c7f7e00005d/train/python

# Passed

def knight_vs_rook(knight, rook):
    knight_square, knight_file = knight
    rook_square, rook_file = rook
    
    knight_moves = []
    for direction in [1, -1]:
        knight_moves.extend(
            [   
                (knight_square + direction, chr(ord(knight_file) + 2)),
                (knight_square + direction, chr(ord(knight_file) - 2)),
                (knight_square + 2 * direction, chr(ord(knight_file) + 1)),
                (knight_square + 2 * direction, chr(ord(knight_file) - 1))
            ]
        )
    if knight_file == rook_file or knight_square == rook_square:
        result = "Rook"
    elif any(knight_move == rook for knight_move in knight_moves):
        result = "Knight"
    else:
        result = "None"
        
    return result

output = knight_vs_rook((6,'D'), (4,'C'))
print(output)