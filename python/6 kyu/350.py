# https://www.codewars.com/kata/56cf0eb69e14db4897000b97/train/python

# Passed

def goldbach(even_number):
    def is_prime(n):
        is_prime = n != 1
        for num in range(2, (n//2) + 1):
            if n % num == 0:
                is_prime = False
                break
        
        return is_prime
    
    all_primes = {num for num in range(even_number) if is_prime(num)}
    all_pairs = []
    seen = set()
    for num in range(even_number):
        if num not in all_primes or (even_number - num) not in all_primes:
            continue

        if num in seen:
            continue
            
        pair = sorted([num, even_number - num])
        seen.update(pair)
        all_pairs.append(pair)

    all_pairs.sort(key=lambda x: x[0])
    return all_pairs

output = goldbach(10)
print(output)