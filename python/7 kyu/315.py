# https://www.codewars.com/kata/5705ca6a41e5be67720012c0/train/python

# Passed

def square_it(digits):
    digits_str = str(digits)
    digits_length = len(digits_str)
    square_root = digits_length ** 0.5
    result = "Not a perfect square!"
    square_root_int = int(square_root)
    if square_root == square_root_int:
        lines = [digits_str[idx:idx+square_root_int] for idx in range(0, digits_length, square_root_int)]
        result = "\n".join(lines)
        
    return result

output = square_it(123123123)
print(output)