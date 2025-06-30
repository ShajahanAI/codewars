# https://www.codewars.com/kata/5d62961d18198b000e2f22b3/train/python

# Passed

def generate_number(squad, n):
    squad = set(squad)
    if n not in squad:
        return n # n is available to be taken
    
    replacements = sorted([int(f"{num}{n - num}") for num in range(1, n) if len(str(num)) == 1 and len(str(n - num)) == 1])
    for replacement in replacements:
        if replacement not in squad:
            return replacement
        
output = generate_number([1,2,3,4,6,9,10,11,15,29, 69], 11)
print(output)