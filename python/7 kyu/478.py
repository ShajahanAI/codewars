# https://www.codewars.com/kata/6aa8e25b5ae7dfbbe29e8fb8/train/python

# Passed

def successful_mission(solar_system, destination_planet, fuel):
    fuel_map = {
      "Asteroid": 1,
      "Mercury": 2,
      "Venus": 4,
      "Mars": 3,
      "Jupiter": 12,
      "Saturn": 11,
      "Uranus": 8,
      "Neptune": 7
    }
        
    earth_idx = solar_system.index("Earth")
    destination_idx = solar_system.index(destination_planet)
    
    direction = 1 if destination_idx > earth_idx else -1
    for idx in range(earth_idx + direction, destination_idx + direction, direction):
        current_object = solar_system[idx]
        fuel_used = fuel_map[current_object]
        
        if idx == destination_idx:
            fuel_used *= 2
        
        fuel -= fuel_used
        if fuel < 0:
            return False
    
    return True

output = successful_mission(["Mercury", "Asteroid", "Earth", "Asteroid", "Saturn", "Venus", "Neptune", "Asteroid"], "Neptune", 33)
print(output)