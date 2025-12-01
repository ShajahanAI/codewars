# https://www.codewars.com/kata/588856a82ffea640c80000cc/train/python

# Passed

def array_previous_less(arr):
    result = [None] * len(arr)
    for idx in range(len(arr)):
        prev_min_item = -1
        curr_item = arr[idx]
        if idx != 0:
            for i in range(idx + 1):
                if arr[idx - i] < arr[idx]:
                    prev_min_item = arr[idx - i]
                    break

        result[idx] = prev_min_item
        
    return result

output = array_previous_less([2, 2, 1, 3, 4, 5, 5, 3])
print(output)