# https://www.codewars.com/kata/5a4b16435f08299c7000274f/train/python

# Passed

def sum_square_even_root_odd(nums):
    processed_nums = []
    for num in nums:
        if num % 2 == 0:
            processed_num = num ** 2
        else:
            processed_num = num ** (1/2)
            
        processed_nums.append(processed_num)
        
    result = round(sum(processed_nums), 2)
    return result

output = sum_square_even_root_odd([1, 14, 9, 8, 17, 21])
print(output)