# https://www.codewars.com/kata/5a9996fa8e503f2b4a002e7a/train/python

# Passed

import math

def odd_not_prime(n):
    def is_prime(num):
        if num == 1:
            return False
        
        for possible_factor in range(2,  math.ceil(num / 2)):
            if num % possible_factor == 0:
                return False
        
        return True
    
    odd_but_not_prime_numbers = []
    for num in range(n + 1):
        if num % 2 == 0:
            # is even
            continue
            
        if not is_prime(num):
            odd_but_not_prime_numbers.append(num)
    
    result = len(odd_but_not_prime_numbers)
    return result

output = odd_not_prime(99)
print(output)