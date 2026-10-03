# https://www.codewars.com/kata/649c4012aaad69003f1299c1/train/python

# Passed

def rgb_to_grayscale(color):
    r, g, b = color[1:3], color[3:5], color[5:]
    luminance = 0.299 * int(r, 16) + 0.587 * int(g, 16) + 0.114 * int(b, 16)
    
    grayscale_component = hex(round(luminance)).split("x")[-1]
    
    result = "#" + grayscale_component.zfill(2).upper() * 3
    return result

output = rgb_to_grayscale("#00FF00")
print(output)