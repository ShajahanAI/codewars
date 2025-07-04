# https://www.codewars.com/kata/562e6df5cf2d3908ad00019e/train/python

# Passed

def separate_liquids(glass):
    if len(glass) == 0:
        return [] # empty glass

    density_dict = {
        "H": 1.36, # honey
        "W": 1.00, # water
        "A": 0.87, # alcohol
        "O": 0.80, # oil
    }

    glass_contents = []
    for row in glass:
        glass_contents.extend(row)

    glass_contents.sort(key=lambda liquid: density_dict[liquid])
    glass_width = len(glass[0])

    layered_glass = []
    idx = 0
    while idx < len(glass_contents):
        layer = glass_contents[idx:idx+glass_width]
        layered_glass.append(layer)
        idx += glass_width    
    
    return layered_glass

output = separate_liquids([['H', 'H', 'W', 'O'],['W','W','O','W'],['H','H','O','O']])
print(output)