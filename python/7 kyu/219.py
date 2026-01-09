# https://www.codewars.com/kata/5700c9acc1555755be00027e/train/python

# Passed

def contain_all_rots(strng, arr):
    all_rotations = []
    for start_idx in range(len(strng)):
        rotation = strng[start_idx:] + strng[:start_idx]
        all_rotations.append(rotation)
    
    strings_to_check_set = set(arr)
    for rotation in all_rotations:
        if rotation not in strings_to_check_set:
            return False
        
    return True

output = contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"])
print(output)