# https://www.codewars.com/kata/55caf1fd8063ddfa8e000018/train/python

# Passed

def arithmetic_sequence_elements(a, d, n):
    sequence = []
    for _ in range(n):
        sequence.append(str(a))
        a += d
        
    result = ", ".join(sequence)
    return result

output = arithmetic_sequence_elements(1, 2, 5)
print(output)