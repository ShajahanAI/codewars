# https://www.codewars.com/kata/5665d30b3ea3d84a2c000025/train/python

# Passed

import math

def gifts(number):
    GIFTS = {
      1: 'Toy Soldier',
      2: 'Wooden Train',
      4: 'Hoop',
      8: 'Chess Board',
      16: 'Horse',
      32: 'Teddy',
      64: 'Lego',
      128: 'Football',
      256: 'Doll',
      512: "Rubik's Cube"
    }
    toys_to_gift = []
    gift_numbers = list(GIFTS.keys())
    while number > 0 and gift_numbers:        
        best_gift_number = 2 ** math.floor(math.log(number, 2))
        if best_gift_number > 512:
            best_gift_number = max(gift_numbers)

        number -= best_gift_number
        toys_to_gift.append(GIFTS[best_gift_number])
        gift_numbers.remove(best_gift_number) # santa doesn't give the same gift twice
    
    toys_to_gift.sort() # to help out the elfs
    return toys_to_gift

output = gifts(160)
print(output)