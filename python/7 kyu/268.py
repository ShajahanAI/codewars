# https://www.codewars.com/kata/5a34da5dee1aae516d00004a/train/python

# Passed

def get_matrix(n):
    matrix = []
    for idx in range(n):
        row = [0] * n
        row[idx] = 1
        matrix.append(row)
        
    return matrix

output = get_matrix(3)
print(output)