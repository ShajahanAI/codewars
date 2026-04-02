# https://www.codewars.com/kata/667dfbaa4570b2db26aedc8c/train/python

# Passed

def size_to_number(size):
    if len(size) == 0:
        return None
    
    base = size[-1]
    base_to_size_dict = {
                         "s": 36, 
                         "m": 38, 
                         "l": 40
                        }
    if base not in base_to_size_dict:
        return None
    
    if base == "m" and len(size) > 1:
        return None
    
    size_value = base_to_size_dict[base]
    if len(size) > 1:
        for modifier in size[:-1]:
            if modifier != "x":
                return None
            
            if base == "l":
                size_value += 2
            elif base == "s":
                size_value -= 2
    
    return size_value

output = size_to_number("xxxs")
print(output)