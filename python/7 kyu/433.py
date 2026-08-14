# https://www.codewars.com/kata/6347f9715467f0001b434936/train/python

# Passed

def thin_or_fat(matrix):
    rooted_widths_sum = 0
    rooted_heights_sum = 0
    for row in matrix:
        width_sum = sum(row)
        if width_sum < 0:
            return None

        rooted_widths_sum += width_sum ** 0.5
    
    for col_idx in range(len(matrix[0])):
        height_sum = sum(matrix[row_idx][col_idx] for row_idx in range(len(matrix)))
        if height_sum < 0:
            return None
        
        rooted_heights_sum +=  height_sum ** 0.5
        
    if rooted_widths_sum > rooted_heights_sum:
        result = "fat"
    elif rooted_widths_sum < rooted_heights_sum:
        result = "thin"
    else:
        result = "perfect"
        
    return result

output = thin_or_fat([[1,3], [5,7]])
print(output)