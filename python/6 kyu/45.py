# https://www.codewars.com/kata/56d3c1eb3323a88d0a000305/train/python

# Passed

def find_super_man(s):
    string_to_look_for = "superman"
    for string in [s, s[::-1]]:
        idx = 0
        avoid_next_char = False
        for char in string.lower():
            if avoid_next_char:
                avoid_next_char = False
                continue

            if string_to_look_for[idx] == char:
                idx += 1
                avoid_next_char = True 
                if char == "n":
                    return "Hi, SuperMan!"
            
    return 'Are you crazy?'

output = find_super_man('qj vsdljd yobuvdwqclf p  ixlktefwlyztrk d mai wg wjn')
print(output)