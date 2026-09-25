# https://www.codewars.com/kata/5803753aab6c2099e600000e/train/python

# Passed

from datetime import datetime

def age_in_days(year, month, day):
    birthdate = datetime(year, month, day)
    days = (datetime.today() - birthdate).days
    
    result = f"You are {days} days old"
    return result

output = age_in_days(2025, 9, 25)
print(output)