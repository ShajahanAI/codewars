# https://www.codewars.com/kata/67d4554cd94fdfdab4239cfa/train/python

# Passed

def is_planet_mnemonic_correct(solar_system, mnemonic):
    mnemonic_words = mnemonic.split()
    filtered_solar_system = [planet for planet in solar_system if planet.lower() != "asteroid"]
    
    if len(mnemonic_words) != len(filtered_solar_system):
        return False

    for planet, mnemonic_word in zip(filtered_solar_system, mnemonic_words):
        if planet[0] != mnemonic_word[0]:
            return False

    return True

output = is_planet_mnemonic_correct(["Earth", "Jupiter", "Asteroid", "Asteroid", "Mercury", "Asteroid", "Saturn"], "Even Jaguars Make Spaghetti")
print(output)