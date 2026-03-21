# https://www.codewars.com/kata/5650ab06d11d675371000003/train/python

# Passed

def split_in_parts(s, part_length): 
    sub_strings = [s[idx:idx+part_length] for idx in range(0, len(s), part_length)]
    result = " ".join(sub_strings)
    return result

output = split_in_parts("supercalifragilisticexpialidocious", 3)
print(output)