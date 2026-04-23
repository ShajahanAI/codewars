# https://www.codewars.com/kata/583df40bf30065fa9900010c/train/python

# Passed

def get_mean(arr,x,y):
    if not all(limit > 1 and limit <= len(arr) for limit in [x, y]):
        result = -1
    else:
        first_mean = sum(arr[:x]) / x
        second_mean = sum(arr[-y:]) / y
        result = (first_mean + second_mean)/ 2
        
    return result

output = get_mean([1, 3, 2, 4], 2, 3)
print(output)