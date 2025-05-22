# https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/python

# Passed

def reverse_letter(st):
    result = str()
    for char in st[::-1]:
        if char.isalpha():
            result += char
    return result

output = reverse_letter("ultr53o?n")
print(output)