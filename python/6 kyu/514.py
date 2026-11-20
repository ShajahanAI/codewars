# https://www.codewars.com/kata/587309155cfd6b9fb60000a0/train/python

# Passed

def money_value(s):
    is_negative = "-" in s
    modified_string = s.replace('$', str()).replace(' ', str()).replace('-', str())
    result = float(modified_string) if modified_string else 0.0
    if is_negative:
        result *= -1
    
    return result

output = money_value(" $5.67")
print(output)