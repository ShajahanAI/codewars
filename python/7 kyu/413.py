# https://www.codewars.com/kata/5a8c1b06fd5777d4c00000dd/train/python

# Passed

def diagonal(matrix):
    principal_diagonal_values = [matrix[idx][idx] for idx in range(len(matrix))]
    secondary_diagonal_values = [matrix[idx][-idx - 1] for idx in range(len(matrix))]
    
    principal_score = sum(principal_diagonal_values)
    secondary_score = sum(secondary_diagonal_values)
    
    if principal_score > secondary_score:
        result = "Principal Diagonal win!"
    elif secondary_score > principal_score:
        result = "Secondary Diagonal win!"
    else:
        result = "Draw!"
        
    return result

output = diagonal([[2,2,2],
                   [4,2,6],
                   [1,8,2]])
print(output)