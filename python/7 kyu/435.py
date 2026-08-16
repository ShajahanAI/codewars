# https://www.codewars.com/kata/553f01db29490a69ff000049/train/python

# Passed

def validate_sequence(sequence):
    diff_set = {sequence[idx + 1] - sequence[idx] for idx in range(0, len(sequence) - 1)}
    result = len(diff_set) == 1
    return result

output = validate_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(output)