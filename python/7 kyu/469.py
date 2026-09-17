# https://www.codewars.com/kata/6501aa820038a6b0bd098afb/train/python

# Passed

def safecracker(start, incs):
    result = []
    turn_right = True
    current_num = start
    for inc in incs:
        if turn_right:
            current_num -= inc
        else:
            current_num += inc
        
        current_num %= 100
        result.append(current_num)
        turn_right = not turn_right
    
    result = tuple(result)
    return result

output = safecracker(99, (87, 61, 91))
print(output)