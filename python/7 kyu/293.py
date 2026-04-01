# https://www.codewars.com/kata/56a4872cbb65f3a610000026/train/python

# Passed

def max_rot(n):
    rot_string = lambda string: string[1:] + string[0]
    digits_count = len(str(n))
    numbers = [n]
    for idx in range(digits_count):
        n = int(str(n)[:idx] + rot_string(str(n)[idx:]))
        numbers.append(n)
    
    max_num = max(numbers)
    return max_num

output = max_rot(38458215)
print(output)