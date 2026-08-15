# https://www.codewars.com/kata/63b4758f27f8e5000fc1e427/train/python

# Passed

def yahtzee_upper(dice):
    value_to_scores_dict = dict()
    for value in dice:
        if value not in value_to_scores_dict:
            value_to_scores_dict[value] = 0
            
        value_to_scores_dict[value] += value
        
    result = max(value_to_scores_dict.values())
    return result

output = yahtzee_upper([15, 9, 9, 8, 9])
print(output)