# https://www.codewars.com/kata/59daf400beec9780a9000045/train/python

# Passed

def name_in_str(strng : str, name : str) -> bool:
    name_indexes = []
    strng, name = strng.lower(), name.lower()
    for char in name:
        split_idx = name_indexes[-1] if len(name_indexes) != 0 else -1
        strng_to_check = strng[split_idx + 1:]
        if char not in strng_to_check:
            return False
        
        char_index = split_idx + 1 + strng_to_check.index(char)
        name_indexes.append(char_index)

    return True

output = name_in_str("Across the rivers", "chris")
print(output)