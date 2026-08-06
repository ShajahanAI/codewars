# https://www.codewars.com/kata/594093784aafb857f0000122/train/python

# Passed

def diff(a, b):
    set_a = set(a)
    set_b = set(b)
    
    result = []
    for item in set_a:
        if item not in set_b:
            result.append(item)
            
    for item in set_b:
        if item not in set_a:
            result.append(item)
    
    result.sort()
    return result

output = diff(['a','b','z','d','e','d'], ['a','b','j','j'])
print(output)