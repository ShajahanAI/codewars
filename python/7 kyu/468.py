# https://www.codewars.com/kata/58702c0ca44cfc50dc000245/train/python

# Passed

def pig_latin(word):
    result = word
    if len(word) > 3:
        result = word[1:] + word[0] + "ay"
    return result

output = pig_latin('hello')
print(output)