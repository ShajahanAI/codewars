# https://www.codewars.com/kata/54fdadc8762e2e51e400032c/train/python

# Passed

def my_parse_int(strn):
    result = int(strn.strip()) if strn.strip().isdigit() else "NaN"
    return result

output = my_parse_int("1")
print(output)