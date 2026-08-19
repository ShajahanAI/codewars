# https://www.codewars.com/kata/62eb800ba29959001c07dfee/train/python

# Passed

def brightest(colors):
    hex_to_decimal = lambda hex: int(hex, 16) 
    result = max(colors, key=lambda color: max(hex_to_decimal(color[idx:idx+2]) for idx in range(1, 7, 2)))
    return result

output = brightest(["#FFFFFF", "#1234FF"])
print(output)