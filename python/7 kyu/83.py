# https://www.codewars.com/kata/65128732b5aff40032a3d8f0/train/python

# Passed

def neutralise(s1, s2):
    neutralised_string = str()
    for idx in range(len(s1)):
        if s1[idx] == s2[idx]:
            neutralised_string += s1[idx]
            continue
        neutralised_string += "0"

    return neutralised_string

output = neutralise("+++--+---", "++----++-")
print(output)