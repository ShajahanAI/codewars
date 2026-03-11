# https://www.codewars.com/kata/56f3a1e899b386da78000732/train/python

# Passed

def partlist(arr):
    parts_arr = []
    for idx in range(1, len(arr)):
        first_part = " ".join(arr[:idx])
        second_part = " ".join(arr[idx:])
        part = (first_part, second_part)
        parts_arr.append(part)
        
    return parts_arr

output = partlist(["cdIw", "tzIy", "xDu", "rThG"])
print(output)