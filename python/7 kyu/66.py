# https://www.codewars.com/kata/55a3cb91d1c9ecaa2900001b/train/python

# Passed

import math

def strong_enough(earthquake, age):
    # according to the linked wikipedia article
    # n(t) = n0 * e ^ (- l * t)
    
    # caluclating earthquake stength
    shockwaves = [sum(shockwave) for shockwave in earthquake]
    earthquake_strength = 1
    for shockwave in shockwaves:
        earthquake_strength *= shockwave
    
    # calculating building strength
    exponential_decay = 1/100
    initial_building_strength = 1000
    building_strength = initial_building_strength * math.e ** (-exponential_decay * age)
    
    return "Safe!" if building_strength > earthquake_strength else "Needs Reinforcement!"

output = strong_enough([[1,8,7],[1,3,1],[6,2,1]], 30)
print(output)