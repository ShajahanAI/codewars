# https://www.codewars.com/kata/58249d08b81f70a2fc0001a4/train/python

# Passed

def closest_multiple_10(i):
    remainder = i % 10
    if remainder < 5:
        result = i // 10 * 10
    else:
        result = (i // 10 + 1) * 10
    
    return result

output = closest_multiple_10(54)
print(output)