# https://www.codewars.com/kata/633a870b198a4c00286ad2b7/train/python

# Passed

from datetime import datetime, timedelta

def life_predictor(date):
    date_format = "%Y-%m-%d"
    birthday = datetime.strptime(date, date_format)
    real_birthday = birthday + timedelta(days=-280)
    real_birthday_str = real_birthday.strftime(date_format)
    return real_birthday_str
    
output = life_predictor("2000-09-18")
print(output)