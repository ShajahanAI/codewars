# https://www.codewars.com/kata/5a434a9dc5e284724f000011/train/python

# Passed

def replace_common(st, letter):
    character_count_to_characters_dict = dict()
    character_to_count_dict = dict()
    
    for char in st:
        if char not in character_to_count_dict:
            character_to_count_dict[char] = 0
            
        character_to_count_dict[char] += 1
    
    seen = set()
    max_character_count = 0
    for char in st:
        if char in seen or char == " ":
            continue
            
        character_count = character_to_count_dict[char]
        if character_count not in character_count_to_characters_dict:
            character_count_to_characters_dict[character_count] = list()
            
        character_count_to_characters_dict[character_count].append(char)
        if character_count > max_character_count:
            max_character_count = character_count
            
        seen.add(char)
            
    char_to_replace = character_count_to_characters_dict[max_character_count][0]
    result = st.replace(char_to_replace, letter)
    
    return result

output = replace_common('great job go ahead', 'k')
print(output)