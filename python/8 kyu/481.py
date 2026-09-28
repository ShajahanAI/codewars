# https://www.codewars.com/kata/56170e844da7c6f647000063/train/python

# Passed

def people_with_age_drink(age):
    if age < 14:
        drink = "toddy"
    elif age < 18:
        drink = "coke"
    elif age < 21:
        drink = "beer"
    else:
        drink = "whisky"
    
    result = f"drink {drink}"
    return result

output = people_with_age_drink(15)
print(output)