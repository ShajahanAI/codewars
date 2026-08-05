# https://www.codewars.com/kata/59b0ab12cf3395ef68000081/train/python

# Passed

def to_12_hour_time(time_string):
    hours, minutes = int(time_string[:2]), int(time_string[2:])
    is_am = not hours >= 12
    if hours == 0:
        hours = 12
    elif hours >= 13:
        hours -= 12
    
    result = f"{hours}:{str(minutes).zfill(2)} {'am' if is_am else 'pm'}"
    return result

output = to_12_hour_time('2145')
print(output)