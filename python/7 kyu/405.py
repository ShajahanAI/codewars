# https://www.codewars.com/kata/51c38e14ea1c97ffaf000003/train/python

# Passed

def populate_dict(keys, default):
    result = dict.fromkeys(keys, default)
    return result

output = populate_dict(["draft", "completed"], 0)
print(output)