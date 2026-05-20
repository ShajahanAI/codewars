# https://www.codewars.com/kata/539de388a540db7fec000642/train/python

# Passed

from datetime import datetime

def check_coupon(entered_code, correct_code, current_date: str, expiration_date: str) -> bool:
    format_string = "%B %d, %Y"
    current_datetime = datetime.strptime(current_date, format_string)
    expiration_datetime = datetime.strptime(expiration_date, format_string)
    
    coupon_valid = (current_datetime <= expiration_datetime and 
                    type(entered_code) == type(correct_code) and
                    entered_code == correct_code)

    return coupon_valid

output = check_coupon('123','123','September 5, 2014','October 1, 2014')
print(output)