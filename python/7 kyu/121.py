# https://www.codewars.com/kata/5738f5ea9545204cec000155/train/python

# Passed

def count_letters_and_digits(s):
    count = 0
    for char in s:
        if char.isalpha() or char.isdigit():
            count += 1

    return count

output = count_letters_and_digits('de?=?=tttes!!t')
print(output)