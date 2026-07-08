# https://www.codewars.com/kata/58856a06760b85c4e6000055/train/python

# Passed

def bits_battle(numbers):
    evens_odds = [0, 0]
    for num in numbers:
        if num == 0:
            continue

        idx = num % 2
        count = bin(num).split('b')[-1].count(str(idx))
        evens_odds[idx] += count
    
    evens_count, odds_count = evens_odds
    if evens_count == odds_count:
        result = "tie"
    elif evens_count > odds_count:
        result = "evens win"
    else:
        result = "odds win"
        
    return result

output = bits_battle([3, 8, 22, 15, 78])
print(output)