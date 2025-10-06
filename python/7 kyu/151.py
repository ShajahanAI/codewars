# https://www.codewars.com/kata/59afff65f1c8274f270020f5/train/python

# Passed

def spinning_rings(inner_max, outer_max):
    inner = inner_max
    outer = 1
    
    move_count = 1
    while inner != outer:
        inner -= 1
        inner = inner_max if inner < 0 else inner 

        outer += 1
        outer = 0 if outer > outer_max else outer
        
        move_count += 1

    return move_count

output = spinning_rings(2, 3)
print(output)