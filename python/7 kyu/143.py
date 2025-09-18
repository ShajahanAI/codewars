# https://www.codewars.com/kata/68c31c23f0aee823d84cdd42/train/python

# Passed

def set_the_alarms_up(time, n):
    current_hours, current_minutes = [int(i) for i in time.split(":")]
    time_in_minutes = current_hours * 60 + current_minutes
    alarms = [time]
    for _ in range(n - 1):
        time_in_minutes += 5
        if time_in_minutes >= 24 * 60:
            time_in_minutes -= 24 * 60  
        
        hours_part = str(time_in_minutes // 60)
        minutes_part = str(time_in_minutes % 60)
        
        if len(hours_part) == 1:
            hours_part = "0" + hours_part

        if len(minutes_part) == 1:
            minutes_part = "0" + minutes_part
            
        alarm = f"{hours_part}:{minutes_part}"
        alarms.append(alarm)

    return alarms

output = set_the_alarms_up("08:00", 4)
print(output)