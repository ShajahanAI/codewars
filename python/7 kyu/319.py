# https://www.codewars.com/kata/5a0b72484bebaefe60001867/train/python

# Passed

def distance(p1, p2):
    arr_length = len(p1)
    if arr_length == 0 or any(len(arr) != arr_length for arr in [p1, p2]):
        return -1
    
    diff_squares = [(p1[idx] - p2[idx]) ** 2 for idx in range(len(p1))]
    distance = sum(diff_squares) ** 0.5
    return distance

output = distance([2,1,3,1], [2,0,2,-1])
print(output)