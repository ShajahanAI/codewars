# https://www.codewars.com/kata/60b0a562639df90006a106f4/train/python

# Passed

def traffic_jam(traffic, green_light_duration):
    result = 0
    while len(traffic) != 0:
        current_light_duration = green_light_duration
        for vehicle_time in traffic[::-1]:
            if vehicle_time <= current_light_duration:
                traffic.pop()
                current_light_duration -= vehicle_time
            else:
                break
        
        result += 1

    return result

output = traffic_jam([15, 2, 8, 7], 16)
print(output)