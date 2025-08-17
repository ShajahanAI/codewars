# https://www.codewars.com/kata/55ee3ebff71e82a30000006a/train/python

# Passed

from string import ascii_lowercase

def title_to_number(title):
    title = title.lower()
    alphabets_to_number = {alphabet: num for num, alphabet in enumerate(ascii_lowercase, start=1)}
    result = 0
    for idx, letter in enumerate(title[::-1]):
        column_value = alphabets_to_number[letter]
        result += 26 ** idx * column_value

    return result

output = title_to_number("AA")
print(output)