# https://www.codewars.com/kata/625ea5c1a071210065c923af/train/python

# Passed

def plastic_balance(lst):
    result = [] if lst != [0] else lst
    for idx in range(len(lst) // 2):
        sides_sum = lst[idx] + lst[len(lst) - 1 - idx]
        
        middle_arr = lst[idx + 1: len(lst) - 1 - idx]
        middle_sum = sum(middle_arr)
        
        if sides_sum == middle_sum:
            result = lst[idx:len(lst) - idx]
            break
    
    return result

output = plastic_balance([0, 104, 3, 101, 0, 111])
print(output)