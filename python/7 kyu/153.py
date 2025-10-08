# https://www.codewars.com/kata/585eaef9851516fcae00004d/train/python

# Passed

def what_list_am_i_on(actions):
    naughty_alphabets = ['b', 'f', 'k']
    nice_alphabets = ['g', 's', 'n']
    
    naughty_count = 0
    nice_count = 0
    for action in actions:
        action = action.lower()
        if any(action.startswith(alphabet) for alphabet in naughty_alphabets):
            naughty_count += 1
        elif any(action.startswith(alphabet) for alphabet in nice_alphabets):
            nice_count += 1

    if naughty_count >= nice_count:
        return 'naughty'
    else:
        return 'nice'
    
output = what_list_am_i_on(['got someone a new car', 'saved a man from drowning', 'never got into a fight'])
print(output)