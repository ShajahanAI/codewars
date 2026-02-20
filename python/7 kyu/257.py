# https://www.codewars.com/kata/5982619d2671576e90000017/train/python

# Passed

def sponge_meme(s):
    result = str()
    transform_to_upper = True
    for char in s:
        result += char.upper() if transform_to_upper else char.lower()
        transform_to_upper = not transform_to_upper
        
    return result

output = sponge_meme("stop Making spongebob Memes!")
print(output)