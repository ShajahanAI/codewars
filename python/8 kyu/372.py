# https://www.codewars.com/kata/577a6e90d48e51c55e000217/train/python

# Passed

def hotpo(n):
    counter = 0
    while n != 1:
        counter += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
            
    return counter

output = hotpo(23)
print(output)