# https://www.codewars.com/kata/583ade15666df5a64e000058/train/python

# Passed

def evens_and_odds(n):
    if n % 2 == 0:
        result = bin(n).split('b')[-1]
    else:
        result = hex(n).split('x')[-1]
        
    return result

output = evens_and_odds(8172381723)
print(output)