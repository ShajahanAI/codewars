# https://www.codewars.com/kata/6277a3342c28814667504250/train/python

# Passed

def enough_ink(image, r, g, b):
    for sub_arr in image:
        for hex_code in sub_arr:
            r_code, g_code, b_code = hex_code[:2], hex_code[2:4], hex_code[4:]
            required_red, required_green, required_blue = 255 - int(r_code, 16), 255 - int(g_code, 16), 255 - int(b_code, 16)

            r -= required_red
            g -= required_green
            b -= required_blue

            if r < 0 or g < 0 or b < 0:
                return False
        
    return True

output = enough_ink([["fefefe", "fefefe", "fefefe"], ["fefefe", "fefefe", "fefefe"], ["fefefe", "fefefe", "fefefe"]], 9, 9, 9)
print(output)