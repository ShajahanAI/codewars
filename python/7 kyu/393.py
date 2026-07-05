# https://www.codewars.com/kata/58fd52b59a9f65c398000096/train/python

# Passed

def min_and_max(l, d, x):
    get_sum_of_digits = lambda num: sum(int(digit) for digit in str(num))
    result = []
    for num in range(l, d + 1):
        sum_of_digits = get_sum_of_digits(num)
        if sum_of_digits == x:
            result.append(num)
            
    minimal_int, maximal_int = result[0], result[-1]
    result = [minimal_int, maximal_int]
    return result

output = min_and_max(100, 200, 10)
print(output)