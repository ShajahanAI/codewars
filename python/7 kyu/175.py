# https://www.codewars.com/kata/57873ab5e55533a2890000c7/train/python

# Passed

def time_correct(t):
    if t is None:
        return None
    
    if t == str():
        return ""
    
    hours_minutes_seconds = t.split(":")
    if len(hours_minutes_seconds) != 3:
        return None
    
    hours, minutes, seconds = hours_minutes_seconds
    if not hours.isdigit() or not minutes.isdigit() or not seconds.isdigit():
        return None
    
    if not(len(hours) == 2 and len(minutes) == 2 and len(seconds) == 2):
        return None
    
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    if seconds > 59:
        minutes += seconds // 60
        seconds %= 60
        
    if minutes > 59:
        hours += minutes // 60
        minutes %= 60
        
    if hours > 23:
        hours %= 24
        
    
    hours, minutes, seconds = str(hours), str(minutes), str(seconds)
    if len(hours) == 1:
        hours = "0" + hours
        
    if len(minutes) == 1:
        minutes = "0" + minutes
        
    if len(seconds) == 1:
        seconds = "0" + seconds
    
    corrected_time = ":".join([hours, minutes, seconds])
    return corrected_time

output = time_correct("11:70:10")
print(output) 