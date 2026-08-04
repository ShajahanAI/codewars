# https://www.codewars.com/kata/57a60bad72292d3e93000a5a/train/python

# Passed

def to_acronym(inp):
    words = inp.split()
    result = str()
    for word in words:
        result += word[0].upper()
        
    return result

output = to_acronym("hyper text markup language")
print(output)