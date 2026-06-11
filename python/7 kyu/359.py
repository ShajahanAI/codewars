# https://www.codewars.com/kata/628e3ee2e1daf90030239e8a/train/python

# Passed

def interlockable(a, b):
    a_binary = bin(a).split('b')[1]
    b_binary = bin(b).split('b')[1]
    
    result = True
    for group in zip(a_binary[::-1], b_binary[::-1]):
        if group == ('1', '1'):
            result = False
            break
            
    return result

output = interlockable(9, 4)
print(output)