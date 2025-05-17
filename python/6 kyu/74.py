# https://www.codewars.com/kata/52b013920b1d45c8b4000355/train/python

# Passed

def gamble(rolls, my_coins, pot):
    dreidel_rolls = {
        'nun': lambda pot: 0, # nothing happens
        'gimel': lambda pot: pot, # you take the pot,
        'hei': lambda pot: int(pot / 2), # half the pot rounded down,
        'shin': lambda pot: -1, # you put a piece in the pot
    }
    
    for roll in rolls:
        coins_to_take = dreidel_rolls[roll.lower()](pot)
        my_coins += coins_to_take
        pot -= coins_to_take
        
    return my_coins

output = gamble(['Hei', 'Shin'], 10, 20)
print(output)