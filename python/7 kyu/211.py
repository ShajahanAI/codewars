# https://www.codewars.com/kata/5bbd279c8f8bbd5ee500000f/train/python

# Passed

def find_screen_height(width, ratio):
    height_and_width = [int(num) for num in ratio.split(":")[::-1]]
    height = width * height_and_width[0] / height_and_width[1] # h = w * (h/w)
    height = int(height)
    screen_dimensions = f"{width}x{height}"
    return screen_dimensions

output = find_screen_height(1920, "16:9")
print(output)