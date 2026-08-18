# https://www.codewars.com/kata/5a5915b8d39ec5aa18000030/train/python

# Passed

from collections import Counter

def find_missing(arr1, arr2):
    arr1_counter = Counter(arr1)
    for num in arr2:
        arr1_counter[num] -= 1
        
    for num in arr1_counter:
        if arr1_counter[num] == 1:
            result = num
            break
            
    return result  

output = find_missing([4, 3, 3, 61, 8, 8], [8, 61, 8, 3, 4])
print(output)