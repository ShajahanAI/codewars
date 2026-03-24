# https://www.codewars.com/kata/58545549b45c01ccab00058c/train/python

# Passed

def calculate_total(subtotal, tax, tip):
    total = round(subtotal * (1 + (tax + tip) / 100), 2)
    return total

output = calculate_total(5.00, 5, 10)
print(output)