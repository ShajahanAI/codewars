# https://www.codewars.com/kata/55d5434f269c0c3f1b000058/train/python

# Passed

def triple_double(num1, num2):
    def get_straight_count_dict(num):
        digit_to_straight_count_dict = dict()
        prev_digit = None
        straight_count = 0
        for digit in str(num) + " ":
            if prev_digit is None:
                straight_count += 1
                prev_digit = digit
                continue
            
            if prev_digit == digit:
                straight_count += 1
            else:
                digit_to_straight_count_dict[prev_digit] = max(straight_count, digit_to_straight_count_dict.get(prev_digit, 0))
                straight_count = 1
            
            prev_digit = digit
        
        
        return digit_to_straight_count_dict
    
    num_1_digit_to_straight_count_dict = get_straight_count_dict(num1)
    num_2_digit_to_straight_count_dict = get_straight_count_dict(num2)
    
    result = 0
    num_1_digits = set(str(num1))
    for digit in num_1_digits:
        if digit not in num_2_digit_to_straight_count_dict:
            continue

        num_1_digit_straight_count = num_1_digit_to_straight_count_dict[digit]
        num_2_digit_straight_count = num_2_digit_to_straight_count_dict[digit]
        
        if num_1_digit_straight_count >= 3 and num_2_digit_straight_count >= 2:
            result = 1
            break
    
    return result

output = triple_double(451999277, 41177722899)
print(output)