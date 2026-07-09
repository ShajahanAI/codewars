# https://www.codewars.com/kata/5782a87d9fb2a5e623000158/train/python

# Passed

def clock_degree(s) :
    hours, minutes = [int(num) for num in s.split(":")]
    result = "Check your time !"
    if minutes > 60 or minutes < 0:
        return result
    
    if hours > 23 or hours < 0:
        return result
    
    hours_degrees = 30 * (hours % 12 if hours % 12 else 12)
    minutes_degrees = 6 * (minutes if minutes else 60)
    
    result = f"{hours_degrees}:{minutes_degrees}"
    return result

output = clock_degree("01:30")
print(output)