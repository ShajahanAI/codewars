# https://www.codewars.com/kata/64fd5072fa88ae669bf15342/train/python

# Passed

def tree_photography(lst):
    def get_max_tree_view(arr):
        max_num = None
        max_tree_view = 0
        for num in arr:
            if max_num is None or num > max_num:
                max_num = num
                max_tree_view += 1
        
        return max_tree_view
    
    left_max_tree_view = get_max_tree_view(lst)
    right_max_tree_view = get_max_tree_view(lst[::-1])
    
    if left_max_tree_view > right_max_tree_view:
        result = "left"
    else:
        result = "right"
    
    return result

output = tree_photography([1, 1, 2, 2, 2, 2, 3])
print(output)