# https://www.codewars.com/kata/590ac6b9be4dff49b0000042/train/python

# Passed

def convert(degrees): 
    degrees_val = int(degrees)
    minutes = (degrees % 1)
    
    minutes_val = int(minutes * 60)
    seconds_val = round(((minutes * 60) % 1) * 60)
    if seconds_val == 60:
        minutes_val += 1
        seconds_val = 0
        
    if minutes_val == 60:
        degrees_val += 1
        minutes_val = 0
        
    result = [degrees_val]
    if minutes_val:
        result.append(minutes_val)
        
        if seconds_val:
            result.append(seconds_val)
    else:
        if seconds_val:
            result.extend([minutes_val, seconds_val])

    return result

output = convert(40.567)
print(output)