# https://www.codewars.com/kata/57ae18c6e298a7a6d5000c7a/train/python

# Passed

def replace_all(obj, find, replace):
    items = list(obj) if type(obj) == str else obj
    for idx, item in enumerate(items):
        if item == find:
            items[idx] = replace
            
    if type(obj) == str:
        res = ''.join(items)
    else:
        res = obj
    
    return res

output = replace_all([1, 1, 2], 1, 2)
print(output)        