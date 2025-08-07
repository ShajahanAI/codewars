# https://www.codewars.com/kata/55ea5304685da2fb40000018/train/python

# Passed

def heggeleggleggo(word):
    vowels = set('aeiou ')
    result = str()
    for char in word:
        result += char
        if char.lower() not in vowels:
            result += "egg"

    return result

output = heggeleggleggo("code here")
print(output)