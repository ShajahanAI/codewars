# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

# Passed

def find_even_index(arr):
    for idx in range(len(arr)):
        left_sum = sum(arr[:idx])
        right_sum = sum(arr[idx + 1:])
        
        if left_sum == right_sum:
            result = idx
            break
    else:
        result = -1
    
    return result

output = find_even_index([1, 2, 3, 4, 3, 2, 1])
print(output)