# https://www.codewars.com/kata/58b3c2bd917a5caec0000017/train/python

# Passed

def sum_groups(arr):
    result_arr = []
    is_even = lambda num: num % 2 == 0
    is_odd = lambda num: not is_even(num)
    
    had_to_sum = False
    for num in arr:
        if len(result_arr) == 0:
            result_arr.append(num)
            check_if_even = is_even(result_arr[-1])
            continue
        
        should_sum_function = is_even if check_if_even else is_odd
        if should_sum_function(num):
            result_arr[-1] += num
            had_to_sum = True
        else:
            result_arr.append(num)
            check_if_even = not check_if_even
    
    result = sum_groups(result_arr) if had_to_sum else len(result_arr)
    return result

output = sum_groups([2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9])
print(output)