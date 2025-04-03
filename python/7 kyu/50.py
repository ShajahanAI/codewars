# https://www.codewars.com/kata/564ab935de55a747d7000040/train/python

# Passed

def remove(text, what):
    for char in what:
        for _ in range(what[char]):
            characters = list(text)
            try:
                characters.remove(char)
            except Exception:
                break
                
            text = ''.join(characters)
            
    return text

output = remove('this is a string',{'t':1, 'i':2})
print(output)