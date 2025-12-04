# https://www.codewars.com/kata/57ad85bb7cb1f3ae7c000039/train/python

# Passed

def numbers_with_digit_inside(x, d):
    valid_nums = []
    for num in range(1, x + 1):
        if str(d) in str(num):
            valid_nums.append(num)
            
    valid_nums_count = len(valid_nums)
    valid_nums_sum = sum(valid_nums)
    
    if valid_nums_count == 0:
        valid_nums_product = 0
    else:
        valid_nums_product = 1
        for valid_num in valid_nums:
            valid_nums_product *= valid_num
    
    result = [valid_nums_count, valid_nums_sum, valid_nums_product]
    return result

output = numbers_with_digit_inside(44, 4)
print(output)