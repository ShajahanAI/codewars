# https://www.codewars.com/kata/55633765da97b266e3000067/train/python

# Passed

def elo(experience, opponent, score, *k):
    if not k:
        if len(experience) < 30:
            k_value = 25
        else:
            if (max(experience) < 2400):
                k_value = 15
            else:
                k_value = 10
    else:
        k_value = k[0](experience)
        
    player_rating = experience[-1] if len(experience) else 1000
    expectation = 1 / (1 + 10 ** ((opponent - player_rating)/400))
    
    new_player_rating = round(player_rating + k_value * (score - expectation))
    return new_player_rating

output = elo([975, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200, 1225,
              1250, 1275, 1300, 1325, 1350, 1375, 1400, 1425, 1450, 1475,
              1500, 1525, 1550, 1575, 1600, 1625, 1650, 1675, 1700, 1725], 1000, 0)
print(output)