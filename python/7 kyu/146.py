# https://www.codewars.com/kata/57e17750621bca9e6f00006f/train/python

# Passed

def hex_color(codes):
    if not codes or codes == "000 000 000":
        return "black"

    red, green, blue = codes.split()
    red, green, blue = int(red), int(green), int(blue)
    if len(set([red, green, blue])) == 1:
        return "white"
    else:
        if red == blue and red > green: # magenta
            return 'magenta'
        elif green == red and green > blue: # yellow
            return 'yellow'
        elif blue == green and blue > red: # cyan
            return 'cyan'
        else:
            # one color has major concentration
            concentration_colour_dict = {
                red: 'red',
                green: 'green',
                blue: 'blue'
            }

            return concentration_colour_dict[max(red, green, blue)]
        
output = hex_color('027 100 100')
print(output)