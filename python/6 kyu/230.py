# https://www.codewars.com/kata/52dca71390c32d8fb900002b/train/python

# Passed

def number_to_ordinal(n: int) -> str:
    num_str = str(n)
    if n == 0:
        return num_str

    end_str_to_suffix_dict = {
        "1": "st",
        "2": "nd",
        "3": "rd",
    }
    
    suffix = "th"
    last_digit = num_str[-1]
    if last_digit in end_str_to_suffix_dict:
        if len(num_str) == 1 or (len(num_str) > 1 and num_str[-2] != '1'):
            suffix = end_str_to_suffix_dict[last_digit]
            
    result = num_str + suffix
    return result

output = number_to_ordinal(4)
print(output)