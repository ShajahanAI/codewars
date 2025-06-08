# https://www.codewars.com/kata/5cb05eee03c3ff002153d4ef/train/python

# Passed

def get_section_id(scroll, sizes):
    current_position = 0
    for idx, size in enumerate(sizes):
        current_position += size
        if current_position > scroll:
            return idx

    return -1 # past last section

output = get_section_id(300, [300, 200, 400, 600, 100])
print(output)