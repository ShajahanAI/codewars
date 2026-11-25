# https://www.codewars.com/kata/56aaf25213edd3a88a000002/train/python

# Passed

from collections.abc import Callable

def lstzip(a: list, b: list, fn: Callable) -> list:
    result = [fn(*a_b) for a_b in zip(a, b)]
    return result

output = lstzip([1, 2, 3, 4, 5], ['a','b','c','d','e'], lambda a, b: str(a) + str(b))
print(output)