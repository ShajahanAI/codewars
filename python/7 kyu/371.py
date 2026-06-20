# https://www.codewars.com/kata/546ba103f0cf8f7982000df4/train/python

# Passed

def calculate(n1, n2, o):
    operations = {
        'add': lambda decimal_num_1, decimal_num_2: decimal_num_1 + decimal_num_2,
        'multiply': lambda decimal_num_1, decimal_num_2: decimal_num_1 * decimal_num_2,
        'subtract': lambda decimal_num_1, decimal_num_2: decimal_num_1 - decimal_num_2
    }
    
    operation = operations[o]
    binary_result = bin(operation(int(n1, 2), int(n2, 2)))
    sign, binary = binary_result.split('b')
    result = ('' if sign == '0' else '-') + binary
    
    return result

output = calculate('1', '1', 'add')
print(output)