# https://www.codewars.com/kata/58162692c2a518f03a000189/train/python

# Passed

def time(distance,boat_speed,stream):
    stream_type, stream_speed = stream.split(' ')
    stream_speed = int(stream_speed)
    
    if stream_type.lower() == 'downstream':
        boat_speed += stream_speed
    elif stream_type.lower() == 'upstream':
        boat_speed -= stream_speed
        
    total_time = round(distance / boat_speed, 2)
    return total_time

output = time(54,28,"Downstream 3")
print(output)