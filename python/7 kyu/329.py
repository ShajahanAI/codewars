# https://www.codewars.com/kata/56e3cd1d93c3d940e50006a4/train/python 

# Passed

def make_valley(arr):
    descending_arr = sorted(arr, reverse=True)
    left_wing, right_wing = [], []
    for idx in range(len(descending_arr)):
        if idx % 2 == 0:
            left_wing.append(descending_arr[idx])
        else:
            right_wing.append(descending_arr[idx])
            
    right_wing = right_wing[::-1]
    result = left_wing + right_wing
    return result

output = make_valley([17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1])
print(output)