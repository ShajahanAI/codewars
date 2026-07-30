# https://www.codewars.com/kata/58880c6e79a0a3e459000004/train/python

# Passed

def house_numbers_sum(inp):
    result = 0
    for num in inp:
        if num == 0:
            break
            
        result += num
        
    return result

output = house_numbers_sum([5, 1, 2, 3, 0, 1, 5, 0, 2])
print(output)