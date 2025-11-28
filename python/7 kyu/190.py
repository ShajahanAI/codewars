# https://www.codewars.com/kata/562d8d4c434582007300004e/train/python

# Passed

def obfuscate(email):
    char_to_substitute_dict = {
                        "@": " [at] ",
                        ".": " [dot] "
                            }
    
    for char in char_to_substitute_dict:
        substitute = char_to_substitute_dict[char]
        email = email.replace(char, substitute)
        
    return email

output = obfuscate('user_name@example.com')
print(output)