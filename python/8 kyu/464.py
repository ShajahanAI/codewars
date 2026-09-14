# https://www.codewars.com/kata/572b6b2772a38bc1e700007a/train/python

# Passed

def uni_total(s):
    result = sum(ord(char) for char in s)
    return result

output = uni_total("abc")
print(output)