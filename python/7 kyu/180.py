# https://www.codewars.com/kata/580a4734d6df748060000045/train/python

# Passed

def is_sorted_and_how(arr):
    sorted_arr = list(sorted(arr))
    if arr == sorted_arr:
        return "yes, ascending"
    elif arr == sorted_arr[::-1]:
        return "yes, descending"
    else:
        return "no"
    
output = is_sorted_and_how([15, 7, 3, -8])
print(output)