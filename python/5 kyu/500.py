# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

# Passed

def rgb(r, g, b):
    to_hex = lambda decimal_val: hex(min(max(0, decimal_val), 255)).split("x")[-1].zfill(2).upper()
    result = "".join(map(to_hex, [r, g, b]))
    return result

output = rgb(254, 253, 252)
print(output)