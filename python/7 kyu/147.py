# https://www.codewars.com/kata/5b6d065a1db5ce9b4c00003c/train/python

# Passed

def dropzone(fire, dropzones):
    calculate_distance = lambda fire, dropzone: ((fire[0] - dropzone[0]) ** 2 + (fire[1] - dropzone[1]) ** 2) ** 0.5
    current_min_distance = float("inf")
    optimal_dropzone = None
    for dropzone in dropzones:
        dist_from_fire = calculate_distance(fire, dropzone)
        if dist_from_fire < current_min_distance:
            optimal_dropzone = dropzone
            current_min_distance = dist_from_fire

    return optimal_dropzone
    
output = dropzone([6,8], [[3,2],[6,1],[7,9]])
print(output)