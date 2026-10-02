# https://www.codewars.com/kata/5bce125d3bb2adff0d000245/train/python

# Passed

def london_city_hacker(journey): 
    last_medium_is_bus = False
    cost = 0
    for tube_or_bus in journey:
        if type(tube_or_bus) == int:
            if last_medium_is_bus:
                last_medium_is_bus = False
                continue # covered via previous bus

            last_medium_is_bus = True
            cost += 1.50
        else:
            last_medium_is_bus = False
            cost += 2.40
    
    result = "£" + str(round(cost, 2))
    
    if "." not in result:
        result += ".00"
    elif len(result.split(".")[1]) == 1:
        result += "0"
    
    return result

output = london_city_hacker(['Piccadilly', 56, 93, 243])
print(output)