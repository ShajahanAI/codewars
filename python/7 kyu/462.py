# https://www.codewars.com/kata/56b12e3ad2387de332000041/train/python

# Passed

def diff(arr):
    def get_number_couple_difference(number_couple):
        num_1, num_2 = map(int, number_couple.split("-"))
        return abs(num_1 - num_2)
    
    number_couple_differences = [get_number_couple_difference(number_couple) for number_couple in arr]
    
    if len(set(number_couple_differences)) == 1:
        result = False
    else:
        result = max(enumerate(arr), key = lambda idx_number_couple: number_couple_differences[idx_number_couple[0]], default = False)
        if type(result) != bool:
            result = result[1]

    return result

output = diff(['1-2','2-4','5-7','8-9','44-45'])
print(output)