# https://www.codewars.com/kata/557af4c6169ac832300000ba/train/python

# Passed

def remove_rotten(bag_of_fruits):
    if bag_of_fruits is None:
        return []    

    replaced_fruits = []
    for fruit in bag_of_fruits:
        replaced_fruit = fruit.replace("rotten", str()).lower()
        replaced_fruits.append(replaced_fruit)

    return replaced_fruits

output = remove_rotten(["apple","rottenBanana","apple"])
print(output)