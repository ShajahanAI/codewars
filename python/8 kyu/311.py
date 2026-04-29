# https://www.codewars.com/kata/568dcc3c7f12767a62000038/train/python

# Passed

def set_alarm(employed, vacation):
    result = employed and not vacation
    return result

output = set_alarm(True, False)
print(output)