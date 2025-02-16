# https://www.codewars.com/kata/565f5825379664a26b00007c/train/python

# Passed

def get_size(w,h,d):
    area = 2 * (w * h + h * d + d * w)
    volume = w * h * d

    return [area, volume]

output = get_size(4, 8, 6)
print(output)