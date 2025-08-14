# https://www.codewars.com/kata/5bbb8887484fcd36fb0020ca/train/python

# Passed

def catch_sign_change(lst):
    sign_change = 0
    if not lst:
        return sign_change
    
    current_sign = "positive" if lst[0] >= 0 else "negative"
    for num in lst:
        if current_sign == "positive":
            if num < 0:
                # sign change occured
                sign_change += 1
                current_sign = "negative"
        else:
            if num >= 0:
                # sign change occured
                sign_change += 1
                current_sign = "positive"

    return sign_change
        
        
output = catch_sign_change([-8,4,-1,5,-3,-3,-2,-2])
print(output)