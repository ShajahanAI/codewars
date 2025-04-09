# https://www.codewars.com/kata/5a04133e32b8b998dc000089/train/python

# Passed

def solve(arr, current_array=[]):
    if arr == current_array:
        return current_array
    
    array_to_return = list()
    for idx, num in enumerate(arr):
        if idx == len(arr) - 1:
            # last element
            array_to_return.append(num)
            return solve(array_to_return, current_array=arr)
        
        if num > arr[idx + 1]:
            array_to_return.append(num)

output = solve([92,52,93,31,89,87,77,105])
print(output)
