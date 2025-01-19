# https://www.codewars.com/kata/57d147bcc98a521016000320/train/python

# Passed

def pillow(s):
    fridge = 'n'
    pillow = 'B'
    for i in range(len(s)):
        string = s[i]
        if fridge in string and i != len(s) - 1:
            for string in s[i + 1:]:
                if pillow in string:
                    return True
            return False
    return False

output = pillow(['n', 'B'])
print(output)