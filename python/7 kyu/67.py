# https://www.codewars.com/kata/58311faba317216aad000168/train/python

# Passed

def print_nums(*args):
    if len(args) == 0:
        return str()
    
    numbers_as_string = [str(num) for num in args]
    max_num_string = max(numbers_as_string, key=lambda num_string: len(num_string))
    max_zeroes_to_prefix = len(max_num_string)
    formatted_numbers = list()
    for num_string in numbers_as_string:
        formatted_number = "0" * (max_zeroes_to_prefix - len(num_string)) + num_string
        formatted_numbers.append(formatted_number)
    formatted_string = '\n'.join(formatted_numbers)
    return formatted_string

output = print_nums(2, 10, 3)
print(output)