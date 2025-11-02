# https://www.codewars.com/kata/5a005f4fba2a14897f000086/train/python

# Passed

from string import ascii_lowercase

def sum_it_up(numbers_with_bases):
    result = 0
    letters_to_idx_dict = {letter: idx for idx, letter in enumerate(ascii_lowercase)}
    for info in numbers_with_bases:
        number, base = info
        for pow, num in enumerate(number[::-1]):
            if not num.isdigit():
                num = 10 + letters_to_idx_dict[num.lower()]
            result += base ** pow * int(num)
            
    return result

output = sum_it_up([["ABC",16], ["11",2]])
print(output)