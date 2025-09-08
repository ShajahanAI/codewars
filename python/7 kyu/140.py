# https://www.codewars.com/kata/687dd1e199ab3955339b8071/train/python

# Passed

def can_play(hand, face_up):
    face_up_colour, face_up_number = face_up.split(" ")
    can_make_play = any([face_up_colour in card or face_up_number in card for card in hand])
    return can_make_play

output = can_play(['yellow 3', 'yellow 5', 'red 8'], 'red 2')
print(output)