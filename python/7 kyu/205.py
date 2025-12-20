# https://www.codewars.com/kata/5ae7e3f068e6445bc8000046/train/python

# Passed

def next_happy_year(year):
    year += 1
    while len(str(year)) != len(set(str(year))):
        year += 1
        
    return year

output = next_happy_year(1987)
print(output)