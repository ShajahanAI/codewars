# https://www.codewars.com/kata/626466bdd13ea6923d0663ea/train/python

# Passed

def tunnel_digging(r):
    part_rock_to_minutes_dict = {
        '[': 30,
        ']': 30,
        '{': 25,
        '}': 25,
        '(': 20,
        ')': 20,
        '|': 15,
        '|': 15,
        ':': 10,
        ':': 10,
        " ": 0
    }
    
    total_minutes_required = 0
    for idx, rock in enumerate(r):
        minutes_required = sum([part_rock_to_minutes_dict[part_rock] for part_rock in rock])
        total_minutes_required += minutes_required 
        
        if idx % 3 == 2:
            total_minutes_required += 30
            
    return total_minutes_required

output = tunnel_digging(['|)', '{ ', '{ ', '|]', '{ ', ' }'])
print(output)