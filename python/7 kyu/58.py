# https://www.codewars.com/kata/5a1ebc2480171f29cf0000e5/train/python

# Passed

from math import pi

def sort_by_area(seq): 
    area_dimension_dict = dict()
    area_functions = {
        'circle': lambda radius: pi * radius ** 2,
        'rectangle': lambda dimensions: dimensions[0] * dimensions[1]
    }

    for dimensions in seq:
        if type(dimensions) in [float, int]:
            # it's a circle
            area_function = area_functions['circle']
        else:
            area_function = area_functions['rectangle']
            
        area = area_function(dimensions)
        area_dimension_dict[area] = dimensions
        
    sorted_areas = sorted(list(set(area_dimension_dict.keys())))
    sorted_dimensions = [area_dimension_dict[area] for area in sorted_areas]
    
    return sorted_dimensions

output = sort_by_area([(4.23, 6.43), 1.23, 3.444, (1.342, 3.212)])
print(output)