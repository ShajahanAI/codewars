# https://www.codewars.com/kata/558dd9a1b3f79dc88e000001/train/python

# Passed

def find_dup(arr):
    seen = set()
    result = None
    for num in arr:
        if num in seen:
            result = num
            break

        seen.add(num)
        
    return result

output = find_dup([8,2,6,3,7,2,5,1,4])
print(output)