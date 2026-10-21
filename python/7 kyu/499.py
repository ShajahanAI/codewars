# https://www.codewars.com/kata/59859f435f5d18ede7000050/train/python

# Passed

def word_to_bin(word):
    result = []
    for char in word:
        binary_char = bin(ord(char))
        result.append("".join(binary_char.split('b')))
    
    return result

output = word_to_bin('Ruby')
print(output)