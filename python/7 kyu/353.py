# https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/python

# Passed

def calc(x):
    character_codes = [str(ord(character)) for character in x]
    total1 = int("".join(character_codes))
    total2 = int(str(total1).replace("7", "1"))
    
    get_digits_sum = lambda num: sum([int(digit) for digit in str(num)])
    
    result = get_digits_sum(total1) - get_digits_sum(total2)
    return result

output = calc('abcdef')
print(output)