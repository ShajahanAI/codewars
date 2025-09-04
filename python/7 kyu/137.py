# https://www.codewars.com/kata/5250a89b1625e5decd000413/train/python

# Passed

def flatten(lst):
    result = list()
    for elem in lst:
        if type(elem) == list:
            result.extend(elem)
        else:
            result.append(elem)

    return result

output = flatten([[1,2,3], ["a", "b", "c"], [1,2,3]])
print(output)