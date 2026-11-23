# https://www.codewars.com/kata/64fbf7eb2b610b1a6eff0e44/train/python

# Passed

def nonstop_hotspot(area):
    area = area.replace(" ", str())
    phone_idx = area.index('P')
    result = 0
    
    # going left and right
    for direction in range(2):
        start = phone_idx + 1 if direction else phone_idx - 1
        end = len(area) if direction else -1 
        step = 1 if direction else -1
        for idx in range(start, end, step):
            if area[idx] == "*":
                result += 1
            elif area[idx] == "#":
                break
    
    return result

output = nonstop_hotspot('*  * #  * P # * #')
print(output)