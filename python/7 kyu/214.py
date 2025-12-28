# https://www.codewars.com/kata/5b72970db3d977e0f9000030/train/python

# Passed

def crossedwords(str1, str2):
    for letter in str2:
        if letter in str1:
            col_idx = str1.index(letter)
            row_idx = str2.index(letter)
            break
            
    crossword_rows = []
    for idx, char in enumerate(str2):
        if idx != row_idx:
            crossword_row = [" "] * len(str1)
            crossword_row[col_idx] = str2[idx]
        else:
            crossword_row = list(str1)
            
        crossword_rows.append(crossword_row)
    
    crossword_representation = "\n".join([''.join(row) for row in crossword_rows]) + "\n"
    return crossword_representation

output = crossedwords('GRAPHICAL', 'SYNTHESIS')
print(output)