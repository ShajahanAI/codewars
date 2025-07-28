# https://www.codewars.com/kata/57de78848a8b8df8f10005b1/train/python

# Passed

def how_much_coffee(events):
    valid_events = {'cw', 'dog', 'cat', 'movie'}
    coffee_count = 0
    for event in events:
        if event.lower() in valid_events:
            if event.isupper(): 
                # we need more coffee
                coffee_count += 2
            else:
                coffee_count += 1

    return "You need extra sleep" if coffee_count > 3 else coffee_count

output = how_much_coffee(['cw','CAT'])
print(output)