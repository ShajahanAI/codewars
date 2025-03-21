# https://www.codewars.com/kata/595519279be6c575b5000016/train/python

# Passed

def battle(x, y):
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'.upper()
    x_score, y_score = 0, 0
    
    # calculating scores
    for char in x:
        x_score += LETTERS.index(char) + 1
        
    for char in y:
        y_score += LETTERS.index(char) + 1
        
    if x_score == y_score:
        return 'Tie!'
    
    return x if x_score > y_score else y
    
output = battle("ONE", "TWO")
print(output)