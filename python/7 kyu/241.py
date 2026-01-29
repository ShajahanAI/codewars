# https://www.codewars.com/kata/5b5e0ef007a26632c400002a/train/python

# Passed

def elements_sum(arr, d=0):
    total_sum = 0
    start_idx = len(arr) - 1
    for sub_arr in arr:
        if start_idx < len(sub_arr):
            total_sum += sub_arr[start_idx]
        else:
            total_sum += d
        
        if start_idx == 0:
            break
            
        start_idx -= 1
        
    return total_sum

output = elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], [9, 8, 7, 4]])
print(output)