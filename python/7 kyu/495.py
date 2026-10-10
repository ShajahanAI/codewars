# https://www.codewars.com/kata/56e9ac87c3e7d512bc001363/train/python

# Passed

def ascii_encrypt(plaintext):
    new_char_codes = [ord(char) + idx for idx, char in enumerate(plaintext)]
    result = "".join(chr(char_code) for char_code in new_char_codes)
    return result
    
def ascii_decrypt(encrypted):
    new_char_codes = [ord(char) - idx for idx, char in enumerate(encrypted)]
    result = "".join(chr(char_code) for char_code in new_char_codes)
    return result

output1 = ascii_encrypt("password")
output2 = ascii_decrypt("pbuv{txk")
print(output1, output2)