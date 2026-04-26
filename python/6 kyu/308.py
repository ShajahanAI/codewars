# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

# Passed

def find_missing_letter(chars):
    missing_letter = None
    for idx in range(len(chars) - 1):
        letter_1, letter_2 = chars[idx], chars[idx + 1]
        code_difference = ord(letter_2) - ord(letter_1)
        if code_difference != 1:
            missing_letter = chr(ord(letter_1) + 1)
            break
            
    return missing_letter

output = find_missing_letter(['O','Q','R','S'])
print(output)