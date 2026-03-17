# https://www.codewars.com/kata/5641275f07335295f10000d0/train/python

# Passed

def split_the_bill(x):
    average = sum(x.values()) / len(x)
    result = {
        person: round(spend_amt - average, 2) for person, spend_amt in x.items()
    }
    
    return result

output = split_the_bill({'A': 20, 'B': 15, 'C': 10})
print(output)