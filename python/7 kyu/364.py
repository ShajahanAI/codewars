# https://www.codewars.com/kata/64cf34314e8a905162e32ff5/train/python

# Passed

def smallest_transform(num):
    candidates = {int(digit) for digit in str(num)}
    candidates_to_steps_required = dict()
    for candidate in candidates:
        for digit in str(num):
            steps_required = abs(int(digit) - candidate)
            if candidate not in candidates_to_steps_required:
                candidates_to_steps_required[candidate] = 0

            candidates_to_steps_required[candidate] += steps_required

    result = min(candidates_to_steps_required.values())
    return result

output = smallest_transform(1234)
print(output)