# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python

# Passed

def count_sheep(n):
    sheep_sequence = [f'{sheep_count} sheep...' for sheep_count in range(1, n + 1)]
    sheep_sequence_str = ''.join(sheep_sequence)
    return sheep_sequence_str

output = count_sheep(3)
print(output)