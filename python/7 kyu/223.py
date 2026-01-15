# https://www.codewars.com/kata/5ac54bcbb925d9b437000001/train/python

# Passed

def find_middle(st):
    if type(st) != str:
        return -1
    
    digits = []
    for char in st:
        if char.isdigit():
            digits.append(int(char))
    
    if len(digits) == 0:
        return - 1
            
    product = 1
    for digit in digits:
        product *= digit
    
    product = str(product)
    if len(product) % 2 == 0:
        start_idx = int(len(product) / 2 - 1)
        end_idx = start_idx + 2
        middle = int(product[start_idx:end_idx])
    else:
        middle = int(product[len(product) // 2])
        
    return middle

output = find_middle('58jd9fgh/fgh6s.,sdf')
print(output)