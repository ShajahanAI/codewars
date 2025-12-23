# https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python

# Passed

def capitals(word):
    capital_indices = []
    for idx, letter in enumerate(word):
        if letter.isupper():
            capital_indices.append(idx)
            
    return capital_indices

output = capitals('CodEWaRs')
print(output)