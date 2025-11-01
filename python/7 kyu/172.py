# https://www.codewars.com/kata/541629460b198da04e000bb9/train/python

# Passed

def last(*args):
    if len(args) == 1:
        elem = args[0]
        if type(elem) == int:
            return elem
        
        return elem[-1]
    
    return args[-1]

output = last(123, [4, 5, 6])
print(output)