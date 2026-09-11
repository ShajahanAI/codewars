# http://codewars.com/kata/58e0f0bf92d04ccf0a000010/train/python

# Passed

def lost_sheep(friday,saturday,total):
    friday_total = sum(friday)
    saturday_total = sum(saturday)
    
    result = total - (friday_total + saturday_total)
    return result

output = lost_sheep([3, 1, 2], [4, 5], 21)
print(output)