# https://www.codewars.com/kata/5831c204a31721e2ae000294/train/python

# Passed

def swap(st):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = str()
    for char in st:
        if char.lower() in vowels:
            char = char.upper()
            
        result += char
        
    return result       

output = swap("Codewars")
print(output)