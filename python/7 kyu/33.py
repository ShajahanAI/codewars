# https://www.codewars.com/kata/5eb34624fec7d10016de426e/train/python

# Passed

def martingale(bank, outcomes):
    stake = 100
    for outcome in outcomes:
        win = outcome
        if win:
            bank += stake
            stake = 100
        else:
            bank -= stake
            stake *= 2 
    
    return bank

output = martingale(1000, [1, 1, 0, 0, 1])
print(output)
