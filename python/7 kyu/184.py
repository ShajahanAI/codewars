# https://www.codewars.com/kata/58aa68605aab54a26c0001a6/train/python

# Passed

def distinct_digit_year(year):
    is_distinct = False
    while not is_distinct:
        year += 1
        is_distinct = len(set(str(year))) == len(str(year))
        
    return year

output = distinct_digit_year(1987)
print(output)