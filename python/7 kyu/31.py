# https://www.codewars.com/kata/5ebd53ea50d0680031190b96/train/python

# Passed

def get_turkish_number(num):
    turkish_number_dict = {
        0:"sıfır",
        1:"bir",
        2:"iki",
        3:"üç",
        4:"dört",
        5:"beş",
        6:"altı",
        7:"yedi",
        8:"sekiz",
        9:"dokuz",
        10:"on",
        20:"yirmi",
        30:"otuz",
        40:"kırk",
        50:"elli",
        60:"altmış",
        70:"yetmiş",
        80:"seksen",
        90:"doksan",
    }
    
    if turkish_number_dict.get(num):
        return turkish_number_dict.get(num)
    
    quotient = num // 10
    remainder = num % 10

    return " ".join([turkish_number_dict.get(quotient * 10), turkish_number_dict.get(remainder)])

output = get_turkish_number(94)
print(output)
        