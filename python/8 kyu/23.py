# https://www.codewars.com/kata/56598d8076ee7a0759000087/

# Passed

from math import ceil

def calculate_tip(amount, rating):
    amount_percent_dict = {
        'terrible': 0,
        'poor': 5,
        'good': 10,
        'great': 15,
        'excellent': 20
    }
    
    return ceil(amount_percent_dict[rating.lower()] / 100 * amount) if rating.lower() in amount_percent_dict else 'Rating not recognised'