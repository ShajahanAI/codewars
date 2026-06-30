# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python

# Passed

def find_needle(haystack):
    result = None
    for idx, elem in enumerate(haystack):
        if elem == "needle":
            result = f"found the needle at position {idx}"
            break
    
    return result

output = find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])
print(output)