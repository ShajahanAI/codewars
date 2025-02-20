# https://www.codewars.com/kata/57ec8bd8f670e9a47a000f89/train/python

# Passed

def mouth_size(animal): 
    return "small" if animal.lower().strip() == 'alligator' else 'wide'

output = mouth_size("toucan")
print(output)