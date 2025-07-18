# https://www.codewars.com/kata/58fd91af13b0012e8e000010/train/python

# Passed

from collections import defaultdict

def strange_coach(players):
    letter_count_dict = defaultdict(int)
    for player in players:
        letter_count_dict[player[0]] += 1

    valid_players = [player for player in players if letter_count_dict[player[0]] >= 5]
    if not valid_players:
        return "forfeit"

    first_letters = [letter for letter in letter_count_dict if letter_count_dict[letter] >= 5]
    first_letters.sort()

    result = "".join(first_letters)
    return result

output = strange_coach(["babic","keksic","boric","bukic",
                        "sarmic","balic","kruzic","hrenovkic",
                        "beslic","boksic","krafnic","pecivic",
                        "klavirkovic","kukumaric","sunkic","kolacic",
                        "kovacic","prijestolonasljednikovic"])
print(output)