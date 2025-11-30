# https://www.codewars.com/kata/559fed8454b12433ff0000a2/train/python

# Passed

def total(arr):
    if len(arr) == 1:
        total_sum = arr[0]
        return total_sum
    
    reduced_arr = []
    for idx in range(len(arr)):
        if idx == len(arr) - 1:
            break
        
        reduced_arr.append(arr[idx] + arr[idx + 1])
        
    if len(reduced_arr) > 1:
        return total(reduced_arr)

    total_sum = reduced_arr[0]
    return total_sum
    
output = total([4,4,52,23,32,1,-1])
print(output)