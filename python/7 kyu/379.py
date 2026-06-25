# https://www.codewars.com/kata/54fb853b2c8785dd5e000957/train/python

# Passed

def chain(init_val, functions):
    for func in functions:
        init_val = func(init_val)
        
    return init_val

add10 = lambda x: x + 10
mul30 = lambda x: x * 30

output = chain(50, [mul30, add10])
print(output)