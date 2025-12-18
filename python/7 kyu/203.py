# https://www.codewars.com/kata/56f7493f5d7c12d1690000b6/train/python

# Passed

def mean(lst):
    integers = []
    characters = []
    for char in lst:
        if char.isdigit():
            integers.append(int(char))
        else:
            characters.append(char)
            
    mean = sum(integers) / len(integers)
    concatenated_string = "".join(characters)
    
    result = [mean, concatenated_string]
    return result

output = mean(["u", "6", "d", "1", "i", "w", "6", "s", "t", "4", "a", "6", "g", "1", "2", "w", "8", "o", "2", "0"])
print(output)