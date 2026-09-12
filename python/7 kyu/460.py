# https://www.codewars.com/kata/58b63cb2b7d86adb650000b7/train/python

# Passed

def which_bus_to_take(buses_colors, going_to_school):
    result = None
    for idx, bus_goes_to_school in enumerate(going_to_school):
        if bus_goes_to_school:
            bus_color = buses_colors[idx]
            if bus_color == "red":
                result = idx
                break
            elif result is None:
                result = idx
                
                
    return result

output = which_bus_to_take(["blue","red","red","red","blue","red","blue"], [True, False, False, False, True, True, False])
print(output)