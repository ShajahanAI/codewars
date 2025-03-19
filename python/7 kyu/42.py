# https://www.codewars.com/kata/678e32f27625ec1b6a0e5976/train/python

# Passed

def jumbled_solar_system(solar_system):
    solar_order = ["Asteroid", "Pluto", "Mercury", "Mars", "Venus", "Earth", "Neptune", "Uranus", "Saturn", "Jupiter"]
    result = []
    for celestial_body_idx in range(len(solar_system) - 1):
        curr_celestial_body = solar_order.index(solar_system[celestial_body_idx])
        next_celestial_body = solar_order.index(solar_system[celestial_body_idx + 1])
        
        if next_celestial_body < curr_celestial_body:
            result.append('<')
        elif next_celestial_body > curr_celestial_body:
            result.append('>')
        else:
            result.append('=')
            
    return result

output = jumbled_solar_system(['Venus', 'Jupiter', 'Mercury'])
print(output)