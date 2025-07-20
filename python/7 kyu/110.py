# https://www.codewars.com/kata/59b844528bcb7735560000a0/train/python

# Passed

def is_nice(arr):
    if not arr:
        return False

    nice_counterparts = set()
    for num in arr:
        if num in nice_counterparts:
            continue # nice_counterpart already exists

        if num - 1 in arr or num + 1 in arr:
            nice_counterparts.add(num - 1)
            nice_counterparts.add(num + 1)
        else:
            return False

    return True

output = is_nice([2,10,9,3])
print(output)