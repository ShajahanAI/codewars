# https://www.codewars.com/kata/5effa412233ac3002a9e471d/train/python

# Passed

def add(num1, num2):
    larger_number = str(max(num1, num2))
    num1, num2 = str(num1), str(num2)
    modified_num_1 = (len(larger_number) - len(num1)) * "0" + str(num1)
    modified_num_2 = (len(larger_number) - len(num2)) * "0" + str(num2)

    result = str()
    for idx in range(len(str(larger_number))):
        digit_1 = int(modified_num_1[idx])
        digit_2 = int(modified_num_2[idx])
        sum_of_digits = digit_1 + digit_2
        
        result += str(sum_of_digits)
    
    result = int(result)
    return result

output = add(122, 81)
print(output)