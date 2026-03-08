# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

# Passed

def is_isogram(string):
    whether_isogram = len(set(string.lower())) == len(string.lower())
    return whether_isogram

output = is_isogram("Dermatoglyphics")
print(output)