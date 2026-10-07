# https://www.codewars.com/kata/58c9322bedb4235468000019/train/python

# Passed

def is_very_even_number(n):
    n_str = str(n)
    if len(n_str) == 1:
        result = n % 2 == 0 
    else:
        new_number = sum(map(int, n_str))
        result = is_very_even_number(new_number)
    
    return result

output = is_very_even_number(222)
print(output)