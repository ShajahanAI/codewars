# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

# Passed

def likes(names):
    if len(names) == 0:
        prefix = "no one"
    elif len(names) == 1:
        prefix = names[0]
    elif len(names) == 2:
        prefix = " and ".join(names)
    else:
        prefix = ", ".join(names[:2]) + f" and {names[-1] if len(names) == 3 else (str(len(names) - 2) + ' others')}"

    result = prefix + (" likes this" if len(names) in [0, 1] else " like this")
    return result

output = likes(['Alex', 'Jacob', 'Mark', 'Max'])
print(output)