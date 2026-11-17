# https://www.codewars.com/kata/5865cff66b5699883f0001aa/train/python

# Passed

def to_time(seconds):
    hours = seconds // (60 * 60)
    minutes = (seconds - hours * 60 * 60) // 60
    
    result = f"{hours} hour(s) and {minutes} minute(s)"
    return result

output = to_time(323500)
print(output)