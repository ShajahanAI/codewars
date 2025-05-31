# https://www.codewars.com/kata/5701e43f86306a615c001868/train/python

# Passed

def get_issuer(number):
    card_type_checks = {
        'AMEX': lambda n: len(n) == 15 and (n.startswith('34') or n.startswith('37')),
        'Discover': lambda n: len(n) == 16 and n.startswith('6011'),
        'Mastercard': lambda n: len(n) == 16 and n.startswith('5') and n[1] in '12345',
        'VISA': lambda n: (len(n) == 13 or len(n) == 16) and n.startswith('4')
    }
    
    number = str(number)
    card_number_type = 'Unknown'
    for card_type in card_type_checks:
        check_function = card_type_checks[card_type]
        if check_function(number):
            card_number_type = card_type
            break

    return card_number_type

output = get_issuer(378282246310005)
print(output)