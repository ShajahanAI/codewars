# https://www.codewars.com/kata/580a0347430590220e000091/train/python

# Passed

def area(d, l): 
    if d <= l:
        return "Not a rectangle"
    
    b = (d ** 2 - l ** 2) ** 0.5
    result = round(l * b, 2)
    return result

output = area(5, 4)
print(output)