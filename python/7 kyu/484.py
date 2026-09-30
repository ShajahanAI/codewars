# https://www.codewars.com/kata/65126a26597b8597d809de48/train/python

# Passed

def numbers_need_friends_too(n):
    result = str()
    
    num_str = str(n)
    if len(num_str) == 1:
        result = int(num_str * 3)
        return result

    for idx in range(len(num_str)):
        if idx == 0:
            indexes_to_check = [idx + 1]
        elif idx == len(num_str) - 1:
            indexes_to_check = [idx - 1]
        else:
            indexes_to_check = [idx - 1, idx + 1]
        
        digit_str = num_str[idx]
        if any(digit_str == num_str[index] for index in indexes_to_check):
            result += digit_str
        else:
            result += digit_str * 3
            
    result = int(result)
    return result

output = numbers_need_friends_too(56657)
print(output)