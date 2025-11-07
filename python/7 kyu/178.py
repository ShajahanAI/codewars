# https://www.codewars.com/kata/59fb783bab11f89202001083/train/python

# Passed

def recycle_me(rubbish):
    recycling_boxes = [0] * 3
    for trash in rubbish:
        if trash > 0:
            recycling_boxes[0] += 1
        elif trash < 0:
            recycling_boxes[1] += 1
        else:
            recycling_boxes[2] += 1
    
    recycling_boxes = tuple(recycling_boxes)
    return recycling_boxes

output = recycle_me([5, -9, 0, 6, -84, -95, 15]) 
print(output)