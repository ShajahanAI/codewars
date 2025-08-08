# https://www.codewars.com/kata/5a0be7ea8ba914fc9c00006b/train/python

# Passed

def sakura_fall(v):
    if v <= 0:
        return 0

    time_in_seconds = (5 * 80) / v
    return time_in_seconds

output = sakura_fall(10)
print(output)