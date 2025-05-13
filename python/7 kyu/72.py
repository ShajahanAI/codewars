# https://www.codewars.com/kata/53921994d8f00b93df000bea/train/python

# Passed

def content_weight(bottle_weight, scale): 
    scaler = int(scale.split()[0])
    if scale.endswith("larger"):
        multiplier = scaler / (scaler + 1)
    else:
        multiplier = 1/ (scaler + 1)

    contents_weight = bottle_weight * multiplier
    return contents_weight

output = content_weight(1000, "49 times larger")
print(output)