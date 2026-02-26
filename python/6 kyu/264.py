# https://www.codewars.com/kata/5800b6568f7ddad2c10000ae/train/python

# Passed

def simplify(number): 
    terms = []
    for pos, digit in enumerate(str(number), start=1):
        if digit == "0":
            continue
        
        pow = len(str(number)) - pos
        term = f"{digit}*{10 ** pow}" if pow != 0 else digit
        terms.append(term)
        
    equation = "+".join(terms)
    return equation

output = simplify(196587)
print(output)