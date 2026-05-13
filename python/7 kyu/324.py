# https://www.codewars.com/kata/582642b1083e12521f0000da/train/python

# Passed

def array_mash(a, b):
    result = []
    for idx in range(len(a)):
        result.extend([a[idx], b[idx]])
        
    return result

output = array_mash([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])
print(output)