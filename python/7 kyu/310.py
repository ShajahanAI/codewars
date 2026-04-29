# https://www.codewars.com/kata/56f253dd75e340ff670002ac/train/python

# Passed

def compose(s1, s2):
    s1_lines, s2_lines = s1.splitlines(), s2.splitlines()
    
    s1_start_index = 0
    s1_end_index = 1
    
    s2_start_index = 0
    s2_end_index = len(s2_lines[0])
    
    squared_string_lines = []
    for s1_line, s2_line in zip(s1_lines, s2_lines[::-1]):
        squared_string_line = s1_line[s1_start_index:s1_end_index] + s2_line[s2_start_index:s2_end_index]
        s1_end_index += 1
        s2_end_index -= 1
        squared_string_lines.append(squared_string_line)

    squared_string = "\n".join(squared_string_lines)
    return squared_string

output = compose("tSrJ\nOONy\nsqPF\nxMkB", "hLqw\nEZuh\nmYFl\nzlYf")
print(output)