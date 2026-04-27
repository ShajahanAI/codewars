# https://www.codewars.com/kata/5dd5128f16eced000e4c42ba/train/python

# Passed

def solve(st):
    char_to_data_dict = dict()
    for char_idx, char in enumerate(st):
        if char not in char_to_data_dict:
            data_dict = dict(first_occurence=char_idx, last_occurence=char_idx, value=0)
            char_to_data_dict[char] = data_dict
        else:
            data_dict = char_to_data_dict[char]
            data_dict["last_occurence"] = char_idx
            data_dict["value"] = data_dict["last_occurence"] - data_dict["first_occurence"]
            
    value_to_characters = dict()
    for char in char_to_data_dict:        
        data_dict = char_to_data_dict[char]
        value = data_dict['value']
        if value not in value_to_characters:
            value_to_characters[value] = list()
            
        value_to_characters[value].append(char)
        
    max_value = max(value_to_characters)
    max_value_characters = sorted(value_to_characters[max_value])
    result = max_value_characters[0]
            
    return result

output = solve('axyzxyz')
print(output)