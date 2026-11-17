# https://www.codewars.com/kata/596b8a3fc4cb1de46b000001/train/python

# Passed

def center(strng, width, fill=' '):
    padding_length = (width - len(strng)) // 2
    if padding_length < 0:
        return strng
    
    result = padding_length * fill + strng + padding_length * fill
    if (len(strng) - width) % 2 == 1:
        result = fill + result
    
    return result

output = center("abc", 10, '_')
print(output)