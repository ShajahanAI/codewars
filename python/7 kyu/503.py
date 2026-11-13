# https://www.codewars.com/kata/54c91b5228ec4c3b5900036e/train/python

# Passed

def center(mat):
    if len(mat) % 2 == 0:
        return None
    
    center_row_idx = len(mat) // 2
    center_row = mat[center_row_idx]
    
    if len(center_row) % 2 == 0:
        return None
    
    center_elem_idx = len(center_row) // 2
    result = center_row[center_elem_idx]
    return result

output = center([[5,1,3], [6,2,6], [7,4,5]])
print(output)