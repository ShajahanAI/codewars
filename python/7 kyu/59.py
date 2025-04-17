# https://www.codewars.com/kata/568c3498e48a0231d200001f/train/python

# Passed

def calc_tip(p, r):
    # rounding from price to figure tip
    if p % 5 == 0:
        tip = round(p + 1, -1)
    else:
        tip = round(p, -1)
    
    # dropping the singles digit
    tip /= 10

    if r == 1:
        # the service was good
        tip += 1
    elif r == 0:
        # the service was bad
        tip -= 1 
    elif r == -1:
        # the service was terrible
        tip = int(tip / 2) - 1
    
    return max(int(tip), 0)

output = calc_tip(125, 1)
print(output)