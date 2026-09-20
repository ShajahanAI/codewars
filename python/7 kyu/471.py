# https://www.codewars.com/kata/589ebcb9926baae92e000001/train/python

# Passed

def convert(number):
    ascii_pairs = [number[idx:idx+2] for idx in range(0, len(number), 2)]
    chars = [chr(int(num)) for num in ascii_pairs]
    result = "".join(chars)
    return result

output = convert("676584")
print(output)