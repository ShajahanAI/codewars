# https://www.codewars.com/kata/56ec1e8492446a415e000b63/train/python

# Passed

def ones_counter(inp):
    result = []
    current_counter = 0
    for num in inp + [0]:
        if num == 1:
            current_counter += num
        else:
            if current_counter:
                result.append(current_counter)
            current_counter = 0
    
    return result

output = ones_counter([1, 1, 1, 0, 0, 1, 0, 1, 1, 0])
print(output)