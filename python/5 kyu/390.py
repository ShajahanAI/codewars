# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

# Passed

def cakes(recipe, available):
    result = 0
    can_bake_cakes = True
    while can_bake_cakes:
        for ingredient in recipe:
            quantity_required = recipe[ingredient]
            available[ingredient] = available.get(ingredient, 0) - quantity_required
            if available[ingredient] < 0:
                can_bake_cakes = False
                break
        else:
            result += 1
            
    return result

output = cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
print(output)