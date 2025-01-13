# https://www.codewars.com/kata/5286b2e162056fd0cb000c20/solutions/python

# Passed

# 21 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
def collatz(n, sequence_parts=[], initialize_sequence_parts=True):
    if initialize_sequence_parts:
        sequence_parts = []
    
    if n < 0:
        return []

    if n == 1:
        sequence_parts += [1]
        return "->".join(map(str, sequence_parts))

    sequence_parts.append(n)
    if n % 2 == 0:  
        # n is even      
        return collatz(n // 2, sequence_parts, False)
    else:
        # n is odd
        return collatz(3 * n + 1, sequence_parts, False)
    
output = collatz(3)
print(output)