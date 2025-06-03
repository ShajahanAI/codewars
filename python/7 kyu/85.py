# https://www.codewars.com/kata/57aa218e72292d98d500240f/train/python

# Passed

def heron(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s -c)) ** 0.5
    return area

output = heron(3, 4, 5)
print(output)