# https://www.codewars.com/kata/5966eeb31b229e44eb00007a/

# Passed

def vaporcode(s):
    return '  '.join([i for i in s.upper() if i != ' '])