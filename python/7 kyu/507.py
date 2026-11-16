# https://www.codewars.com/kata/5681bc8d17af37f50e000015/train/python

# Passed

def primes(start: int, end: int) -> list[int] | None:
    def is_prime(num):
        if num <= 1:
            return False
        
        for possible_factor in range(2, num // 2 + 1):
            if num % possible_factor == 0:
                return False
        
        return True
    
    result = []
    for num in range(start, end + 1):
        if is_prime(num):
            result.append(num)
    
    result = result if result else None
    
    return result

output = primes(1, 100)
print(output)