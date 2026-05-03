# https://www.codewars.com/kata/5fdb2ef8656423001c00e648/train/python

# Passed

def determine_winner(board):
    black_pieces, white_pieces = 0, 0
    for row in board:
        for piece in row:
            if piece == 'B':
                black_pieces += 1
            elif piece == 'W':
                white_pieces += 1    
    if black_pieces == white_pieces:
        result = ('T', black_pieces)
    elif black_pieces > white_pieces:
        result = ('B', black_pieces)
    else:
        result = ('W', white_pieces)

    return result

output = determine_winner([["W","W","W","B","B","B"], 
                           ["W","W","W","W","B","B"],
                           ["W","W","W","B","B","B"], 
                           ["W","X","W","B","B","B"], 
                           ["X","W","B","B","B","B"], 
                           ["W","W","B","X","B","X"]])
print(output)