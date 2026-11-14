# https://www.codewars.com/kata/590ee3c979ae8923bf00095b/train/python

# Passed

def color_2_grey(image):
    result = []
    for row in image:
        grayscale_row = []
        for pixel in row:
            grayscale_pixel = [round(sum(pixel) / 3)] * 3
            grayscale_row.append(grayscale_pixel)
        result.append(grayscale_row)
    
    return result

output = color_2_grey([
    [[123,231,12],[56,43,124]],
    [[78,152,76],[64,132,200]]
    ])
print(output)