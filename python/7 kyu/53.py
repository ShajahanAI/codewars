# https://www.codewars.com/kata/5a090c4e697598d0b9000004/train/python

# Passed

def solve(arr):
    res = list()
    arr.sort()
    total_numbers = len(arr)
    for idx in range(total_numbers // 2):
        res.extend([arr[total_numbers - 1 - idx], arr[idx]])

    if total_numbers % 2:
        # we have odd number of total numbers
        res.append(arr[total_numbers//2])

    return res

output = solve([15,11,10,7,12])
print(output)