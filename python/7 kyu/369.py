# https://www.codewars.com/kata/5aee86c5783bb432cd000018/train/python

# Passed

def hydrate(drink_string): 
    all_numbers = [int(num) for num in drink_string.split() if num.isdigit()]
    total_sum = sum(all_numbers)
    
    result = f"{total_sum} {'glass' if total_sum == 1 else 'glasses'} of water"
    return result

output = hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer")
print(output)