# https://www.codewars.com/kata/588e0f11b7b4a5b373000041/train/python

# Passed

def lowest_temp(t):
    return min([int(i) for i in t.split()]) if t.strip() else None