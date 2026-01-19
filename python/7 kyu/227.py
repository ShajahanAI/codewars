# https://www.codewars.com/kata/55caef80d691f65cb6000040/train/python

# Passed

def geometric_sequence_elements(a, r, n):
    sequence = [str(a * r ** pow) for pow in range(n)]
    sequence_str = ", ".join(sequence)
    return sequence_str

output = geometric_sequence_elements(2, 3, 5)
print(output)