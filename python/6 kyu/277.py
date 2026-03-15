# https://www.codewars.com/kata/52af1f150fcae8d33d0009bc/train/python

# Passed

def ho(*args):
    result = "Ho!"
    if args:
        result = "Ho " + args[0]
        
    return result

output = ho()
print(output)