# https://www.codewars.com/kata/58644e8ddf95f81a38001d8d/train/python

# Passed

def box(n):
    # your code here!
    return [
        ''.rjust(n, '-') if i == 1 or i == n else "-" + (" " * (n - 2)) + "-" for i in range(1, n + 1)
    ]

my_box = box(4)
print(my_box)