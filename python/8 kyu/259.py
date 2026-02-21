# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

# Passed

def abbrev_name(name):
    first, last = name.split(' ')
    initials = first[0].upper() + "." + last[0].upper()
    return initials

output = abbrev_name("Sam Harris")
print(output)