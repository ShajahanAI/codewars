# https://www.codewars.com/kata/56b5ebaa26fd54188b000018/train/python

# Passed

def get_factors(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    return factors 

def amicable_numbers(n1,n2):
    return sum(get_factors(n1)) == n2 and sum(get_factors(n2)) == n1

output = amicable_numbers(220, 285)
print(output)
