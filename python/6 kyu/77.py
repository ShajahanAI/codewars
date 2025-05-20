# https://www.codewars.com/kata/55208f16ecb433c5c90001d2/train/python

# Passed

def trace(matrix):
    if not matrix or not all([len(row) == len(matrix) for row in matrix]):
        # matrix is empty or is not square
        return None

    trace_value = 0
    for idx in range(len(matrix)):
        trace_value += matrix[idx][idx]
    
    return trace_value

output = trace([[1,2,3], [4,5,6], [7,8,9]])
print(output)