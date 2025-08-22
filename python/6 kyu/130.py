# https://www.codewars.com/kata/559536379512a64472000053/train/python

# Passed

def play_pass(s, n):
    result = str()
    n = n if n < 27 else n % 26
    for idx, char in enumerate(s):
        modified_char = char
        if char.isalpha():
            modified_char = modified_char.upper()
            code = ord(char) + n
            if code > 90:
                code -= 26 # circular shift

            modified_char = chr(code)
        elif char.isdigit():
            modified_char = str(9 - int(char))

        if idx % 2 == 0:
            modified_char = modified_char.upper()
        else:
            modified_char = modified_char.lower()

        result += modified_char

    result = result[::-1]
    return result    

output = play_pass("IN 2012 TWO CAMBRIDGE UNIVERSITY RESEARCHERS ANALYSED PASSPHRASES FROM THE AMAZON PAY SYSTEM...", 23)
print(output)