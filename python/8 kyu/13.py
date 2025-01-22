# https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python

# Passed

def cookie(x):
    if type(x) == str:
        cookie_eater = 'Zach'
    elif type(x) == float or type(x) == int:
        cookie_eater = "Monica"
    else:
        cookie_eater = "the dog"

    return f"Who ate the last cookie? It was {cookie_eater}!"

output = cookie('hi')
print(output)