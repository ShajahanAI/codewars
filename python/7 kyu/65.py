# https://www.codewars.com/kata/55de6173a8fbe814ee000061/train/python

# Passed

def unused_digits(*numbers):
    digits = set("1234567890")
    digits_in_numbers = set()
    for num in numbers:
        digits_in_numbers.update(set(str(num)))

    digits_to_use = list(digits - digits_in_numbers)
    digits_to_use.sort()
    unused_digits = "".join(digits_to_use)
    return unused_digits

output = unused_digits(2015, 8, 26)
print(output)