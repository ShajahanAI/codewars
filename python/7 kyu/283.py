# https://www.codewars.com/kata/566fc12495810954b1000030/train/python

# Passed

def nb_dig(n, d):
    squares = [num ** 2 for num in range(n + 1)]
    result = sum(str(square).count(str(d)) for square in squares)
    return result

output = nb_dig(11011, 2)
print(output)