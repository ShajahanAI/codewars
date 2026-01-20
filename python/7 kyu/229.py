# https://www.codewars.com/kata/559cc2d2b802a5c94700000c/train/python

# Passed

def consecutive(arr):
    if len(arr) == 0 or len(arr) == 1:
        return 0
    
    arr.sort()
    range_differences = []
    for idx in range(len(arr)):
        if idx == len(arr) - 1:
            break
            
        range_difference = arr[idx + 1] - arr[idx] - 1
        range_differences.append(range_difference)
        
    result = sum(range_differences)
    return result

output = consecutive([4, 8, 6])
print(output)