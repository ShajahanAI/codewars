# https://www.codewars.com/kata/59547688d8e005759e000092/train/python

# Passed

def distribution_of(golds):
    a_b_holdings = [0, 0]
    idx = 0
    while golds:
        gold_amt = max(golds[0], golds[-1])
        if golds[0] == gold_amt:
            del golds[0]
        else:
            del golds[-1]

        a_b_holdings[idx] += gold_amt
        idx = -1 if idx == 0 else 0

    return a_b_holdings

output = distribution_of([4,7,2,9,5,2])
print(output)