# https://www.codewars.com/kata/552e45cc30b0dbd01100001a/train/python

# Passed

def zipvalidate(postcode):
    invalid_starters = ["0", "5", "7", "8", "9"]
    if len(postcode) != 6:
        # has to be 6 digits
        return False

    if any([postcode.startswith(digit) for digit in invalid_starters]):
        # can't start with invalid starters
        return False

    if not all([possible_digit.isdigit() for possible_digit in postcode]):
        # every character has to be a digit
        return False

    return True

output = zipvalidate('310003')
print(output)