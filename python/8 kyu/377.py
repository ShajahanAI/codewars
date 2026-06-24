# https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python

# Passed

def whatday(num):
    day_number_to_day_dict = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    
    result = day_number_to_day_dict.get(num, "Wrong, please enter a number between 1 and 7")
    return result

output = whatday(3)
print(output)