# https://www.codewars.com/kata/58a6841442fd72aeb4000080/train/python

# Passed

def similarity(a, b):
    set_a, set_b = set(a), set(b)
    intersection_length = len(set_a & set_b)
    union_length = len(set_a | set_b)
    
    result = intersection_length / union_length
    return result

output = similarity([1, 2, 4, 6, 7], [2, 3, 4, 7])
print(output)