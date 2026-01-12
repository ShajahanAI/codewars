# https://www.codewars.com/kata/67f186c91c59535d5dbd4f2d/train/python

# Passed

def is_valid_dni(s: str) -> bool:
    if len(s) != 9:
        return False
    
    if not s[:8].isdigit():
        return False
    
    if not s[-1].isalpha() or not s[-1].isupper():
        return False
    
    number = int(s[:8])
    letter = s[-1]
    
    remainder_to_letter_dict = {
        0: "T",
        1: "R",
        2: "W",
        3: "A",
        4: "G",
        5: "M",
        6: "Y",
        7: "F",
        8: "P",
        9: "D",
        10: "X",
        11: "B",
        12: "N",
        13: "J",
        14: "Z",
        15: "S",
        16: "Q",
        17: "V",
        18: "H",
        19: "L",
        20: "C",
        21: "K",
        22: "E",
    }
    
    remainder = number % 23
    if remainder_to_letter_dict[remainder] != letter:
        return False
    
    return True

output = is_valid_dni("99999999R")
print(output)