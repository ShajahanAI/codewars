# https://www.codewars.com/kata/65128d27a5de2b3539408d83/train/python

# Passed

def win_round(you, opp):
    get_number = lambda arr: int("".join(map(str, sorted(arr, reverse=True)[:2])))
    your_number = get_number(you)
    opponent_number = get_number(opp)
    
    result = your_number > opponent_number
    return result

output = win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2])
print(output)