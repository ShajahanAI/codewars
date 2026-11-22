# https://www.codewars.com/kata/56dc83840a10fee472000ca1/train/python

# Passed

def is_fibo(a: int, b: int, f: int) -> bool:
    current_fibo = a + b
    last_term = b
    result = f in [a, b, current_fibo]
    while current_fibo < f:
        current_fibo += last_term
        last_term = current_fibo - last_term
        if current_fibo == f:
            result = True
    
    return result

output = is_fibo(4, 5, 23)
print(output)