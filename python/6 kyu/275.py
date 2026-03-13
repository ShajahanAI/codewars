# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python

# Passed

def clean_string(s):
    modified_characters = []
    for char in s:
        if char == "#":
            if len(modified_characters) == 0:
                continue

            modified_characters.pop()
        else:
            modified_characters.append(char)

    result = "".join(modified_characters)
    return result

output = clean_string('abc#d##c')
print(output)