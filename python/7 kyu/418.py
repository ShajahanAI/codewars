# https://www.codewars.com/kata/6a68ed7894f29599a1f7a248/train/python

# Passed

def split_by_mask(strng, mask):
    if sum(mask) != len(strng):
        return None
    
    result = []
    start_idx = 0
    for length in mask:
        sub_string = strng[start_idx:start_idx+length]
        result.append(sub_string)
        start_idx = start_idx + length
        
    return result

output = split_by_mask('1234567890', (3, 3, 4))
print(output)