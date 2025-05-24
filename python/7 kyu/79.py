# https://www.codewars.com/kata/55cb000321ca31039e00007d/train/python

# Passed

def geometric_sequence_sum(a, r, n):
    sequence_sum = a
    current_term = a
    for _ in range(1, n):
        term_value = r * current_term
        current_term = term_value
        sequence_sum += term_value

    return sequence_sum

output = geometric_sequence_sum(2, 3, 5)
print(output)