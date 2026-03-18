# https://www.codewars.com/kata/529fdef7488f509b81000061/train/python 

# Passed

def solve(input_string):
    numbers_to_add_list = input_string.split('\n')
    carry_operations = []
    for numbers_to_add in numbers_to_add_list:
        carry_operations_count = 0
        carry_over = False
        num_1, num_2 = numbers_to_add.split(' ')
        for idx in range(len(num_1)):
            digit_1, digit_2 = num_1[len(num_1) - idx - 1], num_2[len(num_2) - idx - 1]
            if carry_over:
                carry_operations_count += 1
                digit_1 = str(int(digit_1) + 1)
                carry_over = False
            
            if int(digit_1) + int(digit_2) >= 10:
                carry_over = True
                
                if idx == len(num_1) - 1:
                    carry_operations_count += 1
        
        carry_operations.append(carry_operations_count)
        
    result = "\n".join([f"{'No' if carry_operation_count == 0 else carry_operation_count} carry operation{'s' if carry_operation_count else str()}" for carry_operation_count in carry_operations])
    return result

output = solve("123 456\n555 555\n123 594")
print(output)