# https://www.codewars.com/kata/58902f676f4873338700011f/train/python

# Passed

def is_lucky(ticket):
    if len(ticket) != 6:
        return False
    
    for digit in ticket:
        if not digit.isdigit():
            return False
        
    first_3_digits, last_3_digits = [int(digit) for digit in ticket[:3]], [int(digit) for digit in ticket[3:]]
    is_lucky_ticket = sum(first_3_digits) == sum(last_3_digits)
    return is_lucky_ticket
    
output = is_lucky('912435')
print(output)