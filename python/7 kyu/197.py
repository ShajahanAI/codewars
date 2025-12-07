# https://www.codewars.com/kata/5951b409aea9beff3f0000c6/train/python

# Passed

from math import gcd

def final_attack_value(x, monster_list):
    player_attack_points = x
    for monster_attack_points in monster_list:
        if player_attack_points >= monster_attack_points:
            player_attack_points += monster_attack_points
        else:
            player_attack_points += gcd(player_attack_points, monster_attack_points)
            
    return player_attack_points

output = final_attack_value(50,[50,105,200])
print(output)