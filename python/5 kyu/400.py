# https://www.codewars.com/kata/526dbd6c8c0eb53254000110/train/python

# Passed

def alphanumeric(password: str) -> bool:
    result = len(password) > 0 and all(char.isalnum() for char in password)
    return result

output = alphanumeric("PassW0rd")
print(output)