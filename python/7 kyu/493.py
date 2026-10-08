# https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/python

# Passed

def solve(s):
    result = [0, 0, 0, 0]
    for char in s:
        if char.isupper():
            result[0] += 1
        elif char.islower():
            result[1] += 1
        elif char.isdigit():
            result[2] += 1
        else:
            result[3] += 1
    
    return result

output = solve("bgA5<1d-tOwUZTS8yQ")
print(output)