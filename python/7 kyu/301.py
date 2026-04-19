# https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d/train/python

# Passed

def halving_sum(n): 
    total_sum = 0
    divisor = 1
    while (term := n // divisor) > 0:
        total_sum += term
        divisor *= 2
    
    return total_sum

output = halving_sum(25)
print(output)