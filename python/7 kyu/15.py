# https://www.codewars.com/kata/593b1909e68ff627c9000186/train/python

# Passed

def nickname_generator(name):
    if len(name) < 4:
        return "Error: Name too short"
    
    return name[:4] if name[2] in 'aeiou' else name[:3]

output = nickname_generator("Kimberly")
print(output)
