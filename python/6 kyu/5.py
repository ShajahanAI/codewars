# https://www.codewars.com/kata/5a0178f66f793bc5b0001728/train/python

# Hannhhahasd -> to lowercase hanhhnahasd -> {h: 4, a: 3, n: 2, s: 1, d: 1} -> 4 + 2 + 2 + 0 + 0 + 1

# Passed

def longest_palindrome(s):
    s = s.lower()
    count_dictionary = {
        char: s.count(char) for char in s
    }

    length = 0
    add_one = False
    for char in count_dictionary:
        if not char.isalnum():
            continue

        if count_dictionary[char] % 2 == 0:
            # It's an even number
            length += count_dictionary[char]
        else:
            # It's an odd number

            add_one = True
            length += count_dictionary[char] - 1
    
    return length + 1 if add_one else length

output = longest_palindrome('hananah')
print(output)

