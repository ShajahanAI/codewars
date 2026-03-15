# https://www.codewars.com/kata/586bca7fa44cfc833e00005c/train/python

# Passed

def create_array_of_tiers(n):
    result = []
    str_num = str(n)
    for end_idx in range(1, len(str_num) + 1):
        result.append(str_num[:end_idx])
        
    return result

output = create_array_of_tiers(80200)
print(output)