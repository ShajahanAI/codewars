# https://www.codewars.com/kata/55cc20eb943f1d8b11000045/train/python

# Passed

def x(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]
    start_column, end_column = 0, -1
    for row_idx in range(n):
        row = matrix[row_idx]
        row[start_column] = 1
        row[end_column] = 1
        start_column += 1
        end_column -= 1

    return matrix

output = x(5)
print(output)