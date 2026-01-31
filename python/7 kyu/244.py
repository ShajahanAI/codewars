# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python

# Passed

def solve(s):
    uppercase_letters = 0
    lowercase_letters = 0
    
    for char in s:
        if char.isupper():
            uppercase_letters += 1
        elif char.islower():
            lowercase_letters += 1
            
    if uppercase_letters > lowercase_letters:
        s = s.upper()
    else:
        s = s.lower()
        
    return s

output = solve("CODe")
print(output)