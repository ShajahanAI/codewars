# https://www.codewars.com/kata/5aca48db188ab3558e0030fa/train/python

# Passed

def calc_type(a, b, res):
    calculations = {
        'addition': lambda a, b : a + b,
        'subtraction': lambda a, b : a - b,
        'division': lambda a, b : a / b,
        'multiplication': lambda a, b : a * b,
    }
    
    for calculation in calculations:
        calculate = calculations[calculation]
        if calculate(a, b) == res:
            return calculation
        
output = calc_type(1, 2, 3)
print(output)