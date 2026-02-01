# https://www.codewars.com/kata/56bd9e4b0d0b64eaf5000819/train/python

# Passed

def combine(*kwargs):
    result = dict()
    for dictionary in kwargs:
        for key in dictionary:
            if key not in result:
                result[key] = 0
                
            result[key] += dictionary[key]
            
    return result

output = combine({ 'a': 10, 'b': 20, 'c': 30 }, { 'a': 3, 'c': 6, 'd': 3 })
print(output)