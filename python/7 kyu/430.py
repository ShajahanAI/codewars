# https://www.codewars.com/kata/5a731b36e19d14400f000c19/train/python

# Passed

def decode_pass(pass_list, bits):
    password_from_binary = "".join(chr(int(bit, 2)) for bit in bits.split(' '))
    result = password_from_binary if password_from_binary in pass_list else False
    return result

output = decode_pass(['password123', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011')
print(output)