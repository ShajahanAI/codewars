# https://www.codewars.com/kata/578de3801499359921000130/train/python

# Passed

def two_by_two(animals):
    if len(animals) == 0:
        return False
    
    animal_to_count_dict = dict()
    for animal in animals:
        if animal not in animal_to_count_dict:
            animal_to_count_dict[animal] = 0
        
        animal_to_count_dict[animal] += 1
    
    result = dict()
    for animal in animal_to_count_dict:
        count = animal_to_count_dict[animal]
        if count >= 2:
            result[animal] = 2
    
    return result

output = two_by_two(["goat", "goat", "rabbit", "rabbit", "rabbit", "duck", "horse", "horse", "swan"])
print(output)