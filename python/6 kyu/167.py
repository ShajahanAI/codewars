# https://www.codewars.com/kata/520d9c27e9940532eb00018e/train/python

# Passed

def solution(*args):
    contains_duplicate_args = len(args) != len(set(args))
    return contains_duplicate_args
    
output = solution(1, 2, 3, 1, 2)
print(output)