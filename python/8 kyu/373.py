# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python

# Passed

def is_uppercase(inp):
    result = all(not char.islower() for char in inp)
    return result

output = is_uppercase("HELLO I AM DONALD")
print(output)