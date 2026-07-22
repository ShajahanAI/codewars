# https://www.codewars.com/kata/6a5c17e763f7de3497eec2e2/train/python

# Passed

from collections.abc import Iterable
from typing_extensions import enum

class Hand(enum.IntEnum):
    NONE  = 0
    LEFT  = 1
    RIGHT = 2
    BOTH  = 3
(NONE,LEFT,RIGHT,BOTH) = Hand

def which_hand(word: Iterable[str]) -> Hand:
    left_hand_letters = set("qwertasdfgzxcvb")
    right_hand_letters = set("yuiophjklnm")
    left_right = [False, False]
    
    result = NONE
    for letter in word:
        if letter in left_hand_letters:
            left_right[0] = True
            result = LEFT
        elif letter in right_hand_letters:
            left_right[1] = True
            result = RIGHT
            
        if all(left_right):
            result = BOTH
            break
            
    return result

output = which_hand("cards")
print(output)