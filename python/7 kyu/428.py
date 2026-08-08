# https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2/train/python

# Passed

def sum_no_duplicates(l):
    item_to_count_dict = dict()
    for num in l:
        if num not in item_to_count_dict:
            item_to_count_dict[num] = 0
            
        item_to_count_dict[num] += 1
    
    result = 0
    nums = set(l)
    for num in nums:
        if item_to_count_dict[num] == 1:
            result += num
            
    return result

output = sum_no_duplicates([5, 6, 10, 3, 10, 10, 6, 7, 0, 9, 1, 1, 6, 3, 1])
print(output)