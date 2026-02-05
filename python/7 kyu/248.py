# https://www.codewars.com/kata/563fb342f47611dae800003c/train/python

# Passed

def trim(phrase, size):
    SUFFIX = "..."    
    if len(phrase) <= size:
        return phrase
    elif size <= 3:
        result = phrase[:size] + SUFFIX
    else:
        result = phrase[:size - 3] + SUFFIX
    
    return result

output = trim("Creating kata is fun", 14)
print(output)