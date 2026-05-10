# https://www.codewars.com/kata/5258b272e6925db09900386a/train/python

# Passed

def numbers(*args):
    result = all(type(arg) in [int, float] for arg in args)
    return result

output = numbers(1, 2, 3, 4)
print(output)