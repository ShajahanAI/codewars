# https://www.codewars.com/kata/56dc695b2a4504b95000004e/train/python

# Passed

def caeser(message, key):
    encrypted_text = str()
    for char in message.lower():
        if char.isalpha():
            encrypted_char_code = ord(char) + key
            if encrypted_char_code > 122:
                encrypted_char_code -= 26
        else:
            encrypted_char_code = ord(char)

        encrypted_text += chr(encrypted_char_code).upper()

    return encrypted_text

output = caeser("who are you?", 18)
print(output)