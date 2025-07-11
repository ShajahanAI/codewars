# https://www.codewars.com/kata/57d2ba8095497e484e00002e/train/python

# Passed

def borrow(s):
    borrower_speak = str()
    for char in s:
        if char.isalpha():
            borrower_speak += char.lower()

    return borrower_speak

output = borrow('THE big PeOpLE Here!!')
print(output)