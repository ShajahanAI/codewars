# https://www.codewars.com/kata/5470ae03304c1250b4000e57/train/python

# Passed

def identify_weapon(character):
    character_weapon_dict = {
    character_weapon.split("-")[0].strip(): character_weapon.strip() for character_weapon in 
     '''Laval-Shado Valious
        Cragger-Vengdualize
        Lagravis-Blazeprowlor
        Crominus-Grandorius
        Tormak-Tygafyre
        LiElla-Roarburn'''.splitlines()
    }
    weapon = character_weapon_dict.get(character, "Not a character")
    return weapon

output = identify_weapon("Crominus")
print(output)