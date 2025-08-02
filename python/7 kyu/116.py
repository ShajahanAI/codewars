# https://www.codewars.com/kata/588425ee4e8efb583d000088/train/python

# Passed

def phone_call(min1, min2_10, min11, s):
    current_minute = 1
    while True:
        if current_minute == 1:
            s -= min1
        elif current_minute > 1 and current_minute < 11:
            s -= min2_10
        else:
            s -= min11
        
        if s <= 0:
            if s < 0:
                current_minute -= 1 # last minute isn't valid
            break        

        current_minute += 1

    return current_minute

output = phone_call(3,1,2,20)
print(output)