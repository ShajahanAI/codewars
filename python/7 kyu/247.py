# https://www.codewars.com/kata/5840586b5225616069000001/train/python

# Passed

def highest_value(a, b):
    calculate_value = lambda string: sum(ord(char) for char in string)
    a_value = calculate_value(a)
    b_value = calculate_value(b)
    
    more_valuable_string = b if b_value > a_value else a
    return more_valuable_string

output = highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567")
print(output)