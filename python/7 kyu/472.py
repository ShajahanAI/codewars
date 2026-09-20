# https://www.codewars.com/kata/65126d52a5de2b11c94096d2/train/python

# Passed

def closing_in_sum(n):
    digits = list(str(n))
    pairs = [int(digits[idx] + digits[-idx - 1]) for idx in range(len(digits) // 2)]
    
    if len(digits) % 2 == 1:
        pairs.append(int(digits[len(digits) // 2]))
    
    result = sum(pairs)
    return result

output = closing_in_sum(5332824166496569)
print(output)