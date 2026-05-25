# https://www.codewars.com/kata/5932c94f6aa4d1d786000028/train/python

# Passed

def perfect_roots(n):
    root_to_take_arr = [2, 4, 8]
    for root_to_take in root_to_take_arr:
        val = n ** (1/root_to_take)
        if int(val) != val:
            result = False
            break
    else:
        result = True
        
    return result

output = perfect_roots(256)
print(output)