# https://www.codewars.com/kata/5603a4dd3d96ef798f000068/train/python

# Passed

def share_price(invested, changes):
    for change in changes:
        invested *= (100 + change)/100

    invested = str(float(round(invested, 2)))
    if len(invested.split(".")[-1]) != 2:
        invested += '0'

    return invested

output = share_price(1000, [0, 2, 3, 6])
print(output)