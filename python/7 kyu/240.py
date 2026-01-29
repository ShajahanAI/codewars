# https://www.codewars.com/kata/5a15a4db06d5b6d33c000018/train/python

# Passed

def sum_nested(lst):
    total_sum = 0
    for possible_num in lst:
        if type(possible_num) == list:
            total_sum += sum_nested(possible_num)
        else:
            total_sum += possible_num
            
    return total_sum

output = sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]])
print(output)