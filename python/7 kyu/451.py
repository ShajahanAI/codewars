# https://www.codewars.com/kata/59952e17f902df0e5f000078/train/python

# Passed

def passer_rating(att, yds, comp, td, ints):
    a = ((comp / att) - 0.3) * 5
    b = ((yds / att) - 3) * 0.25
    c = (td / att) * 20
    d = 2.375 - ((ints / att) * 25)
    
    normalize_calculation = lambda calculation: min(2.375, max(calculation, 0))
    result = round((sum(normalize_calculation(calculation) for calculation in (a, b, c, d)) / 6) * 100, 1)
    return result

output = passer_rating(432, 3554, 291, 28, 2)
print(output)