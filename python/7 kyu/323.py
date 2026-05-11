# https://www.codewars.com/kata/5a8059b1fd577709860000f6/train/python

# Passed

def alphabetic(s):
    s = s.lower()
    result = True
    for idx in range(len(s) - 1):
        if ord(s[idx]) > ord(s[idx + 1]):
            result = False
            break
        
    return result

output = alphabetic('door')
print(output)