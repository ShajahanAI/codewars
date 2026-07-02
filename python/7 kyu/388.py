# https://www.codewars.com/kata/6a3ce10b3ac2038a3741c9b8/train/python

# Passed

from math import pi

def tire_rotations(tire_size: str, distance_km: float) -> float:
    distance_mm = distance_km * 10 ** 6
    thread_width_in_mm, aspect_ratio_rim_diameter_in_inches = tire_size.split("/")    
    thread_width_in_mm = float(thread_width_in_mm)
    
    possible_split_characters = ['ZR', 'R', 'B', 'D']
    for possible_split_character in possible_split_characters:
        if possible_split_character in aspect_ratio_rim_diameter_in_inches:
            split_char = possible_split_character
            break
    
    aspect_ratio, rim_diameter_in_inches = [float(num) for num in aspect_ratio_rim_diameter_in_inches.split(split_char)]
    sidewall_height_in_mm = thread_width_in_mm * aspect_ratio / 100
    rim_diameter_in_mm = rim_diameter_in_inches * 25.4

    tire_diameter_in_mm = sidewall_height_in_mm * 2 + rim_diameter_in_mm
    tire_circumference_in_mm = 2 * pi * (tire_diameter_in_mm / 2)
    
    rotations_required = distance_mm / tire_circumference_in_mm
    return rotations_required

output = tire_rotations("205/55R16", 110)
print(output)