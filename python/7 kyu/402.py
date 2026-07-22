# https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python

# Passed

def adjacent_element_product(array):
    max_adjacent_product = float("-inf")
    for idx in range(len(array)):
        if idx == len(array) - 1:
            break
        
        product = array[idx] * array[idx + 1]
        if product > max_adjacent_product:
            max_adjacent_product = product
            
    return max_adjacent_product

output = adjacent_element_product([3, 6, -2, -5, 7, 3])
print(output)