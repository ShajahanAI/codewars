# https://www.codewars.com/kata/5a1e6323ffe75f71ae000026/train/python

# Passed

def is_turing_equation(s):
    get_proper_num = lambda num: int(num[::-1])
    first_num, second_num, total_sum = list(map(get_proper_num, s.replace("=", "+").split("+")))
    result = first_num + second_num == total_sum
    return result

output = is_turing_equation('73+42=16')
print(output)