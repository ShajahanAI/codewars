# https://www.codewars.com/kata/522551eee9abb932420004a0/train/python

# Passed

def nth_fib(n, memo=dict()):
    if n in memo:
        return memo[n]
    
    if n in [0, 1]:
        return 0
    elif n == 2:
        return 1
    
    fibonnaci_number = nth_fib(n - 1, memo=memo) + nth_fib(n - 2, memo=memo)
    memo[n] = fibonnaci_number
    
    return fibonnaci_number 

output = nth_fib(20)
print(output)